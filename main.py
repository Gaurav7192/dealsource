from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
from models import Sale, SaleCreate
from db import get_connection

app = FastAPI(
    title="iPhone Sales Tracker API"
)


@app.post("/sales", response_model=Sale, status_code=201)
def create_sale(sale: SaleCreate):
    with get_connection() as c:
        with c.cursor() as cur:
            query = """INSERT INTO iphone_sales (customer_name, phone_model, color, storage_gb, price, sale_date, store_location)VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *;"""
            cur.execute(query, (
                sale.customer_name, sale.phone_model, sale.color,
                sale.storage_gb, sale.price, sale.sale_date, sale.store_location
            ))
            new_record = cur.fetchone()
            c.commit()
            return new_record


@app.get("/sales", response_model=List[Sale])# this is a function to get all sales  (if you not pass  model name then it give all iphone sales else if you enter iphone model then it give specific data)
def get_all_sales(phone_model: Optional[str] = Query(None)):
    with get_connection() as c:
        with c.cursor() as cur:
            if phone_model:
                cur.execute("SELECT * FROM iphone_sales WHERE phone_model = %s", (phone_model,))
            else:
                cur.execute("SELECT * FROM iphone_sales")
            return cur.fetchall()


@app.get("/sales/stats")# this is a get function for some insteads such as total sales ,total revenue and most sale iphone
def get_sales_stats():
    with get_connection() as c:
        with c.cursor() as cur:
            cur.execute("""SELECT COUNT(*) as total_count,SUM(price) as total_revenue,AVG(price) as avg_price,(SELECT phone_model FROM iphone_sales GROUP BY phone_model ORDER BY COUNT(id) DESC LIMIT 1) as popular_model FROM iphone_sales;""")
            stats = cur.fetchone()

            # Handle empty database scenario
            if not stats or stats['total_count'] == 0:
                return {"message": "No sales data available"}

            return {
                "total_sales_count": stats['total_count'],
                "total_revenue": float(stats['total_revenue'] or 0),
                "average_sale_price": round(float(stats['avg_price'] or 0), 2),
                "most_popular_phone_model": stats['popular_model']
            }


@app.get("/sales/{sale_id}", response_model=Sale)# this is a get function which is use for to get single iphone sales (particular iphone sales data by using sale_id)
def get_sale_by_id(sale_id: int):
    with get_connection() as c:
        with c.cursor() as cur:
            cur.execute("SELECT * FROM iphone_sales WHERE id = %s", (sale_id,))
            sale = cur.fetchone()
            if not sale:
                raise HTTPException(status_code=404, detail="Sale not found")
            return sale


@app.put("/sales/{sale_id}", response_model=Sale)# this is a put method wherre you can update sales record by giving sales id
def update_sale(sale_id: int, sale_update: SaleCreate):
    with get_connection() as c:
        with c.cursor() as cur:
            query = """UPDATE iphone_sales SET customer_name=%s, phone_model=%s, color=%s,storage_gb=%s, price=%s, sale_date=%s, store_location=%s WHERE id = %s RETURNING *;"""
            cur.execute(query, (
                sale_update.customer_name, sale_update.phone_model, sale_update.color,
                sale_update.storage_gb, sale_update.price, sale_update.sale_date,
                sale_update.store_location, sale_id
            ))
            updated_record = cur.fetchone()
            if not updated_record:
                raise HTTPException(status_code=404, detail="Sale not found")
            c.commit()
            return updated_record


@app.delete("/sales/{sale_id}")# this function is for iphone deletion where i can delete iphone sales  by there sales id.
def delete_sale(sale_id: int):
    with get_connection() as c:
        with c.cursor() as cur:
            cur.execute("DELETE FROM iphone_sales WHERE id = %s", (sale_id,))
            if cur.rowcount == 0:
                raise HTTPException(status_code=404, detail="Sale not found")
            c.commit()
            return {"message": f"Sale record {sale_id} deleted successfully"}
import psycopg2


try:
    conn = psycopg2.connect("dbname=myduka user=postgres password=123nish")
    cur= conn.cursor()
except Exception as error:
    print(error)

def fetch_data(tbln):
        try:
            q = "SELECT * FROM " + tbln +  ";"
            cur.execute(q)
            records = cur.fetchall()
            return records
        except Exception as Error:
            return error


products = fetch_data("products")

sales = fetch_data("sales")


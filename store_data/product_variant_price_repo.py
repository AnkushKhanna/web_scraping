import datetime
import sqlite3


class ProductVariantPriceRepo:
    def __init__(self):
        pass

    @staticmethod
    def get_product_variant(product_id):
        start_date = str(datetime.date.today())
        end_date = str(datetime.date.today() + datetime.timedelta(1))
        conn = ProductVariantPriceRepo.__create_connection__()
        v = conn.execute(
            "SELECT * FROM  main.product_variant_price WHERE product_name = :product_id AND created_date > :start_date AND created_date < :end_date;",
            {"product_id": product_id, "start_date": start_date, "end_date": end_date})

        conn.commit()
        data = v.fetchall()
        conn.close()
        return data

    @staticmethod
    def update_product_variant(product_variant_price, product_id=10180460):

        list = []
        for key, value in product_variant_price.items():
            list.append((product_id, key, value))
        conn = ProductVariantPriceRepo.__create_connection__()
        v = conn.executemany(
            'INSERT INTO main.product_variant_price (product_name, variant, price) VALUES (?,?,?)',
            list
        )

        rowcount = v.rowcount
        conn.commit()
        conn.close()
        return rowcount

    @staticmethod
    def __create_connection__():
        return sqlite3.connect('/Users/ankukhanna/Documents/rebuy_apple_watch/rebuy_test.db')

from retrieve_data.reponse_price_template import ResponsePriceTemplate
from store_data.product_variant_price_repo import ProductVariantPriceRepo


class PriceService:

    @staticmethod
    def update_price_watch():
        dict_price = ResponsePriceTemplate.get_apple_watch_response()
        row_count = ProductVariantPriceRepo.update_product_variant(dict_price)
        print("Updating price for watch, count: " + str(row_count))
        return row_count

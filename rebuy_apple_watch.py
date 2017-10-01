from flask import Flask

from retrieve_data.reponse_price_template import ResponsePriceTemplate
from service.price_service import PriceService
from service.scheduler_price import SchedulerPrice
from store_data.product_variant_price_repo import ProductVariantPriceRepo

app = Flask(__name__)

@app.route('/apple-watch/price', methods=['POST'])
def apple_watch_data_update():
    v = PriceService.update_price_watch()
    return str(v)


@app.route('/apple-watch/price', methods=['GET'])
def apple_watch_data_rebuy():
    return str(ResponsePriceTemplate.get_apple_watch_response())


@app.route('/rebuy/price/<product_id>')
def get_apple_watch_data(product_id):
    return str(ProductVariantPriceRepo.get_product_variant(product_id))


print("STARTING APP!!!")
PriceService.update_price_watch()
SchedulerPrice().__init__()

if __name__ == '__main__':
    app.run()

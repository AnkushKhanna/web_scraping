import atexit

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

from service.price_service import PriceService


class SchedulerPrice:
    def __init__(self):
        scheduler = BackgroundScheduler()
        scheduler.start()
        scheduler.add_job(
            func=PriceService.update_price_watch,
            trigger=IntervalTrigger(minutes=30),
            id='update_price',
            name='Updating price on interval',
            replace_existing=True)
        # Shut down the scheduler when exiting the app
        atexit.register(lambda: scheduler.shutdown())

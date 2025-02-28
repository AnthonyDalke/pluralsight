from abs_subscription import Subscription
from datetime import timedelta


class Monthly(Subscription):
    @property
    def price_base(self):
        return 50.00

    @property
    def expiration(self):
        return self._enrolled + timedelta(days=30)

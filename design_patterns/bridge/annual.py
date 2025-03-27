from abs_subscription import Subscription
from datetime import timedelta


class Annual(Subscription):
    @property
    def price_base(self):
        return 250.00

    @property
    def expiration(self):
        return self._enrolled + timedelta(days=365)

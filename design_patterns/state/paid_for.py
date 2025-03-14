from abs_state import AbsState


class PaidFor(AbsState):
    def add_item(self):
        print("Already paid for cart")

    def remove_item(self):
        print("Can't remove items from purchase already completed")

    def checkout(self):
        print("Already paid for cart")

    def pay(self):
        print("Already paid for cart")

    def empty_cart(self):
        print("Can't remove items from purchase already completed")

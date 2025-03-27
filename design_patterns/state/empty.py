from abs_state import AbsState


class Empty(AbsState):
    def add_item(self):
        self._cart.items += 1
        print("Added first item")
        self._cart.state = self._cart.not_empty

    def remove_item(self):
        print("Cart empty, nothing to remove")

    def checkout(self):
        print("Cart empty, nothing to checkout")

    def pay(self):
        print("Cart empty, nothing to buy")

    def empty_cart(self):
        print("Cart already empty")

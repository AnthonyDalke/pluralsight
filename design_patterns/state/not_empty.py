from abs_state import AbsState


class NotEmpty(AbsState):
    def add_item(self):
        self._cart.items += 1
        print(f"Cart now contains {self._cart.items} items")

    def remove_item(self):
        self._cart.items -= 1
        if self._cart.items:
            print(f"Cart now contains {self._cart.items} items")
        else:
            print("Cart empty again")
            self._cart.state = self._cart.empty

    def checkout(self):
        print("Ready for checkout")
        self._cart.state = self._cart.check_out

    def pay(self):
        print("Go to checkout to pay")

    def empty_cart(self):
        print("Cart can only get emptied at checkout")

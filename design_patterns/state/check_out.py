from abs_state import AbsState


class AtCheckOut(AbsState):
    def add_item(self):
        print("Can't add items at checkout counter")

    def remove_item(self):
        self._cart.items -= 1
        if self._cart.items:
            print(f"Cart now has {self._cart.items} items")
        else:
            print("Cart empty again")
            self._cart.state = self._cart.empty

    def checkout(self):
        print("Already at checkout")

    def pay(self):
        print(f"Paid for {self._cart.items} items")
        self._cart.state = self._cart.paid

    def empty_cart(self):
        self._cart.items = 0
        self._cart.state = self._cart.empty
        print("Cart empty again")

from shopping_cart import ShoppingCart


def main():
    print("First cart")
    cart = ShoppingCart()
    cart.add_item()
    cart.remove_item()
    cart.add_item()
    cart.add_item()
    cart.add_item()
    cart.remove_item()
    cart.checkout()
    cart.pay()

    print("Second cart")
    cart = ShoppingCart()
    cart.add_item()
    cart.add_item()
    cart.checkout()
    cart.empty_cart()
    cart.add_item()
    cart.checkout()
    cart.pay()

    print("expect an error next")
    cart.add_item()


main()

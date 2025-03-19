class FishHandler:
    def handle(self, request):
        if request.request_type == "cats":
            print("I can't find Nemo!")
            return True

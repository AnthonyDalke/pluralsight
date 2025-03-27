class DogHandler:
    def handle(self, request):
        if request.request_type == "dogs":
            print("Who let the dogs out?")
            return True

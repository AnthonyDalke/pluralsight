class CatHandler:
    def handle(self, request):
        if request.request_type == "cats":
            print("People have dogs, cats have staff.")
            return True

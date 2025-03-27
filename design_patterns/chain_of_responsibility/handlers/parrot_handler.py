class ParrotHandler:
    def handle(self, request):
        if request.request_type == "cats":
            print("I know a dead parrot when I see one.")
            return True

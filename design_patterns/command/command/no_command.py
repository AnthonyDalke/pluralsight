from .command_abc import AbsCommand


class NoCommand(AbsCommand):
    def __init__(self, args):
        self._command = args[0]
        pass

    def execute(self):
        print(f"No command name {self._command}")

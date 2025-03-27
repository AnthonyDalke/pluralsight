from command.command.create_order import CreateOrder
from command.command.update_order import UpdateOrder
from command.command.ship_order import ShipOrder
from command.command.no_command import NoCommand
import sys
import inspect


def main():
    commands = get_commands()
    if len(sys.argv) < 2:
        print_usage(commands)
        exit()

    command = parse_command(commands, sys.argv[1:])
    command.execute()


def get_commands():
    commands = (CreateOrder, UpdateOrder, ShipOrder)
    return dict([cls.name, cls] for cls in commands)


def print_usage(commands):
    print("Usage: python -m Command CommandName [arguments]")
    print("Commands:")
    for command in commands.values():
        print(f"  {command.description}")


def parse_command(commands, args):
    command = commands.setdefault(args[0], NoCommand)
    s = inspect.signature(command)
    return command(args) if len(s.parameters) else command()


if __name__ == "__main__":
    main()

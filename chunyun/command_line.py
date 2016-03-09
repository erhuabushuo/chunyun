import argparse
import sys

from .create_command import CreateCommand
from .init_command import InitCommand


def get_command(command):
    """
    Let's be dynamic
    :return: command
    """
    commands = {'create': CreateCommand, 'init': InitCommand}
    return commands.get(command, None)


def main():
    """
    命令工具户主入口
    :return: None
    """
    parser = argparse.ArgumentParser(description="A simple database migration tool")

    subparsers = parser.add_subparsers(help="commands", dest="command")
    # create
    create_parser = subparsers.add_parser("create", help="Create a new project")
    create_parser.add_argument('dirname', action='store', default='.',
                               help="The directory to create your project. (default: %(default)s)")

    # init
    init_parser = subparsers.add_parser("init", help="Init your project")

    arguments = parser.parse_args()
    if arguments.command is None:
        print(parser.print_help())
        return

    Command = get_command(arguments.command)
    if Command is None:
        print("An error occurred", file=sys.stderr)
        sys.exit(-1)

    command = Command(arguments)
    command.run()










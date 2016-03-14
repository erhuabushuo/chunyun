from unittest import TestCase
import os
import shutil

from chunyun.command_line import parse_args
from chunyun.create_command import CreateCommand


class TestBase(TestCase):

    def setUp(self):
        # 通过命令行执行：chunyun create .
        arguments = parse_args(['create', '.'])
        command = CreateCommand(arguments)
        command.run()

    def tearDown(self):
        os.remove("config.ini")
        shutil.rmtree("migrations")


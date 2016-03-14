import os

from .test_base import TestBase
from chunyun.command_line import parse_args
from chunyun.create_command import CONFIG_TPL


class TestCreateCommand(TestBase):

    def test_will_create_config_ini_file(self):
        # 此时当前应该产生了config.ini文件
        self.assertTrue(os.path.exists('config.ini'), "config.ini文件不存在！")
        # 文件内容为初始化状态
        with open("config.ini") as handle:
            self.assertEqual(CONFIG_TPL, handle.read())

    def test_will_create_migrations_folder(self):
        # 此时应该存在目录migrations
        self.assertTrue(os.path.exists("migrations"))

    def test_duplicate_create_will_raise_exception(self):
        # 如果重复create项目应该抛出Exception
        with self.assertRaises(Exception):
            self.setUp()



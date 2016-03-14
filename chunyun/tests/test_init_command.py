import os
from unittest.mock import Mock

from .test_base import TestBase
from chunyun.command_line import parse_args
from chunyun.init_command import InitCommand


class TestInitCommand(TestBase):
    def setUp(self):
        super(TestInitCommand, self).setUp()
        self.mock_create_migration_table = Mock()
        self.mock_insert_init_record = Mock()
        arguments = parse_args(['init'])
        command = InitCommand(arguments)
        command.dump = Mock(return_value="whatever")
        command.create_migration_table = self.mock_create_migration_table
        command.insert_init_record = self.mock_insert_init_record
        command.run()


    def test_init_will_create_001_init_sql(self):
        self.assertTrue(os.path.exists(os.path.join("migrations", "001_init.sql")))

    def test_dump_sql_to_001_init_sql(self):
        with open(os.path.join("migrations", "001_init.sql")) as handle:
            content = handle.read()
            self.assertIn("whatever", content)

    def test_assert_create_migration_table_is_called(self):
        self.assertTrue(self.mock_create_migration_table.called)

    def test_assert_insert_init_record_is_called(self):
        self.assertTrue(self.mock_insert_init_record.called)

    def tearDown(self):
        super(TestInitCommand, self).tearDown()





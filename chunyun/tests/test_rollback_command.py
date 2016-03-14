import os
import builtins
from unittest.mock import Mock, mock_open, patch, ANY

from .test_base import TestBase
from chunyun.command_line import parse_args
from chunyun.rollback_command import RollbackCommand


class TestRollBackCommand(TestBase):

    def setUp(self):
        super(TestRollBackCommand, self).setUp()
        with patch("os.path.exists") as m:
            m.return_value = True
            arguments = parse_args(['rollback',])
            self.open_mock = mock_open(read_data='create table users\n-- @down\ndrop table users;')
            self.get_latest_migration_mock = Mock(return_value="002_create_user.sql")
            self.sync_migration_mock = Mock()
            self.remove_migration_record_mock = Mock()
            with patch.object(builtins, 'open', self.open_mock):
                command = RollbackCommand(arguments)
                command.get_latest_migration = self.get_latest_migration_mock
                command.sync_migration = self.sync_migration_mock
                command.remove_migration_record = self.remove_migration_record_mock
                command.run()

    def test_open_file_correct(self):
        self.open_mock.assert_called_with(os.path.join("migrations", "002_create_user.sql"))

    def test_sync_sql(self):
        self.sync_migration_mock.assert_called_once_with(ANY, "\ndrop table users;")

    def test_remove_migration_record(self):
        self.remove_migration_record_mock.assert_called_once_with(ANY, "002_create_user.sql")


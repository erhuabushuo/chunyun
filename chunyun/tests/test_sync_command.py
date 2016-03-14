import os
from unittest.mock import Mock, patch, mock_open, ANY
import builtins

from .test_base import TestBase
from chunyun.command_line import parse_args
from chunyun.sync_command import SyncCommand


class TestSyncCommand(TestBase):
    def setUp(self):
        super(TestSyncCommand, self).setUp()
        arguments = parse_args(['sync',])
        self.open_mock = mock_open(read_data='create table users\n-- @down')
        self.get_latest_migration_mock = Mock(return_value="002_create_user.sql")
        self.get_migration_files_mock = Mock(return_value=["001_init.sql", "002_create_user.sql", "003_whatever.sql"])
        self.sync_migration_mock = Mock()
        self.insert_migration_record_mock = Mock()
        with patch.object(builtins, 'open', self.open_mock):
            command = SyncCommand(arguments)
            command.get_latest_migration = self.get_latest_migration_mock
            command.get_migration_files = self.get_migration_files_mock
            command.sync_migration = self.sync_migration_mock
            command.insert_migration_record = self.insert_migration_record_mock
            command.run()

    def test_open_file_correct(self):
        self.open_mock.assert_called_with(os.path.join("migrations", "003_whatever.sql"))

    def test_sync_sql(self):
        self.sync_migration_mock.assert_called_once_with(ANY, "create table users\n")

    def test_insert_migration_record(self):
        self.insert_migration_record_mock.assert_called_once_with(ANY, "003_whatever.sql")










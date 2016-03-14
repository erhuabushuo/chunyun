import os
from configparser import ConfigParser
from tempfile import NamedTemporaryFile
import subprocess

from .command import Command

GET_LATEST_MIGRATION = "'SELECT name FROM chunyun_migrations ORDER BY ID DESC LIMIT 1'"
NEW_MIGRATION = "'INSERT INTO chunyun_migrations(name) VALUES($${0}$$)'"


class SyncCommand(Command):

    def get_latest_migration(self, option):
        os.environ['PGPASSWORD'] = option.get(self.args.env, "password")
        cmd = "psql -h {host} -p {port}  -U {user} {name} -t -c {sql}".format(
                            host=option.get(self.args.env, 'host'),
                            port=option.get(self.args.env, 'port'),
                            user=option.get(self.args.env, 'user'),
                            name=option.get(self.args.env, 'database'),
                            sql=GET_LATEST_MIGRATION)
        handle = os.popen(cmd)
        output = handle.read().strip()
        handle.close()
        return output

    def insert_migration_record(self, option, name):
        os.environ['PGPASSWORD'] = option.get(self.args.env, "password")
        cmd = "psql -h {host} -p {port}  -U {user} {name} -c {sql}".format(
                            host=option.get(self.args.env, 'host'),
                            port=option.get(self.args.env, 'port'),
                            user=option.get(self.args.env, 'user'),
                            name=option.get(self.args.env, 'database'),
                            sql=NEW_MIGRATION.format(name))
        handle = os.popen(cmd)
        output = handle.read()
        handle.close()
        #print(output)

    def sync_migration(self, option, sql):
        handle = NamedTemporaryFile(delete=False)
        os.chmod(handle.name, 0o777)
        handle.write(sql.encode("utf-8"))
        handle.close()
        os.environ['PGPASSWORD'] = option.get(self.args.env, "password")
        cmd = "psql -h {host} -p {port}  -U {user} {name} -f '{file}'".format(
                            host=option.get(self.args.env, 'host'),
                            port=option.get(self.args.env, 'port'),
                            user=option.get(self.args.env, 'user'),
                            name=option.get(self.args.env, 'database'),
                            file=str(handle.name))
        cmd_handle = os.popen(cmd)
        output = cmd_handle.read()
        cmd_handle.close()
        os.unlink(handle.name)

    def get_migration_files(self):
        files = os.listdir('migrations')
        files.sort()
        return files

    def run(self):
        parser = ConfigParser()
        parser.read("config.ini")

        # 获取migrations表里最新同步文件
        latest_migration = self.get_latest_migration(parser)
        files = self.get_migration_files()

        idx = -1
        try:
            idx = files.index(latest_migration)
        except:
            pass

        for file in files[idx+1:]:
            with open(os.path.join("migrations", file)) as handle:
                sql = handle.read()
                sql, _ = sql.split("-- @down")
                self.sync_migration(parser, sql)
                self.insert_migration_record(parser, file)

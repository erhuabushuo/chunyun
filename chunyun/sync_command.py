import os

from .command import Command

GET_MIGRATIONS_RECORDS = "'SELECT name FROM chunyun_migrations WHERE '"


class SyncCommand(Command):

    def create_migration_table(self, option):
        os.environ['PGPASSWORD'] = option.get(self.args.env, "password")
        cmd = "psql -h {host} -p {port}  -U {user} {name} -c {sql}".format(
                            host=option.get(self.args.env, 'host'),
                            port=option.get(self.args.env, 'port'),
                            user=option.get(self.args.env, 'user'),
                            name=option.get(self.args.env, 'database'),
                            sql=GET_MIGRATIONS_RECORDS)
        handle = os.popen(cmd)
        output = handle.read()
        handle.close()
        print(output)

    def run(self):
        pass

class User:
    def __init__(self, conn):
        self.conn = conn

    def drop_table(self):
        cmd = '''
            DROP TABLE IF EXISTS users
        '''
        try:
            self.conn.execute(cmd)
            print("Dropped users table")
            self.conn.commit()
        except Exception as e:
            print(e)
            return

    def create_table(self):
        cmd = '''
                CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                gender text NOT NULL,
                age INTEGER NOT NULL,
                occupation text NOT NULL,
                zipcode TEXT NOT NULL
                )
        '''

        try:
            self.conn.execute(cmd)
            self.conn.commit()
            print("Table users created")
        except Exception as e:
            print(e)
            return

    def insert(self, uid, gender, age, occupation, zip):
        cmd = ''' INSERT INTO users values (?, ?, ?, ?, ?)'''
        try:
            self.conn.execute(cmd, [uid, gender, int(age), occupation, zip])
            self.conn.commit()
        except Exception as e:
            print(e)
            return

    def load_table(self):
        count = 0
        with open("ml-1m/users.dat") as f:
            for line in f:
                uid, gender, age, occupation, zip = line.strip().split('::')
                self.insert(uid, gender, age, occupation, zip)
                count += 1
            self.conn.commit()
            print(f'Inserted {count} users')





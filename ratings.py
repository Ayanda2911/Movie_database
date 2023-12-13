import sqlite3


class Rating:
    def __init__(self, conn):
        self.conn = conn
        self.c = conn.cursor()
    def drop_table(self):
        cmd = """ drop table if exists ratings """
        try:
            self.conn.execute(cmd)
            print("Dropped ratings table")
            self.conn.commit()
        except Exception as e:
            print(e)
            return

    def create_table(self):
        # UserID::MovieID::Rating::Timestamp
        cmd = """
            create table if not exists ratings(
                id INTEGER PRIMARY KEY,
                user_id INTEGER NOT NULL,
                movie_id INTEGER NOT NULL,
                rating INTEGER NOT NULL,
                timestamp INTEGER NOT NULL,
                FOREIGN KEY(user_id) REFERENCES users(id),
                FOREIGN KEY(movie_id) REFERENCES movies(id)
            )
        """
        try:
            self.conn.execute(cmd)
            self.conn.commit()
            print("Table ratings created")
        except Exception as e:
            print(e)
            return
    def insert(self, uid, mid, rating, timestamp):
        cmd = """ insert into ratings(user_id, movie_id, rating, timestamp) values (?, ?, ?, ?)"""
        try:
            self.conn.execute(cmd, [uid, mid, rating, timestamp])
            self.conn.commit()
        except Exception as e:
            print(e)
            return
    def load_table(self):
        count = 0
        with open('ml-1m/ratings.dat') as f:
            for line in f:
                uid, mid, rating, timestamp = line.strip().split('::')
                self.insert(uid, mid, rating, timestamp)
                count += 1
            self.conn.commit()
            print(f'Inserted {count} ratings')





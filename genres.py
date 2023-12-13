import sqlite3
class Genre:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.c = conn.cursor()

    def drop_table(self):
        drop = "DROP TABLE IF EXISTS genres"
        try:
            self.conn.execute(drop)
            print("Dropped genres table")
            self.conn.commit()
        except Exception as e:
            print(e)
            return

    def create_table(self):
        cmd = """
                CREATE TABLE IF NOT EXISTS genres(
                id INTEGER NOT NULL,
                genre TEXT NOT NULL ,
                FOREIGN KEY(id) references movies(id) ON DELETE CASCADE,
                PRIMARY KEY (id, genre) 
                )
        """
        try:
            self.conn.execute(cmd)
            self.conn.commit()
            print("Table genres created")
        except Exception as e:
            print(e)
            return

    def insert(self, id, genre):
        insert = ''' INSERT INTO genres values (?, ?)'''
        try:
            self.conn.execute(insert, [id, genre])
            self.conn.commit()
        except Exception as e:
            print(e)
            return

    def load_table(self):
        count = 0
        with open('ml-1m/movies.dat') as f:
            for line in f:
                id, _, genres = line.strip().split('::')
                for genre in genres.split('|'):
                    self.insert(id, genre)
                    count += 1
            self.conn.commit()
            print(f'Inserted {count} genres')




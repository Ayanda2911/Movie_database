import sqlite3


class Movie:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.c = conn.cursor()

    def create_table(self):
        cmd = '''
            CREATE TABLE IF NOT EXISTS movies (
            id text PRIMARY KEY,
            title TEXT NOT NULL,
            year INTEGER NOT NULL
        )
        '''
        try:
            self.c.execute(cmd)
            self.conn.commit()
            print("Movies table created")
        except Exception as e:
            print(e)
            return

    def insert(self, id, title, year):
        cmd = ''' INSERT INTO movies values (?, ?, ?)'''

        try:
            self.c.execute(cmd, [id, title, int(year)])
            self.conn.commit()
        except Exception as e:
            print(e)
            return

    def drop_table(self):
        cmd = ''' drop table if exists movies'''
        try:
            self.c.execute(cmd)
            print("Dropped movies table")
            self.conn.commit()
        except Exception as e:
            print(e)
            return

    def load_table(self):
        count = 0
        with open('ml-1m/movies.dat', 'r') as f:
            for line in f:
                id, titleandyear,_ = line.strip().split('::')
                title, year = titleandyear[:-7], titleandyear[-5:-1]
                self.insert(id, title, year)
                count += 1
            self.conn.commit()
            print(f'Inserted {count} movies')

    def sort_average_rating(self):
        cmd = '''select 
                        movies.title, round(avg(ratings.rating), 2) as avg_rating 
                from 
                    movies join ratings on movies.id = ratings.movie_id 
                group by movies.title, movies.id 
                order by avg_rating desc'''
        try:
            self.c.execute(cmd)
            rv = []
            for row in self.c:
                rv.append(row)
            return rv
        except Exception as e:
            print(e)
            return

    #For each movie, calculate the average rating by male and female users .
    # e.g. Movie_Name - 3.5 (Avg. male users rating) - 4.5 (Avg. female Users rating)
    def average_rating_by_gender(self):
        cmd = '''select 
                        movies.title, users.gender , round(avg(ratings.rating), 2) as avg_rating 
                from 
                    movies 
                    join ratings on movies.id = ratings.movie_id
                    join users on users.id = ratings.user_id
                group by movies.id , movies.title, users.gender
                order by avg_rating desc'''
        try:
            self.c.execute(cmd)
            rv = []
            for row in self.c:
                rv.append(row)
            return rv
        except Exception as e:
            print(e)
            return
    def genre_distribution_analysis_by_year(self):
        cmd = '''
                select year, genre, count(*) as count
                from movies join genres on movies.id = genres.id
                group by year, genre      
        '''

        try:
            self.c.execute(cmd)
            rv = []
            for row in self.c:
                rv.append(row)
            return rv
        except Exception as e:
            print(e)
if __name__ == "__main__":
    conn = sqlite3.connect('MoviesDatabase.db')
    m = Movie(conn)



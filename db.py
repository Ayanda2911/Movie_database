import sqlite3
import genres
import movies
import ratings
import users


class MoviesDatabase:
    def __init__(self, rebuild: bool = False):
        try:
            self.conn = sqlite3.connect('MoviesDatabase.db')
            self.conn.execute("PRAGMA foreign_keys = ON")
            self.movies = movies.Movie(self.conn)
            self.genres = genres.Genre(self.conn)
            self.ratings = ratings.Rating(self.conn)
            self.users = users.User(self.conn)

            if rebuild:
                print("---Rebuilding database---")
                print("Dropping tables...")
                self.genres.drop_table()
                self.ratings.drop_table()
                self.users.drop_table()
                self.movies.drop_table()

                print("Creating tables...")
                self.movies.create_table()
                self.genres.create_table()
                self.ratings.create_table()
                self.users.create_table()

                print("Loading tables...")
                self.movies.load_table()
                self.genres.load_table()
                self.users.load_table()
                self.ratings.load_table()
                print("---Rebuilding complete---")
        except Exception as e:
            print(e)
            return

    def genre_distribution_analysis_by_year(self):
        return self.movies.genre_distribution_analysis_by_year()

    def sort_average_rating(self):
        return self.movies.sort_average_rating()

    def average_rating_by_gender(self):
        return self.movies.average_rating_by_gender()

    def close(self):
        self.conn.close()



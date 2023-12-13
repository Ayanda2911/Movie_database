import db
import tabulate as t


def display_menu():
    print("1. Genre Distribution Analysis by Year")
    print("2. Sort Movies by Average Rating")
    print("3. Average Rating by Gender")
    print("4. Exit")

class ConsoleApp:
    def __init__(self):
        self.db = db.MoviesDatabase(rebuild=True)

    def output(self):
        while True:
            display_menu()
            choice = input("Enter your choice (1-4): ").strip()

            match choice:
                case "1":
                    print(t.tabulate(self.db.genre_distribution_analysis_by_year(),
                            headers=['Year', 'Genre', 'Count'], tablefmt='psql'))
                case "2":
                    print(t.tabulate(self.db.sort_average_rating(),
                            headers=['Title', 'Average Rating'], tablefmt='psql'))
                case "3":
                    print(t.tabulate(self.db.average_rating_by_gender(),
                            headers=['Title', 'Gender', 'Average Rating'], tablefmt='psql'))
                case "4":
                    self.exit_program()
                    self.db.close()
                    print("Exiting program. Goodbye!")
                case _:
                    print("Invalid choice. Please enter a number between 1 and 4.")

    def exit_program(self):
        print("Exiting program. Goodbye!")
        exit()
class Publication:
    def __init__(self):
        self.title = ""
        self.price = 0.0

    def get(self):
        self.title = input("Enter the title: ")
        self.price = float(input("Enter the price: "))

    def set(self):
        print(f"Title: {self.title}, Price: ${self.price:.2f}")


class Book(Publication):
    def __init__(self):
        super().__init__()
        self.page_count = 0

    def get(self):
        super().get()  # Get title and price from Publication
        self.page_count = int(input("Enter the page count: "))

    def set(self):
        super().set()  # Display title and price
        print(f"Page Count: {self.page_count}")


class Tape(Publication):
    def __init__(self):
        super().__init__()
        self.playing_time = 0

    def get(self):
        super().get()  # Get title and price from Publication
        self.playing_time = int(input("Enter the playing time (in minutes): "))

    def set(self):
        super().set()  # Display title and price
        print(f"Playing Time: {self.playing_time} minutes")


def main():
    print("Enter details for a Book:")
    book = Book()
    book.get()
    print("\nBook Details:")
    book.set()

    print("\nEnter details for a Tape:")
    tape = Tape()
    tape.get()
    print("\nTape Details:")
    tape.set()


if __name__ == "__main__":
    main()

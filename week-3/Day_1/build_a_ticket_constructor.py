class MovieTicket:
    def __init__(self, movie, seats_available, seats_requested):
        self.movie = movie
        self.seats_available = seats_available
        self.seats_requested = seats_requested
        self.confirmed_seats = min(seats_available, seats_requested)

        if seats_available >= seats_requested:
            self.message = "Full request confirmed"
        else:
            self.message = "Only partial seats available"

    def display(self):
        print("Movie:", self.movie)
        print("Confirmed Seats:", self.confirmed_seats)
        print("Status:", self.message)
        print()


ticket1 = MovieTicket("Inception", 100, 5)
ticket2 = MovieTicket("The Matrix", 50, 60)

ticket1.display()
# Number of seats available in ticketing system
NUM_SEATS = 500

class TicketSystem:
    def __init__(self):
        self.next_seat = 1
        self.returned = []
    def has_tickets(self):
        return self.next_seat <= NUM_SEATS or self.returned
    def next_ticket(self):
        if self.returned:
            return self.returned.pop(0)
        elif self.next_seat <= NUM_SEATS:
            ticket = self.next_seat
            self.next_seat += 1
            return ticket
        else:
            return -1
    def return_ticket(self, ticket):
        self.returned.append(ticket)
"""
File: counter.py
----------------
This file defines a Class for a Counter that simply issues
a sequential series of integers (tickets) starting at 1.  A new
number (ticket) is produced when the Counter is asked for the next
ticket.
"""


class Counter:

    def __init__(self):
        """
        Creates a Counter object and initializes the internal ticket number
        """
        self.ticket_num = 0   # instance variable to keep track of tickets

    def next_value(self):
        """
        Returns the next ticket number for this counter.
        """
        self.ticket_num += 1
        return self.ticket_num

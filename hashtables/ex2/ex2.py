#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    cache = {}
    for ticket in tickets:
        ticket.next = ticket.destination
        cache[ticket.source] = ticket.next

    route = []
    current = cache["NONE"]
    
    for i in range(length):
        route.append(current)
        current = cache[current]
    
    return route

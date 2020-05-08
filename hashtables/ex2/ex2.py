class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):

    cache = {}
    route = []
    
    """
    YOUR CODE HERE
    """

    for index, ticket in enumerate(tickets):
        cache[ticket.source] = ticket.destination
    first_ticket = cache['NONE']
    while first_ticket is not 'NONE':
        route.append(first_ticket)
        first_ticket = cache[first_ticket]
    route.append(first_ticket)
    
    return route
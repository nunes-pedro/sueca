
class Round:
    """ Class for the round logic, diagram available in doc """
    self.iteration = 0
    self.ready = False

    def __init__(self, players, deck):
        roles = ['shuffler', 'none', 'cutter', 'dealer']
        if(len(players) == 4):
            for i in range(4):
                players[i].assignRole(roles[((-self.iteration + i) % 4)])
            # self.iteration += 1
            for p in players:
                trump = p.doJob(deck)
            self.trump = trump  # Major chance of conflict, observe behavior
            self.ready = True  # This supposedly triggers an event
        else:
            print('Non correct number of players in the table')

    def playHand(self, players):
        # this is the event triggered
        h = Hand(trump, players)


class Hand:
    """ Class for hand logic """
    self.iteration = 0

    def __init__(self, trump):
        self._trump = trump

    def checkWinner(self):
        pass

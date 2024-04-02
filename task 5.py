class Game:
    def __init__(self, team_info):
        self.teams = team_info
        self.score = {team_info['command1']: 0, team_info['command2']: 0}

    def ball_thrown(self, command, points):
        """
        Method adds points scored to the team
        """
        if command == 1:
            self.score[team_info['command1']] = points
        if command == 2:
            self.score[team_info['command2']] = points

    def get_score(self):
        """
        Method that outputs the current account
        """
        return f"{(self.score[team_info['command1']], self.score[team_info['command2']])}"

    def get_winner(self):
        """
        Method that outputs the winner in the game
        """
        if self.score[team_info['command1']] < self.score[team_info['command2']]:
            return team_info['command2']
        if self.score[team_info['command1']] > self.score[team_info['command2']]:
            return team_info['command1']
        if self.score[team_info['command1']] == self.score[team_info['command2']]:
            return 'Ничья'


team_info = {'command1': 'team A', 'command2': 'team B'}
game = Game(team_info)
game.ball_thrown(1, 5)
print(game.get_score())
print(game.get_winner())



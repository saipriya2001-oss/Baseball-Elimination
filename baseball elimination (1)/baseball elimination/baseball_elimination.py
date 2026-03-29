import sys

class BaseballElimination:
    """
    Python implementation of the Baseball Elimination trivial logic.
    Provides methods to check if a team is mathematically eliminated based on 
    current wins and remaining games.
    """
    
    def __init__(self, filename):
        """Constructor: Read teams and statistics from file."""
        try:
            with open(filename, 'r') as f:
                lines = [line.strip() for line in f if line.strip()]
            
            if not lines:
                raise ValueError("The file is empty")
                
            self.n = int(lines[0])
            self.team_names = []
            self.wins_list = []
            self.losses_list = []
            self.remaining_list = []
            self.games = [[0] * self.n for _ in range(self.n)]
            self.team_to_index = {}
            
            for i in range(self.n):
                parts = lines[i + 1].split()
                team = parts[0]
                self.team_names.append(team)
                self.team_to_index[team] = i
                self.wins_list.append(int(parts[1]))
                self.losses_list.append(int(parts[2]))
                self.remaining_list.append(int(parts[3]))
                
                # Games played against other teams
                for j in range(self.n):
                    self.games[i][j] = int(parts[4 + j])
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            sys.exit(1)
        except Exception as e:
            print(f"Error reading file: {e}")
            sys.exit(1)

    def number_of_teams(self):
        """Returns the number of teams."""
        return self.n

    def teams(self):
        """Returns all team names."""
        return self.team_names

    def _validate_team(self, team):
        """Validates team name and returns its index."""
        if team not in self.team_to_index:
            raise ValueError(f"Invalid team name: {team}")
        return self.team_to_index[team]

    def wins(self, team):
        """Returns wins for the given team."""
        return self.wins_list[self._validate_team(team)]

    def losses(self, team):
        """Returns losses for the given team."""
        return self.losses_list[self._validate_team(team)]

    def remaining(self, team):
        """Returns remaining games for the given team."""
        return self.remaining_list[self._validate_team(team)]

    def against(self, team1, team2):
        """Returns games left between team1 and team2."""
        idx1 = self._validate_team(team1)
        idx2 = self._validate_team(team2)
        return self.games[idx1][idx2]

    def is_eliminated(self, team):
        """Trivial Elimination logic: Checks if w[x] + r[x] < w[i]."""
        x = self._validate_team(team)
        max_wins_potential = self.wins_list[x] + self.remaining_list[x]
        
        for i in range(self.n):
            if i == x:
                continue
            if max_wins_potential < self.wins_list[i]:
                return True  # Trivially eliminated by team i
        
        return False

    def certificate_of_elimination(self, team):
        """Returns a list of teams that eliminate the given team (trivial case)."""
        x = self._validate_team(team)
        max_wins_potential = self.wins_list[x] + self.remaining_list[x]
        
        for i in range(self.n):
            if i != x and max_wins_potential < self.wins_list[i]:
                return [self.team_names[i]]
        
        return None

def main():
    """Simple test block similar to the Java main method."""
    if len(sys.argv) < 2:
        filename = "teams4.txt"
    else:
        filename = sys.argv[1]
        
    division = BaseballElimination(filename)
    for team in division.teams():
        if division.is_eliminated(team):
            cert = division.certificate_of_elimination(team)
            cert_str = " ".join(cert) if cert else ""
            print(f"{team} is eliminated by the subset {{ {cert_str} }}")
        else:
            print(f"{team} is not eliminated")

if __name__ == "__main__":
    main()

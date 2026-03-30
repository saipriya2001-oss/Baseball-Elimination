import sys
from team_manager import TeamManager
from elimination_checker import check_elimination

def main():
    """
    Main entry point for the Baseball Elimination application.
    """
    try:
        # Read n teams
        line = sys.stdin.readline().strip()
        if not line:
            return
        n = int(line)
        
        data = []
        for _ in range(n):
            row = sys.stdin.readline().split()
            if not row:
                break
            data.append(row)
            
        if len(data) < n:
            print("Error: Incomplete data provided.")
            return

        # Initialize team manager
        tm = TeamManager(n, data)
        
        # Check elimination for each team
        for team in tm.teams:
            eliminated, sub_r = check_elimination(tm, team)
            if eliminated:
                print(f"{team} is eliminated by the subset R = {sub_r}")
            else:
                print(f"{team} is not eliminated")
                
    except ValueError as e:
        print(f"Error: Invalid input format ({e})")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

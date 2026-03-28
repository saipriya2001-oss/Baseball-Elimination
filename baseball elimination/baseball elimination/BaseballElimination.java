import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdOut;
import java.util.HashMap;
import java.util.ArrayList;

public class BaseballElimination {

    private final int n; // [AI-Assisted] Number of teams
    private final String[] teamNames; // [AI-Assisted] Team names
    private final int[] wins; // [AI-Assisted] Wins per team
    private final int[] losses; // [AI-Assisted] Losses per team
    private final int[] remaining; // [AI-Assisted] Remaining games per team
    private final int[][] games; // [AI-Assisted] Games against other teams
    private final HashMap<String, Integer> teamToIndex; // [AI-Assisted] Quick lookup map

    // [AI-Assisted] Constructor: Read teams and statistics from file
    public BaseballElimination(String filename) {
        if (filename == null) throw new IllegalArgumentException("filename is null");
        
        In in = new In(filename);
        if (!in.exists()) throw new IllegalArgumentException("file does not exist");
        
        this.n = in.readInt();
        this.teamNames = new String[n];
        this.wins = new int[n];
        this.losses = new int[n];
        this.remaining = new int[n];
        this.games = new int[n][n];
        this.teamToIndex = new HashMap<>();

        for (int i = 0; i < n; i++) {
            String team = in.readString();
            teamNames[i] = team;
            teamToIndex.put(team, i);
            wins[i] = in.readInt();
            losses[i] = in.readInt();
            remaining[i] = in.readInt();
            for (int j = 0; j < n; j++) {
                games[i][j] = in.readInt();
            }
        }
    }

    // [AI-Assisted] Returns the number of teams
    public int numberOfTeams() {
        return n;
    }

    // [AI-Assisted] Returns all team names as an Iterable
    public Iterable<String> teams() {
        ArrayList<String> list = new ArrayList<>();
        for (String team : teamNames) {
            list.add(team);
        }
        return list;
    }

    // [AI-Assisted] Validates team name and returns its index
    private int validateTeam(String team) {
        if (team == null || !teamToIndex.containsKey(team)) {
            throw new IllegalArgumentException("Invalid team name: " + team);
        }
        return teamToIndex.get(team);
    }

    // [AI-Assisted] Returns wins for the given team
    public int wins(String team) {
        return wins[validateTeam(team)];
    }

    // [AI-Assisted] Returns losses for the given team
    public int losses(String team) {
        return losses[validateTeam(team)];
    }

    // [AI-Assisted] Returns remaining games for the given team
    public int remaining(String team) {
        return remaining[validateTeam(team)];
    }

    // [AI-Assisted] Returns games left between team1 and team2
    public int against(String team1, String team2) {
        return games[validateTeam(team1)][validateTeam(team2)];
    }

    // [AI-Assisted] Trivial Elimination logic: Checks if w[x] + r[x] < w[i]
    public boolean isEliminated(String team) {
        int x = validateTeam(team);
        int maxWinsPotential = wins[x] + remaining[x];
        
        for (int i = 0; i < n; i++) {
            if (i == x) continue;
            if (maxWinsPotential < wins[i]) {
                return true;
            }
        }
        
        return false;
    }

    // [AI-Assisted] Certificate of elimination (to be implemented in the second half)
    public Iterable<String> certificateOfElimination(String team) {
        validateTeam(team);
        // Trivial case for certificate
        int x = validateTeam(team);
        int maxWinsPotential = wins[x] + remaining[x];
        for (int i = 0; i < n; i++) {
            if (i != x && maxWinsPotential < wins[i]) {
                ArrayList<String> cert = new ArrayList<>();
                cert.add(teamNames[i]);
                return cert;
            }
        }
        return null; // For now
    }

    public static void main(String[] args) {
        // [AI-Assisted] Simple test with teams4.txt
        BaseballElimination division = new BaseballElimination("teams4.txt");
        for (String team : division.teams()) {
            if (division.isEliminated(team)) {
                StdOut.print(team + " is eliminated by the subset { ");
                for (String t : division.certificateOfElimination(team)) {
                    StdOut.print(t + " ");
                }
                StdOut.println("}");
            }
            else {
                StdOut.println(team + " is not eliminated");
            }
        }
    }
}

namespace day02; 
    
internal static class Program
{
    private static readonly Dictionary<string, int> ColorInd =
        new Dictionary<string, int>
        {
            { "red", 0 }, { "green", 1 }, { "blue", 2 }
        };
    
    public static void Main(string[] args)
    {
        if (args.Length != 1)
        {
            Console.WriteLine("Bad arguments!");
            Environment.Exit(1);
        }

        var inputPath = args[0];
        if (!File.Exists(inputPath))
        {
            Console.WriteLine("File does not exist!");
            Environment.Exit(1);
        }

        var games = (from game in File.ReadAllLines(inputPath) select ParseGame(game)).ToList();
        

        List<int> bag = [12, 13, 14];
        var possibleGames = from game in games select GameIsPossible(game, bag);
        var sumOfIds = possibleGames.Sum();

        Console.WriteLine("Part 01:");
        Console.WriteLine($"Answer = {sumOfIds}");
        
        Console.WriteLine();

        var cubePowers = from game in games select CalcCubePowers(game);
        var sumOfPowers = cubePowers.Sum();
        
        Console.WriteLine("Part 01:");
        Console.WriteLine($"Answer = {sumOfPowers}");
    }

    private static List<List<int>> ParseGame(string gameString)
    {
        var game = gameString.Split(": ");
        var rounds = game[1].Split("; ");
        var gameId = int.Parse(game[0].Split(" ")[1]);
        List<List<int>> cubeCombos = [[gameId]];
        foreach (var round in rounds)
        {
            List<int> roundColors = [ 0, 0, 0 ];
            foreach (var cubes in round.Split(", "))
            {
                var info = cubes.Split(" ");
                roundColors[ColorInd[info[1]]] = int.Parse(info[0]);
            }
            cubeCombos.Add(roundColors);
        }
        return cubeCombos;
    }

    private static int GameIsPossible(List<List<int>> game, List<int> bagCombo)
    {
        foreach (var round in game[1..])
        {
            for (var i = 0; i <= 2; ++i)
            {
                if (round[i] > bagCombo[i])
                {
                    return 0;
                }
            }
        }
        
        return game[0][0];
    }

    private static int CalcCubePowers(List<List<int>> game)
    {
        List<int> minCubes = [0, 0, 0];
        foreach (var round in game[1..])
        {
            for (var i = 0; i < minCubes.Count; ++i)
            {
                if (round[i] > minCubes[i] || minCubes[i] == -1)
                {
                    minCubes[i] = round[i];
                }
            }
        }
        return minCubes.Aggregate((x, y) => x * y);
    }
}
using Microsoft.VisualBasic.CompilerServices;

namespace day06;

internal static class Program
{
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

        var lines = File.ReadAllLines(inputPath);

        var times = lines[0].Split((char[]?) null, StringSplitOptions.RemoveEmptyEntries)[1..];
        var dists = lines[1].Split((char[]?) null,  StringSplitOptions.RemoveEmptyEntries)[1..];
        
        var margins = from race
                                    in times.Select(long.Parse).ToArray().Zip(dists.Select(long.Parse).ToArray())
                                    select CalcMargin(race.First, race.Second);
        var finalMargin = margins.Aggregate((x, y) => x * y);

        Console.WriteLine("Part 01:");
        Console.WriteLine($"Answer = {finalMargin}");

        Console.WriteLine();

        var time = long.Parse(string.Join("", times));
        var dist = long.Parse(string.Join("", dists));
        var margin = CalcMargin(time, dist);
        Console.WriteLine("Part 02:");
        Console.WriteLine($"Answer = {margin}");
    }

    private static int CalcMargin(long time, long dist)
    {
        var raceMargin = from speed in Enumerable.Range(0, (int) time)
                                       where speed * (time - speed) > dist select speed;
        return raceMargin.Count();
    }
}
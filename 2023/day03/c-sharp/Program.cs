namespace day03;

internal static class Program
{
    private static readonly List<(int, int)> AdjacentOffsets = [(-1, -1), (-1, 0), (-1, 1),
                                                                (0, -1),           (0, 1),
                                                                (1, -1),  (1, 0),  (1, 1)];
    
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

        Console.WriteLine("Part 01:");
        Console.WriteLine($"Answer = {null}");

        Console.WriteLine();

        Console.WriteLine("Part 02:");
        Console.WriteLine($"Answer = {null}");
    }
}
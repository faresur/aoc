namespace day04;

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
        
        var pointsWon = (from card in lines select GetPoints(card.Trim())).Sum();

        Console.WriteLine("Part 01:");
        Console.WriteLine($"Answer = {pointsWon}");

        Console.WriteLine();

        var amountOfCards = ProcessCards(lines).Sum();

        Console.WriteLine("Part 02:");
        Console.WriteLine($"Answer = {amountOfCards}");
    }

    private static int GetPoints(string card)
    {
        var nums = card.Split(": ")[1].Split("|");
        var firstNums = nums[0].Split((char[]?) null, StringSplitOptions.RemoveEmptyEntries);
        var secondNums = nums[1].Split((char[]?) null, StringSplitOptions.RemoveEmptyEntries);

        var winningNums = (from i in firstNums select int.Parse(i)).ToHashSet();
        var ownedNums = (from i in secondNums select int.Parse(i)).ToHashSet();
        winningNums.IntersectWith(ownedNums);
        return (int) Math.Pow(2, winningNums.Count - 1);
    }

    private static int[] ProcessCards(string[] cards)
    {
        var amountOfEach = new int[cards.Length];
        for (var i = 0; i < cards.Length; ++i)
        {
            amountOfEach[i] = 1;
        }
        for (var i = 0; i < cards.Length; ++i)
        {
            var nums = cards[i].Trim().Split(": ")[1].Split("|");
            var firstNums = nums[0].Split((char[]?) null, StringSplitOptions.RemoveEmptyEntries);
            var secondNums = nums[1].Split((char[]?) null, StringSplitOptions.RemoveEmptyEntries);

            var winningNums = (from k in firstNums select int.Parse(k)).ToHashSet();
            var ownedNums = (from k in secondNums select int.Parse(k)).ToHashSet();
            winningNums.IntersectWith(ownedNums);
            for (var j = i + 1; j < i + winningNums.Count + 1; ++j)
            {
                amountOfEach[j] += amountOfEach[i];
            }
        }
        return amountOfEach;
    }
}
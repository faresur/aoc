using System.Text.RegularExpressions;

namespace day01;

public static class Program
{
    private static Dictionary<string, string> Mappings { set; get; } = 
        new Dictionary<string, string>() {
            {"one", "1"}, {"two", "2"}, {"three", "3"},
            {"four", "4"}, {"five", "5"}, {"six", "6"},
            {"seven", "7"}, {"eight", "8"}, {"nine", "9"}
            
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
        
        var lines = File.ReadAllLines(inputPath);

        var calibrationValues = from line in lines select GetValue(line);
        var totalValue = calibrationValues.Sum();

        Console.WriteLine("Part 01:");
        Console.WriteLine($"Answer = {totalValue}");
        
        Console.WriteLine();
        
        var spelledValues = from line in lines select GetSpelledValue(line);
        var totalSpelledValue = spelledValues.Sum();
        
        Console.WriteLine("Part 02:");
        Console.WriteLine($"Answer = {totalSpelledValue}");
    }

    private static int GetValue(string line)
    {
        var matches = Regex.Matches(line, @"\d");
        return int.Parse(matches[0].ToString() + matches[^1].ToString());
    }

    private static int GetSpelledValue(string line)
    {
        const string regexPattern = @"\d|one|two|three|four|five|six|seven|eight|nine";
        var regex = new Regex(regexPattern);
        var matches = new List<Match>() { regex.Match(line) };
        while (matches[^1].Success)
        {
            matches.Add(regex.Match(line, matches[^1].Index + 1));
        }
        string numString1 = Mappings.GetValueOrDefault(matches[0].ToString()) ?? matches[0].ToString();
        string numString2 = Mappings.GetValueOrDefault(matches[^2].ToString()) ?? matches[^2].ToString();
        return int.Parse(numString1 + numString2);
    }
}
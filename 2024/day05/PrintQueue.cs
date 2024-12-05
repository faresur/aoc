List<string> inputLines = [];
while (Console.ReadLine() is { } input)
    inputLines.Add(input);

var splitIndex = inputLines.FindIndex(a => a == "");
var rules = inputLines[..splitIndex];
var updates = inputLines.Skip(splitIndex+1).ToList();

var updateComparer = new UpdateComparer(rules);

var updateSum = updates
    .Select(update => update.Split(",").Select(int.Parse).ToList())
    .Where(update =>
        new List<int>(update)
            .OrderBy(x => x, updateComparer)
            .SequenceEqual(update))
    .Sum(update => update[update.Count / 2]);

var incorrectUpdateSum = updates
    .Select(update =>
        (update.Split(",")
                .Select(int.Parse)
                .ToList(),
            update.Split(",")
                .Select(int.Parse)
                .OrderBy(x => x, updateComparer)
                .ToList()))
    .Where(updateWithExpected =>
        !updateWithExpected.Item1.SequenceEqual(updateWithExpected.Item2))
    .Sum(updateWithExpected =>
        updateWithExpected.Item2[updateWithExpected.Item2.Count / 2]);

Console.WriteLine($"Part 1 Answer: {updateSum}");
Console.WriteLine($"Part 2 Answer: {incorrectUpdateSum}");

internal class UpdateComparer : IComparer<int>
{
    private readonly Dictionary<int, HashSet<int>> _order;

    public UpdateComparer(IEnumerable<string> rules) => _order = rules
        .Select(rule => rule.Split("|").Select(int.Parse).ToList())
        .GroupBy(rule => rule[0])
        .ToDictionary(
            group => group.Key,
            group => group.Select(rule => rule[1]).ToHashSet());
    
    public int Compare(int x, int y)
    {
        if (_order.TryGetValue(x, out var greaterThanA) &&
            (greaterThanA?.Contains(y) ?? false))
            return -1;
        if (_order.TryGetValue(y, out var greaterThanB) &&
            (greaterThanB?.Contains(x) ?? false))
            return 1;
        return 0;
    }
}
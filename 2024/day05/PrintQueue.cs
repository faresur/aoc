List<string> inputLines = [];
var input = Console.ReadLine();
while (input is not null)
{
    inputLines.Add(input);
    input = Console.ReadLine();
}

var splitIndex = inputLines.FindIndex(a => a == "");

var order = inputLines[..splitIndex]
    .Select(rule => rule.Split("|").Select(int.Parse).ToList())
    .GroupBy(rule => rule[0])
    .ToDictionary(
        group => group.Key,
        group => group.ToList().Select(rule => rule[1]).ToHashSet());

var updateSum = inputLines.Skip(splitIndex + 1)
    .Select(update => update.Split(",").Select(int.Parse).ToList())
    .Where(update =>
    {
        var sorted = new List<int>(update);
        sorted.Sort(Compare);
        return Enumerable.SequenceEqual(sorted, update);
    })
    .Select(update => update[update.Count / 2])
    .Sum();

Console.WriteLine($"Part 1 Answer: {updateSum}");

var incorrectUpdateSum = inputLines.Skip(splitIndex + 1)
    .Select(update =>
    {
        var unSorted = update.Split(",").Select(int.Parse).ToList();
        var sorted = new List<int>(unSorted);
        sorted.Sort(Compare);
        return (!Enumerable.SequenceEqual(sorted, unSorted))
            ? sorted[sorted.Count / 2]
            : 0;
    })
    .Sum();

Console.WriteLine($"Part 2 Answer: {incorrectUpdateSum}");

int Compare(int a, int b)
{
    order.TryGetValue(a, out var greaterThanA);
    if (greaterThanA is not null && greaterThanA.Contains(b))
        return -1;
    
    order.TryGetValue(b, out var greaterThanB);
    if (greaterThanB is not null && greaterThanB.Contains(a))
        return 1;
    return 0;
}
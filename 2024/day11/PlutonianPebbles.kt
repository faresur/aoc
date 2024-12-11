fun applyRule(number: String): List<String> {
    if (number == "0")
        return listOf("1")
    if (number.length % 2 == 0)
        return listOf(number.take(number.length / 2).toLong().toString(),
            number.takeLast(number.length / 2).toLong().toString())
    return listOf((number.toLong() * 2024L).toString())
}

fun applyRuleCached(number: String, blinks: Int, cache: HashMap<Pair<String, Int>, Long>): Long {
    if (cache.containsKey(Pair(number, blinks)))
        return cache[Pair(number, blinks)]!!
    if (blinks == 1)
        return applyRule(number).size.toLong()
    val nextNumbers = applyRule(number)
    cache[number to blinks] = nextNumbers.sumOf { applyRuleCached(it, blinks - 1, cache) }
    return cache[number to blinks]!!
}

fun blinks(numbers: List<String>, blinks: Int): Long {
    val cache = HashMap<Pair<String, Int>, Long>()
    return numbers.sumOf { applyRuleCached(it, blinks, cache) }
}

fun main() {
    val numbers = readln().trim().split(" ")

    val part1Result = blinks(numbers, 25)
    println("Part 1 answer: $part1Result")

    val part2Result = blinks(numbers, 75)
    println("Part 2 answer: $part2Result")
}
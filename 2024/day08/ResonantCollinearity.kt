typealias Location = Pair<Int, Int>
typealias Antenna = Triple<String, Int, Int>

fun isWithinBounds(i: Int, j: Int, boundI: Int, boundJ: Int): Boolean = i >= 0 && j >= 0 && i < boundI && j < boundJ

fun findTwoClosestAntinodes(node1: Location,
                  node2: Location,
                  boundI: Int,
                  boundJ: Int): List<Location> {
    if (node1 == node2)
        return emptyList()
    val dX = node1.second - node2.second
    val dY = node1.first - node2.first
    return listOf(
        Location(node1.first + dY, node1.second + dX),
        Location(node2.first - dY, node2.second - dX)
    ).filter { isWithinBounds(it.first, it.second, boundI, boundJ) }
}

fun findAllClosestAntinodes(nodes: List<Location>, boundI: Int, boundJ: Int): List<Location> = nodes.map { node1 ->
    nodes.map { node2 ->
        findTwoClosestAntinodes(node1, node2, boundI, boundJ)
    }.flatten()
}.flatten().distinct()

tailrec fun findAntinodesNegative(accumAntinodes: List<Location>,
                                  node: Location,
                                  diff: Location,
                                  boundI: Int,
                                  boundJ: Int): List<Location> =
    if (!isWithinBounds(node.first, node.second, boundI, boundJ)) accumAntinodes
    else findAntinodesNegative(accumAntinodes + listOf(node),
        Location(node.first - diff.first, node.second - diff.second),
        diff, boundI, boundJ)

tailrec fun findAntinodesPositive(accumAntinodes: List<Location>,
                                  node: Location,
                                  diff: Location,
                                  boundI: Int,
                                  boundJ: Int): List<Location> =
    if (!isWithinBounds(node.first, node.second, boundI, boundJ)) accumAntinodes
    else findAntinodesPositive(accumAntinodes + listOf(node),
        Location(node.first + diff.first, node.second + diff.second),
        diff, boundI, boundJ)

fun findAntinodes(node1: Location,
                     node2: Location,
                     boundI: Int,
                     boundJ: Int): List<Location> {
    if (node1 == node2)
        return emptyList()
    val diff = Pair(node1.first - node2.first, node1.second - node2.second)
    return findAntinodesPositive(emptyList(), node1, diff, boundI, boundJ) +
            findAntinodesNegative(emptyList(), node2, diff, boundI, boundJ)
}

fun findAllAntinodes(nodes: List<Location>, boundI: Int, boundJ: Int): List<Location> = nodes.map { node1 ->
    nodes.map { node2 ->
        findAntinodes(node1, node2, boundI, boundJ)
    }.flatten()
}.flatten().distinct()

fun main() {
    val inputGrid = generateSequence(::readLine).map {
        it.toList().map(Char::toString).filter(String::isNotBlank)
    }.toList()

    val antennas: Map<String, List<Location>> = inputGrid.indices.map { i ->
        inputGrid[i].indices.filter{ j ->
            inputGrid[i][j] != "."
        }.map { j ->
            Antenna(inputGrid[i][j], i, j)
        }
    }.flatten().groupBy({ it.first }, { Location(it.second, it.third) })

    val amountOfClosestAntinodes = antennas.map {
        (_, nodes) -> findAllClosestAntinodes(nodes, inputGrid.size, inputGrid[0].size)
    }.flatten().distinct().count()

    val amountOfAntinodes = antennas.map {
        (_, nodes) -> findAllAntinodes(nodes, inputGrid.size, inputGrid[0].size)
    }.flatten().distinct().count()

    println("Part 1 answer: $amountOfClosestAntinodes")
    println("Part 2 answer: $amountOfAntinodes")
}
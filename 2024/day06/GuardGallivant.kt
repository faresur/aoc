enum class Direction {
    Up,
    Down,
    Left,
    Right
}

fun isOutOfBounds(i: Int, j: Int, boundI: Int, boundJ: Int): Boolean = !(i >= 0 && j >= 0 && i < boundI && j < boundJ)

fun moveInDirection(direction: Direction, position: Pair<Int, Int>): Pair<Int, Int> = when (direction) {
    Direction.Up -> Pair(position.first - 1, position.second)
    Direction.Down -> Pair(position.first + 1, position.second)
    Direction.Left -> Pair(position.first, position.second - 1)
    Direction.Right -> Pair(position.first, position.second + 1)
}

fun clockwiseTurn(direction: Direction): Direction = when (direction) {
    Direction.Up -> Direction.Right
    Direction.Down -> Direction.Left
    Direction.Left -> Direction.Up
    Direction.Right -> Direction.Down
}

tailrec fun walkPath(visited: List<Pair<Pair<Int, Int>, Direction>>,
                guardPosition: Pair<Int, Int>,
                direction: Direction,
                grid: List<List<String>>) : List<Pair<Pair<Int, Int>,Direction>> {
    var nextPosition = moveInDirection(direction, guardPosition)
    if (isOutOfBounds(nextPosition.first, nextPosition.second, grid.size, grid[0].size))
        return visited
    var nextDirection = direction
    while (grid[nextPosition.first][nextPosition.second] == "#") {
        nextDirection = clockwiseTurn(nextDirection)
        nextPosition = moveInDirection(nextDirection, guardPosition)
    }
    if (visited.contains(Pair(nextPosition, nextDirection)))
        throw Exception("Infinite loop detected!")
    val nextVisited = visited + Pair(nextPosition, nextDirection)
    return walkPath(nextVisited, nextPosition, nextDirection, grid)
}

fun amountOfPossibleObstacles(initialState: Pair<Pair<Int, Int>, Direction>,
                              walkedPath: List<Pair<Int, Int>>,
                              grid: MutableList<MutableList<String>>): Int {
    var total = 0
    val (initialPos, initialDir) = initialState
    for (position in walkedPath.drop(1)) {
        val (i, j) = position
        if (position == initialPos || isOutOfBounds(i, j, grid.size, grid[0].size) || grid[i][j] == "#")
            continue
        grid[i][j] = "#"
        try {
            walkPath(listOf(Pair(initialPos, initialDir)), initialPos, initialDir, grid)
        } catch (e: Exception) {
            total += 1
        }
        grid[i][j] = "."
    }
    return total
}

fun main() {
    val inputGrid = generateSequence(::readLine).map {
        it.toList().map(Char::toString).filter(String::isNotEmpty)
    }.toList()

    val i = inputGrid.indices.first {
        inputGrid[it].contains("^")
    }
    val guardLocation = Pair(i, inputGrid[i].indexOf("^"))

    val walkedPath = walkPath(listOf(Pair(guardLocation, Direction.Up)), guardLocation, Direction.Up, inputGrid)
    val distinctPath = walkedPath.map {
        it.first
    }.distinct()

    val mutableGrid = inputGrid.map { it.toMutableList() }.toMutableList()
    val amountOfLocations = amountOfPossibleObstacles(Pair(guardLocation, Direction.Up), distinctPath, mutableGrid)

    println("Part 1 answer: ${distinctPath.size}")
    println("Part 2 answer: $amountOfLocations")
}

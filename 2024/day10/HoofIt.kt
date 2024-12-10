enum class Direction {
    Up,
    Down,
    Left,
    Right
}

fun isWithinBounds(i: Int, j: Int, boundI: Int, boundJ: Int): Boolean = i >= 0 && j >= 0 && i < boundI && j < boundJ

fun moveInDirection(direction: Direction, position: Pair<Int, Int>): Pair<Int, Int> = when (direction) {
    Direction.Up -> Pair(position.first - 1, position.second)
    Direction.Down -> Pair(position.first + 1, position.second)
    Direction.Left -> Pair(position.first, position.second - 1)
    Direction.Right -> Pair(position.first, position.second + 1)
}

fun nextSteps(currentPosition: Pair<Int, Int>,
              visited: HashSet<Pair<Int, Int>>,
              grid: List<List<Int>>): List<Pair<Int, Int>> = Direction.entries.map {
                  moveInDirection(it, currentPosition)
              }.filter { (a, b) ->
                  isWithinBounds(a, b, grid.size, grid[0].size) &&
                          !visited.contains(a to b) &&
                          grid[a][b] == grid[currentPosition.first][currentPosition.second] + 1
              }

fun calcScore(currentPosition: Pair<Int, Int>, visited: HashSet<Pair<Int, Int>>, grid: List<List<Int>>): Int {
    if (grid[currentPosition.first][currentPosition.second] == 9) return 1
    val next = nextSteps(currentPosition, visited, grid)
    visited.apply {
        add(currentPosition)
        addAll(next)
    }
    return next.sumOf { calcScore(it, visited, grid) }
}

fun calcAllScores(grid: List<List<Int>>): Int  = grid.indices.sumOf { i ->
    grid[i].indices.sumOf { j ->
        if (grid[i][j] == 0) calcScore(i to j, hashSetOf(), grid) else 0
    }
}

fun calcRating(currentPosition: Pair<Int, Int>, visited: HashSet<Pair<Int, Int>>, grid: List<List<Int>>): Int {
    if (grid[currentPosition.first][currentPosition.second] == 9) return 1
    val next = nextSteps(currentPosition, visited, grid)
    val nextVisited = HashSet<Pair<Int, Int>>(visited).apply {
        add(currentPosition)
        addAll(next)
    }
    return next.sumOf { calcRating(it, nextVisited, grid) }
}

fun calcAllRatings(grid: List<List<Int>>): Int = grid.indices.sumOf { i ->
    grid[i].indices.sumOf { j ->
        if (grid[i][j] == 0) calcRating(i to j, hashSetOf(), grid) else 0
    }
}

fun main() {
    val inputGrid = generateSequence(::readLine).map {
        it.toList().map(Char::digitToInt)
    }.toList()

    println("Part 1 answer: ${calcAllScores(inputGrid)}")
    println("Part 2 answer: ${calcAllRatings(inputGrid)}")
}
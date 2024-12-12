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
              letter: String,
              visited: HashSet<Pair<Int, Int>>,
              grid: List<List<String>>): List<Pair<Int, Int>> =
    Direction.entries.map {
        moveInDirection(it, currentPosition)
    }.filter { (a, b) ->
        isWithinBounds(a, b, grid.size, grid[0].size) &&
                !visited.contains(a to b) &&
                grid[a][b] == letter
    }

fun calcPerimeter(currentPosition: Pair<Int, Int>,
                  letter: String,
                  grid: List<List<String>>): Int =
    Direction.entries.map {
        moveInDirection(it, currentPosition)
    }.count { (a, b) ->
        !isWithinBounds(a, b, grid.size, grid[0].size) || grid[a][b] != letter
    }

fun findAreaPerimeter(currentPosition: Pair<Int, Int>,
                      letter: String,
                      visited: HashSet<Pair<Int, Int>>,
                      grid: List<List<String>>): List<Int> {
    if (grid[currentPosition.first][currentPosition.second] != letter || visited.contains(currentPosition))
        return listOf()
    val next = nextSteps(currentPosition, letter, visited, grid)
    visited.add(currentPosition)
    val perimeter = calcPerimeter(currentPosition, letter, grid)
    return listOf(perimeter) + next.map { findAreaPerimeter(it, letter, visited, grid) }.flatten()
}

fun calcPrice(grid: List<List<String>>): Int {
    val visited = HashSet<Pair<Int, Int>>()
    return grid.indices.sumOf { i ->
        grid[i].indices.sumOf { j ->
            val region = findAreaPerimeter(i to j, grid[i][j], visited, grid)
            val area = region.size
            val perimeter = region.sum()
            area * perimeter
        }
    }
}

fun findAreaSides(currentPosition: Pair<Int, Int>,
                  letter: String,
                  visited: HashSet<Pair<Int, Int>>,
                  rows: HashMap<Int, List<Int>>,
                  columns: HashMap<Int, List<Int>>,
                  grid: List<List<String>>): Int {
    if (grid[currentPosition.first][currentPosition.second] != letter || visited.contains(currentPosition))
        return 0

    val (i1, j1) = moveInDirection(Direction.Up, currentPosition)
    if (!isWithinBounds(i1, j1, grid.size, grid[0].size) || grid[i1][j1] != letter)
        rows[i1] = rows.getOrDefault(i1, listOf()) + listOf((j1 + 1) * -1)
    val (i2, j2) = moveInDirection(Direction.Down, currentPosition)
    if (!isWithinBounds(i2, j2, grid.size, grid[0].size) || grid[i2][j2] != letter)
        rows[i2] = rows.getOrDefault(i2, listOf()) + listOf(j2 + 1)
    val (i3, j3) = moveInDirection(Direction.Left, currentPosition)
    if (!isWithinBounds(i3, j3, grid.size, grid[0].size) || grid[i3][j3] != letter)
        columns[j3] = columns.getOrDefault(j3, listOf()) + listOf((i3 + 1) * -1)
    val (i4, j4) = moveInDirection(Direction.Right, currentPosition)
    if (!isWithinBounds(i4, j4, grid.size, grid[0].size) || grid[i4][j4] != letter)
        columns[j4] = columns.getOrDefault(j4, listOf()) + listOf(i4 + 1)

    val next = nextSteps(currentPosition, letter, visited, grid)
    visited.add(currentPosition)
    return 1 + next.sumOf { findAreaSides(it, letter, visited, rows, columns, grid) }
}

fun getDuplicates(list: List<Int>): List<Int> {
    val found = HashSet<Int>()
    val out = mutableListOf<Int>()
    list.forEach {
        if (it in found)
            out.add(it)
        else
            found.add(it)
    }
    return out.sorted().toList()
}

fun calcSides(axis: HashMap<Int, List<Int>>): Int = axis.map { (_, otherAxis) ->
    val duplicates = getDuplicates(otherAxis)
    val unique = otherAxis.toHashSet().toList()
    unique.sorted().zip(unique.indices).groupBy { (a, b) -> b - a }.count() +
            duplicates.sorted().zip(duplicates.indices).groupBy { (a, b) -> b - a }.count()
}.sum()

fun calcDiscountPrice(grid: List<List<String>>): Int {
    val visited = HashSet<Pair<Int, Int>>()
    return grid.indices.sumOf { i ->
        grid[i].indices.sumOf { j ->
            val rows = HashMap<Int, List<Int>>()
            val columns = HashMap<Int, List<Int>>()
            val area = findAreaSides(i to j, grid[i][j], visited, rows, columns, grid)
            val sides = calcSides(rows) + calcSides(columns)
            area * sides
        }
    }
}

fun main() {
    val inputGrid = generateSequence(::readLine).map {
        it.toList().map(Char::toString).filter(String::isNotEmpty)
    }.toList()

    val price = calcPrice(inputGrid)
    println("Part 1 answer: $price")

    val discountPrice = calcDiscountPrice(inputGrid)
    println("Part 2 answer: $discountPrice")
}
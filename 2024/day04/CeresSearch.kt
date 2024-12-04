fun isOutOfBounds(i: Int, j: Int, boundI: Int, boundJ: Int): Boolean = !(i >= 0 && j >= 0 && i < boundI && j < boundJ)

fun checkDirection(expected: String, i: Int, j: Int, offsetI: Int, offsetJ: Int, grid: List<List<String>>): Int =
    if (isOutOfBounds(i, j, grid.size, grid[0].size) || grid[i][j] != expected) 0
    else when (expected) {
        "X" -> checkDirection("M", i+offsetI, j+offsetJ, offsetI, offsetJ, grid)
        "M" -> checkDirection("A", i+offsetI, j+offsetJ, offsetI, offsetJ, grid)
        "A" -> checkDirection("S", i+offsetI, j+offsetJ, offsetI, offsetJ, grid)
        "S" -> 1
        else -> 0
    }

fun findWordsByDir(i: Int, j: Int, grid: List<List<String>>): Int =
    checkDirection("X", i, j, -1, -1, grid) +
    checkDirection("X", i, j,  -1, 0, grid) +
    checkDirection("X", i, j,  0, -1, grid) +
    checkDirection("X", i, j,  1, 0, grid) +
    checkDirection("X", i, j,  0, 1, grid) +
    checkDirection("X", i, j,  -1, 1, grid) +
    checkDirection("X", i, j,  1, -1, grid) +
    checkDirection("X", i, j,  1, 1, grid)

fun isCenterOfXMas(i: Int, j: Int, grid: List<List<String>>): Boolean {
    val diagonalNeighbours = listOf(Pair(i-1,j-1), Pair(i-1,j+1), Pair(i+1,j-1), Pair(i+1,j+1)).map {
        (a, b) -> if (isOutOfBounds(a, b, grid.size, grid[0].size)) "." else grid[a][b]
    }
    val possibilities = listOf(
        listOf("M", "M", "S", "S"),
        listOf("M", "S", "M", "S"),
        listOf("S", "S", "M", "M"),
        listOf("S", "M", "S", "M"),
    )
    return grid[i][j] == "A" && possibilities.any { it == diagonalNeighbours }
}

fun main() {
    val letterGrid = generateSequence(::readLine).map {
        it.toList().map(Char::toString).filter(String::isNotBlank)
    }.toList()

    val xmasWordCount = letterGrid.indices.sumOf {
        i -> letterGrid[i].indices.sumOf {
            j -> findWordsByDir(i, j, letterGrid)
        }
    }

    println("Part 1 Answer: $xmasWordCount")

    val xmasXCount = letterGrid.indices.sumOf {
        i -> letterGrid[i].indices.count {
            j -> isCenterOfXMas(i, j, letterGrid)
        }
    }

    println("Part 2 Answer: $xmasXCount")
}

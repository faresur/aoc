enum class Direction {
    Up,
    Down,
    Left,
    Right
}

fun moveInDirection(direction: Direction, position: Pair<Int, Int>): Pair<Int, Int> = when (direction) {
    Direction.Up -> Pair(position.first - 1, position.second)
    Direction.Down -> Pair(position.first + 1, position.second)
    Direction.Left -> Pair(position.first, position.second - 1)
    Direction.Right -> Pair(position.first, position.second + 1)
}

fun parseDirection(direction: Char): Direction = when (direction) {
    '^' -> Direction.Up
    '>' -> Direction.Right
    '<' -> Direction.Left
    'v' -> Direction.Down
    else -> throw IllegalArgumentException("Unknown direction: $direction")
}

typealias Grid = MutableList<MutableList<String>>

fun Grid.toWide(): Grid = this.map { row ->
    row.joinToString("") { column ->
        when (column) {
            "#" -> "##"
            "O" -> "[]"
            "." -> ".."
            "@" -> "@."
            else -> throw Exception("Unknown symbol: $column")
        }
    }.toList().map(Char::toString).filter(String::isNotEmpty).toMutableList()
}.toMutableList()

fun Grid.isAbleToMove(position: Pair<Int, Int>, direction: Direction): Boolean {
    val (i, j) = position
    if (this[i][j] == "#") return false
    if (this[i][j] == ".") return true
    val nextPosition = moveInDirection(direction, position)
    if (this[i][j] == "[" && (direction == Direction.Up || direction == Direction.Down))
        return this.isAbleToMove(nextPosition, direction) &&
                this.isAbleToMove(moveInDirection(direction, i to (j + 1)), direction)
    if (this[i][j] == "]" && (direction == Direction.Up || direction == Direction.Down))
        return this.isAbleToMove(nextPosition, direction) &&
                this.isAbleToMove(moveInDirection(direction, i to (j - 1)), direction)
    return this.isAbleToMove(nextPosition, direction)
}

fun Grid.moveWideStep(positionA: Pair<Int, Int>,
                      positionB: Pair<Int, Int>,
                      direction: Direction): Pair<Pair<Int, Int>, Pair<Int, Int>> {
    val (aI, aJ) = positionA
    val nextAPos = moveInDirection(direction, positionA)
    val (nextAI, nextAJ) = nextAPos
    val (bI, bJ) = positionB
    val nextBPos = moveInDirection(direction, positionB)
    val (nextBI, nextBJ) = nextBPos
    if (this[nextAI][nextAJ] == "#" || this[nextBI][nextBJ] == "#") return positionA to positionB
    if ((this[nextAI][nextAJ] != "." || this[nextBI][nextBJ] != ".") &&
        this.isAbleToMove(nextAPos, direction) &&
        this.isAbleToMove(nextBPos, direction)) {
        if (this[nextAI][nextAJ] != ".") this.moveStep(nextAPos, direction)
        if (this[nextBI][nextBJ] != ".") this.moveStep(nextBPos, direction)
    }
    if (this[nextAI][nextAJ] == "." && this[nextBI][nextBJ] == ".") {
        val aSymbol = this[aI][aJ]
        val bSymbol = this[bI][bJ]
        this[aI][aJ] = "."
        this[bI][bJ] = "."
        this[nextAI][nextAJ] = aSymbol
        this[nextBI][nextBJ] = bSymbol
    }
    return positionA to positionB
}

fun Grid.moveStep(position: Pair<Int, Int>, direction: Direction): Pair<Int, Int> {
    val (i, j) = position
    if (this[i][j] == "[" && (direction == Direction.Up || direction == Direction.Down))
        return this.moveWideStep(position, i to (j + 1), direction).first
    if (this[i][j] == "]" && (direction == Direction.Up || direction == Direction.Down))
        return this.moveWideStep(position, i to (j - 1), direction).first
    val nextPosition = moveInDirection(direction, position)
    val (nextI, nextJ) = nextPosition
    if (this[nextI][nextJ] == "#") return position
    if (this[nextI][nextJ] in listOf("O", "[", "]")) this.moveStep(nextPosition, direction)
    if (this[nextI][nextJ] == ".") {
        val currentSymbol = this[i][j]
        this[i][j] = "."
        this[nextI][nextJ] = currentSymbol
        return nextPosition
    }
    return position
}

tailrec fun Grid.moveSymbol(position: Pair<Int, Int>, movements: List<Direction>) {
    if (movements.isEmpty()) return
    val nextPosition = this.moveStep(position, movements.first())
    return moveSymbol(nextPosition, movements.drop(1))
}

fun Grid.moveRobot(movements: List<Direction>) {
    val i = this.indexOfFirst { it.contains("@") }
    val j = this[i].indexOfFirst { it == "@" }
    this.moveSymbol(i to j, movements)
}

fun Grid.calcGPSSum(): Int = this.indices.sumOf { i ->
    this[i].indices.sumOf { j ->
        if (this[i][j] == "O" || this[i][j] == "[") 100 * i + j else 0
    }
}

fun main() {
    val input = generateSequence(::readLine).toList()
    val separatorIndex = input.indexOfFirst { it.isEmpty() }
    val grid: Grid = input.take(separatorIndex).map {
        it.toList().map(Char::toString).filter(String::isNotEmpty).toMutableList()
    }.toMutableList()
    val movements = input.drop(separatorIndex + 1).map {
        it.toList().map(::parseDirection)
    }.flatten()
    val wideGrid: Grid = grid.toWide()

    grid.moveRobot(movements)
    println("Part 1 answer: ${grid.calcGPSSum()}")

    wideGrid.moveRobot(movements)
    println("Part 2 answer: ${wideGrid.calcGPSSum()}")
}
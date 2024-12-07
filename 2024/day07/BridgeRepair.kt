fun isPossible(testValue: Long,
               equationMembers: List<Long>,
               operators: List<(Long, Long) -> Long>): Boolean {
    if (equationMembers.isEmpty())
        return false
    if (equationMembers.size == 1)
        return testValue == equationMembers.first()
    val (firstValue, secondValue) = equationMembers.take(2)
    val tailValues = equationMembers.drop(2)
    return operators.any { operator ->
        isPossible(testValue,
            listOf(operator(firstValue, secondValue)) + tailValues,
            operators)
    }
}

fun main() {
    val calibrationTests = generateSequence(::readLine).map {
        it.split(Regex("( |: )")).map { i -> i.toLong() }
    }.toList()

    val operators01: List<(Long, Long) -> Long> = listOf(
        { a, b -> a + b },
        { a, b -> a * b },
    )
    val sumOfPossibleTestValues01 = calibrationTests.filter {
        isPossible(it.first(), it.drop(1), operators01)
    }.sumOf { it.first() }

    val operators02: List<(Long, Long) -> Long> = listOf(
        { a, b -> a * b },
        { a, b -> a + b },
        { a, b -> "$a$b".toLong() },
    )
    val sumOfPossibleTestValues02 = calibrationTests.filter {
        isPossible(it.first(), it.drop(1), operators02)
    }.sumOf { it.first() }

    println("Part 1 answer: $sumOfPossibleTestValues01")
    println("Part 2 answer: $sumOfPossibleTestValues02")
}
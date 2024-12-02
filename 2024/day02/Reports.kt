fun isSafe(report: List<Int>): Boolean =
    with(report.zip(report.drop(1)).map { (a, b) -> a - b }) {
        all { diff -> diff in 1..3 } ||
                all { diff -> diff in -3..-1 }
    }

fun amountOfSafeReports(reports: List<String>): Int = reports.map {
    it.trim().split(" ").map { num -> num.toInt() }
}.count { isSafe(it) }

fun amountOfSafeReportsWithTolerance(reports: List<String>): Int = reports.map {
    it.trim().split(" ").map { num -> num.toInt() }
}.count {
    isSafe(it) || it.indices.any {
        index ->
        val report = it.toMutableList()
        report.removeAt(index)
        isSafe(report)
    }
}

fun main() {
    val inputLines = generateSequence(::readLine).toList()
    println("Part 1 answer: ${amountOfSafeReports(inputLines)}")
    println("Part 2 answer: ${amountOfSafeReportsWithTolerance(inputLines)}")
}

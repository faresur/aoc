typealias Drone = Pair<Pair<Int, Int>, Pair<Int, Int>>

operator fun Pair<Int, Int>.plus(other: Pair<Int, Int>): Pair<Int, Int> =
    this.first + other.first to this.second + other.second

operator fun Pair<Int, Int>.rem(other: Pair<Int, Int>): Pair<Int, Int> =
    Math.floorMod(this.first, other.first) to Math.floorMod(this.second, other.second)

fun move(drone: Drone, bound: Pair<Int, Int>): Drone {
    val (position, velocity) = drone
    val nextPosition = (position + velocity) % bound
    return Drone(nextPosition, velocity)
}

tailrec fun simulate(drones: List<Drone>, bound: Pair<Int, Int>, seconds: Int): List<Drone> {
    val movedDrones = drones.map { move(it, bound) }
    if (seconds <= 1) return movedDrones
    return simulate(movedDrones, bound, seconds - 1)
}

fun calcSafetyFactor(drones: List<Drone>, bound: Pair<Int, Int>, seconds: Int): Int {
    val dronesAtLocation = simulate(drones, bound, seconds)
        .map { it.first }
        .groupingBy { it }
        .eachCount()

    val (x, y) = bound + (-1 to -1)
    val midX = x / 2
    val midY = y / 2

    val quad1 = (0..<midX).sumOf { i ->
        (0..<midY).sumOf { j ->
            dronesAtLocation.getOrDefault(i to j, 0)
        }
    }
    val quad2 = (midX+1..x).sumOf { i ->
        (0..<midY).sumOf { j ->
            dronesAtLocation.getOrDefault(i to j, 0)
        }
    }
    val quad3 = (0..<midX).sumOf { i ->
        (midY+1..y).sumOf { j ->
            dronesAtLocation.getOrDefault(i to j, 0)
        }
    }
    val quad4 = (midX+1..x).sumOf { i ->
        (midY+1..y).sumOf { j ->
            dronesAtLocation.getOrDefault(i to j, 0)
        }
    }
    return quad1 * quad2 * quad3 * quad4
}

fun parseDrone(line: String): Drone {
    val (x, y, dx, dy) = "-?[0-9]+".toRegex()
        .findAll(line)
        .map { it.value.toInt() }
        .toList()
    return Drone(x to y, dx to dy)
}

fun dronesToString(drones: List<Drone>, bound: Pair<Int, Int>): String {
    val dronesAtLocation = drones.map { it.first }
        .groupingBy { it }
        .eachCount()
    val (x, y) = bound + (-1 to -1)
    return (0..y).joinToString("\n") { i ->
        (0..x).joinToString("") { j ->
            val num = dronesAtLocation.getOrDefault(j to i, 0)
            if (num > 0) "#" else " "
        }
    }
}

tailrec fun firstOccurrenceOfTree(drones: List<Drone>,
                                  bound: Pair<Int, Int>,
                                  treeRegex: Regex,
                                  seconds: Int): Int {
    val movedDrones = ArrayList(drones).map { move(it, bound) }
    val droneFrame = dronesToString(movedDrones, bound)
    if (treeRegex.containsMatchIn(droneFrame)) return seconds + 1
    return firstOccurrenceOfTree(movedDrones, bound, treeRegex, seconds + 1)
}

fun main() {
    val drones = generateSequence(::readLine).map(::parseDrone).toList()

    val safetyFactor = calcSafetyFactor(drones, 101 to 103, 100)
    println("Part 1 answer: $safetyFactor")

    val treeRegex = ("###############################.*\\n.*?" +
            "#                             #.*\\n.*?" +
            "#                             #.*\\n.*?" +
            "#                             #.*\\n.*?" +
            "#                             #.*\\n.*?" +
            "#              #              #.*\\n.*?" +
            "#             ###             #.*\\n.*?" +
            "#            #####            #.*\\n.*?" +
            "#           #######           #.*\\n.*?" +
            "#          #########          #.*\\n.*?" +
            "#            #####            #.*\\n.*?" +
            "#           #######           #.*\\n.*?" +
            "#          #########          #.*\\n.*?" +
            "#         ###########         #.*\\n.*?" +
            "#        #############        #.*\\n.*?" +
            "#          #########          #.*\\n.*?" +
            "#         ###########         #.*\\n.*?" +
            "#        #############        #.*\\n.*?" +
            "#       ###############       #.*\\n.*?" +
            "#      #################      #.*\\n.*?" +
            "#        #############        #.*\\n.*?" +
            "#       ###############       #.*\\n.*?" +
            "#      #################      #.*\\n.*?" +
            "#     ###################     #.*\\n.*?" +
            "#    #####################    #.*\\n.*?" +
            "#             ###             #.*\\n.*?" +
            "#             ###             #.*\\n.*?" +
            "#             ###             #.*\\n.*?" +
            "#                             #.*\\n.*?" +
            "#                             #.*\\n.*?" +
            "#                             #.*\\n.*?" +
            "#                             #.*\\n.*?" +
            "###############################").toRegex()

    val easterEggTime = firstOccurrenceOfTree(drones, 101 to 103, treeRegex, 0)
    println("Part 2 answer: $easterEggTime")
 }
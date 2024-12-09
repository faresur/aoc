fun decompress(compressedDisk: String): List<Long> = compressedDisk.indices.map {
    val number = if (it % 2 == 0) (it / 2).toLong() else -1L
    (1..compressedDisk[it].digitToInt()).map { number }
}.flatten()

fun compactStep(disk: List<Long>): List<Long> {
    val last = disk.last { it != -1L }
    val lastInd = disk.indexOfLast { it != -1L }
    val firstInd = disk.indexOfFirst { it == -1L }
    val newDisk = disk.toMutableList()
    newDisk[lastInd] = -1
    newDisk[firstInd] = last
    return newDisk.toList()
}

tailrec fun compact(disk: List<Long>): List<Long> {
    val newDisk = compactStep(disk)
    if (newDisk.indexOfFirst { it == -1L } > newDisk.indexOfLast { it != -1L })
        return newDisk
    return compact(newDisk)
}

fun calcChecksum(disk: List<Long>): Long = disk.indices.sumOf {
    if (disk[it] != -1L) it * disk[it] else 0
}

fun decompressToFiles(compressedDisk: String): List<List<Long>> = compressedDisk.indices.map {
    val number = if (it % 2 == 0) (it / 2).toLong() else -1L
    (1..compressedDisk[it].digitToInt()).map { number }
}.filter { it.isNotEmpty() }

fun findFree(disk: List<List<Long>>, size: Int): Int =
    disk.indexOfFirst {
        it.contains(-1L) && it.size >= size
    }

fun mergeFree(disk: List<List<Long>>): List<List<Long>> {
    val out = mutableListOf<MutableList<Long>>()
    disk.forEach {
        if (it.contains(-1L) && out.last().contains(-1L)) {
            out.last().addAll(it)
        } else {
            out.add(it.toMutableList())
        }
    }
    return out.map { it.toList() }.toList()
}

fun compactFilesStep(disk: List<List<Long>>, fileId: Long): List<List<Long>> {
    if (disk.isEmpty())
        return emptyList()
    val fileIndex = disk.indexOfFirst { it.contains(fileId) }
    if (fileIndex == -1)
        return disk
    val freeBlockIndex = findFree(disk, disk[fileIndex].size)
    if (freeBlockIndex == -1 || freeBlockIndex > fileIndex)
        return disk
    val sizeDiff = disk[freeBlockIndex].size - disk[fileIndex].size
    val newDisk = disk.mapIndexed { index, list -> if (index == fileIndex) list.map { -1L } else list }
    if (sizeDiff == 0)
        return newDisk.take(freeBlockIndex) + listOf(disk[fileIndex]) + newDisk.drop(freeBlockIndex + 1)
    val diffList = (1..sizeDiff).map { -1L }
    return newDisk.take(freeBlockIndex) + listOf(disk[fileIndex]) + listOf(diffList) + newDisk.drop(freeBlockIndex + 1)
}

fun compactFiles(disk: List<List<Long>>): List<Long> {
    val fileCount = disk.count { !it.contains(-1L) }
    var newDisk = disk
    (0..<fileCount).reversed().forEach {
        newDisk = mergeFree(compactFilesStep(newDisk, it.toLong()))
    }
    return newDisk.flatten()
}

fun main() {
    val inputCompressedDisk = readlnOrNull() ?: ""

    val checksum1 = calcChecksum(compact(decompress(inputCompressedDisk)))
    println("Part 1 answer: $checksum1")

    val checksum2 = calcChecksum(compactFiles(decompressToFiles(inputCompressedDisk)))
    println("Part 2 answer: $checksum2")
}
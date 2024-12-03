package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func getUnconditional(instructions []string) (unconditionalResult int) {
	unconditionalResult = 0
	for _, instruction := range instructions {
		if instruction == "do()" || instruction == "don't()" {
			continue
		}

		inside := instruction[4 : len(instruction)-1]
		numStrings := strings.Split(inside, ",")

		i, _ := strconv.Atoi(numStrings[0])
		j, _ := strconv.Atoi(numStrings[1])
		unconditionalResult += i * j
	}
	return
}

func getConditional(instructions []string) (conditionalResult int) {
	conditionalResult = 0
	mulEnabled := true
	for _, instruction := range instructions {
		if instruction == "don't()" {
			mulEnabled = false
			continue
		} else if instruction == "do()" {
			mulEnabled = true
			continue
		}
		if !mulEnabled {
			continue
		}

		inside := instruction[4 : len(instruction)-1]
		numStrings := strings.Split(inside, ",")

		i, _ := strconv.Atoi(numStrings[0])
		j, _ := strconv.Atoi(numStrings[1])
		conditionalResult += i * j
	}
	return
}

func main() {
	var inputLines []string
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()
		inputLines = append(inputLines, line)
	}

	r, _ := regexp.Compile("(mul[(][0-9]+,[0-9]+[)]|do[(][)]|don't[(][)])")
	var instructions []string
	for _, line := range inputLines {
		instructions = append(instructions, r.FindAllString(line, -1)...)
	}

	fmt.Printf("Part 1 answer: %d\n", getUnconditional(instructions))
	fmt.Printf("Part 2 answer: %d\n", getConditional(instructions))
}

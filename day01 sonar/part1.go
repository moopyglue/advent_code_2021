package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
)

var filename = "day01 sonar/tmp1"

func in_file(filename string) []string {

	var result []string

	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	s := bufio.NewScanner(file)
	for s.Scan() {
		result = append(result, s.Text())
	}

	return result
}

func grep(pattern string, lines []string) []string {
	var result []string
	var re = regexp.MustCompile(pattern)
	for _, kk := range lines {
		if re.MatchString(kk) {
			result = append(result, kk)
		}
	}
	return result
}

func pprint(p) {

}
func main() {
	fmt.Println(in_file(filename))
}

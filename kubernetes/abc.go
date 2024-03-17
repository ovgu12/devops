package main

import "fmt"

func Hello(name string) string {
	message := fmt.Sprintf("Hi, %v. Welcome!", name)
	names := []string{
		"A",
		"B",
		"C",
		"D",
	}

	for i, n := range names {
		fmt.Println(i, ":", n)
	}
	return message
}

func main() {
	fmt.Println(Hello(("Friend")))
}

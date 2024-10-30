package main

import "fmt"

func main() {
	var count int
	fmt.Scanf("%d", &count)
	fmt.Print("W")
  for i := 0; i< count; i++ {
		fmt.Print("o")
	}
	fmt.Print("w!")
}

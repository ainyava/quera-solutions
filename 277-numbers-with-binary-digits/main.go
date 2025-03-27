package main

import (
	"container/list"
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)

	count := 0
	queue := list.New()
	queue.PushBack(1)

	for queue.Len() > 0 {
		current := queue.Front()
		queue.Remove(current)
		num := current.Value.(int)

		if num > n {
			continue
		}
		count++
		queue.PushBack(num * 10)
		queue.PushBack(num*10 + 1)
	}

	fmt.Println(count)
}

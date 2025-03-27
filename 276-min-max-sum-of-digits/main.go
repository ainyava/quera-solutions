package main

import (
	"fmt"
)

func findMinMax(m, s int) (string, string) {
	if s == 0 {
		if m == 1 {
			return "0", "0"
		} else {
			return "-1", "-1"
		}
	}

	if s > 9*m {
		return "-1", "-1"
	}

	largest := make([]byte, m)
	remaining := s
	for i := 0; i < m; i++ {
		if remaining >= 9 {
			largest[i] = '9'
			remaining -= 9
		} else {
			largest[i] = byte(remaining) + '0'
			remaining = 0
		}
	}

	smallest := make([]byte, m)
	remaining = s
	for i := m - 1; i >= 0; i-- {
		if i == 0 {
			smallest[i] = byte(remaining) + '0'
		} else {
			if remaining > 1 {
				if remaining-1 >= 9 {
					smallest[i] = '9'
					remaining -= 9
				} else {
					smallest[i] = byte(remaining-1) + '0'
					remaining = 1
				}
			} else {
				smallest[i] = '0'
			}
		}
	}
	smallest[0] = byte(remaining) + '0'

	if smallest[0] == '0' {
		return "-1", "-1"
	}

	return string(smallest), string(largest)
}

func main() {
	var m, s int
	fmt.Scan(&m, &s)

	min, max := findMinMax(m, s)
	fmt.Println(min, max)
}

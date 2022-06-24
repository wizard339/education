package main

import "fmt"

func gorner_scheme(arr []int, x int) {
	res := arr[len(arr)-1]
	for i := (len(arr) - 1); i > 0; i-- {
		res = res*x + arr[i-1]
	}
	res = res + arr[0]
	fmt.Println(res)

}

func main() {
	gorner_scheme([]int{0, 1, 2, 3, 4}, 2)
}

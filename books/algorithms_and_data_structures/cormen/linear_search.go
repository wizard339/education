package main

import "fmt"

func linear_search(arr []int, v int) int {
	/*
	   Аlgorithm `Linear search` sequentially scans the array in search of an element.
	   Алгоритм `линейного поиска` последовательно просматривает массив в поисках элемента.

	   __________________
	   Input::  `arr` is the sequence of n numbers (a1, a2, ..., an);
	            `v` is the number we a looking for.
	   Output:: `i` is the index for which v = arr[i] or a special value `-1` if `v` not in `arr`.
	   __________________

	   Example input::  [31, 41, 59, 26, 41, 58], 20.
	   Example output:: -1.
	*/
	for i := (len(arr) - 1); i > 0; i-- {
		if arr[i] == v {
			return i
		}
	}
	return -1
}

func main() {
	result := linear_search([]int{31, 41, 59, 26, 41, 58}, 20)
	fmt.Println(result)
}

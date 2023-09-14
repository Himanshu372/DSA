package main

import "fmt"

func maximumInvitations(favorite []int) int {
	g := make(map[int][]int)
	cycleLen := make([]int, 0)
	for ind, fav := range favorite {
		if _, ok := g[fav]; ok {
			g[fav] = append(g[fav], ind)
		} else {
			g[fav] = []int{ind}
		}
		//g[ind] = Element{
		//	left:  fav,
		//	right: -1,
		//}
	}
	for key := range g {
		visited := make(map[int]bool)
		//toVisit := g[key]
		//counter := 0
		//cyclenLen := make([]int, 0)
		traverse(g, key, visited, &cycleLen)
		//if counter != 0 {
		//}
		//if len(visited) != 0 {
		//	l := len(visited) - 1
		//	if g[key].right == -1 {
		//		l++
		//	}
		//if len(currCycleLen) > 0 {
		//	cycleLen = append(cycleLen, currCycleLen...)
		//}
		//}

	}
	m := arrayMax(cycleLen)
	if m == 2 && len(favorite) > 2 {
		return m + 1
	}
	return m
}

func traverse(g map[int][]int, start int, visited map[int]bool, cycleLen *[]int) {
	if _, found := visited[start]; found {
		//if g[start].right == -1 {
		//	g[start] = Element{
		//		left:  g[start].left,
		//		right: 0,
		//	}
		//}
		if len(visited) > 1 {
			*cycleLen = append(*cycleLen, len(visited))
		}
		visited = make(map[int]bool)
		return
	}
	if key, isKey := g[start]; isKey {
		//for _, key := range g[start] {
		//delete(g, start)
		for _, item := range key {
			//}
			//counter += 1
			visited[start] = true
			traverse(g, item, visited, cycleLen)
		}
		//counter = 0
	}
	return
}

func arrayMax(q []int) int {
	max := 0
	for _, i := range q {
		if i > max {
			max = i
		}
	}
	return max
}

func main() {
	input := map[int][]int{
		1: {2, 2, 1, 2},
		2: {1, 2, 0},
		3: {3, 0, 1, 4, 1},
	}
	for _, val := range input {
		fmt.Println(maximumInvitations(val))
	}
}

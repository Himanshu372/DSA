package main

import "fmt"

func arrayMax(q []int) int {
	max := 0
	for _, i := range q {
		if i > max {
			max = i
		}
	}
	return max
}

func reverse(s string) (result string) {
	for _, v := range s {
		result = string(v) + result
	}
	return
}

func maximumInvitations(favorite []int) int {
	g := make(map[int][]int)
	cycleLen := make([]int, 0)
	for ind, fav := range favorite {
		if _, ok := g[fav]; ok {
			g[fav] = append(g[fav], ind)
		} else {
			g[fav] = []int{ind}
		}
	}
	for key := range g {
		visited := make(map[int]bool)
		traverse(g, key, visited, &cycleLen)

	}
	m := arrayMax(cycleLen)
	if m == 2 && len(favorite) > 2 {
		return m + 1
	}
	return m
}

func traverse(g map[int][]int, start int, visited map[int]bool, cycleLen *[]int) {
	if _, found := visited[start]; found {
		if len(visited) > 1 {
			*cycleLen = append(*cycleLen, len(visited))
		}
		visited = make(map[int]bool)
		return
	}
	if key, isKey := g[start]; isKey {
		for _, item := range key {
			visited[start] = true
			traverse(g, item, visited, cycleLen)
		}
	}
	return
}

type EquationGraph struct {
	vertex string
	value  float64
}

func calcEquation(equations [][]string, values []float64, queries [][]string) (r []float64) {
	g, err := makeGraph(equations, values)
	if err != nil {
		panic(err)
	}
	for _, query := range queries {
		if len(query) != 2 {
			panic("query has len greater or less than 2")
		}
		found := true
		if _, found1 := g[query[0]]; !found1 {
			found = found && found1
		}
		if _, found2 := g[query[1]]; !found2 {
			found = found && found2
		}
		if !found {
			r = append(r, -1.0)
			continue
		}
		if query[0] == reverse(query[1]) {
			r = append(r, 1.0)
			continue
		}
		var res1 float64
		visited := make(map[string]bool)
		res1 = dfs(query[0], query[1], g, visited)
		if res1 != -1.0 {
			r = append(r, res1)
			continue
		}
		r = append(r, -1.0)
	}
	return r
}

func makeGraph(equations [][]string, vals []float64) (map[string][]EquationGraph, error) {
	g := make(map[string][]EquationGraph)
	for index, eachPair := range equations {
		if len(eachPair) != 2 {
			return nil, fmt.Errorf("equation key %s has different len %d", eachPair, len(eachPair))
		}
		val1 := EquationGraph{
			vertex: eachPair[1],
			value:  vals[index],
		}
		val2 := EquationGraph{
			vertex: eachPair[0],
			value:  1 / vals[index],
		}
		if _, ok := g[eachPair[0]]; ok {
			g[eachPair[0]] = append(g[eachPair[0]], val1)
		} else {
			g[eachPair[0]] = []EquationGraph{val1}
		}
		if _, ok := g[eachPair[1]]; ok {
			g[eachPair[1]] = append(g[eachPair[1]], val2)
		} else {
			g[eachPair[1]] = []EquationGraph{val2}
		}
	}
	return g, nil
}

func dfs(start, end string, g map[string][]EquationGraph, visited map[string]bool) float64 {
	if start == end {
		return 1.0
	}
	visited[start] = true
	for _, currVal := range g[start] {
		if _, isVisited := visited[currVal.vertex]; isVisited {
			continue
		}
		r := dfs(currVal.vertex, end, g, visited)
		if r > 0 {
			return r * currVal.value
		}
	}
	return -1.0
}

type testCasesCalcEquations struct {
	equations [][]string
	values    []float64
	queries   [][]string
}

func main() {
	fmt.Println("=====Started===")
	testCases := []testCasesCalcEquations{
		{
			equations: [][]string{
				{"x1", "x2"},
				{"x2", "x3"},
				{"x3", "x4"},
				{"x4", "x5"},
			},
			values: []float64{3.0, 4.0, 5.0, 6.0},
			queries: [][]string{
				{"x1", "x5"},
				{"x5", "x2"},
				{"x2", "x4"},
				{"x2", "x2"},
				{"x2", "x9"},
				{"x9", "x9"},
			},
		},
		{
			equations: [][]string{
				{"a", "b"},
				{"b", "c"},
				{"bc", "cd"},
			},
			values: []float64{1.5, 2.5, 5.0},
			queries: [][]string{
				{"a", "c"},
				{"c", "b"},
				{"bc", "cd"},
				{"cd", "bc"},
			},
		},
		{
			equations: [][]string{
				{"a", "b"},
			},
			values: []float64{0.5},
			queries: [][]string{
				{"a", "b"},
				{"b", "a"},
				{"a", "c"},
			},
		},
	}
	for _, testCase := range testCases {
		fmt.Printf("%v\n", calcEquation(testCase.equations, testCase.values, testCase.queries))
	}
	fmt.Println("=====Ended===")
}

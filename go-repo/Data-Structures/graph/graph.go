package graph

import (
	"fmt"
	"time"
)

type MatrixGraph struct {
	Mat [][]int
}

func NewMatrixGraph(size int) *MatrixGraph {
	m := make([][]int, size)
	return &MatrixGraph{m}
}

func (m *MatrixGraph) AddEdge(i, j int) {
	m.Mat[i][j] = 1
	m.Mat[j][i] = 1
	return
}

func (m *MatrixGraph) Print() {
	//rows, cols := len(m.Mat), len(m.Mat[0])
	//g := make([])
	for rowIndex, row := range m.Mat {
		for _, col := range row {
			if m.Mat[rowIndex][col] == 1 {
				fmt.Printf("%d\n", rowIndex)
			}
		}
	}
}

type Vertex struct {
	Neighbours []*Vertex `json:"neighbours"`
	Name       string    `json:"name"`
	Color      string    `json:"color"`
}

func NewVertex(name string) (*Vertex, error) {
	n := make([]*Vertex, 0)
	return &Vertex{
		Name:       name,
		Color:      "black",
		Neighbours: n,
	}, nil
}

func (v *Vertex) AddNeighbour(vv *Vertex) error {
	if v != nil && vv != nil {
		v.Neighbours = append(v.Neighbours, vv)
		return nil
	}
	return fmt.Errorf("neighbours array is not initiated for vertex: %v", v)
}

type Graph struct {
	Vertices []*Vertex
}

func NewGraph() (*Graph, error) {
	vertices := make([]*Vertex, 0)
	return &Graph{Vertices: vertices}, nil
}

func (g *Graph) AddVertex(i interface{}) error {
	switch i.(type) {
	case *Vertex:
		g.Vertices = append(g.Vertices, i.(*Vertex))
	case []*Vertex:
		verticesArr := i.([]*Vertex)
		g.Vertices = append(g.Vertices, verticesArr...)
	}
	return nil
}

func (g *Graph) AddEdge(u, v *Vertex) error {
	var err error
	err = u.AddNeighbour(v)
	if err != nil {
		return err
	}
	return nil
}

func (g *Graph) DFS(v *Vertex) error {
	var err error
	var startTime, endTime time.Time
	startTime = time.Now()
	// v is now visited
	v.Color = "red"
	for _, vertice := range v.Neighbours {
		if vertice.Color != "red" {
			vertice.Color = "red"
			err = g.DFS(vertice)
			if err != nil {
				return fmt.Errorf("error occurred on vertex: %v\n", vertice)
			}
		}
	}
	endTime = time.Now()
	duration := endTime.Sub(startTime)
	fmt.Printf("duration for dfs search from vertex %v is %f\n", v, duration.Seconds())
	return nil
}

func (g *Graph) RecursiveDFS(v *Vertex) error {
	if v.Color == "red" {
		return nil
	}
	v.Color = "red"
	for _, neighbour := range v.Neighbours {
		err := g.RecursiveDFS(neighbour)
		if err != nil {
			return err
		}
	}
	return nil
}

func (g *Graph) BFS(v *Vertex) error {
	var startTime, endTime time.Time
	startTime = time.Now()
	v.Color = "red"
	fmt.Printf("visited vertex: %s\n", v.Name)
	visited := make([]*Vertex, 0)
	for _, vertice := range v.Neighbours {
		vertice.Color = "red"
		fmt.Printf("visited vertex: %s\n", vertice.Name)
		visited = append(visited, vertice)
	}
	for len(visited) != 0 {
		curr_vertice := visited[0]
		visited = visited[1:]
		for _, vertice := range curr_vertice.Neighbours {
			if vertice.Color != "red" {
				vertice.Color = "red"
				fmt.Printf("visited vertex: %s\n", vertice.Name)
			}
			visited = append(visited, vertice)
		}
	}
	endTime = time.Now()
	duration := endTime.Sub(startTime)
	fmt.Printf("duration for bfs search from vertex %s is %f\n", v.Name, duration.Seconds())
	return nil
}

func (g *Graph) RecursiveBFS(v *Vertex) error {
	if v.Color == "red" {
		return nil
	}
	v.Color = "red"
	toBeVisited := make([]*Vertex, 0)
	for _, neighbour := range v.Neighbours {
		neighbour.Color = "red"
		toBeVisited = append(toBeVisited, neighbour)
	}
	for _, toVisit := range toBeVisited {
		err := g.RecursiveBFS(toVisit)
		if err != nil {
			return err
		}
	}
	return nil
}

func (g *Graph) Print() error {
	if len(g.Vertices) == 0 {
		fmt.Printf("graph: %v has not vertices", g)
		return nil
	}
	for _, vertice := range g.Vertices {
		fmt.Printf("vertex: %s, neighbours: %v", vertice.Name, vertice.Neighbours)
	}
	return nil
}

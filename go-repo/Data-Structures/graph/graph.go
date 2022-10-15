package graph

import (
	"fmt"
	"time"
)

type Vertex struct {
	Neighbours []*Vertex
	Name       string
	Color      string
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
	err = v.AddNeighbour(u)
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

func (g *Graph) Print() error {
	if len(g.Vertices) == 0 {
		fmt.Printf("graph: %v has not vertices")
		return nil
	}
	for _, vertice := range g.Vertices {
		fmt.Printf("vertex: %s, neighbours: %v", vertice.Name, vertice.Neighbours)
	}
	return nil
}

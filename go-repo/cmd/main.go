package main

import (
	"bytes"
	"fmt"
	"gorepo/v1/Data-Structures/arrays"
	"gorepo/v1/Data-Structures/doublylinkedlists"
	"gorepo/v1/Data-Structures/graph"
	"gorepo/v1/Data-Structures/linkedlists"
	"io"
	"io/ioutil"
	"os"
	"strings"
	"time"
)

type Vertex struct {
	X, Y float64
}

func (v *Vertex) Abs(ver *Vertex) {
	//fmt.Println(2, &v)
	//fmt.Println(3, &ver)
	fmt.Printf("2 %p\n", v)
	fmt.Printf("3 %p\n", ver)
	v.X = 10 * v.X
	v.Y = 10 * v.Y
	return
}

func main() {
	ver := &Vertex{3, 4}
	fmt.Println(1, &ver)
	ver.Abs(ver)
	fmt.Println(4, &ver)
	fmt.Println("======= LinkedLists =========")
	var ll *linkedlists.SinglyLinkedList
	var err error
	ll, err = linkedlists.NewLinkedList(5)
	if err != nil {
		panic(err)
	}
	ll.InsertAtEnd(10)
	ll.InsertAtEnd(15)
	ll.InsertInBetween(7)
	ll.InsertAtStart(2)
	ll.Delete(15)
	ll.PrintLinkedList()
	var reversedLinkedList *linkedlists.SinglyLinkedList
	reversedLinkedList, err = ll.ReverseLinkedList()
	if err != nil {
		panic(err)
	}
	fmt.Println("Reversed LinkedList")
	reversedLinkedList.PrintLinkedList()
	fmt.Println("======= DoublyLinkedLists =========")
	var dll *doublylinkedlists.DoublyLinkedList
	dll, err = doublylinkedlists.NewDoublyLinkedList(5)
	if err != nil {
		panic(err)
	}
	dll.InsertAtEnd(10)
	dll.InsertAtEnd(15)
	dll.InsertAtEnd(20)
	dll.InsertInBetween(7)
	dll.InsertAtStart(2)
	dll.PrintDoublyLinkedList()
	dll.ReverseDoublyLinkedList()
	fmt.Println("Reversed DoublyLinkedList")
	dll.PrintDoublyLinkedList()

	fmt.Println("======= Graph =======")
	v, err := graph.NewVertex("classic")
	if err != nil {
		panic(err)
	}
	fmt.Println(v)
	g, err := graph.NewGraph()
	if err != nil {
		panic(err)
	}
	u, err := graph.NewVertex("strange")
	if err != nil {
		panic(err)
	}
	x, err := graph.NewVertex("new")
	if err != nil {
		panic(err)
	}
	y, err := graph.NewVertex("shiny")
	if err != nil {
		panic(err)
	}
	z, err := graph.NewVertex("dark")
	if err != nil {
		panic(err)
	}
	err = g.AddVertex([]*graph.Vertex{u, v, x, y, z})
	if err != nil {
		panic(err)
	}
	err = g.AddEdge(u, v)
	if err != nil {
		panic(err)
	}
	err = g.AddEdge(v, x)
	if err != nil {
		panic(err)
	}
	err = g.AddEdge(v, x)
	if err != nil {
		panic(err)
	}
	err = g.AddEdge(x, y)
	if err != nil {
		panic(err)
	}
	err = g.AddEdge(x, z)
	if err != nil {
		panic(err)
	}

	//err = g.DFS(u)
	//if err != nil {
	//	panic(err)
	//}
	//err = g.BFS(u)
	//if err != nil {
	//	panic(err)
	//}

	s1 := time.Now()
	err = g.RecursiveDFS(u)
	e1 := time.Now()
	fmt.Printf("Time for RecursiveDFS: %d\n", e1.Sub(s1).Nanoseconds())
	if err != nil {
		panic(err)
	}
	s2 := time.Now()
	err = g.RecursiveBFS(u)
	if err != nil {
		panic(err)
	}
	e2 := time.Now()
	fmt.Printf("Time for RecursiveBFS: %d\n", e2.Sub(s2).Nanoseconds())
	g.Print()
	fmt.Println("======+Arrays=======")
	testArray := []int{84, -37, 32, 40, 95}
	sumRequired := 167
	//minLen := arrays.ShortestSubarraySum(testArray, sumRequired)
	//fmt.Printf("array: %v, sum>=: %d, shortest subarray len: %d", testArray, sumRequired, minLen)
	minLenWithMonoqueue := arrays.ShortestSubArraySumWithQueue(testArray, sumRequired)
	fmt.Printf("array: %v, sum>=: %d, shortest subarray len: %d\n", testArray, sumRequired, minLenWithMonoqueue)

	f, err := ioutil.TempFile("", "file")
	if err != nil {
		panic(err)
	}
	_, err = io.Copy(f, strings.NewReader("New string"))
	if err != nil {
		panic(err)
	}
	_, err = f.Seek(0, io.SeekStart)
	if err != nil {
		panic(err)
	}
	err = os.Remove(f.Name())
	if err != nil {
		panic(err)
	}
	buff := bytes.NewBuffer([]byte{})
	_, err = io.Copy(buff, f)
	if err != nil {
		panic(err)
	}
	fmt.Printf("%s", buff.String())
}

package main

import (
	"fmt"
	"gorepo/v1/arrays"
	"gorepo/v1/doublylinkedlists"
	"gorepo/v1/linkedlists"
	)

func main() {
	fmt.Println("======= LinkedLists =========")
	var ll *linkedlists.SinglyLinkedList
	var err error
	ll, err  = linkedlists.NewLinkedList(5)
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
	dll, err  = doublylinkedlists.NewDoublyLinkedList(5)
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
	fmt.Println("======+Arrays=======")
	testArray := []int{84,-37,32,40,95}
	sumRequired := 167
	//minLen := arrays.ShortestSubarraySum(testArray, sumRequired)
	//fmt.Printf("array: %v, sum>=: %d, shortest subarray len: %d", testArray, sumRequired, minLen)
	minLenWithMonoqueue := arrays.ShortestSubArraySumWithQueue(testArray, sumRequired)
	fmt.Printf("array: %v, sum>=: %d, shortest subarray len: %d", testArray, sumRequired, minLenWithMonoqueue)
}
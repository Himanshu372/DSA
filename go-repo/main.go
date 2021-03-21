package main

import (
	"fmt"
	"gorepo/v1/linkedlists"
	)

func main() {
	var ll *linkedlists.SinglyLinkedList
	var err error
	ll, err  = linkedlists.NewLinkedList(5)
	if err != nil {
		panic(err)
	}
	ll.InsertAtEnd(10)
	ll.InsertAtEnd(15)
	ll.PrintLinkedList()
	var reversedLinkedList *linkedlists.SinglyLinkedList
	reversedLinkedList, err = ll.ReverseLinkedList()
	if err != nil {
		panic(err)
	}
	fmt.Println("Reversed LinkedList")
	reversedLinkedList.PrintLinkedList()
}
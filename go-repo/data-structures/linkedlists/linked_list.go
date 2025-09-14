package linkedlists

import (
	"fmt"

	"github.com/pkg/errors"
)

type Node struct {
	value int
	next  *Node
}

func NewNode(val int) (*Node, error) {
	return &Node{
		value: val,
		next:  nil}, nil
}

type SinglyLinkedList struct {
	Head *Node
}

func NewLinkedList(HeadVal int) (*SinglyLinkedList, error) {
	node, err := NewNode(HeadVal)
	if err != nil {
		return nil, err
	}
	return &SinglyLinkedList{
		Head: node,
	}, nil
}

func (ll *SinglyLinkedList) len() (int, error) {
	var length int
	length = 0
	currentHead := ll.Head
	for {
		length += 1
		if currentHead.next == nil {
			break
		}
		currentHead = currentHead.next
	}
	return length, nil
}

func (ll *SinglyLinkedList) get(value int) (*Node, error) {
	currentHead := ll.Head
	for {
		if currentHead.value == value {
			return currentHead, nil
		}
		currentHead = currentHead.next
	}
	return nil, errors.New("Node not found")
}

func (ll *SinglyLinkedList) InsertAtEnd(value int) error {
	var newNode *Node
	var err error
	newNode, err = NewNode(value)
	if err != nil {
		return err
	}
	currentHead := ll.Head
	for {
		if currentHead.next == nil {
			currentHead.next = newNode
			break
		}
		currentHead = currentHead.next
	}
	return nil
}

func (ll *SinglyLinkedList) InsertAtStart(value int) error {
	var newNode *Node
	var err error
	newNode, err = NewNode(value)
	if err != nil {
		return err
	}
	currentHead := ll.Head
	ll.Head = newNode
	newNode.next = currentHead
	return nil
}

func (ll *SinglyLinkedList) InsertInBetween(value int) error {
	var newNode *Node
	var err error
	newNode, err = NewNode(value)
	if err != nil {
		return err
	}
	currentHead := ll.Head
	lenght, err := ll.len()
	if err != nil {
		return err
	}
	mid := lenght / 2
	for i := 0; i < mid; i++ {
		currentHead = currentHead.next
	}
	nextNode := currentHead.next
	currentHead.next = newNode
	newNode.next = nextNode
	return nil
}

func (ll *SinglyLinkedList) Delete(value int) error {
	currentHead := ll.Head
	var previousNode *Node
	var nextNode *Node
	for {
		if currentHead.value == value {
			nextNode = currentHead.next
			previousNode.next = nextNode
			break
		}
		previousNode = currentHead
		currentHead = currentHead.next
	}
	return nil
}

func (ll *SinglyLinkedList) PrintLinkedList() error {
	currentHead := ll.Head
	for {
		if currentHead.next == nil {
			break
		}
		fmt.Println(currentHead.value)
		currentHead = currentHead.next
	}
	fmt.Println(currentHead.value)
	return nil
}

func (ll *SinglyLinkedList) ReverseLinkedList() (*SinglyLinkedList, error) {
	var lenght int
	var err error
	reversedLinkedList := &SinglyLinkedList{Head: nil}
	lenght, err = ll.len()
	if err != nil {
		return nil, err
	}
	var currentHead *Node
	var nextNode *Node
	var previousNode *Node
	currentHead = ll.Head
	nextNode = currentHead.next
	previousNode = nil
	reversedLinkedListMap := make(map[int]*Node, 0)
	var index int
	var node *Node
	for i := 0; i < lenght; i++ {
		index = (lenght - 1) - i
		node = currentHead
		node.next = previousNode
		reversedLinkedListMap[index] = node
		previousNode = currentHead
		currentHead = nextNode
		if nextNode.next != nil {
			nextNode = nextNode.next
		}
	}
	reversedLinkedList.Head = reversedLinkedListMap[0]
	return reversedLinkedList, nil
}

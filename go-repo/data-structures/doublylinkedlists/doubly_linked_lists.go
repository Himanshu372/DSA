package doublylinkedlists

import (
	"fmt"
)

type DoublyLinkedNode struct {
	val      int
	previous *DoublyLinkedNode
	next     *DoublyLinkedNode
}

func NewDoublyLinkedNode(value int) (*DoublyLinkedNode, error) {
	return &DoublyLinkedNode{
		val:      value,
		previous: nil,
		next:     nil,
	}, nil
}

type DoublyLinkedList struct {
	head                *DoublyLinkedNode
	doublyLinkedListMap map[int]*DoublyLinkedNode
}

func NewDoublyLinkedList(value int) (dll *DoublyLinkedList, err error) {
	var dllNode *DoublyLinkedNode
	dllNode, err = NewDoublyLinkedNode(value)
	if err != nil {
		return nil, err
	}
	doublyLinkedListMap := make(map[int]*DoublyLinkedNode, 0)
	doublyLinkedListMap[0] = dllNode
	return &DoublyLinkedList{
		dllNode,
		doublyLinkedListMap,
	}, nil
}

func (dll *DoublyLinkedList) len() (lenght int, err error) {
	var currentHead *DoublyLinkedNode
	currentHead = dll.head
	for {
		lenght += 1
		if currentHead.next == nil {
			break
		}
		currentHead = currentHead.next
	}
	return lenght, nil
}

func (dll *DoublyLinkedList) get(value int) (node *DoublyLinkedNode, err error) {
	var currentHead *DoublyLinkedNode
	currentHead = dll.head
	for {
		if currentHead.next == nil {
			node = nil
			err = fmt.Errorf("node with value %d not found in the doublyLinkedList", value)
			break
		}
		if currentHead.val == value {
			node = currentHead
			err = nil
			break
		}
		currentHead = currentHead.next
	}
	return node, err
}

func (dll *DoublyLinkedList) InsertAtStart(value int) (err error) {
	var currentHead *DoublyLinkedNode
	var newHead *DoublyLinkedNode
	var tempNode *DoublyLinkedNode
	var lenght int
	var i int
	lenght, err = dll.len()
	if err != nil {
		return err
	}
	currentHead = dll.head
	newHead, err = NewDoublyLinkedNode(value)
	if err != nil {
		return err
	}
	currentHead.previous = newHead
	newHead.next = currentHead
	dll.head = newHead
	for i = lenght; i >= 1; i-- {
		tempNode = dll.doublyLinkedListMap[i-1]
		dll.doublyLinkedListMap[i] = tempNode
	}
	dll.doublyLinkedListMap[0] = newHead
	dll.doublyLinkedListMap[1] = currentHead
	return nil
}

func (dll *DoublyLinkedList) InsertAtEnd(value int) (err error) {
	var previousLastNode *DoublyLinkedNode
	var newLastNode *DoublyLinkedNode
	var lenght int
	newLastNode, err = NewDoublyLinkedNode(value)
	if err != nil {
		return err
	}
	lenght, err = dll.len()
	if err != nil {
		return err
	}
	previousLastNode = dll.doublyLinkedListMap[lenght-1]
	previousLastNode.next = newLastNode
	newLastNode.previous = previousLastNode
	dll.doublyLinkedListMap[lenght] = newLastNode
	return nil
}

func (dll *DoublyLinkedList) InsertInBetween(value int) (err error) {
	var previousNode *DoublyLinkedNode
	var nextNode *DoublyLinkedNode
	var newNode *DoublyLinkedNode
	var lenght int
	var midLenght int
	newNode, err = NewDoublyLinkedNode(value)
	if err != nil {
		return err
	}
	lenght, err = dll.len()
	if err != nil {
		return err
	}
	if lenght%2 == 0 {
		midLenght = (lenght / 2) - 1
	} else {
		midLenght = lenght / 2
	}
	nextNode = dll.doublyLinkedListMap[midLenght].next
	previousNode = dll.doublyLinkedListMap[midLenght]
	nextNode.previous = newNode
	previousNode.next = newNode
	for i := lenght - 1; i > midLenght; i-- {
		var tempNode *DoublyLinkedNode
		tempNode = dll.doublyLinkedListMap[i]
		dll.doublyLinkedListMap[i+1] = tempNode
	}
	dll.doublyLinkedListMap[midLenght+1] = newNode
	dll.doublyLinkedListMap[midLenght+1].previous = previousNode
	dll.doublyLinkedListMap[midLenght+1].next = nextNode
	return nil
}

func (dll *DoublyLinkedList) ReverseDoublyLinkedList() (err error) {
	reversedDoublyLinkedListMap := make(map[int]*DoublyLinkedNode, 0)
	var nextNode *DoublyLinkedNode
	var previousNode *DoublyLinkedNode
	var lenght int
	var newIndex int
	var i int
	lenght, err = dll.len()
	if err != nil {
		return err
	}
	for i = lenght - 1; i >= 0; i-- {
		nextNode = dll.doublyLinkedListMap[i].next
		previousNode = dll.doublyLinkedListMap[i].previous
		newIndex = (lenght - 1) - i
		reversedDoublyLinkedListMap[newIndex] = dll.doublyLinkedListMap[i]
		reversedDoublyLinkedListMap[newIndex].previous = nextNode
		reversedDoublyLinkedListMap[newIndex].next = previousNode
	}
	dll.head = reversedDoublyLinkedListMap[0]
	dll.doublyLinkedListMap = reversedDoublyLinkedListMap
	return nil
}

func (dll *DoublyLinkedList) PrintDoublyLinkedList() error {
	currentHead := dll.head
	for {
		if currentHead.next == nil {
			break
		}
		fmt.Println(currentHead.val)
		currentHead = currentHead.next
	}
	fmt.Println(currentHead.val)
	return nil
}

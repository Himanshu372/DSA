package doublylinkedlists

import (
	"fmt"
)

type DoublyLinkedNode struct {
	val			int
	previous	*DoublyLinkedNode
	next		*DoublyLinkedNode
}

func NewDoublyLinkedNode(value int) (*DoublyLinkedNode, error) {
	return &DoublyLinkedNode{
		val:      value,
		previous: nil,
		next:     nil,
	}, nil
}

type DoublyLinkedList struct {
	head					*DoublyLinkedNode
	doublyLinkedListMap		map[int]*DoublyLinkedNode
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
	lenght = 0
	for {
		if currentHead.next != nil {
			lenght += 1
			currentHead = currentHead.next
		}
		break
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
	currentHead = dll.head
	newHead, err = NewDoublyLinkedNode(value)
	if err != nil {
		return err
	}
	currentHead.previous = newHead
	newHead.next = currentHead
	dll.head = newHead
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
	previousLastNode = dll.doublyLinkedListMap[lenght - 1]
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
	if lenght % 2 != 0 {
		midLenght = lenght - 1
	}

	return nil
}
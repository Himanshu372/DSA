package queues

type Queue struct {
	Front int
	Size  int
	Array map[int]int `default:nil`
}

func NewQueue(size int) (*Queue, error) {
	array := make(map[int]int, size)
	return &Queue{
		Front: 0,
		Size:  size,
		Array: array,
	}, nil
}

func (queue *Queue) resize() (err error) {
	newSize := queue.Size * 2
	front := queue.Front
	newArray := make(map[int]int, newSize)
	oldSize := queue.Size
	for i := front; i < oldSize; i++ {
		newArray[i%newSize] = queue.Array[i]
	}
	queue.Array = newArray
	queue.Size = newSize
	return nil
}

//func (queue *Queue) add (val int) (err error) {
//	for i := 0; i < queue.Size; i++ {
//		if i
//	}
//}

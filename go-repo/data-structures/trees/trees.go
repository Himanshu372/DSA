package trees

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type BinarySearchTree struct {
	Root *TreeNode
}

func (t *BinarySearchTree) add(node *TreeNode, val int) int {
	switch {
	case val < node.Val:
		if node.Left != nil {
			return -1
		}
		node.Left = &TreeNode{
			Val: val,
		}
		return 0
	case val > node.Val:
		if node.Right != nil {
			return 1
		}
		node.Right = &TreeNode{
			Val: val,
		}
		return 0
	default:
		return 0
	}
}

func (t *BinarySearchTree) AddElement(val int) {
	start := t.Root
	for {
		if t.add(start, val) == 0 {
			break
		}
		res := t.add(start, val)
		switch {
		case res < 0:
			start = start.Left
		case res > 0:
			start = start.Right
		}
	}

}

func (t *BinarySearchTree) InOrderTraversal(node *TreeNode, vals *[]int) {
	if node == nil {
		node = t.Root
	}
	if node.Left != nil {
		t.InOrderTraversal(node.Left, vals)
	}
	*vals = append(*vals, node.Val)
	if node.Right != nil {
		t.InOrderTraversal(node.Right, vals)
	}
}

func (t *BinarySearchTree) PreOrderTraversal(node *TreeNode, vals *[]int) {
	if node == nil {
		node = t.Root
	}
	*vals = append(*vals, node.Val)
	if node.Left != nil {
		t.PreOrderTraversal(node.Left, vals)
	}
	if node.Right != nil {
		t.PreOrderTraversal(node.Right, vals)
	}
}

func (t *BinarySearchTree) PostOrderTraversal(node *TreeNode, vals *[]int) {
	if node == nil {
		node = t.Root
	}
	if node.Left != nil {
		t.PostOrderTraversal(node.Left, vals)
	}
	if node.Right != nil {
		t.PostOrderTraversal(node.Right, vals)
	}
	*vals = append(*vals, node.Val)
}

func (t *BinarySearchTree) BFS() []int {
	startNode := t.Root
	q := make([]int, 0)
	visited := make([]*TreeNode, 0)
	visited = append(visited, startNode)
	q = append(q, startNode.Val)
	for {
		if len(visited) == 0 {
			break
		}
		startNode = visited[0]
		var left, right *TreeNode
		if startNode.Left != nil {
			left = startNode.Left
			visited = append(visited, left)
			q = append(q, left.Val)
		}
		if startNode.Right != nil {
			right = startNode.Right
			visited = append(visited, right)
			q = append(q, right.Val)
		}
		visited = visited[1:]
	}
	return q
}

func (t *BinarySearchTree) Print() {
	vals := make([]int, 0)
	t.InOrderTraversal(t.Root, &vals)
	for _, val := range vals {
		fmt.Printf("%d\n", val)
	}
}

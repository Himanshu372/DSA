package trees

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type BinarySearchTree struct {
	Root *TreeNode
}

func (t *BinarySearchTree) AddElement(rootNode *TreeNode, val int) {
	switch {
	case val < rootNode.Val:
		if rootNode.Left == nil {
			node := &TreeNode{
				Val: val,
			}
			rootNode.Left = node
			return
		}
		if val < rootNode.Left.Val {
			t.AddElement(rootNode.Left, val)
		} else {
			t.AddElement(rootNode.Right, val)
		}
	case val > rootNode.Val:
		if rootNode.Right == nil {
			node := &TreeNode{
				Val: val,
			}
			rootNode.Right = node
			return
		}
		if val < rootNode.Left.Val {
			t.AddElement(rootNode.Left, val)
		} else {
			t.AddElement(rootNode.Right, val)
		}
	default:
		return
	}
}

func (t *BinarySearchTree) InOrderTraversal() []int {
	startNode := t.Root
	vals := make([]int, 0)
	for {
		if startNode.Left == nil {
			break
		}
		currVal := startNode.Left.Val
		vals = append(vals, currVal)
		startNode = startNode.Left
	}
	vals = append(vals, t.Root.Val)
	startNode = t.Root
	for {
		if startNode.Right == nil {
			break
		}
		currVal := startNode.Right.Val
		vals = append(vals, currVal)
		startNode = startNode.Right
	}
	return vals
}

func (t *BinarySearchTree) PreOrderTraversal() []int {
	startNode := t.Root
	vals := make([]int, 0)
	vals = append(vals, t.Root.Val)
	for {
		if startNode.Left == nil {
			break
		}
		currVal := startNode.Left.Val
		vals = append(vals, currVal)
		startNode = startNode.Left
	}
	startNode = t.Root
	for {
		if startNode.Right == nil {
			break
		}
		currVal := startNode.Right.Val
		vals = append(vals, currVal)
		startNode = startNode.Right
	}
	return vals
}

func (t *BinarySearchTree) PostOrderTraversal() []int {
	startNode := t.Root
	vals := make([]int, 0)
	for {
		if startNode.Right == nil {
			break
		}
		currVal := startNode.Right.Val
		vals = append(vals, currVal)
		startNode = startNode.Right
	}
	vals = append(vals, t.Root.Val)
	startNode = t.Root
	for {
		if startNode.Left == nil {
			break
		}
		currVal := startNode.Left.Val
		vals = append(vals, currVal)
		startNode = startNode.Left
	}

	return vals
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

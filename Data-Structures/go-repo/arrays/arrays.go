package arrays


import (
	"math"
)



func ShortestSubarraySun(nums []int, k int) int {
	numLen := len(nums)
	minLenArray := numLen + 1
	if numLen == 1 && nums[0] >= k {
		return 1
	}
	for start := 0; start <= numLen - 1; start++ {
		currentSum := nums[start]
		if currentSum >= k {
			return 1
		}
		for end := start + 1; end < numLen; end++ {
			currentSum += nums[end]
			//fmt.Printf("currentSubArray: %v\tcurrentSum: %d\n",nums[start: end + 1], currentSum)
			if currentSum >= k && (end - start + 1) < minLenArray {
				minLenArray = end - start + 1
			}
		}
	}
	if minLenArray == numLen + 1 {
		return -1
	}
	return minLenArray
}

func ShortestSubArraySumWithQueue(nums []int, k int) int {
	prefixSumArray := []int{0}
	monoQueue := make([]int, 0)
	minLen := int(^uint(0) >> 1)
	for _, eachElement := range nums {
		sum := eachElement + prefixSumArray[len(prefixSumArray)- 1]
		prefixSumArray = append(prefixSumArray, sum)
	}
	for curIndex, curElement := range prefixSumArray {
		for {
			if len(monoQueue) != 0 && prefixSumArray[monoQueue[len(monoQueue) - 1]] >= curElement {
				monoQueue = monoQueue[:len(monoQueue) - 1]
			} else {
				break
			}
		}
		for {
			if len(monoQueue) != 0 && curElement - prefixSumArray[monoQueue[0]] >= k {
				head := curIndex
				tail := monoQueue[0]
				monoQueue = monoQueue[1:]
				minLen = int(math.Min(float64(minLen), float64(head - tail)))
			} else {
				break
			}
		}
		monoQueue = append(monoQueue, curIndex)
	}
	if minLen == int(^uint(0) >> 1) {
		return -1
	}
	return minLen
}
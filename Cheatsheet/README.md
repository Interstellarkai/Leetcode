# LEETCODE CHEAT SHEET

Big-O notations indicate the algorithm’s general time complexity
n indicates the total number of elements in the input

Other good reference: 
1. [Python Cheat Sheet](https://leetcode.com/discuss/study-guide/2122306/Python-Cheat-Sheet-for-Leetcode)
2. [Comprehensive DSA](https://leetcode.com/discuss/study-guide/494279/Comprehensive-Data-Structure-and-Algorithm-Study-Guide)
3. [OOP](https://leetcode.com/discuss/study-guide/1852219/Object-Oriented-Programming-Made-Easy)
4. [14 Patterns](https://hackernoon.com/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed)
5. [NUS Graph Visualization](https://visualgo.net/en)

## Input Array is Sorted
#### - Binary Search: O(log n)
#### - Two Pointers: O(n)

## Input is a Binary Tree
#### - DFS (Preorder, Inorder, Postorder): O(n)
#### - BFS (Level Order): O(n)

## Input is a Binary Search Tree
#### - Left < Cur < Right: O(log n)
#### - Inorder Traversal visits the nodes in ascending (sorted) order: O(n)
  - A binary search tree is a binary tree where the left child is smaller and the right child is greater than its parent. 
  - Traverse a BST using Inorder to:
      - visit the tree in sorted order
      - validate whether a binary tree is a binary search tree

## Input is a Matrix/Graph
#### - DFS (Recursion, Stack): O(n)
#### - BFS (Queue): O(n)

## Find the Shortest/Nearest Path/Distance in a Tree/Matrix/Graph
#### - BFS (non-weighted): O(n)
#### - Dijkstra (weighted): O(E log V)

## String Concatenation
#### - String is immutable
#### - String concatenation += is expensive
  - When you concatenate two strings, it doesn’t simply add one string at the end of another; it creates a new string (ouch).
  - Use a StringBuilder instead (or string.join() on a list in Python), which essentially is a List<Character>.
    - String += c → linear
    - StringBuilder.append(c) → constant
  #### - StringBuilder(): O(n) (Java, C#, etc.)
    ```
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < n; i++) {
        sb.append(c);
    }
    return sb.toString();
    ```
  #### - String.join(): O(n) (Python)
    ```
    return ''.join([c for _ in range(n)])
    ```

## Input is a Linked List
#### - Dummy Node
#### - Two Pointers: O(n)
#### - Fast & Slow Pointers: O(n)

## Recomputing the Same Input
#### - Memoization

## Recursion is Banned
#### - Stack

## Permutations/Combinations/Subsets
#### - Backtracking

## Find the Top/Least Kth element
#### - Heap: O(n log k)
- The easiest way? 
  - Sort the array. But that’s O(n log n).
- Can we do better?
  - Sure! How about using a PriorityQueue? That’s O(n log k)!
- Can we do even better? 
  - Use Quick Select; the algorithm’s linear on average.
#### - QuickSelect: O(n) average, O(n²) worst
  - Why O(n)?
    - The algorithm recurs only for the part that contains the kth largest element. If we assume it recurs half the list each time, it processes n elements in the first recursive call, n/2 in the second, n/4 in the third, and so on, until there’s only 1 element remaining. 
  - Remember geometric series?
    - 1 + (1 / 2) + (1 / 4) + ... + (1 / n) = 2.
    - Similarly, n + (n / 2) + (n / 4) + ... + 1 = 2n. 
  - Average:  O(n) 
  - Worst: O(n²) if the array is already sorted
  ```
    --PYTHON
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def qselect(nums: List[int], l: int, r: int, k: int) -> None:
            p = partition(nums, l, r)
            
            if p < k: 
                return qselect(nums, p + 1, r, k)
            if p > k: 
                return qselect(nums, l, p - 1, k)
            
            return nums[p]

        def partition(nums: List[int], l: int, r: int) -> int:
            pivot, p = nums[r], r

            i = l
            while i < p:
                if nums[i] > pivot: 
                    nums[i], nums[p - 1] = nums[p - 1], nums[i]
                    nums[p], nums[p - 1] = nums[p - 1], nums[p]
                    i -= 1
                    p -= 1
                    
                i += 1

            return p

        return qselect(nums, 0, len(nums) - 1, len(nums) - k)
  ```

## Common Strings
#### - Map
#### - Trie

## Sort
#### - Quick Sort: O(n log n) average, O(n²) worst
#### - Merge Sort: O(n log n)
#### - Built-in sorts: O(n log n)

## Find the Smallest/Largest/Median in a Stream
#### - Two Heaps

## Must Solve In-Place
#### - Swap corresponding values
#### - Store different values in the same pointer

## Maximum/Minimum Subarray/Subset/Options
#### - Dynamic Programming

## Map/Set
#### - Time: O(1)
#### - Space: O(n)

## Deque
#### - Replaces Stack, Queue, and LinkedList
#### - Time: O(1)
- One data structure to rule them all. A Deque (pronounced "Deck") is a double-ended queue that can add or remove elements from both ends in amortized constant time O(1). This allows us to replace Stack, Queue, and LinkedList with just four interfaces: 
  - Python
    - appendleft(), append()
    - popleft(), pop()
  - Java
    - addFirst(), addLast()
    - removeFirst(), removeLast()
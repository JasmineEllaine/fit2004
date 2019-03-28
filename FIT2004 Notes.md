# FIT2004: Notes



## Week 1: Preparation

8 March 2019



### Online Resources

* [Proof by induction by Khan Academy](https://www.khanacademy.org/math/algebra-home/alg-series-and-induction/alg-induction/v/proof-by-induction)
* [Algorithmic Analysis](http://users.monash.edu/~lloyd/tildeAlgDS/Math/)



## Week 1: Chapter 1: Analysis of Algorithms Part I

21 March 2019



### Intro

* Testing a program can only demonstrate if a program is wrong, not that it is always correct.



### Program Verification

* Prove that: 
  * Algorithm must terminate. 
  * Algorithm must produce the correct result. Can be checked using invariance. 

#### Proving Binary Search

* Establish an **invariant**:
  * If key $\in$ array, then at each iteration:
    1. Array[lo] $\leq$ key
    2. Array[hi] $>$ key, assuming array[n+1] = $\infty$
* These two conditions imply that array[lo] $\leq$ key < array[hi]. Combined with the sordidness of the array, this implies that key (if it exists) lies within the range [lo..hi).
* We can now re-write brinary search such that every action it takes is simply to aim to maintain these invariants. 



### Arguing Correctness

* Prove three things:
  * **Initialisation:** prove invariants hold at the beginning
  * **Maintenance:** prove the invariants remain true throughout the algorithm
  * **Termination:** prove the invariants at termination imply correctness of algorithm

#### Binary Search

##### Case 1: Key in Array

* initialise ==lo = 1, hi = n+1==
  1. if key $\in$ array, since the array is sorted, lo = 1 implies that the array[lo] is the minimum element, hence array[lo] $\leq$ key
  2. If we take array[n+1] = $\infty$, then since hi = n+1, array[hi] > key
* therefore invariant is true in the beginnign of search
* at each step of iteration, we compute ==mid = [(lo+hi)/2]==, and compare mid to key.
* the conditional statement int he loop forces the invariant
  1. if key $\geq$ array[mid], then after setting lo = mid, we will still have array[lo] $\leq$ key
  2. if key < arrayp[mid], then after setting hi = mid, we will still have array[hi] > key

##### Case 2: Key not in Array

* provided that the algorithm terminates, regardless of the value of lo, array[lo] $\neq$ key and hence the algorithm correctly identifikes that key is not in array



### Arguing Termination

* loop condoition for binary search is ==lo < hi - 1==

* hence whlie we are looping this inequality holds:
  $$
  mid = \bigg\lfloor \frac{lo + hi}{2} \bigg\rfloor
  $$

* if lo < hi, then ==lo < mid < hi==

#### Proof

* Since mid is the floor of (lo+hi)/2, it is true that:

$$
\frac{lo+hi}{2} < mid \leq \frac{lo+hi}{2}
$$

* multiplying by 2, we find

$$
lo + hi - 2 < 2 \times mid \leq lo + hi
$$

* lo < hi -1, we have lo $\leq$ hi - 2. We replace hi - 2 with lo on the leftmost term in the inequality

$$
2 \times lo < 2 \times mid < lo + hi + 1
$$

* we add 1 to the rightmost term

$$
2 \times lo < 2 \times mid < lo + hi + 1
$$

* since lo < hi - 1, we have lo+1 < hi. We replace lo+1 with hi on the rightmost term

$$
2 \times lo < 2 \times mid < 2 \times hi
$$

* and hence

$$
lo < mid <hi
$$



### Complexity Analysis

* we can express the number of operations performes by the binary search algorithm $T(n)$ as a function of the size *n* of the input data:

$$
T(n) = 
\left\{
\begin{array}{ll}
      T(\frac{n}{2}) + a & if \, n > 1 \\
      b & if \, n = 1\\
\end{array} 
\right.
$$

* where $a​$ is some constant number of operations that we perform each step, and $b​$ is some constant number of operations requires at the end of the algorithm
* explicit solution of above:

$$
T(n) = a\,log_{2}(n) + b
$$

#### Proof

* **Base Case:** if $n=1$, then $a \, log_{2} (n) + b=b$, which agrees with our definition of T(n)
* **Induction:** for some $n$, it is the case that $T(\frac{n}{2}) = a\,log_{2}(\frac{n}{2}) + b$. It is then true that:

$$
\begin{align*}
T(n) &= T\bigg(\frac{n}{2}\bigg) +a \\
&= a\,log_{2} \bigg(\frac{n}{2}\bigg) + b + a \\
&= a(log_{2}(n) - a\,log_{2}(2)) + b + a\\ \\
&= a\,log_{2}(n) - a + b + a \\
&= a\,log_{2}(n) + b 
\end{align*}
$$

* **Conclusion:** complexity of binary search is ==$O(log(n))$==



### Solution to Common Recurrence Relations

#### Logarithmic Complexity

$$
\begin{align*}
T(n) &= 
\left\{
\begin{array}{ll}
      T(\frac{n}{2}) + a & if \, n > 1 \\
      b & if \, n = 1\\
\end{array} 
\right. \\
T(n) &= a\,log_{2}(n) + b
\end{align*}
$$

#### Linear Complexity

$$
\begin{align*}
T(n) &= 
\left\{
\begin{array}{ll}
      T(n-1) + a & if \, n > 0 \\
      b & if \, n = 0\\
\end{array} 
\right. \\
T(n) &= an + b
\end{align*}
$$

#### Superlinear Complexity

$$
\begin{align*}
T(n) &= 
\left\{
\begin{array}{ll}
      2T(\frac{n}{2}) + an & if \, n > 1 \\
      b & if \, n = 1\\
\end{array} 
\right. \\
T(n) &= an\,log(n) + bn
\end{align*}
$$

#### Quadratic Complexity

$$
\begin{align*}
T(n) &= 
\left\{
\begin{array}{ll}
      T(n-1) + cn & if \, n > 0 \\
      b & if \, n = 0\\
\end{array} 
\right. \\
T(n) &= c\bigg(\frac{n(n+1)}{2}\bigg) + b
\end{align*}
$$

#### Exponential Complexity

$$
\begin{align*}
T(n) &= 
\left\{
\begin{array}{ll}
      2T(n-1) + a & if \, n > 0 \\
      b & if \, n = 0\\
\end{array} 
\right. \\
T(n) &= (a+b)\times2^{n}-a
\end{align*}
$$



### Asymptotic Notation

* when analysing complexity ofl algorithms, we typically only look at the order of magnitude of the running time for large values of n. 

#### Big-O Notation

* denotes an **upper bound** on the size of a function
* ==$f(n)= O(g(n))$== means that $f(n)$ is no bigger than the order of magnitude of $g(n)$
  * For values of n above some threshold, f is always no bigger than some constant multiple of g.
  * Behaviour ofl f for small value sis irrelevant
  * $f(n)= O(g(n))$ as $n \rightarrow \infty$ if:

$$
\begin{array}{ll}
    f(n) \leq c\,g(n) &&for \,all \,n \geq n_{0}
\end{array}
$$

####  Big-$\Omega$ Notation

* denotes a **lower bound** 
* ==$f(n)= \Omega(g(n))$== means that $f(n)$ is at least as big as the order of magnitude of $g(n)$
  - This is used to state that an algorithm has to do at least a certain amount of operations
  - $f(n)=\Omega(g(n))​$ as $n \rightarrow \infty​$ if:

$$
\begin{array}{ll}
    f(n) \geq c\,g(n) &&for \,all \,n \geq n_{0}
\end{array}
$$

#### Big-$\Theta$ Notation

* Combination of big O and big $\Omega​$
* ==$f(n)= \Theta(g(n))$== means that $f(n)$ is the same the order of magnitude of $g(n)$
  - The amount of operations performed by an algorithm is precise.
  - $f(n)=\Theta(g(n))$ as $n \rightarrow \infty$ if:

$$
\begin{array}{ll}
    f(n) = c\,g(n) & and & f(n)=\Omega(g(n)) &&as\, n \rightarrow 
    \infty
\end{array}
$$

or
$$
\begin{array}{ll}
    f(n) = c\,g(n) & and & g(n)=O(f(n)) &&as\, n \rightarrow 
    \infty
\end{array}
$$


### Solving Recurrence Relations

```
power(x, N) {
    if (N==0)
    	return 1
    if (N==1)
    	return x
    else
    	return x*power(x, N-1)
}
```

- Cost when N = 1: $T(1) = b​$
- Cost for general case: $T(N) = T(N-1) + c$
- Cost for N-1: $T(N-1) = T(N-2) + c$
  - Replacing $T(N-1)$ in general case: $T(N) = (T(N-2) + c) + c = T(N-2) + 2*c$

* General pattern for substitution: $T(N) = T(N-k)+k*c​$

* Substitue $N-1$ for $k​$: 

$$
T(N) = T(N - (N-1)) + (N-1)*c \\
T(N) = T(1) + (N-1)*c \\
\therefore T(N) = b + (N-1)*c \implies O(N)
$$



### Proof by Induction

* Prove base case (e.g. for the first state).
* Assume the proof holds for a state k. Show that it also holds for the next state k+1.

$$
S(n) = \frac{n(n+1)}{2} \\
S(1) = \frac{1(1+1)}{2} = 1 \\
S(k) = \frac{k(k+1)}{2} \\
S(k+1) = \frac{(k+1)((k+1)+1)}{2} \\
S(k+1) = 1+2+...+k+(k+1) \\
= \frac{k(k+1)}{2} + (k+1) \\
= \frac{k(k+1)}{2} + \frac{2(k+1)}{2} \\
= \frac{k(k+1)+2(k+1)}{2} \\
= \frac{(k+1)(k+2)}{2} \\
\therefore \frac{(k+1)((k+1)+1)}{2}
$$



## Week 2: Chapter 2: Analysis of Algorithms Part II

21 March 2019



### Quadratic Sorting Algorithms

#### Selection Sort

##### Key Ideas

* Consider the list to be sorted as being divided into two parts
  1. The first part consists of the list that is currently sorted
  2. The remaining part consists of the elements that are yet to be sorted
* Initially, the sorted part is empty, while the reminaing is the entire list
* Sort list like so:
  1. Search the unsorted part for the smallest element
  2. Swap this element with the first element of the unsorted part
  3. the sorted part is now one element longer (and the usorted part one element shorter)

```
function SLEECTION_SORT(array[1...n])
	for i = 1 to n do
		Set min = i
		for j = 1 + 1 to n do
			if array[j] < array[min] then
				min = j
			end if
		end for
		swap(array[i], array[min])
	end for
end function
```

* at some given value of i in the main loop, we have two sublists:
  * **array[1…i-1]** – sorted part
  * **array[i…n]** – unsorted part

##### Invariants

* for any given value of i in the main loop, at the beginning of the iteration:
  1. **arrya[1…i-1]** is sorted
  2. for any c $\in$ array[1…i-1] and y $\in$ array[i…n], x $\leq$ y

##### Initial State of the Invariants

* When i = 1, the sorted part of the array is empty, so the invariants hold.

##### Maintenance of Invariants

* at each iteration of the loop, we get the minimum of the unsorted section and move it to the sorted part, hence invariants hold

##### Termination

* when the algorithm terminates, the invariant must sitll hold
* since it was maintained in iteration i = n, this implies that array[1…n] is sorted

##### Time and Space Complexity

* always does a complete scan of the remainder of the array on each iteration
* number of operations performed is independent of the contents of the array
* best, average, and worst case complexity is ==O(n^2^)==

$$
Proof: \\
\begin{align*}
\sum^{n}_{i=1}(n-i) &= n^2 - \sum^{n}_{i=1}i \\
&= n^2 - \frac{n(n+1)}{2} \\
&= \frac{n^2-n}{2}\\
&= O(n^2)
\end{align*}
$$

* Only require one extra variable and some loop counters, so the space required is constant

|       | Best Case | Average Case | Worst Case |
| ----- | --------- | ------------ | ---------- |
| Time  | O(n^2^)   | O(n^2^)      | O(n^2^)    |
| Space | O(1)      | O(1)         | O(1)       |



#### Insertion Sort

##### Key Ideas

* Maintain two sublists, one sorted and one that is yet to be sorted
* at each iteration, move one new element from the not sorted part of the list into its correct position in the sorted sublist

```
functionm INSERTION_SORT(array[1...n])
	for i = 2 to n do
		Set key = array[i]
		Set j = i - 1
		while j > 0 and array[j] > key do
			array[j+1] = array[j]
			j = j - 1
		end while
		array[j+1] = key
	end for
end function
```

##### Invariants

* For any given value of i, at the begining of the iteration:
  1. Array[1…i-1] is sorted

##### Initial State of the Invariant

* sorted list is empty at the beginning of the loop so the invariant holds

##### Maintenance of the Invariant

* at the beginning the sublist array[1…i-1] is sorted
* the inner while loop swaps the item array[j] one place to the left until array[j-1] $\leq$ array[j]
* since array[1…i-1] was sorted, it is therefore true that after the termination of the while loop, array[1…j] is sorted
* since array[j+1…i] was originally sorted, and for each element of array[j+1…i], we had array[j] < x, it is alsop true that array[j…i] is sorted
* hence Array[1…i] is sorted

##### Termination

* at each iteration of the inner while loop, j is decremented
* either the loop condition j $\geq$ 2 must eventually be false, or it will be the case that array[j-1] $\leq$ array[j]
* since the loop invariant was maintained when i = n, it is tru that array[1…n] is sorted

##### Time and Space Complexity

* if the list is already sorted:
  *  the inner loop will never iterate since it will always be true that array[j-1] $\leq​$ array[j]
  * only operations required are to perform the outer loop from 1 to n
* reverse order:
  * inner loop has to loop the entire way from i to 1 since it will always be untrue that array[j-1] $\leq$ array[j]
  * we perform i - 1 operations for each i from 2 ot n
* Random list:
  * we will need to swap array[j] with roughly half of the proceeding elements
  * still takes O(n^2^) time

|       | Best Case | Average Case | Worst Case |
| ----- | --------- | ------------ | ---------- |
| Time  | O(n)      | O(n^2^)      | O(n^2^)    |
| Space | O(1)      | O(1)         | O(1)       |



### Properties of Algorithms

#### Stable Sorting

* if the relative ordering of elements that compare equal is maintained
  * insertion sort is stable
  * selection sort is not

#### Online Algorithms

* able to process its input sequentially without knowing it all in advance
  * Insertion sort will work if you only know some of the input, and will still continue once you add more input
  * selection sort would have to start all over if there are new elements added to input

#### In-Place Algorithms

* uses O(1) auxillary space
  * hard to satisfy so the bottom are also applicable
* If algorithm does not store or copy the input into any additional data structures, but modifies the input directly to produce the output
* never stores more than O(1) elements of the elements of the input outside of the input



## Week 2: Chapter 3: Fast Sorting Algorithms

21 March 2019



### Heapsort (Revision)

#### Binary Heap Data Structure

##### Definition

* complete binary tree (all levels except for the last are completely filled
* every element in a heap is not smalle rthan its children (i.e. maximum element is at the top)

##### Property

* can be represented as a flat array
  * root node is array[1]
  * for each node array[i], its children (if they exist) are elements array[2i] and array[2i+1]
  * an existing array can be converted into a heap in place in O(n) time
  * a new item can be inserted into a binary heap in O(log(n)) time
  * the max element can be removed form a binary heap in O(log(n)) time

#### Heapsort Algorithm

```
function HEAPSORT(array[1...n])
	heapify(array[1...n])
	for i = n to 1 do
		array[i] = extract_max(array[1...i])
    end for
end function
```

* not an online algorithm since we begin by perofrming heapify which requires knowning the entire array
* not a stable algorithm since the swaps made when heapifyingk and removing elements may move equal elements out of their relative order
* in place algorithm because heapify is in place and each call to EXTRACT_MAX places the element back in the array

#### Time and Space Complexity of Heapsort

* heapsort performs:
  * one heapify (O(n))
  * n invocations of EXTRACT_MAX taking up to log(n) time each
  * total time spent by heapsort is O(nlogn)

* behaviour of heapsort is independent of the structure of the input array, so best, average, and worst case scenarios are asymptotically the same
* since heapofy is in place, O(1) space complexity
* best case scenario:
  * all elements are identical
  * each call to extract max is O(1)

|       | Best Case | Average Case | Worst Case |
| ----- | --------- | ------------ | ---------- |
| Time  | O(n)      | O(nlogn)     | O(nlogn)   |
| Space | O(1)      | O(1)         | O(1)       |

##### Binary Heap Operations

Standard operations on a min/max heap, using a priority queue abstract data type:

* ==Heapify==: convert a given array into a min/max heap
* ==Insert==: insert an element into the heap
* ==Remove==: remove the min/max value from the heap

These are supported by:

* ==Rise==: move an element higher up the heap until it satisfies the heap property
* ==Fall==: move an element down the heap until it satisfies the heap property

##### Max Heap Pseudocode

```
function HEAPIFY(array[1...n])
	for i = n/2 to 1 do
		fall(array[1...n], i)
	end for
end function
```

```
function INSERT(array[1...n], x)
	array.append(x)
	n += 1
	rise(array[1...n], n)
```

```
function EXTRACT_MAX(array[1...n])
	swap(array[1], array[n])
	n = n-1
	fall(array[1...n], 1)
	return array.pop_back()
end function
```

```
function RISE(array[1...n], 1)
	Set parent = [1/2]
	while parent >= 1 dol
		if array[parent] < array[i] then
			swap(array[parent], array[i])
			i = parent
			parent = [i/2]
		else
			break
		end if
	end while
end function
```

```
function FALL(array[1...n], i)
	Set child = 2i
	while child <= n do
		if child < n and array[child+1] > array[child] then
			child += 1
		end if
		if array[i] < array[child] then
			swap(array[i], array[child])
			i = child
			child = 21
		else
			break
		end if
	end while
end function
```



### Merge Sort (Revision)

* divide and conquer algorithm	
  * divide into two halves
  * sort those halves
  * merge sorted halves together

#### Algorithm

```
function MERGE(array1[i...end1], array2[j...end2])
	Set result = empty array
	while i <= end1 or j <= end2 do
		if j > end2 or i <= end1 and array1[i] <= array2[j] then
			result.append(array2[j])
			i += 1
		else
			result.append(array2[j])
			j += 1
		end if
	end while
	return result
end function
```

```
function MERGE_SORT(array[lo...hi], work[lo...hi])
	if hi > lo then
		Set mid = floor((lo+hi)/2)
		MERGE_SORT(array[lo...mid], work[1...mid])
		MERGE_SORT(array)[mid+1...hi], work[mid+1...hi])
		array[lo...hi] = MERGE(work[lo...mid], work[mid+1...hi])
	end if
end function

function MERGE_SORT(array[1...n])
	Set work = copy(input)
	MERGE_SORT(array[1...n], work[1...n])
end function
```



#### Time and Space Complexity

* repeatedly splits the input sequence in half unti lit can no longer do so
  * log~2~(n)
* merging elements take O(n) time 
* doing this recursively results in O(log(n)) time
* this is true regardless of input, so the complexity is the same in all inputs

|       | Best Case  | Average Case | Worst Case |
| ----- | ---------- | ------------ | ---------- |
| Time  | O(nlog(n)) | O(nlog(n))   | O(nlog(n)) |
| Space | O(n)       | O(n)         | O(n)       |



#### Enhancement

* can be implemented bottom up, so there is no need for recursion
* still requires O(n) memory, but eliminates the use of the program stack (for recursion) and hence should be slightly faster
* there are also in place implementations of merge sort that require only O(1) space



### Complexity Lower Bounds for Sorting

* With the assumption that the only valid operations operable on an element are comparisons, we can prove that sorting cannot be possible done faster than O(log(n)) in the worst case

#### Proof

* consider a decision tree that models the knowledge we have about the order of a particular sequence of data after comparing individual elements

![Screen Shot 2019-03-22 at 3.51.06 pm](/Users/jasminebanares/Monash/fit2004/2004 Images/Screen Shot 2019-03-22 at 3.51.06 pm.png)





## Assignment 1: Notes

'''

This function is to do........

Time complexity:

Space complexity:

Error handling:

Parameters:

Return:

'''

\## Body of the function
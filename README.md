<h1 align="center">Radix Sort</h1>

## Overview

**Radix Sort** is a non-comparison sorting algorithm that sorts numbers digit by digit, starting from the least significant digit (LSD) to the most significant digit (MSD), or vice versa.

It does not compare elements directly. Instead, it distributes numbers into buckets based on their digits and repeatedly sorts them using a stable sub-sorting method (often **Counting Sort**).

It is known for being:

* ✅ Linear-time for fixed-length integers
* ✅ Stable when implemented correctly
* ✅ Very fast for large lists of integers
* ❌ Requires extra memory
* ❌ Works best with integers or strings of equal length

---

## ⚙️ How Radix Sort Works

Radix Sort processes numbers one digit at a time.

### Steps

1. Start with the least significant digit (units place)
2. Sort numbers based on that digit (using a stable sort)
3. Move to the next digit (tens, hundreds, etc.)
4. Repeat until all digit places are processed

---

### Example Walkthrough

Sort this list:

```id="0mrr9c"
[170, 45, 75, 90, 802, 24, 2, 66]
```

#### Pass 1 — Sort by units digit

```id="yzrcg1"
[170, 90, 802, 2, 24, 45, 75, 66]
```

#### Pass 2 — Sort by tens digit

```id="0lqqxg"
[802, 2, 24, 45, 66, 170, 75, 90]
```

#### Pass 3 — Sort by hundreds digit

```id="gjo9an"
[2, 24, 45, 66, 75, 90, 170, 802]
```

Final sorted array:

```id="b6p4sz"
[2, 24, 45, 66, 75, 90, 170, 802]
```

---

## ⏱️ Time & Space Complexity

| Case  | Complexity |
| ----- | ---------- |
| Time  | O(n × d)   |
| Space | O(n + k)   |

Where:

* `n` = number of elements
* `d` = number of digits
* `k` = base (10 for decimal numbers)

For fixed-size integers, this behaves like **O(n)**.

---

## 🧠 Python Implementation

```python id="pb2iv6"
def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count occurrences of digits
    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    # Convert to cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output array (stable)
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy back
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10

    return arr


# Example usage
numbers = [170, 45, 75, 90, 802, 24, 2, 66]
print(radix_sort(numbers))
# Output: [2, 24, 45, 66, 75, 90, 170, 802]
```

---

## 🧪 Example Runs

### Example 1

Input:

```id="hcttnp"
[121, 432, 564, 23, 1, 45, 788]
```

Output:

```id="j1v6j4"
[1, 23, 45, 121, 432, 564, 788]
```

### Example 2

Input:

```id="0heq9j"
[9, 4, 10, 3, 20, 15]
```

Output:

```id="xwr4vb"
[3, 4, 9, 10, 15, 20]
```

---

## 👍 Advantages

* Very fast for large lists of integers
* Linear performance for fixed digit sizes
* Stable sorting algorithm
* No comparisons needed

---

## 👎 Disadvantages

* Uses extra memory
* Limited to integers or uniform-length strings
* More complex than simple comparison sorts

---

## 📌 When to Use Radix Sort

Use Radix Sort when:

* Sorting large lists of integers
* Numbers have limited digit length
* Linear-time sorting is required
* Stability matters

Common uses include:

* Sorting phone numbers
* Sorting IDs
* Sorting timestamps
* Used internally in some high-performance systems

---

## 🏁 Summary

Radix Sort is a powerful non-comparison sorting algorithm that can achieve near-linear performance. When applied to integers with bounded digit length, it often outperforms traditional comparison-based sorts, making it ideal for large-scale numeric data.
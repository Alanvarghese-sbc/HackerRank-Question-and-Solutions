
# List Comprehension - 3D Grid Problem

## 📌 Problem Statement

Given four integers `x`, `y`, `z`, and `n`, generate a list of all possible coordinates `[i, j, k]` such that:

- `0 ≤ i ≤ x`
- `0 ≤ j ≤ y`
- `0 ≤ k ≤ z`
- The sum of the coordinates **should not be equal to `n`**

## 🧠 Example

### Input
1
1
1
2

### Output
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]


---

## 🚀 Approaches

### 1. Using Nested Loops

- Iterate through all values of `i`, `j`, and `k`
- Check condition `(i + j + k) != n`
- Append valid coordinates to list

### 2. Using List Comprehension

- A concise and Pythonic way to achieve the same result
- Combines loops and condition in a single line

---

## 📂 Files

- `solution_loops.py` → Basic approach using loops
- `solution_list_comp.py` → Optimized approach using list comprehension

---

## 💡 Key Concepts

- Nested loops
- List comprehension
- Conditional filtering

---

## 🔥 Complexity

- Time Complexity: `O(x * y * z)`
- Space Complexity: `O(x * y * z)`

---

## 🎯 Learning Outcome

- Understanding how to convert nested loops into list comprehensions
- Writing clean and efficient Python code

---



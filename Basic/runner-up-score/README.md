# Runner-Up Score Problem

## 📌 Problem Statement

Given a list of scores, find the runner-up (second highest) score.

- The list may contain duplicate values
- You must ignore duplicates when finding the second highest

---

## 🧠 Example

### Input
5
2 3 6 6 5

### Output


---

## 🚀 Approaches

### 1. Using Built-in Functions

- Remove duplicates using `set()`
- Sort using `sorted() or sort `
- Get second largest using index `[-2]`

```python
print(sorted(set(arr))[-2])
```

### 2. Manual Approach (Without Built-ins)
  - Find maximum value
  - Traverse again to find second maximum (excluding max)

📂 Files
  solution_builtin.py → Pythonic approach using built-ins
  solution_manual.py → Core logic without built-ins
  
💡 Key Concepts
  - Lists and sets
  - Sorting
  - Iteration
  - Edge case handling

⚠️ Edge Cases
  - All elements same → no runner-up
  - Negative values
  - Large input size
    
🎯 Learning Outcome
  - Understanding how to handle duplicates
 - Writing efficient Python code
- Comparing built-in vs manual solutions


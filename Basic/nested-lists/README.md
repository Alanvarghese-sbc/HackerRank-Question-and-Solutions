
# Nested Lists - Second Lowest Score

## 📌 Problem Statement

Given the names and grades of students, store them in a nested list and find the names of students who have the **second lowest score**.

  - If multiple students have the same second lowest score:
  - Print their names in **alphabetical order**
  - Each name on a new line

---

## 🧠 Example

### Input
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39


### Output


Berry
Harry


---

## 🚀 Approaches

### 1. Using Built-in Functions

- Extract scores
- Remove duplicates using `set()`
- Sort using `sorted()`
- Find second lowest score
- Filter names and sort them

---

### 2. Manual Approach (Without Built-ins)

- Find lowest score manually
- Find second lowest score manually
- Collect names with that score
- Sort names using Bubble Sort

---

## 📂 Files

- `solution_builtin.py` → Pythonic approach
- `solution_manual.py` → Core logic without built-ins

---

## 💡 Key Concepts

- Nested lists
- List comprehension
- Sorting
- Filtering
- Manual algorithm implementation

---

## ⚠️ Edge Cases

- Multiple students with same score
- Negative or decimal scores
- Only one student per score

---

## 🎯 Learning Outcome

- Understanding how to work with nested lists
- Handling duplicates and sorting
- Writing both optimized and manual solutions

---


# Split and Join

## 📌 Problem Statement

Given a string of space-separated words, split the string and join it using a hyphen (-).

---

## 🧠 Example

### Input
this is a string


### Output
this-is-a-string


---

## 🚀 Approaches

### 1. Using Built-in Functions

- Use `split()` to divide the string into words
- Use `join()` to combine words with hyphen

```python
"-".join(line.split(" "))
```
### 2. Manual Approach
Split string into list

Loop through words

Build result string manually

## 📂 Files
solution_builtin.py → Pythonic solution

solution_manual.py → Manual logic implementation

##💡 Key Concepts
Strings

split() function

join() function

Looping and string concatenation

## ⚠️ Edge Cases
Single word input

Multiple spaces (handled by split)

## 🎯 Learning Outcome
  - Understanding string manipulation

  - Converting between string and list

`- Writing clean and efficient Python code


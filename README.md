# 🔢 Find the Missing Number

A short Python script that finds the one missing number in a sequence from 1 to N, using a classic maths trick instead of a loop.

## How it works

The sum of 1 to N is known in advance. Subtract the sum of the numbers you actually have, and what's left is the missing one.

```
numbers  = [1, 2, 4, 5]
expected = 1 + 2 + 3 + 4 + 5 = 15
actual   = 1 + 2 + 4 + 5     = 12
missing  = 15 - 12           = 3
```

- **Time:** O(n), one pass to add up the list
- **Space:** O(1)

## Run it

```bash
python FindingMissingNumber.py
```

Output: `The missing number is: 3`

## Assumptions

The list starts at 1, is sorted, and has exactly one number missing (not the last one, since N is taken from the last element). Change `numbers` in the script to try your own list.

INTERPOLATION_SEARCH(arr, target):
low ← 0
high ← len(arr) - 1
WHILE low ≤ high AND target ≥ arr[low] AND target ≤ arr[high]:
IF low = high:
IF arr[low] = target: RETURN low
ELSE: RETURN -1
// Interpolation formula to estimate probe position
pos ← low + ((target - arr[low]) * (high - low)) / (arr[high] - arr[low])
pos ← FLOOR(pos)
IF arr[pos] = target:
RETURN pos
ELIF arr[pos] &lt; target:
low ← pos + 1
ELSE:
high ← pos - 1
RETURN -1 // Element not found

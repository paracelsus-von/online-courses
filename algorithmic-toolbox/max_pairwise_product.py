# Uses python2

n = int(raw_input())
numbers = map(int, raw_input().split())
assert n > 1
assert len(numbers) == n
numbers.sort()
print(numbers[-1] * numbers[-2])

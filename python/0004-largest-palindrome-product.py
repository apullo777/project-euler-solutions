# Find the largest palindrome made from the product of two 3-digit numbers.

ans = 0
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        num = i * j
        if (str(num) == str(num)[::-1]):
            ans = max(ans, num)
        
print(ans)

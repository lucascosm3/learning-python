# Execution priority order

# 1. (n + n) # everything inside parentheses has maximum priority
# 2. **
# 3. *, /, //, %
# 4. + -

account_1 = 1 + 1 ** 5 + 5 #without implicit priority, result = 7
print(account_1)

account_2 = (1 + 1) ** (5 + 5)  # implicit priority, result = 1024
print(account_2)
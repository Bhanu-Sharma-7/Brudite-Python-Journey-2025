def skillbrew_brudite(n: int) -> str:
    """
    Returns specific strings based on divisibility rules:
    - Divisible by both 3 and 5: "BRUDITE - NIRVANA"
    - Divisible by 3: "SKILLBREW"
    - Divisible by 5: "BRUDITE"
    - Else: returns the number as string
    
    Args:
        n: Integer to evaluate
        
    Returns:
        str: Result based on divisibility rules
    """
    if n % 3 == 0 and n % 5 == 0:
        return "BRUDITE - NIRVANA"
    elif n % 3 == 0:
        return "SKILLBREW"
    elif n % 5 == 0:
        return "BRUDITE"
    return str(n)

# Test cases
test_numbers = [3, 5, 15, 7, 30, 9, 10]
results = [(num, skillbrew_brudite(num)) for num in test_numbers]

# Display results
print("TEST RESULTS:")
print("-" * 30)
for num, result in results:
    print(f"{num:>3} → {result}")
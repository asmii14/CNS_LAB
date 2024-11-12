def calculate_bonus(rating):
    even_product = 1
    odd_product = 1
    has_even = False  # To track if there are non-zero even digits

    # Process each digit in the rating
    for digit in str(rating):
        digit = int(digit)
        if digit != 0 and digit % 2 == 0:
            even_product *= digit
            has_even = True
        elif digit % 2 == 1:
            odd_product *= digit

    # If no non-zero even digits, set even_product to 0
    if not has_even:
        even_product = 0

    # Calculate the bonus
    bonus = even_product - odd_product
    return max(bonus, 0)  # Return 0 if the bonus is negative

def calculate_bonus_ratings(n, ratings):
    bonus_ratings = [calculate_bonus(rating) for rating in ratings]
    print(" ".join(map(str, bonus_ratings)))

# Input
n = int(input())
ratings = list(map(int, input().split()))

# Calculate and display the bonus ratings
calculate_bonus_ratings(n, ratings)

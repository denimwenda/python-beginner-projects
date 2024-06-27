def roman_to_integer(roman):
    # Dictionary to map Roman numerals to integers
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    # Loop through each character in the Roman numeral string
    for char in reversed(roman):
        value = roman_numerals[char]

        # If the current value is less than the previous value, subtract it
        if value < prev_value:
            total -= value
        else:
            total += value

        # Update the previous vale
        prev_value = value

    return total

# Example usage
print(roman_to_integer("III"))   # Out[ut: 3
print(roman_to_integer("IV"))    # Output: 4
print(roman_to_integer("IX"))    # Out[ut: 9
print(roman_to_integer("LVIIII"))  # Output: 58
print(roman_to_integer("MCMXCIV"))  # Output: 1994

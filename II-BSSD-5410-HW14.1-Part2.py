def countCharacters(start, end):
    # Function to spell out a single number
    def spell_number(n):
        # Words for numbers
        ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        
        if n == 0:
            return "zero"
        elif n < 10:
            return ones[n]
        elif n < 20:
            return teens[n - 10]
        elif n < 100:
            return tens[n // 10] + ones[n % 10]
        elif n < 1000:
            if n % 100 == 0:
                return ones[n // 100] + "hundred"
            else:
                return ones[n // 100] + "hundred" + spell_number(n % 100)
        elif n == 1000:
            return "onethousand"
        return ""

    # Calculate total 
    total_characters = 0
    for num in range(start, end + 1):
        total_characters += len(spell_number(num))  
    return total_characters

# From examples
print(countCharacters(1, 3))       # Output: 11
print(countCharacters(41, 41))     # Output: 8
print(countCharacters(101, 101))   # Output: 13
print(countCharacters(0, 1000))    # Output: 18455

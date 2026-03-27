# butterflies = 10
# beetles = 12
# ladybugs = 20

# print('I caught ' + str(butterflies) + ' 🦋 butterflies!')
# print('I caught ' + str(beetles) + ' 🪲 beetles!')
# print('I caught ' + str(ladybugs) + ' 🐞 ladybugs!')

# total = butterflies + beetles + ladybugs

# print('I caught ' + str(total) + ' total bugs!')



def calculate_score(elements): # Defines a func and takes one input.
    total_tes = 0 # Creates a running total and starts it at zero. TES is Total Element Score, which will accumulate as we loop.
    for name, base_value, goes in elements: # Loops through each element in the list. Each element is unpacked into 3 variables: element name, the base score and the list of 9 judge scores.
        trimmed = sorted(goes)[1:-1] # Sorts the GOE scores low to high and removes the first (lowest) and last (highest) scores. 
        avg_goe = sum(trimmed) / len(trimmed) # sum(trimmed) adds up all 7 scores and divides by len(trimmed) (which is 7) to get the average GOE.
        total_tes += base_value * (1 + avg_goe * 0.1) # base_value * (1 + avg_goe * 0.1) multiplies the base value by a boost factor. For example, if avg_goe is 2, it becomes base_value * 1.2, meaning a 20% increase, and then adds that to the running total_tes.
    return round(total_tes, 1) # Returns the final total rounded to 1 decimal place.
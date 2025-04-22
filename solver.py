encoded_output = "87|86|94|55|47|48|59|44|27|30|33|37|42|35|27|51|62|63|39|27|53|59|49|27|29|46|33|27|29|40|51|29|53|47|27|47|48|46|59|42|35|57|"

# Remove trailing '|' and split into numbers
encoded_numbers = [int(num) for num in encoded_output.strip('|%').split('|')]

decoded_flag = ""

for n in encoded_numbers:
    found_char = False
    # Try different values of k until we get a printable ASCII character
    for k in range(25): # Iterate through potential k values (usually small)
        x = n - 1354 + k * 79
        if 32 <= x <= 126: # Check for standard printable ASCII range
            decoded_flag += chr(x)
            found_char = True
            break # Found the character, move to the next number
            
    if not found_char:
        decoded_flag += "?" # Add a placeholder if no printable char found
        print(f"Warning: Could not find printable char for encoded value {n}")

print(decoded_flag)

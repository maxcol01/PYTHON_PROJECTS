from morse_dict import morse_code_dict

def convert_string_to_morse(user_input: str) -> str:
    """
    Converts a given string into Morse code representation.

    This function takes a string input, converts each character to its 
    corresponding Morse code using a predefined dictionary (`morse_code_dict`), 
    and returns the Morse code string. Spaces in the input are replaced by 
    the word "stop" to denote word boundaries in Morse code.

    Args:
        user_input (str): The string to be converted into Morse code. It can 
        contain alphabets, numbers, and spaces.

    Returns:
        str: The converted string in Morse code format, with each character 
        represented in Morse code and spaces replaced by the word "stop". 
        Characters not in the dictionary are ignored.

    Example:
        >>> from morse_dict import morse_code_dict
        >>> convert_string_to_morse("Hello World")
        '.... . .-.. .-.. --- stop .-- --- .-. .-.. -..'
        
        >>> convert_string_to_morse("123")
        '.---- ..--- ...--'
    """
    morse_code: str = ""
    for letter in user_input:
        if letter == " ":
            morse_code += " stop "
        else:
            morse_code += morse_code_dict.get(letter.upper(), "")
    return morse_code, user_input



conversion, user_input = convert_string_to_morse(input("Enter a string you want to see transfomr into morse code: "))
print(f"The mose code for '{user_input}/{user_input.upper()}' is: {conversion}")
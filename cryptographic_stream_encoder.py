# Function to encode a message using a Caesar Cipher

def encoding_function(shift):
    # Store the encrypted message
    encoded_text = ""
    user_input = input("Enter the text to encode: ")
    # Loop through each character
    for char in user_input:
        # Only encode letters
        if char.isalpha():
            # Shift the ASCII value
            shifted = ord(char) + shift
            # Wrap lowercase letters
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            # Wrap uppercase letters
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            # Convert back to a character
            encoded_text += chr(shifted)
        # Keep spaces and punctuation unchanged
        else:
            encoded_text += char
    # Display the encrypted message
    print("Encoded text:", encoded_text)


encoding_function(15)

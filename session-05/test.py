# aa
def encryption(message: str, shift: int=3):
    
    '''
    ## shift
        **Type**: int
        *Range*: 1 -> 100
    '''
    
    alphabets = 'abcde'
    encrypted_message = ''
    
    for letter in message:
        
        if letter == ' ':
            encrypted_message += ' '
            continue
        
        current_letter_index = alphabets.index(letter)
        encrypted_letter_index = (current_letter_index + shift) % len(alphabets)
        encrypted_message += alphabets[encrypted_letter_index]
        shift += 1
    
    return encrypted_message

real_msg = 'add eac'
shift = 3
print(encryption.__doc__)
print('Real message:', real_msg)
# print('Encrypted message:', encryption(real_msg))

        
    
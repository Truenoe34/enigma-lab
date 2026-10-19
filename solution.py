import sys

def get_index(char):
    return ord(char) - ord('A')

def get_char(index):
    return chr(index + ord('A'))

operation = input()
shift = int(input())
rotors = [input() for _ in range(3)]
message = input()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if operation == "ENCODE":
    # 1. Етап зсуву (Caesar Shift)
    shifted_msg = []
    for i, char in enumerate(message):
        new_index = (get_index(char) + shift + i) % 26
        shifted_msg.append(alphabet[new_index])
    
    current_text = "".join(shifted_msg)
    
    # 2. Етап заміни через 3 ротори
    for rotor in rotors:
        next_text = []
        for char in current_text:
            idx = get_index(char)
            next_text.append(rotor[idx])
        current_text = "".join(next_text)
        
    print(current_text)

else: # DECODE
    current_text = message
    
    # 1. Зворотна заміна через 3 ротори (від 2-го до 0-го)
    for rotor in reversed(rotors):
        next_text = []
        for char in current_text:
            idx = rotor.index(char)
            next_text.append(alphabet[idx])
        current_text = "".join(next_text)
        
    # 2. Зворотний зсув
    final_msg = []
    for i, char in enumerate(current_text):
        new_index = (get_index(char) - shift - i) % 26
        final_msg.append(alphabet[new_index])
        
    print("".join(final_msg))

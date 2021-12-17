import numpy as np

#ciphertext = "TAOECCLTGIEAOIERMETHPAWEIMMOLCRIRHSTTSHTIACEULIEORHCNNENCDALCCEUGACSMHTOMYRRIORALKIPEYHNLSEIYEDNTIIIETEWHRNUSFYRARAWHACDDEERFNIHSNTIFOEYNULBYSUDLYEORVPTSIEPALGRGACSSSEESSWPMCODAEPIRRPNIALLTOYKSLAME"
ciphertext = "TAOHSTTSIIETESSE"
plaintext = ""
rail_height = 4

textspace = np.zeros((rail_height, len(ciphertext)))

# Putting the cipher text back in the matrix as it was when being encoded
#for i in range(len(ciphertext) % (2 * rail_height - 1) - 1):
 #   ciphertext += "?"                                   #Setting up the ciphertext for easy management

max_normal = int(len(ciphertext) / (2 * rail_height - 1))
normal_string = ciphertext[0:(2 * rail_height - 1)]
print(len(normal_string))
print(normal_string)
for char in range(len(ciphertext)):
    if char <= max_normal * (2 * rail_height - 1):
        pass




string_lists = [ciphertext[i:i + 2 * rail_height - 2] for i in range(0, len(ciphertext), 2 * rail_height - 2)]
print(string_lists)




print(len(ciphertext))
print(ciphertext)
print(plaintext)
print()
print(textspace)

"""current_array = [ [84.  0.  0.  0.  0.  0. 76.  0. 71.  0.  0.  0.  0.  0. 69.  0. 77.]
                     [ 0. 65.  0.  0.  0. 67.  0.  0.  0. 73.  0.  0.  0. 73.  0.  0.  0.]
                     [ 0.  0. 79.  0. 67.  0.  0.  0.  0.  0. 69.  0. 79.  0.  0.  0.  0.]
                     [ 0.  0.  0. 69.  0.  0.  0. 84.  0.  0.  0. 65.  0.  0.  0. 82.  0.]]"""

def encoding_rail_fence(plaintext, rail_height):
    textspace = np.zeros((rail_height, len(plaintext)))
    ciphertext = ""

    # Putting plaintext into a matrix of height rail_height and in the right sequence
    h = 0
    for letter in range(len(plaintext)):
        if (letter + rail_height - 2) % (rail_height - 1) == 0 or letter == 0:                   #Keep track of whether at the end of a rail
            if letter != 1:
                h += 1
                print(letter, h)

        if h < 2:
            textspace[letter % rail_height][letter] = ord(plaintext[letter].upper())
        elif h%2 != 0:
            if (h + rail_height - 1) % rail_height != 0:
                textspace[(letter - 2) % rail_height][letter] = ord(plaintext[letter].upper())
            else:
                textspace[letter % rail_height][letter] = ord(plaintext[letter].upper())
        else:
            textspace[(rail_height - 2 - (letter - 1) % (rail_height - 1))][letter] = ord(plaintext[letter].upper())

    # Decoding the ciphertext based on reading the matrix
    for row in range(rail_height):
        array_section = textspace[row,:]                    #Splitting the large array into one row at a time to read
        for char in range(len(plaintext)):
            if array_section[char] != 0:
                ciphertext += chr(int(array_section[char]))
    return ciphertext
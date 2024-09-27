def main():
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']

    ciphertext = "IT STY XYZRGQJ TAJW XTRJYMNSL GJMNSI DTZ"

    universalCharFreqs = [0.080, 0.015, 0.030, 0.040, 0.130, 0.020, 0.015, 0.060, 0.065, 0.005, 0.005, 0.035, 0.030,
                          0.070, 0.080, 0.020, 0.002, 0.065, 0.060, 0.090, 0.030, 0.010, 0.015, 0.005, 0.020, 0.002]

    counter = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    frequencyInC = []
    correlationOfFrequency = []
    top5keys = []
    spaces = []

    totalChars = 34

    #Fill in counter
    for character in ciphertext:
        for letter in alphabet:
            if character == letter:
                index = alphabet.index(character)
                counter[index] += 1
                #print(letter, counter[index])

    #Calculation for frequency of characters in the ciphertext
    for number in counter:
        freq = number/totalChars
        frequencyInC.append(freq)
    #print(frequencyInC)

    totalCoF = 0
    for i in range (0, 26):
        key = 0
        for e in range (0, 26):
            index = (26 + e - i) % 26
            key += frequencyInC[e] * universalCharFreqs[index]
        correlationOfFrequency.append(key)
    #print(correlationOfFrequency)


    #Find max in correlationOfFrequency[], append its index to top5keys[], remove number, repeat 5x
    for i in range (0,5):
        num = max(correlationOfFrequency)
        index = correlationOfFrequency.index(num)
        top5keys.append(index)
        correlationOfFrequency[index] = 0

    #print(top5keys)

    indices = []
    #Shift the cipher with the top5keys list
    print("Ciphertext: ", ciphertext)
    for i in range (0,5):
        plaintext = ""
        print("Plaintext for key =", top5keys[i], ": ")

        #for character in ciphertext, find its index in the alphabet
        indices = []
        for character in ciphertext:
            for letter in alphabet:
                if character == letter:
                    index = alphabet.index(character)
                    indices.append(index)
        #print(indices)

        #Add the value of the key to the index
        for j in range (0, 34):
            indices[j] -= top5keys[i]
        #print(indices)

        #Plaintext without spaces
        plaintext = ""
        for num in indices:
            plaintext += alphabet[num]

        #Find spaces in ciphertext
        for character in ciphertext:
            if character == " ":
                index = ciphertext.index(" ")
                spaces.append(index)
                ciphertext = ciphertext.replace(" ", "_", 1)

        #print(spaces)
        #print(ciphertext)

        #Insert spaces into plaintext using slices
        for i in range(0, 6):
            index = spaces[i]
            plaintext = plaintext[:index] + " " + plaintext[index:]

        print(plaintext)
        print()
main()

# Plaintext: Do not stumble over something behind you
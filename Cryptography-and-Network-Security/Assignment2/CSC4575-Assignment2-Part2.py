def main():
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    ciphertext = ("UPRCWIHSGYOXQJRIMXTWAXVEBDREGJAFNISEECAGSSBZRTVEZURJCXTOGPCYOOACSEDBGFZIFUBKVMZUFXCADCAXGSFVNKMSGOCGFI"
                  "OWNKSXTSZNVIZHUVMEDSEZULFMBLPIXWRMSPUSFJCCAIRMSRFINCZCXSNIBXAHELGXZCBESFGHLFIVESYWORPGBDSXUARJUSARGYW"
                  "RSGSRZPMDNIHWAPRKHIDHUZBKEQNETEXZGFUIFVRI")
    lengthOfCiphertext = len(ciphertext)
    indexOfCoincidence = 0
    counter = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    #Fill in counter
    for character in ciphertext:
        for letter in alphabet:
            if character == letter:
                index3 = alphabet.index(character)
                counter[index3] += 1

    #for i in range (0,26):
     #   print(alphabet[i], counter[i])

    for i in range(0, 26):
        answer = (1/(lengthOfCiphertext*(lengthOfCiphertext - 1)))*(counter[i]*(counter[i]-1))
        indexOfCoincidence += answer
    print("Index of Coincidence:", indexOfCoincidence)

    #Given that indexOfCoincidence = 0.0425, we can conclude that the key is of length 6.
    alphabet1 = ""
    alphabet2 = ""
    alphabet3 = ""
    alphabet4 = ""
    alphabet5 = ""
    alphabet6 = ""

    alpha = 1

    for character in ciphertext:
        if alpha == 1:
            alphabet1 += ciphertext[0]
        elif alpha == 2:
            alphabet2 += ciphertext[0]
        elif alpha == 3:
            alphabet3 += ciphertext[0]
        elif alpha == 4:
            alphabet4 += ciphertext[0]
        elif alpha == 5:
            alphabet5 += ciphertext[0]
        elif alpha == 6:
            alphabet6 += ciphertext[0]
        else:
            print("Error")

        ciphertext = ciphertext.replace(ciphertext[0], "", 1)
        alpha += 1
        if alpha > 6:
            alpha = 1

    #DEBUGGING
    #print(alphabet1)
    #print(alphabet2)
    #print(alphabet3)
    #print(alphabet4)
    #print(alphabet5)
    #print(alphabet6)

    #NOW BEGIN CAESAR CIPHER ON ALPHABETS
    frequencyInC = []
    correlationOfFrequency = []
    counter2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    universalCharFreqs = [0.080, 0.015, 0.030, 0.040, 0.130, 0.020, 0.015, 0.060, 0.065, 0.005, 0.005, 0.035, 0.030,
                          0.070, 0.080, 0.020, 0.002, 0.065, 0.060, 0.090, 0.030, 0.010, 0.015, 0.005, 0.020, 0.002]
    alphabetkeys = []
    top5keys = []

    #Loop doesn't work. Go to line 91. It works if you change the alphabet manually on that line, but iterating through
    # all of them doesn't work.
    #for i in range(1, 7):  # for alphabets 1-6
    if i == 1:
        cipher = alphabet1
    elif i == 2:
        cipher = alphabet2
        index = 14
    elif i == 3:
        cipher = alphabet3
    elif i == 4:
        cipher = alphabet4
    elif i == 5:
        cipher = alphabet5
    elif i == 6:
        cipher = alphabet6

    cipher = alphabet1 #change the alphabet number here to see plaintext and key for that alphabet
    totalChars = len(cipher)
    # Fill in counter
    for character in cipher:
        for letter in alphabet:
            if character == letter:
                index = alphabet.index(character)
                counter2[index] += 1
                # print(letter, counter2[index])

    # Calculation for frequency of characters in the ciphertext
    for number in counter2:
        freq = number / totalChars
        frequencyInC.append(freq)
    # print(frequencyInC)

    totalCoF = 0
    for i in range(0, 26):
        key = 0
        for e in range(0, 26):
            index = (26 + e - i) % 26
            key += frequencyInC[e] * universalCharFreqs[index]
        correlationOfFrequency.append(key)
    # print(correlationOfFrequency)

    # Find max in correlationOfFrequency[], append its index to top5keys[], remove number, repeat 5x
    num = max(correlationOfFrequency)
    index = correlationOfFrequency.index(num)
    alphabetkeys.append(index)

    #print(alphabetkeys)

    indices = []
    # Shift the cipher with the alphabetkeys list
    print("Ciphertext: ", cipher)
    plaintext = ""
    print("Plaintext for key =", index, ": ")

    # for character in ciphertext, find its index in the alphabet
    indices = []
    for character in cipher:
        for letter in alphabet:
            if character == letter:
                index2 = alphabet.index(character)
                indices.append(index2)
    #print(indices)

    # Add the value of the key to the index
    for j in range(0, totalChars):
        indices[j] -= index
    #print(indices)

    # Plaintext
    for number in indices:
        plaintext += alphabet[number]
    print(plaintext)

    #print(alphabetkeys)
    letterKey = ""
    #Results from loop that doesn't work that you have to change manually:
    alphabetkeys = [12, 14, 13, 17, 14, 4]
    for k in range (0, 6):
        ind = alphabetkeys[k]
        letterKey += alphabet[ind]
    print("Full Key:",letterKey) #MONROE

    # alphabet1plaintext = "IVEHPOSPNHCRTNRTUCHNRTLIOTLONUSDIOGAORSLT"
    # alphabet2plaintext = "BEVIPROLGAANGGOHAIETEYIEUUETOTESMDSPBTCLH"
    # alphabet3plaintext = "ETENEANEETNTOSNAPAMHROESEAAROYLOETFAEHATE"
    # alphabet4plaintext = "LHRGNRPCSYLOTGGTPTWEIUVSVLRUNOFMSHARTINOR
    # alphabet5plaintext = "IAYHSEEHOOELHOSYREHYGBEOELNSEUAEGILTTNFG
    # alphabet6plaintext = "ETTAFAOATUAEIWOOETEAHELYNYTTBRNTONLSEGAE
    #Put together:
    # I BELIEVE THAT EVERYTHING HAPPENS FOR A REASON PEOPLE CHANGE SO THAT YOU CAN LEARN TO LET GO THINGS GO WRONG SO THAT YOU APPRECIATE THEM WHEN
    # THEY ARE RIGHT YOU BELIEVE LIES SO YOU EVENTUALLY LEARN TO TRUST NO ONE BUT YOURSELF AND SOMETIMES GOOD THINGS FALL APART SO BETTER THINGS CAN FALL TOGETHER







main()
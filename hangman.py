hanged = [
  "   +---+" +"\n"+ "       |"+"\n"+ "       |"+ "\n" + "       |"+ "\n" + "      ===" ,    
  "   +---+" +"\n"+ "   O   |"+"\n"+ "       |"+ "\n" + "       |"+ "\n" + "      ===" ,   
  "   +---+" +"\n"+ "   O   |"+"\n"+ "   |   |"+ "\n" + "       |"+ "\n" + "      ===" ,     
  "   +---+" +"\n"+ "   O   |"+"\n"+ "  /|   |"+ "\n" + "       |"+ "\n" + "      ===" ,    
  "   +---+" +"\n"+ "   O   |"+"\n"+ "  /|\\  |"+ "\n" + "       |"+ "\n" + "      ===" ,     
  "   +---+" +"\n"+ "   O   |"+"\n"+ "  /|\\  |"+ "\n" + "  /    |"+ "\n" + "      ===" ,    
  "   +---+" +"\n"+ "   O   |"+"\n"+ "  /|\\  |"+ "\n" + "  / \\  |"+ "\n" + "      ===" ,
]   

import random
with open("python\\hangman_words.txt", "r") as f: 
    words =  f.readlines()
    words = [word.rstrip('\n') for word in words]


is_playing = True
while is_playing: 
    secret_word = random.choice(words)
    correct_guess = set()
    wrond_guess = set()
    tries = 0
    while True: 
        gess0 = input()
        if gess0 not in secret_word:
            tries +=1
            wrond_guess.add(gess0)
        else:
            correct_guess.add(gess0)
        if tries>= 7: 
            print("YOU LOOSE")
            break
        elif set(secret_word)== correct_guess: 
            print("YOU WIN")
            break
        else: 
            for i in range(len(secret_word)): 
                if secret_word[i] in correct_guess: 
                    print(secret_word[i], end= " ")
                else: 
                    print("_", end=' ')
            print(end = "\n")
            print(hanged[tries])
        
    print("Want to play again ? (yes or no)")
    while True:
        match input(): 
            case "yes": 
                is_playing = True
                break
            case "no": 
                is_playing = False
                break
            case _: 
                print("Error")
                continue

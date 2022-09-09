for i in range(0,len(guess)):
        emoji_appearance: int = 0
        for s in range(0, len(secret)):
            if (guess[i] == secret[s]) and (i == s) and (emoji_appearance == 0):
                emoji_string += GREEN_BOX
            elif (guess[i] == secret[s]) and (i != s) and (emoji_appearance == 0):
                emoji_string += YELLOW_BOX
            elif (guess[i] != secret[s]) and (s == len(secret) - 1) and (emoji_appearance == 0):
                emoji_string += WHITE_BOX
            else:
                pass
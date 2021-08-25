# inspired by https://exercism.io/tracks/javascript/exercises/etl/solutions/91f99a3cca9548cebe5975d7ebca6a85


OLD_POINT_STRUCTURE = {
  0: [' '],
  1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
  2: ['D', 'G'],
  3: ['B', 'C', 'M', 'P'],
  4: ['F', 'H', 'V', 'W', 'Y'],
  5: ['K'],
  8: ['J', 'X'],
  10: ['Q', 'Z']
}

def old_scrabble_scorer(word):
    word = word.upper()
    old_point_structure = OLD_POINT_STRUCTURE
    letterPoints = ""

    for char in word:

        for point_value in old_point_structure:

            if char in old_point_structure[point_value]:
                letterPoints += 'Points for {char}: {point_value}\n'.format(char = char, point_value = point_value)

    return letterPoints

# your job is to finish writing these functions and variables that we've named
# don't change the names or your program won't work as expected.
def transform(old_score_system):
    new_score_system = {}
    for point_value_set in  old_score_system:
        for item in old_score_system[point_value_set]:
            new_score_system[item] = point_value_set
    return new_score_system
    
new_point_structure = transform(OLD_POINT_STRUCTURE)

def initial_prompt():
   print("Let's play some Scrabble!\n")
   while 0 == 0:
        user_word = input("What is your word?: ")  
        char_points = 0
        for char in user_word.upper():
            if char not in new_point_structure:
                char_points += 1
        if char_points > 0:
            print("Use only valid letters, no numbers or special characters.")
        else:
            break
   return user_word


def simple_scorer(word):
    word_score = 0
    for char in word:
        if char in new_point_structure:
            word_score += 1
        print(f'Points for {char}: 1')
        
    return word_score

def vowel_bonus_scorer(word):
    word = word.upper()
    vowels = ['A', 'E', 'I', 'O', 'U']
    word_score = 0
    for char in word:
        if char in vowels:
            char_points = 3
            word_score += 3
            print(f'Points for {char}: {char_points}')
        elif char in new_point_structure:
            char_points = 1 
            word_score += 1
            print(f'Points for {char}: {char_points}')
    return word_score


def scrabble_scorer(word):
    word = word.upper() 
    word_score = 0
    for char in word:
        print(f'Points for {char} : {new_point_structure[char]}')
        word_score += (new_point_structure[char])
        
    return word_score


scoring_algorithms = (
    {
        "Option": 0,
        "Name": "Simple Scorer",
        "Description": "Each letter is worth 1 point",
        "Function": 'Simple scorer'
    },
    {
        "Option": 1,
        "Name": "Bonus Vowels",
        "Description": "Vowels are 3 pts, consonants are 1 pt.",
        "Function": 'Vowel bonus scorer'
    },
    {
        "Option": 2,
        "Name": "Scrabble",
        "Description": "The traditional scoring algorithm.",
        "Function": 'Scrabble scorer'
    }

)

def scorer_prompt(word):
    print("Which scoring system would you like to use?")
    for dict_option in scoring_algorithms:
        for kvp in dict_option:
            print(kvp, ":", dict_option[kvp])
        print("<------------->")
    while 0 == 0:
        try:
            score_system_used = int(input("Enter 0, 1, or 2: "))
            if score_system_used >= 0 and score_system_used <= 3:
                break
            else:
                print("Please input a valid number.")    
        except:
            print("An exception occured, please input a valid number.") 
    word_score = 0
    if score_system_used == 0:
        word_score = simple_scorer(word)
    elif score_system_used == 1:
        word_score = vowel_bonus_scorer(word)
    elif score_system_used == 2:
        word_score = scrabble_scorer(word)
    return word_score



def run_program():
    word = initial_prompt()
    score = scorer_prompt(word)
    print(f"The word: {word} scores {score} points.")
    
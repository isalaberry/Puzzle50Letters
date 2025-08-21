from collections import Counter


def find_word_groups(remaining_letters, available_words, current_group=[]):
    """
    A recursive function to find all combinations of words that can be
    formed from a given set of letters.
    """

    # Find all possible words we can make with the letters we have left
    possible_next_words = []
    for word in available_words:
        word_counts = Counter(word)
        if all(remaining_letters[char] >= word_counts[char] for char in word_counts):
            possible_next_words.append(word)

    # For each possible word, recursively find the next words
    for i, word in enumerate(possible_next_words):

        # Form the new group
        new_group = current_group + [word]
        yield new_group  # This makes the current group a valid result

        # Update letters and the list of words to check next
        new_remaining_letters = remaining_letters - Counter(word)

        # We only pass the rest of the list to the next recursive call
        # to avoid duplicate groups (e.g., ['a', 'cat'] and ['cat', 'a'])
        remaining_word_list = possible_next_words[i + 1:]

        # Recurse and yield from the deeper calls
        yield from find_word_groups(new_remaining_letters, remaining_word_list, new_group)


# --- Main script ---

# 1. Your available letters
letter_counts = Counter("aacddddeeeeeeeeefghhhhlloommnnooorrrssstttttttuvwyy")

# 2. Paste the word list from your previous output here
word_string = """
a about after again all also always am an and any are around as at back be
because been before being between big but by call came can car cat child come
could dad daughter day did do does down each eat end even ever every fact few
find first for found from fun game get give go good great had hand has have he
her here him his home house how i if in into is it its just keep know large last
life like little long look made make man many manu manuela may me mean might
more most mother much my name never new no not now of off old on once one only
open or other our out over own part people place play put real right said same
saw say school see she show small so some son state still such take than that
the their them then there these they thing think this those three time to today
together too two under up upon us use very want was way we well went were what
when where which who why will with woman women word work world would year you
young your
able above across act add age ago air alone along always any answer art ask away
bad ball bank bed best better body book boy call case cause change city clear
close cold common course cut dark dear deep door down draw early easy enough
face fall far fast feel few fire food form full game girl ground grow half help
high hold hope hour idea keep kind land learn less let light long low love move
near need next night nothing once open order over play point power ready rest
road run set show side small stand start stop strong sun sure talk tell term
top try turn until wait walk watch water way well word work"""

word_list = sorted(list(set(word_string.split())))

# 3. Find and print the groups
print("Finding all possible word groups... This may take a while.")

# Find all groups that use up all 50 letters
perfect_solutions = []

for group in find_word_groups(letter_counts, word_list):
    # Calculate the total number of letters used in the current group
    group_letter_count = sum(len(word) for word in group)

    # Check if the group uses exactly 50 letters
    if group_letter_count == 50:
        perfect_solutions.append(group)
        print(f"Found a 50-letter solution: {group}")

if perfect_solutions:
    print("\n--- All 50-Letter Solutions ---")
    for solution in perfect_solutions:
        print(solution)
else:
    print("\nNo combinations found that use exactly 50 letters.")
    print("Consider checking for solutions that use fewer letters or expanding your word list.")

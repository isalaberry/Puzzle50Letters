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
        remaining_word_list = possible_next_words

        # Recurse and yield from the deeper calls
        yield from find_word_groups(new_remaining_letters, remaining_word_list, new_group)


# --- Main script ---

# 1. Your available letters
letter_counts = Counter("aacddddeeeeeeeeefghhhhlluummnnooorrrsssttttttuvwyy")

# 2. Paste the word list from your previous output here
# criar um script para pegar a lista de palavras possiveis de serem formadas e outro para pegar as que são mais comuns em ingles dentro das que são possiveis de serem formadas
# #!!!!! o word_string tem que ser o resultado de mostcommonpossible.txt
word_string = """
 
"""

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

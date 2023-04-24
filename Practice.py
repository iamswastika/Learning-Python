hidden_word = "python"
guessed_word = "_" * len(hidden_word)

guess = "o"

for i, letter in enumerate(hidden_word):
    if letter == guess:
        guessed_word = guessed_word[:i] + guess + guessed_word[i+1:]

print(guessed_word)

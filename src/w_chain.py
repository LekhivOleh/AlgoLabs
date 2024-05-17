def read_file(filename: str) -> list[str]:
    with open(f"../resources/{filename}", "r", encoding="utf-8") as file:
        words_amount = int(file.readline())
        words = [file.readline().strip() for _ in range(words_amount)]
    return sorted(words, key=len)


def find_max_sequence_words(words: list[str]) -> int:
    """
    Takes sorted list of words and returns the length of the longest chain of words using dynamic programming.
    """
    words_combinations = {word: 1 for word in words}
    for word in words:
        for i in range(len(word)):
            new_word = word[:i] + word[i+1:]  # Removing one character from the word using slicing
            if new_word in words_combinations:
                words_combinations[word] = max(words_combinations[word], words_combinations[new_word] + 1)
    return max(words_combinations.values())


def write_output(filename: str, result: int) -> None:
    with open(f"../resources/{filename}", "w", encoding="utf-8") as file:
        file.write(str(result))


def find_w_chain_length(input_file: str, output_file: str) -> None:
    try:
        words = read_file(input_file)
    except ValueError:
        write_output(output_file, -1)
        return
    result = find_max_sequence_words(words)
    write_output(output_file, result)

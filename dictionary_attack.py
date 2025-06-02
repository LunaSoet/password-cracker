from hash_utils import hash_string
import time

def dictionary_attack(target_hash, algorithm='sha256', wordlist_path='wordlist.txt'):
    try:
        with open(wordlist_path, 'r') as file:
            words = file.readlines()
    except FileNotFoundError:
        return "[ERROR] wordlist.txt not found."

    start_time = time.time()
    for i, word in enumerate(words):
        word = word.strip()
        if hash_string(word, algorithm) == target_hash:
            duration = time.time() - start_time
            result = f"[SUCCESS] Dictionary match: '{word}' | Attempts: {i+1} | Time: {duration:.2f}s"
            with open("output.txt", "a") as f:
                f.write(result + '\n')
            return result

    return "[FAILURE] No match found in wordlist."

import itertools
import string
import time
from hash_utils import hash_string

def brute_force(target_hash, algorithm='sha256', charset=string.ascii_lowercase, max_length=4):
    start_time = time.time()
    attempts = 0

    for length in range(1, max_length + 1):
        for guess_tuple in itertools.product(charset, repeat=length):
            guess = ''.join(guess_tuple)
            attempts += 1
            if hash_string(guess, algorithm) == target_hash:
                duration = time.time() - start_time
                result = f"[SUCCESS] Found: '{guess}' | Attempts: {attempts} | Time: {duration:.2f}s"
                with open("output.txt", "w") as f:
                    f.write(result + '\n')
                return result

    return "[FAILURE] No match found within length limit."

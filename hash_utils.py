import hashlib

def hash_string(input_string, algorithm='sha256'):
    input_string = input_string.encode()

    if algorithm == 'sha256':
        return hashlib.sha256(input_string).hexdigest()
    elif algorithm == 'sha1':
        return hashlib.sha1(input_string).hexdigest()
    elif algorithm == 'md5':
        return hashlib.md5(input_string).hexdigest()
    else:
        raise ValueError("Unsupported hash algorithm.")

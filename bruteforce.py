# bruteforce.py
# Safe, readable brute-force script for password-protected ZIP files.
# Usage: python bruteforce.py enc.zip rockyou.txt

import sys
import zipfile

def attempt_extract(zf_path, pwd_bytes):
    try:
        with zipfile.ZipFile(zf_path) as zf:
            # testzip returns name of first bad file or None on success.
            zf.extractall(pwd=pwd_bytes)
        return True
    except RuntimeError:
        # Wrong password raises RuntimeError (or zipfile.BadZipFile for other problems)
        return False
    except zipfile.BadZipFile:
        print('[-] Bad ZIP file or corrupt archive.')
        return False
    except Exception as e:
        # Other exceptions (permission, etc.)
        print(f'[-] Extraction failed: {e}')
        return False

def main():
    if len(sys.argv) != 3:
        print('Usage: python bruteforce.py <zipfile> <wordlist>')
        sys.exit(1)

    zf_path = sys.argv[1]
    wordlist = sys.argv[2]

    print('[+] Beginning bruteforce')
    try:
        with open(wordlist, 'rb') as f:
            for line in f:
                password = line.strip()  # bytes
                if not password:
                    continue
                if attempt_extract(zf_path, password):
                    try:
                        # print as decoded if possible, else repr
                        passwd_str = password.decode('utf-8', errors='replace')
                    except Exception:
                        passwd_str = repr(password)
                    print(f'[+] Correct password: {passwd_str}')
                    return 0
                else:
                    print(f'[-] Incorrect password: {repr(password)}')
    except FileNotFoundError:
        print('Wordlist file not found:', wordlist)
        sys.exit(2)

    print('[+] Password not found in list')
    return 1

if __name__ == '__main__':
    sys.exit(main())

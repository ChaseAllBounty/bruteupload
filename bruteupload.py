
import requests
import argparse
import os
import random
import string

# The EICAR test string
EICAR_STRING = "X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"

# Define the custom user agent
FIREFOX_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0"

def create_eicar_file(file_path, add_pdf_header=False):
    with open(file_path, 'w') as f:
        if add_pdf_header:
            f.write("%PDF-1.7\n")
        f.write(EICAR_STRING)

def generate_random_name(length=10):
    """Generate a random name for stealth purposes."""
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def upload_file(url, file_path, file_name, stealth_mode=False, pdf_mode=False):
    try:
        with open(file_path, 'rb') as file:
            # Adjust MIME type based on the file extension
            mime_type = 'application/pdf' if pdf_mode else 'application/octet-stream'

            # In stealth mode, use a random filename
            if stealth_mode:
                random_name = generate_random_name() + os.path.splitext(file_name)[1]
            else:
                random_name = file_name

            # Create a session with the custom user agent
            session = requests.Session()
            session.headers.update({'User-Agent': FIREFOX_USER_AGENT})
            
            files = {'file': (random_name, file, mime_type)}
            response = session.post(url, files=files)
        
        if response.status_code == 200:
            print(f"File '{random_name}' upload successful.")
        else:
            print(f"File '{random_name}' upload failed with status code: {response.status_code}")
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"An error occurred while uploading '{file_name}': {e}")

def test_combination(url, extension, stealth=False, pdf_header=False):
    eicar_file = 'eicar'
    create_eicar_file(eicar_file, pdf_header)
    eicar_file_name = f"{eicar_file}{extension}"
    os.rename(eicar_file, eicar_file_name)
    upload_file(url, eicar_file_name, eicar_file_name, stealth, pdf_header)
    os.remove(eicar_file_name)

def main():
    parser = argparse.ArgumentParser(description='Test unrestricted file upload with EICAR files.')
    parser.add_argument('url', help='URL to send the POST request')
    parser.add_argument('-a', '--all', action='store_true', help='Run all combinations')
    args = parser.parse_args()

    combinations = [
        ('.com', False, False),  # Default
        ('.txt', False, False),  # -t
        ('.pdf', False, False),  # -p
        ('.com', True, False),   # -s
        ('.pdf', True, True),    # -p -s
        ('.txt', True, False)    # -t -s
    ]

    if args.all:
        for ext, stealth, pdf_header in combinations:
            print(f"Testing combination: Extension={ext}, Stealth={stealth}, PDF Header={pdf_header}")
            test_combination(args.url, ext, stealth, pdf_header)
    else:
        print("No combination specified. Use -a flag to run all combinations.")

if __name__ == "__main__":
    main()

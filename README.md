# BruteUpload

A Python script designed to test server vulnerabilities by attempting to upload EICAR test files in various configurations. This tool helps in identifying unrestricted file upload vulnerabilities through different file extensions, MIME types, naming conventions, and now with custom HTTP headers.

## Features

- **EICAR Test**: Uses the EICAR test string to simulate file uploads without actual malware.
- **Multiple File Extensions**: Tests uploads with `.com`, `.txt`, and `.pdf` extensions.
- **Stealth Mode**: Option to use random filenames to potentially bypass simple filename-based security checks.
- **PDF Header Simulation**: Adds `%PDF-1.7` header for `.pdf` files in stealth mode to further mimic actual PDFs.
- **Custom User Agent**: Uses a predefined Firefox user agent for all requests, customizable via configuration.
- **Custom Headers**: Allows setting custom HTTP headers for requests to test more specific scenarios or bypass certain checks.

## Usage

To use `BruteUpload`, clone this repository and run the script from the command line:

```bash
git clone [your-repo-url]
cd BruteUpload
python bruteupload.py <URL> [OPTIONS]
```

Options:

    -a, --all: Run all possible combinations of tests.
        Example: python bruteupload.py http://example.com/upload -a
    --Header="Header-Name: Value": Add custom headers to the HTTP request. This can be used multiple times for different headers.
        Example: python bruteupload.py http://example.com/upload -a --Header="X-Custom-Header: CustomValue" --Header="Another-Header: AnotherValue"


Note: Replace <URL> with the actual URL where you want to test file uploads.

Installation
This script requires Python 3.x and the requests library. 

    Install Python if you haven't already from python.org.
    Install requests


bash
```
pip install requests
```

How It Works

    Default Upload: Tests upload with .com extension.
    Text File: Uses .txt extension to see if servers filter based on file type.
    PDF Simulation: .pdf extension with and without a PDF header to test MIME type handling.
    Stealth: Randomizes filenames to attempt to bypass pattern-based detection.
    Custom Headers: Enhances testing by allowing specific headers to be set, potentially affecting how the server processes the request.


Each test involves creating an EICAR file, renaming it according to the test parameters, attempting to upload it with any specified headers to the given URL, and then cleaning up the test file.

Security Note

    Permission: Only use this tool on systems where you have explicit permission to conduct security testing. Unauthorized testing can be considered an attack.
    Ethics: This tool is for educational and testing purposes only. Do not use it maliciously.


Contributing
Contributions are welcome! If you want to add more test scenarios, improve the code, or fix issues, please:

    Fork this repository.
    Create your feature branch (git checkout -b feature/AmazingFeature).
    Commit your changes (git commit -am 'Add some AmazingFeature').
    Push to the branch (git push origin feature/AmazingFeature).
    Open a Pull Request.


License
This project is licensed under the MIT License - see the LICENSE.md file for details.

Acknowledgments

    Thanks to the Python community for the requests library.
    To the EICAR for providing a safe way to test antivirus systems.
    To all contributors who will make this tool better.


Remember, security testing should always be done with consent and for constructive purposes. Happy testing!

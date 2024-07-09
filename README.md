# PRSEUS SITECHECKER

## Overview
PRSEUS SITECHECKER is a Python-based utility designed to check the status of specific ports for a list of domains. It reads domain names from a file, checks the specified ports, and logs the results to a file.

## Features
- Load domains from a file.
- Check if specified ports are open on each domain.
- Output results to a timestamped file in the `scans` directory.
- Optional verbose mode for detailed output.

## Requirements
- Python 3.x
- PIP

## Installation
1. Clone the repository or download the script.
2. Ensure you have Python 3.x installed.

## Usage
```sh
python sitechecker.py <file> [--ports PORTS] [--verbose]
```

### Arguments
- `file`: Path to the input file containing URLs.

### Optional Arguments
- `--ports`: List of ports to check (default: 80, 443). 
- `--verbose`: Increase output verbosity.

### Example
```sh
python sitechecker.py urls.txt --ports 80 443 --verbose
```

## Input File Format
The input file should contain domains in the following format:
```
# This is a comment
1 example.com
2 anotherexample.org
```
- Lines starting with `#` are treated as comments and ignored.
- Each line should have a domain prefixed with a number.

## Output
The results are saved in the `scans` directory with a timestamped filename in the format `YYYYMMDD-HHMMSS-urls.txt`. The file contains lines in the following format:
```
example.com | 80, 443
anotherexample.org | 80
```

## License
This project is licensed under the MIT License.

## Contributing
Feel free to submit issues or pull requests. Your contributions are welcome!

## Help
If you like my work, you could star it! I will dearly appreciate it! <3

## Contact
For any questions or suggestions, please use the Issues tab.

---
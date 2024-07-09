import argparse
import socket
import datetime
import os

BANNER = """
============================================
            PRSEUS SITECHECKER
============================================
"""
CREDITS = ["prseus"]
INSPIRATION = ["SwiftSec"]

def clearConsole():
    os.system("cls" if os.name=="nt" else "clear")

def print_banner():
    clearConsole()
    print(BANNER)
    print("Credits:", *CREDITS)
    print("Inspiration:", *INSPIRATION)
    print() # NEWLINE

def load_urls(file_path):
    """ Load URLs from the file, discarding comments and IP addresses. """
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    urls = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#'):
            parts = line.split()
            if len(parts) == 2:
                # Extract domain part
                urls.append(parts[1])
    return urls

def check_ports(domain, ports, verbose):
    """ Check if the given ports are open for the domain. """
    open_ports = []
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                result = sock.connect_ex((domain, port))
                if result == 0:
                    open_ports.append(port)
                    if verbose:
                        print(f"Port {port} open on {domain}")
                elif verbose:
                    print(f"Port {port} closed on {domain}")
        except socket.gaierror:
            if verbose:
                print(f"Domain name resolution failed for {domain}")
    return open_ports

def main(file_path, ports, verbose):
    """ Main function to check domains and write results. """
    urls = load_urls(file_path)
    
    # Create scans directory if it doesn't exist
    if not os.path.exists('scans'):
        os.makedirs('scans')
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    output_file = os.path.join('scans', f"{timestamp}-urls.txt")
    
    with open(output_file, 'w') as file:
        for url in urls:
            open_ports = check_ports(url, ports, verbose)
            if open_ports:
                open_ports_str = ', '.join(map(str, open_ports))
                file.write(f"{url} | {open_ports_str}\n")
    
    print(f"Results written to {output_file}")

if __name__ == "__main__":
    print_banner()
    parser = argparse.ArgumentParser(
        description="Check open ports for a list of domains from a file.",
        epilog="Example usage: python sitechecker.py urls.txt --ports 80 443"
    )
    parser.add_argument("file", type=str, help="Path to the input file containing URLs")
    
    group = parser.add_argument_group("optional arguments")
    group.add_argument("--ports", type=int, nargs='*', default=[80, 443], help="Ports to check (default: 80, 443)")
    group.add_argument("--verbose", action="store_true", help="Increase output verbosity")
    
    args = parser.parse_args()
    
    main(args.file, args.ports, args.verbose)

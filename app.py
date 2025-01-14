import argparse
from Crypto.Hash import MD4
from getpass import getpass
from colorama import init, Fore, Style

init(autoreset=True)

def generate_nt_hash(password: str) -> str:
    """Generate NT hash from password."""
    if not password:
        raise ValueError("Password cannot be empty")
    return MD4.new(password.encode('utf-16le')).hexdigest()

def main():
    parser = argparse.ArgumentParser(description='Generate NT hash from password')
    parser.add_argument('-p', '--password', help='Password to hash (not recommended, use interactive mode instead)')
    args = parser.parse_args()

    try:
        if args.password:
            print(f"{Fore.YELLOW}Warning: Providing passwords via command line is not secure!{Style.RESET_ALL}")
            password = args.password
        else:
            password = getpass(f"{Fore.CYAN}Enter password to generate NT hash: {Style.RESET_ALL}")

        nt_hash = generate_nt_hash(password)
        print(f"\n{Fore.GREEN}NT Hash: {Style.BRIGHT}{nt_hash}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}Length: {len(nt_hash)} characters{Style.RESET_ALL}")

    except ValueError as e:
        print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Program terminated by user{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Unexpected error: {str(e)}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()

# colors lib
from colorama import Fore

# cli libs
import argparse

# lib settings
from src.settings import Settings
from src.takeover import Takeover

# lib imports
from urllib.parse import urlparse

# threads
import concurrent.futures

print(Settings.BANNER.value)

# cli parser
parser = argparse.ArgumentParser()
parser.add_argument("-l", help="List of subdomains to check.", default=[], required=False)
parser.add_argument("-d", help="Single subdomain to check.", default=None, required=False)
parser.add_argument("-t", help="Number of threads (default 1)", default=1, required=False)
parser.add_argument("-o", help="Output file name", required=False)
args = parser.parse_args()

print()
print(22 * "-")
print(f"{Fore.CYAN}Mode list{Fore.RESET}: {Fore.BLACK}{'true' if args.l else 'false'}{Fore.RESET}")
print(f"{Fore.CYAN}Mode single{Fore.RESET}: {Fore.BLACK}{'true' if args.d else 'false'}{Fore.RESET}")
print(f"{Fore.CYAN}Number of threads{Fore.RESET}: {Fore.BLACK}{args.t}{Fore.RESET}")
print(22 * "-")
print()

subdomain_takeover = Takeover()

if args.l:
    with open(args.l, "r") as file:
        subdomains = file.read().splitlines()

    def check_subdomain(subdomain):
        if not subdomain.startswith("http") and not subdomain.startswith("https"):
            hostname = subdomain
        else:
            parsed_url = urlparse(subdomain)
            hostname = parsed_url.hostname
        vuln, service, discuss = subdomain_takeover.is_vulnerable(url=hostname)
        if vuln:
            print(f"{Fore.LIGHTGREEN_EX}Vulnerable subdomain: {subdomain}{Fore.RESET}")
            print(f"{Fore.LIGHTGREEN_EX}Service: {service}{Fore.RESET}")
            print(f"{Fore.LIGHTGREEN_EX}Discuss: {discuss}{Fore.RESET}")
        else:
            print(f"{Fore.LIGHTRED_EX}Not vulnerable subdomain: {subdomain}{Fore.RESET}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=int(args.t)) as executor:
        executor.map(check_subdomain, subdomains)

if args.d:
    if not args.d.startswith("http") and not args.d.startswith("https"):
        hostname = args.d
    else:
        parsed_url = urlparse(args.d)
        hostname = parsed_url.hostname
    vuln, service, discuss = subdomain_takeover.is_vulnerable(url=hostname)
    if vuln:
        print(f"{Fore.LIGHTGREEN_EX}Vulnerable subdomain: {args.d}{Fore.RESET}")
        print(f"{Fore.LIGHTGREEN_EX}Service: {service}{Fore.RESET}")
        print(f"{Fore.LIGHTGREEN_EX}Discuss: {discuss}{Fore.RESET}")
    else:
        print(f"{Fore.LIGHTRED_EX}Not vulnerable subdomain: {args.d}{Fore.RESET}")

from colorama import Fore, Style, init

init(autoreset=True)


def banner():
    print(f"{Fore.CYAN}")
    print("====================================")
    print("         PYTHON PACKET SNIFFER      ")
    print("====================================")
    print(f"{Style.RESET_ALL}")


def info(message):
    print(f"{Fore.CYAN}[*] {message}{Style.RESET_ALL}")


def success(message):
    print(f"{Fore.GREEN}[+] {message}{Style.RESET_ALL}")


def warning(message):
    print(f"{Fore.YELLOW}[!] {message}{Style.RESET_ALL}")


def error(message):
    print(f"{Fore.RED}[ERROR] {message}{Style.RESET_ALL}")
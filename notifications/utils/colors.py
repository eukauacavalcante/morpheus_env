from colorama import Fore, Style, init

init(autoreset=True)


def print_success(message):
    print(Fore.GREEN + Style.BRIGHT + str(message))


def print_error(message):
    print(Fore.RED + Style.BRIGHT + str(message))


def print_warning(message):
    print(Fore.YELLOW + Style.BRIGHT + str(message))

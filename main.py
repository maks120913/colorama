import colorama
from colorama import init, Fore, Back, Style

def introspect_module(module, module_name):
    print(f"Inspecting module: {module_name}")
    for attr in dir(module):
        if not attr.startswith('_'):
            print(attr)

def main():
    init(autoreset=True)

    introspect_module(colorama, 'colorama')

    introspect_module(Fore, 'colorama.Fore')

    introspect_module(Back, 'colorama.Back')

    introspect_module(Style, 'colorama.Style')

    print(Fore.RED + "This is red text")
    print(Back.GREEN + "This has a green background")
    print(Style.BRIGHT + "This is bright text")

if __name__ == "__main__":
    main()


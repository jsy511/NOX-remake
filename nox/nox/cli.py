from nox import __version__
from nox.modules import MODULES


def show_help():
    print("""
Available commands:

  help       Show available commands
  info       Show information about NOX
  modules    List available modules
  version    Show NOX version
  exit       Exit NOX
""")


def show_info():
    print("""
NOX
Mobile Cybersecurity Toolkit

Built for:
- Cybersecurity education
- Defensive security
- CTFs
- Authorised security testing
""")


def show_modules():
    print("\nAvailable modules:")

    for module in MODULES:
        print(f"  [ ] {module}")

    print()


def start_cli():
    print("Type 'help' for available commands.")
    print()

    while True:
        try:
            command = input("NOX > ").strip().lower()

            if command == "help":
                show_help()

            elif command == "info":
                show_info()

            elif command == "modules":
                show_modules()

            elif command == "version":
                print(f"NOX v{__version__}")

            elif command == "exit":
                print("Goodbye.")
                break

            elif command:
                print(f"Unknown command: {command}")

        except KeyboardInterrupt:
            print("\nGoodbye.")
            break

        except EOFError:
            print("\nGoodbye.")
            break
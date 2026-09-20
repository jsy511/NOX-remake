def start_cli():
    print("Type 'help' for available commands.")
    print()

    while True:
        try:
            command = input("NOX > ").strip().lower()

            if command == "help":
                print("""
Available commands:

  help       Show available commands
  info       Show information about NOX
  version    Show NOX version
  exit       Exit NOX
""")

            elif command == "info":
                print("""
NOX
Mobile Cybersecurity Toolkit

Built for:
- Cybersecurity education
- Defensive security
- CTFs
- Authorised security testing
""")

            elif command == "version":
                print("NOX v0.1.0")

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
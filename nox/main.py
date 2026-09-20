from nox import __version__
from nox.banner import BANNER


def main():
    print(BANNER)
    print(f"NOX v{__version__}")
    print("NOX is starting...")


if __name__ == "__main__":
    main()
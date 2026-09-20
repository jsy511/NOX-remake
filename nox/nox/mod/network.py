"""
NOX Network Module

Provides basic network information for the local device.
"""

import socket


def get_hostname():
    """Get the device hostname."""
    return socket.gethostname()


def get_local_ip():
    """Get the local IP address."""

    try:
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)

    except socket.gaierror:
        return "Unavailable"


def run():
    """Run the network information module."""

    print("\n--- NOX Network ---")
    print(f"Hostname : {get_hostname()}")
    print(f"Local IP : {get_local_ip()}")
    print("-------------------\n")
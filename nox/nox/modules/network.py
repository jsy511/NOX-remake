"""
NOX Network Module

Safe network diagnostic utilities.
"""

import socket


def get_local_hostname():
    """Return the device hostname."""
    return socket.gethostname()


def get_local_ip():
    """Return the local IP address."""
    hostname = get_local_hostname()

    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        return "Unavailable"


def run():
    """Display basic network information."""
    print("\nNOX Network Diagnostics")
    print("-----------------------")
    print(f"Hostname : {get_local_hostname()}")
    print(f"Local IP : {get_local_ip()}")
    print()
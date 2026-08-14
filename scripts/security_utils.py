import socket
import ipaddress
from urllib.parse import urlparse

def is_safe_url(url: str) -> bool:
    """
    Check if a URL is safe to fetch, preventing SSRF.
    - Only allows http and https schemes.
    - Prevents requests to private, loopback, and reserved IP addresses.
    """
    if not url:
        return False

    try:
        parsed = urlparse(url)
    except Exception:
        return False

    if parsed.scheme not in ("http", "https"):
        return False

    hostname = parsed.hostname
    if not hostname:
        return False

    try:
        # Resolve all IP addresses for the hostname
        # Using socket.getaddrinfo handles both IPv4 and IPv6
        addr_info = socket.getaddrinfo(hostname, None)
        for addr in addr_info:
            ip_str = addr[4][0]
            ip = ipaddress.ip_address(ip_str)

            if (ip.is_private or
                ip.is_loopback or
                ip.is_link_local or
                ip.is_multicast or
                ip.is_reserved or
                ip.is_unspecified):
                return False

        return True
    except (socket.gaierror, ValueError):
        # Could not resolve or invalid IP
        return False

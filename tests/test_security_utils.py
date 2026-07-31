import sys
import os
import unittest
from unittest.mock import patch

# Add scripts to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts")))

from security_utils import is_safe_url

class TestSecurityUtils(unittest.TestCase):

    def test_safe_urls(self):
        # We don't want to actually resolve these if we can avoid it,
        # but for this test we assume public DNS works and these are safe.
        # In a restricted environment, we might need to mock socket.getaddrinfo.
        with patch('socket.getaddrinfo') as mock_getaddrinfo:
            # Mocking a public IP (e.g., Google's 8.8.8.8)
            mock_getaddrinfo.return_value = [(2, 1, 6, '', ('8.8.8.8', 0))]
            self.assertTrue(is_safe_url("https://www.google.com"))
            self.assertTrue(is_safe_url("http://example.com/page"))

    def test_unsafe_schemes(self):
        self.assertFalse(is_safe_url("file:///etc/passwd"))
        self.assertFalse(is_safe_url("ftp://example.com"))
        self.assertFalse(is_safe_url("gopher://example.com"))
        self.assertFalse(is_safe_url("javascript:alert(1)"))

    def test_private_ips(self):
        with patch('socket.getaddrinfo') as mock_getaddrinfo:
            # 127.0.0.1
            mock_getaddrinfo.return_value = [(2, 1, 6, '', ('127.0.0.1', 0))]
            self.assertFalse(is_safe_url("http://127.0.0.1"))
            self.assertFalse(is_safe_url("http://localhost"))

            # 192.168.1.1
            mock_getaddrinfo.return_value = [(2, 1, 6, '', ('192.168.1.1', 0))]
            self.assertFalse(is_safe_url("http://192.168.1.1"))

            # 10.0.0.1
            mock_getaddrinfo.return_value = [(2, 1, 6, '', ('10.0.0.1', 0))]
            self.assertFalse(is_safe_url("http://10.0.0.1"))

            # 169.254.169.254 (AWS Metadata)
            mock_getaddrinfo.return_value = [(2, 1, 6, '', ('169.254.169.254', 0))]
            self.assertFalse(is_safe_url("http://169.254.169.254"))

    def test_ipv6_private(self):
        with patch('socket.getaddrinfo') as mock_getaddrinfo:
            # ::1 (loopback)
            mock_getaddrinfo.return_value = [(socket.AF_INET6, 1, 6, '', ('::1', 0, 0, 0))]
            self.assertFalse(is_safe_url("http://[::1]"))

            # fe80:: (link-local)
            mock_getaddrinfo.return_value = [(socket.AF_INET6, 1, 6, '', ('fe80::1', 0, 0, 0))]
            self.assertFalse(is_safe_url("http://[fe80::1]"))

    def test_resolution_failure(self):
        with patch('socket.getaddrinfo') as mock_getaddrinfo:
            import socket
            mock_getaddrinfo.side_effect = socket.gaierror
            self.assertFalse(is_safe_url("http://nonexistent.domain.that.does.not.resolve"))

if __name__ == "__main__":
    import socket # ensure socket is available for AF_INET6 reference in test
    unittest.main()

import threading
import time
import pytest
from utils.rate_limiter_token_bucket import RateLimiterTokenBucket

# filepath: /home/baongoc/workspaces/python-lab/tests/utils/test_rate_limiter_token_bucket.py


class TestRateLimiterTokenBucket:
    def test_init(self):
        limiter = RateLimiterTokenBucket(request_per_second=10, cleanup_interval=3600)
        assert limiter.request_per_second == 10
        assert limiter.cleanup_interval == 3600
        assert isinstance(limiter.clients, dict)
        assert isinstance(limiter.lock, type(threading.Lock()))

    @pytest.mark.parametrize("rate", [1, 5, 10])
    def test_allow_within_limit(self, rate):
        limiter = RateLimiterTokenBucket(request_per_second=rate)
        client_ip = "192.168.1.1"
        for _ in range(rate):
            assert limiter.is_allowed(client_ip) is True
        # After exhausting tokens, should deny
        assert limiter.is_allowed(client_ip) is False

    def test_deny_after_limit(self):
        limiter = RateLimiterTokenBucket(request_per_second=2)
        client_ip = "192.168.1.1"
        assert limiter.is_allowed(client_ip) is True
        assert limiter.is_allowed(client_ip) is True
        assert limiter.is_allowed(client_ip) is False
        assert limiter.is_allowed(client_ip) is False

    def test_refill_over_time(self):
        limiter = RateLimiterTokenBucket(request_per_second=1)  # 1 request per second
        client_ip = "192.168.1.1"
        assert limiter.is_allowed(client_ip) is True
        assert limiter.is_allowed(client_ip) is False  # Should deny immediately
        time.sleep(1.1)  # Wait for refill
        assert limiter.is_allowed(client_ip) is True  # Should allow after refill

    def test_multiple_clients(self):
        limiter = RateLimiterTokenBucket(request_per_second=2)
        client1 = "192.168.1.1"
        client2 = "192.168.1.2"
        # Client1 uses tokens
        assert limiter.is_allowed(client1) is True
        assert limiter.is_allowed(client1) is True
        assert limiter.is_allowed(client1) is False
        # Client2 should be independent
        assert limiter.is_allowed(client2) is True
        assert limiter.is_allowed(client2) is True
        assert limiter.is_allowed(client2) is False

    @pytest.mark.parametrize("rate", [0, -1])
    def test_edge_cases_zero_or_negative_rate(self, rate):
        limiter = RateLimiterTokenBucket(request_per_second=rate)
        client_ip = "192.168.1.1"
        # For rate=0 or negative, tokens start at rate (0 or negative), so <=0, deny
        assert limiter.is_allowed(client_ip) is False

    def test_new_client_init(self):
        limiter = RateLimiterTokenBucket(request_per_second=5)
        client_ip = "192.168.1.1"
        # First call should init and allow
        assert limiter.is_allowed(client_ip) is True
        # Check internal state
        assert client_ip in limiter.clients
        assert limiter.clients[client_ip]["tokens"] == 4  # After one use

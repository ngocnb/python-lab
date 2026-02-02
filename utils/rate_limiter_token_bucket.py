import math
import threading
import time


class RateLimiterTokenBucket:
    def __init__(self, request_per_second=10, cleanup_interval=3600):
        self.clients: dict[str, dict] = {}
        self.request_per_second = request_per_second
        self.cleanup_interval = cleanup_interval
        self.lock = threading.Lock()

    def is_allowed(self, client_ip: str) -> bool:
        with self.lock:
            now = time.time()

            # init if not presents in clients list
            if client_ip not in self.clients:
                self.clients[client_ip] = {
                    "tokens": self.request_per_second,
                    "last_fill": now,
                }

            # refill token bucket
            refill_tokens = math.floor(now - self.clients[client_ip]["last_fill"])
            self.clients[client_ip]["tokens"] = min(
                self.request_per_second,
                self.clients[client_ip]["tokens"] + refill_tokens,
            )

            if self.clients[client_ip]["tokens"] <= 0:
                return False

            self.clients[client_ip]["tokens"] -= 1

        return True

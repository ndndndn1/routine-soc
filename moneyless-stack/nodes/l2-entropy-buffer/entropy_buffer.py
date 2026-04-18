"""L2 — Entropy Buffer node.

Maintains a slack reservoir. Produces surplus each tick, satisfies
non-essential demand only above a reserve floor. Reserve floor is
motivated by combo-B §5 (Jevons rebound) and enforced hard.
"""

import json
import random
import time


class SlackBuffer:
    def __init__(self, capacity: float = 100.0, reserve_fraction: float = 0.1) -> None:
        self.capacity = capacity
        self.reserve_fraction = reserve_fraction
        self.slack = capacity * 0.5

    def produce(self, amount: float) -> None:
        self.slack = min(self.capacity, self.slack + amount)

    def allocate_nonessential(self, request: float) -> float:
        reserve = self.capacity * self.reserve_fraction
        available = max(0.0, self.slack - reserve)
        granted = min(request, available)
        self.slack -= granted
        return granted


def main() -> None:
    buf = SlackBuffer()
    t = 0
    while True:
        buf.produce(random.uniform(0.5, 2.0))
        req = random.uniform(0.0, 3.0)
        granted = buf.allocate_nonessential(req)
        print(
            json.dumps(
                {
                    "node": "l2-entropy-buffer",
                    "t": t,
                    "slack": round(buf.slack, 3),
                    "reserve_floor": buf.capacity * buf.reserve_fraction,
                    "request": round(req, 3),
                    "granted": round(granted, 3),
                    "denied": round(req - granted, 3),
                }
            ),
            flush=True,
        )
        t += 1
        time.sleep(5)


if __name__ == "__main__":
    main()

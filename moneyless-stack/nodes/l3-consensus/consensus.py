"""L3 — Physical Consensus node.

Stand-alone append-only commit log. Currently single-node; genuine
distributed consensus requires a PHYSICAL_LINKS.md entry for L1↔L3
to reach status=enabled. Until then this node has nothing external
to agree with, and records only its own heartbeat.
"""

import json
import time


class SingleNodeCommitLog:
    def __init__(self) -> None:
        self.log: list[dict] = []

    def heartbeat(self, t: int) -> None:
        self.log.append({"t": t, "kind": "heartbeat"})


def main() -> None:
    cl = SingleNodeCommitLog()
    t = 0
    while True:
        cl.heartbeat(t)
        print(
            json.dumps(
                {
                    "node": "l3-consensus",
                    "t": t,
                    "committed_entries": len(cl.log),
                    "awaiting_links": ["l1-reliability", "l2-entropy-buffer"],
                }
            ),
            flush=True,
        )
        t += 1
        time.sleep(5)


if __name__ == "__main__":
    main()

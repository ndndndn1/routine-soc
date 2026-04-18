"""physical-bridge — adapter stub.

This node exists only as a structural placeholder. It does NOT open
any link by itself. It is gated behind docker-compose profile 'bridge'
so it does not start under normal `docker compose up`.

When a link in PHYSICAL_LINKS.md transitions to status=enabled, this
bridge will host the corresponding adapter (e.g. TPM-attested socket,
sensor-bus reader) in a future run.
"""

import json
import sys
import time


def main() -> None:
    print(
        json.dumps(
            {
                "node": "physical-bridge",
                "status": "disabled",
                "reason": "no link in PHYSICAL_LINKS.md is currently 'enabled'",
            }
        ),
        flush=True,
    )
    sys.stdout.flush()
    # idle briefly then exit, since no work is authorised
    time.sleep(2)


if __name__ == "__main__":
    main()

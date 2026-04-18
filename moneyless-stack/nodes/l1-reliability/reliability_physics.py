"""L1 — Reliability Physics node.

Minimal standalone loop that simulates a degrading asset and emits
a PHM reading with aleatoric/epistemic uncertainty, per combo-A
§1 (B-PINN) and §3 (I-GLIDE). No network I/O — default-deny.
"""

import json
import math
import random
import time


def phm_tick(t: int) -> dict:
    tau = 1000.0
    health_true = math.exp(-t / tau)
    aleatoric_sigma = 0.02
    epistemic_sigma = 0.02 + 0.01 * math.sqrt(t / tau)
    measured = max(0.0, min(1.0, health_true + random.gauss(0, aleatoric_sigma)))
    return {
        "t": t,
        "health": round(measured, 4),
        "sigma_aleatoric": round(aleatoric_sigma, 4),
        "sigma_epistemic": round(epistemic_sigma, 4),
    }


def main() -> None:
    t = 0
    while True:
        reading = phm_tick(t)
        print(json.dumps({"node": "l1-reliability", "reading": reading}), flush=True)
        t += 1
        time.sleep(5)


if __name__ == "__main__":
    main()

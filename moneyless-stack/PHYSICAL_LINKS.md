# PHYSICAL_LINKS

Every inter-node link must be listed here with an engineering basis.
Sociology references are **not** admissible.

Schema:

```
## link: <node_a> ↔ <node_b>
- physical_basis: <why the bits actually move, in physical terms>
- engineering_refs: [combo-X/papers/<id>, ...]
- compose_network: <network name in docker-compose.yml>
- status: enabled | proposed | blocked
- last_verified: <YYYY-MM-DD of run that last checked it>
```

---

_No links yet. Default deny is in effect._

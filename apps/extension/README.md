# apps/extension/

**Purpose:** Browser-assisted extension contract for profile capture and policy-aware recruiter assists.

**Why this folder exists:** Use this folder for extension entrypoints and browser-surface wiring after policy approval.

## Current assets

- `extension_surface_contract.py`

## Responsibility boundaries

This folder should own the concerns described above and should not silently absorb unrelated responsibilities just because it is nearby. If a new file is added here, update this README and the relevant architecture or localization doc in the same session.

## Nearby related docs or modules

- `docs/02_experience/`
- `docs/03_architecture/`
- `docs/06_delivery_operations/`

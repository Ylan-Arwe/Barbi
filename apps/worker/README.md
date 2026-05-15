# apps/worker/

**Purpose:** Background worker runtime contract for queues, jobs, and async processing.

**Why this folder exists:** Use this folder for queue bootstrapping, job registration, and worker lifecycle wiring.

## Current assets

- `worker_surface_contract.py`

## Implemented bootstrap surface

`worker_surface_contract.py` now provides a Celery runtime shell:
- `create_worker_runtime()` to construct and configure broker/backend wiring;
- `register_job_handlers()` with a starter health-check task;
- `run_worker()` to execute worker startup with baseline defaults.

Run locally after runtime dependencies are installed:

```bash
python -c "from apps.worker.worker_surface_contract import create_worker_runtime, run_worker; run_worker(create_worker_runtime())"
```

## Responsibility boundaries

This folder should own the concerns described above and should not silently absorb unrelated responsibilities just because it is nearby. If a new file is added here, update this README and the relevant architecture or localization doc in the same session.

## Nearby related docs or modules

- `docs/02_experience/`
- `docs/03_architecture/`
- `docs/06_delivery_operations/`

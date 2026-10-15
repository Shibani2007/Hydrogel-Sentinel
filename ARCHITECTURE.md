# COSSEN Architecture Overview

Goal: Minimal pipeline to validate and normalize monitoring data for COSSEN indicators.

Components:
- `src/app.py` — CLI orchestrator (ingest → validate → transform → export)
- `src/modules/pipeline.py` — pure functions for validation and transformation
- `data/` — sample input and expected output for integration checks
- `tests/` — pytest unit tests

Data flow:
CSV input → validate required fields → numeric parsing and normalization → CSV output

Deployment:
- Containerize with Dockerfile for reproducible runs
- Add CI to run tests on push

# Lab 7 – Fuzz Testing: Irrigation Scheduler

## Setup
Run from this directory:

```bash
python -m pip install hypothesis pytest
```

## Run the application

```bash
python irrigation_scheduler.py
```

## Run the fuzz tests

```bash
python -m pytest -v test_irrigation_scheduler.py
```

The tests use Hypothesis to generate arbitrary strings and `None` for all three functions, then check properties using valid generated inputs.

Invalid values are handled using safe fallback values:
- `parse_zone`: `("", 0.0)`
- `moisture_average`: `0`
- `water_needed`: `0.0`

Moisture readings must be integers from 0 to 100. Area and rainfall values must be finite and non-negative.

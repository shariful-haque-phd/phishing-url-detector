# Architecture — Phishing Url Detector

```mermaid
flowchart LR
    A["urls.csv"] --> B["Processing modules"]
    B --> C["Console / application output"]
    B -.-> M0["features.py"]
    B -.-> M1["predict.py"]
    B -.-> M2["train.py"]

```

## Inputs

- `sample/urls.csv`

## Source files

- `src/features.py`
- `src/predict.py`
- `src/train.py`

## Output



This representation is intended for source navigation. It does not imply a production deployment or undisclosed components. The editable diagram is available as [`architecture.mmd`](architecture.mmd).

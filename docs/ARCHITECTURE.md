# Architecture — Email Phishing Classifier

```mermaid
flowchart LR
    A["emails.csv"] --> B["Processing modules"]
    B --> C["Console / application output"]
    B -.-> M0["predict.py"]
    B -.-> M1["train.py"]

```

## Inputs

- `sample/emails.csv`

## Source files

- `src/predict.py`
- `src/train.py`

## Output



This representation is intended for source navigation. It does not imply a production deployment or undisclosed components. The editable diagram is available as [`architecture.mmd`](architecture.mmd).

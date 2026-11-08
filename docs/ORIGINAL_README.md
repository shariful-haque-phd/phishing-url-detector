# Phishing URL Detector

A defensive machine-learning baseline that classifies URLs from lexical features only. It avoids visiting or resolving submitted URLs.

## Features
Length, digit ratio, suspicious token count, subdomain depth, IP-host indicator, special-character counts, HTTPS indicator, and other lexical features.

## Train
```bash
pip install -r requirements.txt
python src/train.py sample/urls.csv --model outputs/model.joblib
```

## Predict
```bash
python src/predict.py outputs/model.joblib "https://example.com/login"
```

The included sample dataset is intentionally tiny and exists only to verify the pipeline. Use a properly sourced, current dataset before reporting model performance.

# Email Phishing Classifier

A defensive NLP baseline for classifying email text as likely phishing or legitimate. It uses TF-IDF features and logistic regression and can display the strongest contributing terms.

## Train
```bash
pip install -r requirements.txt
python src/train.py sample/emails.csv --model outputs/model.joblib
```

## Predict
```bash
python src/predict.py outputs/model.joblib "Urgent: verify your account immediately"
```

The included data is a pipeline fixture, not a benchmark dataset.

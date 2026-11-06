# Research brief — Email Phishing Classifier

**Area:** Cybersecurity, Privacy & Abuse Defense  
**Portfolio level:** Foundations

## Research problem

A defensive NLP baseline for classifying email text as likely phishing or legitimate. It uses TF-IDF features and logistic regression and can display the strongest contributing terms.

## Question

What is the performance of simple text classifiers on clearly labeled phishing email samples?

## Implementation scope

- Defensive email NLP classifier

### Reproducible inputs and outputs

The current baseline uses `sample/emails.csv`. The implementation consists of `src/predict.py`, `src/train.py`. Execution records, where available, are retained in [`results/`](../results/).

## Evaluation plan

1. Establish a versioned data protocol, input schema and independent baseline.
2. Evaluate functional correctness and record both successful and failed cases.
3. Compare relevant outcomes under controlled input variations and fixed environment settings.
4. Measure resource use and execution time across replicates when meaningful.
5. Document limitations, data provenance and risks of deployment in consequential environments.

### Validity and scope

The included local inputs are not evidence of population-level accuracy or external impact. Any synthetic inputs, simulations, heuristics and estimated performance figures must remain explicitly identified. Future benchmarks should use representative datasets, appropriate baselines, pre-specified metrics and independently reviewed methods.

## Evidence

Refer to [the recorded run](RESULTS.md), or to [the original project instructions](ORIGINAL_README.md) where local execution is not established. No publication, patent, user adoption or real-world deployment is claimed.

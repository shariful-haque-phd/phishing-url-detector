import argparse, joblib
from features import feature_dict
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("model"); ap.add_argument("url"); a=ap.parse_args()
    m=joblib.load(a.model)
    proba=float(m.predict_proba([feature_dict(a.url)])[0][1])
    print({"url":a.url,"phishing_probability":round(proba,4),"predicted_label":int(proba>=0.5)})
if __name__=="__main__": main()

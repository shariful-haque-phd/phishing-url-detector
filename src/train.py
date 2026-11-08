from pathlib import Path
import argparse, joblib, pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from features import feature_dict

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("csv"); ap.add_argument("--model",default="model.joblib"); a=ap.parse_args()
    df=pd.read_csv(a.csv)
    X=[feature_dict(u) for u in df["url"].astype(str)]
    y=df["label"].astype(int)
    model=Pipeline([("vec",DictVectorizer()),("clf",RandomForestClassifier(n_estimators=250,random_state=42,class_weight="balanced"))])
    if len(df)>=10 and y.nunique()>1:
        Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.3,random_state=42,stratify=y)
        model.fit(Xtr,ytr); print(classification_report(yte,model.predict(Xte),digits=3))
    else:
        model.fit(X,y)
    Path(a.model).parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model,a.model); print("saved",a.model)
if __name__=="__main__": main()

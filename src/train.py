from pathlib import Path
import argparse, joblib, pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("csv"); ap.add_argument("--model",default="model.joblib"); a=ap.parse_args()
    df=pd.read_csv(a.csv)
    model=Pipeline([("tfidf",TfidfVectorizer(ngram_range=(1,2),min_df=1)),
                    ("clf",LogisticRegression(max_iter=1000,class_weight="balanced"))])
    X=df["text"].astype(str); y=df["label"].astype(int)
    if len(df)>=10 and y.nunique()>1:
        Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.3,random_state=42,stratify=y)
        model.fit(Xtr,ytr); print(classification_report(yte,model.predict(Xte),digits=3))
    else: model.fit(X,y)
    Path(a.model).parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model,a.model); print("saved",a.model)
if __name__=="__main__":main()

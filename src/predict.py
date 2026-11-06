import argparse, joblib, numpy as np
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("model"); ap.add_argument("text"); a=ap.parse_args()
    m=joblib.load(a.model); p=float(m.predict_proba([a.text])[0][1])
    vec=m.named_steps["tfidf"]; clf=m.named_steps["clf"]
    x=vec.transform([a.text]); contrib=x.multiply(clf.coef_[0]).toarray()[0]
    names=np.array(vec.get_feature_names_out()); top=np.argsort(contrib)[-5:][::-1]
    terms=[{"term":names[i],"contribution":round(float(contrib[i]),4)} for i in top if contrib[i]>0]
    print({"phishing_probability":round(p,4),"predicted_label":int(p>=.5),"top_phishing_terms":terms})
if __name__=="__main__":main()

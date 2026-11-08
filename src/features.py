from urllib.parse import urlparse
import ipaddress, re
SUSPICIOUS={"login","verify","secure","account","update","password","bank","wallet","confirm","signin"}

def feature_dict(url):
    u=url if "://" in url else "http://"+url
    p=urlparse(u)
    host=p.hostname or ""
    try:
        ipaddress.ip_address(host); is_ip=1
    except ValueError:
        is_ip=0
    lower=url.lower()
    return {
        "length":len(url),
        "digit_ratio":sum(c.isdigit() for c in url)/max(len(url),1),
        "dots":url.count("."),
        "hyphens":url.count("-"),
        "ats":url.count("@"),
        "question_marks":url.count("?"),
        "equals":url.count("="),
        "subdomain_depth":max(0,len(host.split("."))-2),
        "https":int(p.scheme.lower()=="https"),
        "ip_host":is_ip,
        "suspicious_tokens":sum(tok in lower for tok in SUSPICIOUS),
    }

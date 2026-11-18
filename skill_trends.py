import re
from collections import Counter

# (표시명, 정규식) — 단어 경계 주의 (Go, R, C 같은 짧은 이름은 보수적으로)
SKILLS = [
    ("Python", r"\bpython\b"), ("JavaScript", r"\bjavascript\b"),
    ("TypeScript", r"\btypescript\b"), ("Java", r"\bjava\b(?!script)"),
    ("C#/.NET", r"\bc#|\.net\b"), ("C++", r"c\+\+"), ("Go", r"\bgolang\b|\bgo developer\b"),
    ("SQL", r"\bsql\b"), ("React", r"\breact\b"), ("Angular", r"\bangular\b"),
    ("Node.js", r"\bnode\.?js\b"), ("PHP", r"\bphp\b"), ("Rust", r"\brust\b"),
    ("AWS", r"\baws\b|amazon web services"), ("Azure", r"\bazure\b"),
    ("GCP", r"\bgcp\b|google cloud"), ("Docker", r"\bdocker\b"),
    ("Kubernetes", r"\bkubernetes\b|\bk8s\b"), ("Terraform", r"\bterraform\b"),
    ("Linux", r"\blinux\b"), ("Salesforce", r"\bsalesforce\b"),
    ("SAP", r"\bsap\b"), ("Power BI", r"\bpower ?bi\b"),
    ("Machine Learning/AI", r"machine learning|\bml\b|\bai\b|artificial intelligence|llm"),
    ("DevOps", r"\bdevops\b"), ("CI/CD", r"ci/cd|\bcicd\b"),
]

CERTS = [
    ("AWS 자격증", r"aws certified|aws certification|solutions architect"),
    ("Azure 자격증", r"az-\d{3}|azure certif|sc-\d{3}"),
    ("Security+", r"security\+"), ("CISSP", r"\bcissp\b"),
    ("CISM/CISA", r"\bcism\b|\bcisa\b"), ("OSCP", r"\boscp\b"),
    ("CEH", r"\bceh\b"), ("ITIL", r"\bitil\b"), ("PMP", r"\bpmp\b"),
    ("CCNA/Cisco", r"\bccna\b|\bccnp\b|cisco certified"),
    ("ISO 27001", r"iso ?27001"), ("IRAP", r"\birap\b"),
    ("Comptia 계열", r"comptia"), ("Agile/Scrum 자격", r"\bcsm\b|safe agilist|scrum master certif"),
]

ROLES = [
    ("소프트웨어 개발/엔지니어", r"software (engineer|developer)|full ?stack|backend|front ?end|web developer|application developer|programmer"),
    ("사이버 보안", r"cyber|security (engineer|analyst|specialist|consultant|architect)|penetration|soc analyst"),
    ("데이터/AI", r"data (engineer|analyst|scientist)|machine learning|\bai\b|analytics"),
    ("클라우드/DevOps/인프라", r"devops|cloud (engineer|architect)|platform engineer|site reliability|infrastructure|systems engineer|network engineer"),
    ("IT 지원/서비스데스크", r"service desk|help ?desk|support (officer|engineer|analyst|specialist)|desktop support|level [123]"),
    ("BA/PM/딜리버리", r"business analyst|project manager|delivery|product (manager|owner)|scrum master"),
    ("관리자/아키텍트", r"administrator|architect(?!ure)"),
    ("테스트/QA", r"\btest\b|\bqa\b|quality assurance"),
]


def _count(rows, patterns) -> list[dict]:
    counts = Counter()
    for pat_name, pat in patterns:
        rx = re.compile(pat, re.I)
        n = sum(1 for t in rows if rx.search(t))
        if n:
            counts[pat_name] = n
    total = len(rows) or 1
    return [{"name": k, "count": v, "pct": round(v * 100 / total)}
            for k, v in counts.most_common(15)]

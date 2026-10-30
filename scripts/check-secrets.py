"""Offline secret checks. Never prints candidate values; exits nonzero on findings."""
import argparse
import json
from pathlib import Path
import re
import sys

RULES = {
    'secret_key_prefix': r'\bsk-[A-Za-z0-9_-]{12,}',
    'github_token': r'\b(?:gh[pousr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,})',
    'huggingface_token': r'\bhf_[A-Za-z0-9]{20,}',
    'access_key_id': r'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b',
    'private_key': r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
    'literal_credential': r'''(?i)\b(?:api_key|apikey|password|access_token|secret_key)\b\s*[:=]\s*["']([^"'\s]{12,})["']''',
}


def scan(root):
    root = Path(root).resolve()
    findings, references = [], []
    files = 0
    for path in sorted(root.rglob('*')):
        if not path.is_file() or '.git' in path.relative_to(root).parts:
            continue
        rel = path.relative_to(root).as_posix()
        files += 1
        if path.name == '.env' or path.name.startswith('.env.') or re.search('api_key',path.name,re.I):
            findings.append({'file':rel,'rule':'credential_filename'})
        text = path.read_bytes().decode('utf-8-sig',errors='replace')
        for label, pattern in RULES.items():
            for match in re.finditer(pattern,text):
                findings.append({'file':rel,'line':text.count('\n',0,match.start())+1,'rule':label})
        # These are references for manual review, never credential values.
        lines = [i for i,line in enumerate(text.splitlines(),1) if re.search(r'sk-|api_key|DASHSCOPE_API_KEY',line,re.I)]
        if lines:
            references.append({'file':rel,'lines':lines})
    return {'status':'passed' if not findings else 'blocked','scanned_files':files,
        'candidate_credentials':findings,'reference_locations':references,
        'reference_note':'Environment-variable names and scanner patterns are references, not detected credential values.'}


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('root',nargs='?',default=str(Path(__file__).resolve().parent.parent))
    parser.add_argument('--report')
    args=parser.parse_args()
    result=scan(args.root)
    if args.report:
        Path(args.report).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=True))
    sys.exit(0 if result['status']=='passed' else 1)

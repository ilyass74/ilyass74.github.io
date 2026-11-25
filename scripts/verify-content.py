"""Check the publishable directory, links, SEO and content boundaries."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json,re
root=Path(__file__).resolve().parents[1];out=root/'docs'
class Document(HTMLParser):
    def __init__(self,text):
        super().__init__();self.ids=[];self.links=[];self.canonicals=[];self.h1s=0;self.feed(text)
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if 'id' in attrs:self.ids.append(attrs['id'])
        if tag=='h1':self.h1s+=1
        if tag=='a' and 'href' in attrs:self.links.append(attrs['href'])
        if tag=='link' and attrs.get('rel')=='canonical':self.canonicals.append(attrs.get('href'))
documents={p:Document(p.read_text(encoding='utf-8')) for p in out.rglob('*.html')}
assert len(documents)==18
checked=0
for path,doc in documents.items():
    assert len(set(doc.ids))==len(doc.ids),f'Duplicate IDs: {path}'
    assert doc.h1s==1,f'Heading count: {path}'
    if path.name!='404.html':assert len(doc.canonicals)==1,f'Canonical: {path}'
    for href in doc.links:
        url=urlsplit(href)
        if url.scheme or url.netloc:continue
        target=out/unquote(url.path).lstrip('/') if url.path.startswith('/') else path.parent/url.path
        if not url.path:target=path
        if target.is_dir():target=target/'index.html'
        assert target.is_file(),f'Missing internal target: {href} in {path}'
        if url.fragment:assert url.fragment in documents[target].ids,f'Missing fragment: {href}'
        checked+=1
    text=path.read_text(encoding='utf-8')
    for forbidden in ['C:\\Users\\','ANSUF_SCOUT_DATABASE_URL','siwc_bypass_bearer_token','source_repository_credential','github.com/ilyass74/ANSUF/blob/']:
        assert forbidden not in text,f'Forbidden source detail: {path}'
files=list(out.rglob('*'))
assert not any(p.name in ['research','.git','.env','GITHUB_PROJECT_AUDIT.md'] for p in files)
projects=json.loads((root/'content/projects.json').read_text(encoding='utf-8'))
assert len(projects)==13 and projects[0]['slug']=='ansuf'
assert len(next(p for p in projects if p['slug']=='ansuf')['sections'])>=10
assert (out/'assets/social-cover.png').is_file()
report={'htmlPages':len(documents),'internalLinksAndFragments':checked,'projectStudies':len(projects),'leadProject':'ANSUF','privateMaterialExcluded':True,'canonicalAndSocialMetadata':'passed','allChecks':'passed'}
(root/'validation').mkdir(exist_ok=True)
(root/'validation/content-report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report))

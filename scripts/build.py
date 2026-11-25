"""Dependency-free static publishing. Research/private files never enter out/."""
from pathlib import Path
from html import escape as e
import json, shutil, hashlib, sys, os
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from editorial import homepage, venture_brief
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs'
PROJECTS=json.loads((ROOT/'content/projects.json').read_text(encoding='utf-8'))
BY_ID={p['slug']:p for p in PROJECTS}
CV=ROOT/'public/Ilyass_Chakir_PFE_Data_IA_Horizon2027.pdf'

def a(href,label,cls=''):
    return f'<a href="{e(href)}"'+(f' class="{cls}"' if cls else '')+f'>{e(label)}</a>'

def mark(slug,large=False):
    """Authored vector system schematics, never fictional application screens."""
    title={'nerve':'NERVE event-to-evidence architecture','aqua-sentinel':'AQUA historical hydraulic network topology','money-trail':'Money Trail source-to-reviewed-publication architecture','ansuf':'ANSUF geographic knowledge and publication architecture'}.get(slug,'Data processing architecture')
    base=f'<svg class="system-mark {slug}" viewBox="0 0 720 440" role="img" aria-label="{title}" xmlns="http://www.w3.org/2000/svg"><defs><pattern id="grid-{slug}" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r=".8" fill="currentColor" opacity=".16"/></pattern></defs><rect width="720" height="440" fill="url(#grid-{slug})"/>'
    if slug=='aqua-sentinel':
        base+='''<g fill="none" stroke="currentColor" stroke-width="3"><path d="M80 230H230M230 230L410 90L590 230L410 370Z"/></g><g class="svg-label"><text x="137" y="213">P1</text><text x="300" y="145">P2</text><text x="294" y="330">P3</text><text x="505" y="137">P4</text><text x="505" y="334">P5</text></g><g stroke="currentColor" stroke-width="2" fill="var(--panel)"><rect x="58" y="208" width="44" height="44"/><circle cx="230" cy="230" r="14"/><circle cx="410" cy="90" r="14"/><circle cx="590" cy="230" r="14"/><circle cx="410" cy="370" r="14"/></g><circle cx="500" cy="160" r="9" fill="var(--acid)" stroke="currentColor" stroke-width="2"/><g class="svg-label"><text x="74" y="285">R</text><text x="220" y="274">A</text><text x="405" y="55">B</text><text x="618" y="238">D</text><text x="405" y="410">C</text><text x="530" y="184">L4</text></g>'''
    elif slug=='nerve':
        base+='''<g fill="none" stroke="currentColor" stroke-width="2"><path d="M70 112H155V220H225M70 220H225M70 328H155V220H225M325 220H385M485 220H545V112H645M485 220H545V328H645"/><path d="M265 263V345H455" stroke-dasharray="5 7"/></g><g fill="var(--panel)" stroke="currentColor" stroke-width="2"><rect x="225" y="176" width="100" height="88"/><rect x="385" y="176" width="100" height="88"/></g><g class="svg-label"><text x="30" y="92">RIPE</text><text x="30" y="200">LAB</text><text x="30" y="308">OTEL</text><text x="241" y="215">KAFKA</text><text x="242" y="239" class="svg-small">INGEST</text><text x="397" y="215">ICEBERG</text><text x="400" y="239" class="svg-small">B / S / G</text><text x="564" y="92">EVIDENCE</text><text x="565" y="352">FASTAPI</text><text x="292" y="372" class="svg-small">CHECKPOINT / REPLAY</text></g><g fill="var(--acid)" stroke="currentColor" stroke-width="2"><circle cx="70" cy="112" r="7"/><circle cx="70" cy="220" r="7"/><circle cx="70" cy="328" r="7"/><rect x="638" y="105" width="14" height="14"/><rect x="638" y="321" width="14" height="14"/></g>'''
    elif slug=='money-trail':
        base+='''<g fill="var(--panel)" stroke="currentColor" stroke-width="2"><path d="M110 80H260V270H110Z"/><path d="M130 100H280V290H130Z"/><path d="M150 120H300V310H150Z"/><rect x="430" y="120" width="180" height="190"/></g><g fill="none" stroke="currentColor" stroke-width="2"><path d="M178 160H270M178 188H270M178 216H245M178 270H270M300 215H430M350 200V230M367 200V230M460 160H580M460 190H580M460 220H535"/><path d="M480 265l18 18 38-42" stroke-width="4"/></g><rect x="437" y="317" width="169" height="26" fill="var(--acid)"/><g class="svg-label"><text x="150" y="366">SOURCE RECORDS</text><text x="435" y="365">REVIEWED RESULT</text><text x="319" y="180" class="svg-small">DBT</text></g>'''
    elif slug=='ansuf':
        base+='''<g fill="none" stroke="currentColor" stroke-width="1.5" opacity=".7"><path d="M50 135l170-50 170 50 230-60M40 200l200-60 170 60 250-60M40 270l220-60 180 60 240-60M60 345l220-60 180 60 220-60M150 70l100 300M280 50l100 340M420 60l100 320M550 50l100 300"/></g><g stroke="currentColor" fill="var(--panel)" stroke-width="2"><circle cx="250" cy="175" r="45"/><circle cx="480" cy="270" r="45"/><path d="M288 195l152 58" stroke-dasharray="5 5"/></g><g fill="var(--acid)" stroke="currentColor" stroke-width="2"><circle cx="250" cy="175" r="9"/><circle cx="480" cy="270" r="9"/></g><g class="svg-label"><text x="190" y="111">KNOWLEDGE</text><text x="430" y="350">DISCOVERY</text><text x="305" y="205" class="svg-small">PUBLICATION</text></g>'''
    else:
        base+='''<g fill="none" stroke="currentColor" stroke-width="2"><path d="M100 220H620"/></g><g fill="var(--panel)" stroke="currentColor" stroke-width="2"><rect x="95" y="175" width="110" height="90"/><rect x="305" y="175" width="110" height="90"/><rect x="515" y="175" width="110" height="90"/></g><g class="svg-label"><text x="118" y="225">RAW</text><text x="320" y="225">MODEL</text><text x="533" y="225">SERVE</text></g>'''
    return base+'</svg>'

def header(path):
    links=''.join(f'<a href="{url}"'+(' aria-current="page"' if path==url or (url=='/projects/' and path.startswith('/projects/') and path!='/projects/ansuf/') else '')+f'>{label}</a>' for url,label in [('/projects/ansuf/','ANSUF'),('/projects/','Work'),('/experience/','Experience'),('/about/','About')])
    return f'''<a class="skip" href="#main">Skip to content</a><header class="header wrap"><a class="wordmark" href="/" aria-label="Ilyass Chakir, home">IC<span class="brand-square" aria-hidden="true"></span></a><span class="header-caption">ILYASS CHAKIR<br>ENGINEERING PORTFOLIO</span><button class="menu-button" data-menu-button aria-expanded="false" aria-controls="navigation">Menu</button><nav id="navigation" aria-label="Main navigation">{links}<a class="contact-link" href="/about/#contact">Let’s talk</a></nav></header>'''

def footer():
    return '''<footer class="footer wrap"><a class="wordmark" href="/">IC<span class="brand-square" aria-hidden="true"></span></a><p>Data Engineering & AI · EMSI</p><div><a href="https://github.com/ilyass74">GitHub</a><a href="mailto:chakirilyass16@gmail.com">Email</a><a href="/Ilyass_Chakir_PFE_Data_IA_Horizon2027.pdf">CV · PDF</a></div><span class="micro">© 2026 Ilyass Chakir</span></footer>'''

def contact():
    return '''<section class="contact-section" id="contact"><div class="wrap contact-grid"><div><p class="eyebrow">THE NEXT CHAPTER</p><h2>Let’s discuss<br>your next <em>engineering challenge.</em></h2><p>Seeking a PFE internship in Data Engineering & AI<br>from February 2027.</p></div><div class="contact-details"><a class="email" href="mailto:chakirilyass16@gmail.com">chakirilyass16@gmail.com</a><div class="contact-actions"><a class="button dark" href="/Ilyass_Chakir_PFE_Data_IA_Horizon2027.pdf" download>Download CV <span>PDF</span></a><button class="text-button" data-copy-email>Copy email</button></div><p class="micro" data-copy-status role="status"></p><a href="https://ma.linkedin.com/in/ilyass-chakir-ab7201254">LinkedIn / Ilyass Chakir</a><p class="micro">Marrakech, Morocco · Open to engineering conversations</p></div></div></section>'''

def skill_list():
    rows=[('Streaming & reliability','Transport identity, replay, event-time processing and recovery.','Kafka · Spark · Iceberg',['nerve','real-time-commerce-lakehouse']),('Analytics & financial data','Source contracts, reconciliation, SQL models and publication controls.','PostgreSQL · dbt · Delta Lake',['money-trail','retail-lakehouse']),('Applied ML & simulation','Physical models, held-out experiments, detection tradeoffs and human review.','WNTR · scikit-learn · PaddleOCR',['aqua-sentinel','invoice-ai']),('Product & backend systems','Geospatial retrieval, bounded assistance, APIs and privacy-aware workflows.','PostGIS · FastAPI · Next.js',['ansuf','odoo-genai-assistant'])]
    return '<div class="capability-list">'+''.join(f'<div class="capability"><h3>{title}</h3><div><p>{body}</p><span class="micro">{stack}</span></div><div class="capability-proof">'+''.join(a('/projects/'+x+'/',BY_ID[x]['title']) for x in ids)+'</div></div>' for title,body,stack,ids in rows)+'</div>'

def home():
    return homepage(mark,skill_list,contact)

def explorer():
    cats=list(dict.fromkeys(p['category'] for p in PROJECTS))
    controls=''.join(f'<button data-category="{e(cat)}" aria-pressed="{str(cat=="All").lower()}">{e(cat)}</button>' for cat in ['All']+cats)
    rows=''
    for p in PROJECTS:
        slug=p['slug']; text=' '.join([p['title'],p['category'],p['dek']]+p['stack']).lower()
        rows+=f'''<article class="project-row" data-project data-discipline="{e(p['category'])}" data-search="{e(text)}"><div class="project-category"><span class="eyebrow">{e(p['category'])}</span>{'<span class="flagship-label">FEATURED STUDY</span>' if p['flagship'] else ''}</div><div><h2>{a('/projects/'+slug+'/',p['title'])}</h2><p>{e(p['dek'])}</p><span class="stack-line">{' / '.join(p['stack'][:5])}</span></div><a class="row-link" href="/projects/{slug}/" aria-label="Explore {e(p['title'])}">Explore study <span class="plus" aria-hidden="true">+</span></a></article>'''
    return f'''<section class="page-intro wrap"><p class="eyebrow">THE COMPLETE PROJECT INDEX</p><h1>Explore the <em>systems.</em></h1><p class="intro-dek">Streaming platforms. Financial controls. Physical simulations.<br>ANSUF leads the collection, with the implementation behind every project.</p></section><section class="explorer wrap" data-explorer aria-label="Project explorer"><div class="explorer-tools"><label class="search-label" for="project-search">Search projects, tools or disciplines<input id="project-search" type="search" placeholder="Try Kafka, financial or simulation…" autocomplete="off"></label><p class="micro" role="status" data-result-count>13 projects in view</p></div><div class="filters" role="group" aria-label="Filter by engineering discipline">{controls}</div><noscript><p>Search and filters require JavaScript. All thirteen studies are listed below.</p></noscript><div class="project-rows">{rows}</div><div class="empty-state" data-empty hidden><h2>No matching projects.</h2><p>Try another tool or explore the complete index.</p><button class="button dark" data-reset>Clear search and filters</button></div><p class="index-note">All studies distinguish implemented work, historical test evidence, experiments and known limits. ANSUF is private; its source and unpublished assets are not distributed.</p></section>'''+contact()

def architecture(p):
    buttons=''.join(f'<li><button data-node aria-expanded="{str(i==0).lower()}" aria-controls="node-panel-{i}"><span class="node-symbol" aria-hidden="true">{["□","◇","▤","⊞","◎","▣","◉"][i%7]}</span>{e(n[0])}</button></li>' for i,n in enumerate(p['flow']))
    panels=''.join(f'<div id="node-panel-{i}" data-node-panel><h3>{e(n[0])}</h3><p>{e(n[1])}</p></div>' for i,n in enumerate(p['flow']))
    return f'<div class="architecture" data-architecture><p class="micro">SELECT A STAGE TO FOLLOW THE DATA</p><ol class="flow-nodes">{buttons}</ol><div class="node-detail" aria-live="polite">{panels}</div><p class="micro">Conceptual data flow derived from implementation. Connections indicate processing direction, not measured latency.</p></div>'

def section_id(i): return 'engineering-'+str(i+1)

def lead_summary(p):
    return {
        'nerve':'Three source families. One traceable processing chain. Kafka and Spark preserve the relationship between an observation, its analytical window and the evidence served to an investigator.',
        'ansuf':'A geographic product built around a publication boundary: cultural knowledge, nearby discovery and companion assistance share source, freshness and consent rules.',
        'aqua-sentinel':'The original WNTR network contains a reservoir and a four-junction loop. Virtual pressure and flow sensors feed detection experiments; later valve-control work uses a separate laboratory.',
        'money-trail':'A source record passes through validation, typed transformations and a publication gate before a reviewer sees a result. The supporting evidence travels with it.'
    }.get(p['slug'],p['problem'])

def case(p):
    slug=p['slug']; unique={'nerve':'EVENTS / PROCESSING / INVESTIGATION','ansuf':'ENTREPRENEURSHIP / MOROCCAN TOURISM / ENGINEERING','aqua-sentinel':'HYDRAULICS / SENSING / EXPERIMENTS','money-trail':'PROVENANCE / RECONCILIATION / REVIEW'}
    hero=f'''<section class="case-hero wrap"><a class="back-link" href="/projects/">All projects</a><p class="eyebrow">{unique.get(slug,e(p['category']).upper())}</p><h1>{('AQUA NEXUS <span class="former-name">(formerly AQUA Sentinel)</span>' if slug=='aqua-sentinel' else e(p['title']))}</h1><p class="case-dek">{e(p['dek'])}</p><div class="case-meta"><span>{'ENTREPRENEURIAL PROJECT · PRIVATE PREVIEW' if p['private'] else 'INDEPENDENT ENGINEERING PROJECT'}</span><span>{' / '.join(p['stack'])}</span></div></section>'''
    art=f'<div class="case-lead-visual wrap {slug}">{mark(slug)}<div><p class="eyebrow">{e(p["category"])}</p><p>{e(lead_summary(p))}</p><span class="micro">{("Historical network topology from aqua_sentinel_demo.py. Not a physical installation." if slug=="aqua-sentinel" else "Authored conceptual system schematic, derived from implementation.")}</span></div></div>' if p['flagship'] else ''
    nav='<a href="#problem">The problem</a><a href="#architecture">System architecture</a>'+''.join(a('#'+section_id(i),s['title']) for i,s in enumerate(p['sections']))+'<a href="#limits">Scope & limitations</a><a href="#sources">Evidence & source</a>'
    sections=''
    for i,s in enumerate(p['sections']):
        refs=''.join(f'<a href="{p["sources"][r]["url"]}" title="{e(p["sources"][r]["path"])}">{e(p["sources"][r]["label"])}</a>' for r in s['sources'])
        sections+=f'<section class="story-section" id="{section_id(i)}"><h2>{e(s["title"])}</h2><p>{e(s["body"])}</p>'+(f'<div class="inline-sources"><span>Implementation & evidence</span>{refs}</div>' if refs else '')+'</section>'
        if slug=='aqua-sentinel' and i==2:
            sections+='''<figure class="artifact"><img src="/assets/aqua-ml-comparison.png" width="1650" height="1050" loading="lazy" alt="Original AQUA V1 versus V2 plot: simulated leak-event recall, false-alert rates and detection delays"><figcaption>Original repository experiment plot. V1/V2 comparison on the same new 64-scenario simulated test; no field validation.</figcaption></figure>'''
        if slug=='aqua-sentinel' and i==4:
            sections+='''<div class="evidence-table" tabindex="0" role="region" aria-label="Scrollable simulated experiment comparison"><table><caption>Separate simulated experiments — results are not pooled</caption><thead><tr><th scope="col">Experiment</th><th scope="col">Detected events</th><th scope="col">False-alert episodes</th><th scope="col">Within 5 min</th></tr></thead><tbody><tr><th scope="row">V1 ML · new test</th><td>13 / 32</td><td>5</td><td>8 / 32</td></tr><tr><th scope="row">V2 ML · same new test</th><td>31 / 32</td><td>10</td><td>15 / 32</td></tr><tr><th scope="row">Bilans_13 · later test</th><td>32 / 32</td><td>0</td><td>32 / 32</td></tr></tbody></table></div>'''
        if slug=='retail-lakehouse' and i==1:
            sections+='''<figure class="artifact"><img src="/assets/retail-orders.jpg" width="1924" height="1009" loading="lazy" alt="Actual Power BI orders report from the retail lakehouse repository, using filtered synthetic data"><figcaption>Actual repository Power BI screenshot. Filtered synthetic retail data; displayed totals depend on report selections.</figcaption></figure><figure class="artifact"><img src="/assets/retail-cashflow.jpg" width="1924" height="1016" loading="lazy" alt="Actual Power BI cash-flow report with collections and refunds from synthetic retail data"><figcaption>Cash flow is modeled separately from order value. Original report screenshot, not client financial data.</figcaption></figure>'''
    results='<div class="result-grid">'+''.join(f'<div><strong>{e(v)}</strong><span>{e(label)}</span><p>{e(scope)}</p></div>' for v,label,scope in p['results'])+'</div>' if p['results'] else ''
    limitations='<ul class="limit-list">'+''.join(f'<li>{e(x)}</li>' for x in p['limitations'])+'</ul>'
    if p['private']:
        sources='<p>This study is based on authorized private-source inspection. Private source, unpublished interface assets and internal validation documents are not included in the website. No public repository link is implied.</p><p class="micro">Authorized source review covers private-preview work and later local curation and geographic-release development. Historical acceptance evidence is distinct from the portfolio’s browser checks.</p>'
    else:
        sources=f'<p>Source inspection at commit <code>{p["sha"][:7]}</code>. Linked reports describe their original runs; they are not new portfolio test executions.</p><a class="button dark" href="https://github.com/ilyass74/{slug}">Open repository <span>GITHUB</span></a><details class="source-details"><summary>Inspect implementation references ({len(p["sources"])})</summary><ul>'+''.join(f'<li>{a(s["url"],s["path"])}</li>' for s in p['sources'])+'</ul></details>'
        if slug=='nyc-taxi-data-engineering': sources+='<p>'+a('https://github.com/ilyass74/nyc-taxi-data-engineering/tree/feat/apache-iceberg','Inspect the separate Iceberg branch')+'</p>'
    others=[x for x in PROJECTS if x['slug']!=slug and x['flagship']][:2]
    related=''.join(f'<a href="/projects/{x["slug"]}/"><span class="eyebrow">{e(x["category"])}</span><h3>{e(x["title"])}</h3><p>{e(x["dek"])}</p></a>' for x in others)
    return hero+art+(venture_brief() if slug=='ansuf' else '')+f'''<div class="case-layout wrap"><aside class="contents" data-contents><p class="eyebrow">IN THIS STUDY</p><nav aria-label="Study contents">{nav}</nav></aside><article class="case-story"><section class="story-section" id="problem"><p class="eyebrow">THE ENGINEERING QUESTION</p><h2>{e(p['dek'])}</h2><p>{e(p['problem'])}</p>{results}</section><section class="story-section" id="architecture"><p class="eyebrow">FOLLOW THE DATA</p><h2>System architecture</h2>{architecture(p)}</section>{sections}<section class="story-section scope-section" id="limits"><p class="eyebrow">WHAT THIS WORK ESTABLISHES</p><h2>Scope & limitations</h2>{limitations}</section><section class="story-section" id="sources"><p class="eyebrow">TRACE THE CLAIMS</p><h2>Evidence & source</h2>{sources}</section></article></div><section class="related wrap"><p class="eyebrow">CONTINUE EXPLORING</p><div>{related}</div></section>'''+contact()

def experience():
    return '''<section class="page-intro wrap"><p class="eyebrow">PROFESSIONAL EXPERIENCE</p><h1>From business needs<br>to <em>working systems.</em></h1><p class="intro-dek">ERP integration, data migration and client-facing collaboration.<br>Real implementation work with a technical team.</p></section><section class="experience-body wrap"><aside><p class="eyebrow">B TEL BUREAUTIQUE</p><h2>ERP / Odoo</h2><p>Initial internship<br>Ongoing freelance collaboration</p><p class="micro">Professional experience<br>Separate from independent projects</p></aside><div><h2>Understanding the workflow<br><em>before configuring the tool.</em></h2><p>I collaborate with B Tel Bureautique following an initial internship. My work brings me into contact with technical teams, suppliers, restaurants, riads and business owners to understand their requirements and help translate them into technical solutions.</p><div class="experience-task"><h3>ERP integration & configuration</h3><p>Contribute to Odoo integration and configuration in collaboration with technical teams, adapting the system to the business processes discussed with clients.</p></div><div class="experience-task"><h3>Data migration & validation</h3><p>Work on moving and checking data, cleaning source information and validating consistency so the configured system starts from usable records.</p></div><div class="experience-task"><h3>On-site collaboration</h3><p>Visit clients in Casablanca and Marrakech for integration work, discuss business requirements and coordinate practical implementation with the people using the system.</p></div><div class="experience-task"><h3>Engineering with people</h3><p>Learn to connect a technical decision with its operational consequences: how a team works, which information it trusts and what it needs to verify.</p></div><div class="experience-note"><p class="eyebrow">RELATED INDEPENDENT WORK</p><h3>Money Trail</h3><p>My independent financial reconciliation project explores source provenance, invoice balances, dbt controls and documented human review. It is not presented as a B Tel client deliverable.</p><a class="study-link" href="/projects/money-trail/">Read the engineering study</a></div></div></section>'''+contact()

def about():
    return '''<section class="page-intro wrap"><p class="eyebrow">ABOUT / ILYASS CHAKIR</p><h1>Curious about the problem.<br><em>Accountable for the system.</em></h1></section><section class="about-grid wrap"><div class="about-statement"><p>I’m a fifth-year engineering student at EMSI, specializing in Data Engineering & Artificial Intelligence.</p><p>I’m interested in real-world problems and the complete systems needed to solve them: how data arrives, how it changes, how we decide whether it is reliable, and how someone can use the result.</p><p>My independent work includes ANSUF, an entrepreneurial tourism project with the ambition to support informed discovery of Morocco, alongside streaming platforms, financial controls and hydraulic simulation. Alongside it, I collaborate professionally on ERP integration and data migration with B Tel Bureautique.</p><p>I’m seeking a PFE internship from February 2027, where I can contribute to engineering work and learn from the people responsible for running it.</p></div><aside class="about-facts"><dl><dt>EDUCATION</dt><dd>EMSI<br>Fifth-year engineering student</dd><dt>SPECIALIZATION</dt><dd>Data Engineering & AI</dd><dt>BASED IN</dt><dd>Marrakech, Morocco</dd><dt>NEXT STEP</dt><dd>PFE internship<br>From February 2027</dd></dl><a class="button dark" href="/Ilyass_Chakir_PFE_Data_IA_Horizon2027.pdf" download>Download my CV <span>PDF</span></a><p class="micro">Download my current CV in PDF format. Current project maturity is stated in the individual studies.</p></aside></section><section class="capabilities wrap"><div class="section-heading"><div><p class="eyebrow">SKILLS WITH CONTEXT</p><h2>What I work <em>with.</em></h2></div></div>'''+skill_list()+'''<div class="principles"><h3>Trace the source.</h3><h3>Test the boundary.</h3><h3>Explain the limit.</h3></div></section>'''+contact()

def page(path,title,body,description):
    config=ROOT/'.site/public.json'
    origin=json.loads(config.read_text(encoding='utf-8'))['url'].rstrip('/') if config.exists() else ''
    seo=''
    if origin and path!='/404/':
        url=origin+path
        seo=f'<link rel="canonical" href="{e(url)}"><meta property="og:type" content="website"><meta property="og:site_name" content="Ilyass Chakir — Engineering Portfolio"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(description)}"><meta property="og:url" content="{e(url)}"><meta property="og:image" content="{origin}/assets/social-cover.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(title)}"><meta name="twitter:description" content="{e(description)}"><meta name="twitter:image" content="{origin}/assets/social-cover.png">'
        if path=='/':
            person={'@context':'https://schema.org','@type':'Person','name':'Ilyass Chakir','url':origin,'jobTitle':'Engineering student — Data Engineering & AI','email':'mailto:chakirilyass16@gmail.com','sameAs':['https://github.com/ilyass74','https://ma.linkedin.com/in/ilyass-chakir-ab7201254']}
            seo+='<script type="application/ld+json">'+json.dumps(person,ensure_ascii=False).replace('<','\\u003c')+'</script>'
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="{e(description)}"><meta name="theme-color" content="#193b32"><meta name="color-scheme" content="light"><title>{e(title)}</title>{seo}<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/style.css"><script type="module" src="/interactions.js"></script></head><body>{header(path)}<main id="main">{body}</main>{footer()}</body></html>'''

def build():
    OUT.mkdir(exist_ok=True)
    for src in (ROOT/'public').rglob('*'):
        if src.is_file():
            dest=OUT/src.relative_to(ROOT/'public');dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dest)
    for name in ['style.css','interactions.js']: shutil.copy2(ROOT/'src'/name,OUT/name)
    pages=[('/', 'Ilyass Chakir — Data Engineering & AI',home()),('/projects/','Project index | Ilyass Chakir',explorer()),('/experience/','Professional experience | Ilyass Chakir',experience()),('/about/','About & contact | Ilyass Chakir',about())]
    pages += [('/projects/'+p['slug']+'/',p['title']+' — Engineering study | Ilyass Chakir',case(p)) for p in PROJECTS]
    for path,title,body in pages:
        dest=OUT/path.strip('/')/'index.html';dest.parent.mkdir(parents=True,exist_ok=True)
        desc=next((p['dek'] for p in PROJECTS if path=='/projects/'+p['slug']+'/'),'Independent engineering work in data systems, applied AI and geospatial products. PFE internship from February 2027.')
        dest.write_text(page(path,title,body,desc),encoding='utf-8')
    (OUT/'404.html').write_text(page('/404/','Page not found | Ilyass Chakir','<section class="page-intro wrap"><p class="eyebrow">PAGE NOT FOUND</p><h1>Outside the <em>index.</em></h1><p><a class="button dark" href="/projects/">Explore the projects</a></p></section>','Page not found.'),encoding='utf-8')
    config=ROOT/'.site/public.json'
    if config.exists():
        origin=json.loads(config.read_text(encoding='utf-8'))['url'].rstrip('/')
        (OUT/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+origin+'/sitemap.xml\n',encoding='utf-8')
        (OUT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+e(origin+path)+'</loc></url>' for path,_,_ in pages)+'</urlset>',encoding='utf-8')
    (OUT/'_headers').write_text('/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  Permissions-Policy: camera=(), microphone=(), geolocation=()\n',encoding='utf-8')
    manifest={str(x.relative_to(OUT)).replace('\\','/'):dict(bytes=x.stat().st_size,sha256=hashlib.sha256(x.read_bytes()).hexdigest()) for x in OUT.rglob('*') if x.is_file() and x.name!='build-manifest.json'}
    (OUT/'build-manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    print(f'Built {len(pages)} complete static pages + 404. {sum(x["bytes"] for x in manifest.values()):,} bytes. Publishable directory: docs/ only.')

if __name__=='__main__': build()

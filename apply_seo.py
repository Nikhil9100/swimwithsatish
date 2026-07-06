import json
from bs4 import BeautifulSoup

def update_seo():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # 1. Update Title and Meta Tags
    title_tag = soup.find('title')
    if title_tag:
        title_tag.string = "Swimming Coach in Varanasi & Online Sessions | Satish Kumar"

    desc_meta = soup.find('meta', attrs={'name': 'description'})
    if desc_meta:
        desc_meta['content'] = "Join Satish Kumar, NSNIS certified swimming coach in Varanasi. Offering local swim classes (Goldfish to Shark) and 1-on-1 online swimming coach sessions worldwide."

    og_title = soup.find('meta', attrs={'property': 'og:title'})
    if og_title:
        og_title['content'] = "Swimming Coach in Varanasi & Online Sessions | Satish Kumar"

    og_desc = soup.find('meta', attrs={'property': 'og:description'})
    if og_desc:
        og_desc['content'] = "Join Satish Kumar, NSNIS certified swimming coach in Varanasi. Offering local swim classes (Goldfish to Shark) and 1-on-1 online swimming coach sessions worldwide."

    twitter_title = soup.find('meta', attrs={'property': 'twitter:title'})
    if twitter_title:
        twitter_title['content'] = "Swimming Coach in Varanasi & Online Sessions | Satish Kumar"
        
    twitter_desc = soup.find('meta', attrs={'property': 'twitter:description'})
    if twitter_desc:
        twitter_desc['content'] = "Join Satish Kumar, NSNIS certified swimming coach in Varanasi. Offering local swim classes (Goldfish to Shark) and 1-on-1 online swimming coach sessions worldwide."

    # 2. Semantic HTML & Headings
    h1 = soup.find('h1', class_='hero-h1')
    if h1:
        # Rebuild H1 to keep span structure
        h1.clear()
        h1.append("Transform Your ")
        span = soup.new_tag('span', attrs={'class': 'accent'})
        span.string = "Swimming"
        h1.append(span)
        h1.append(" Journey with the Best Swimming Coach in Varanasi")
        
    # Update H2 in Online section if it exists, or just ensure Online section has a proper H2
    online_section = soup.find('section', id='online')
    if online_section:
        h2 = online_section.find('h2', class_='section-title')
        if h2:
            h2.clear()
            em = soup.new_tag('em')
            em.string = "Online Session"
            h2.append(em)
            h2.append(" Swimming Coach")

    # 3. Image Alt tag optimization
    for img in soup.find_all('img'):
        alt = img.get('alt', '').lower()
        if 'satish kumar' in alt or 'coach' in alt:
            img['alt'] = "Satish Kumar - Best Swimming Coach in Varanasi teaching techniques"
        elif 'logo' in alt:
            img['alt'] = "SwimWithSatish Logo - Swimming Academy in Varanasi & Online Coaching"
        elif 'swimmer' in alt or 'fish' in alt or 'mermaid' in alt or 'shark' in alt:
            # Append local intent to existing alt
            if 'varanasi' not in alt:
                img['alt'] = img.get('alt', '') + " - Swimming classes in Varanasi"

    # 4. JSON-LD Schema
    schema_script = soup.find('script', type='application/ld+json')
    if schema_script and schema_script.string:
        try:
            data = json.loads(schema_script.string)
            # Add service schema explicitly for online coaching
            data['description'] = "Premium swimming coaching programs in Varanasi and 1-on-1 Online Swimming Coach sessions worldwide, coached by NSNIS certified Satish Kumar."
            schema_script.string = json.dumps(data, indent=2, ensure_ascii=False)
        except Exception as e:
            print("Error parsing JSON-LD:", e)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
if __name__ == '__main__':
    update_seo()

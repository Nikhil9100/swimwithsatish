import re
import os
import json
from PIL import Image
from bs4 import BeautifulSoup

def convert_to_webp(filepath):
    if not os.path.exists(filepath):
        return None
    if filepath.endswith('.webp'):
        return filepath
    webp_path = filepath.rsplit('.', 1)[0] + '.webp'
    try:
        with Image.open(filepath) as img:
            img.save(webp_path, 'webp')
        return webp_path
    except Exception as e:
        print(f"Failed to convert {filepath}: {e}")
        return None

def update_seo():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # 1. Update Title and Meta Tags
    if soup.title:
        soup.title.string = "Swimming Coach in Varanasi | NSNIS Certified - Satish Kumar"
    
    desc = soup.find('meta', attrs={'name': 'description'})
    if desc:
        desc['content'] = "Join Satish Kumar, NSNIS certified swimming coach in Varanasi. Learn swimming with our Goldfish, Mermaid, and Shark tiers. Expert swim training for all ages."
    
    canonical = soup.find('link', attrs={'rel': 'canonical'})
    if canonical:
        canonical['href'] = "https://swimwithsatish.vercel.app/"
        
    for meta in soup.find_all('meta'):
        if meta.get('property', '').startswith('og:url') or meta.get('property', '').startswith('twitter:url'):
            meta['content'] = "https://swimwithsatish.vercel.app/"
        if meta.get('property') == 'og:title' or meta.get('property') == 'twitter:title':
            meta['content'] = "Swimming Coach in Varanasi | NSNIS Certified - Satish Kumar"
        if meta.get('property') == 'og:description' or meta.get('property') == 'twitter:description':
            meta['content'] = "Join Satish Kumar, NSNIS certified swimming coach in Varanasi. Learn swimming with our Goldfish, Mermaid, and Shark tiers. Expert swim training for all ages."
        if meta.get('property') == 'og:image' or meta.get('property') == 'twitter:image':
            meta['content'] = "https://swimwithsatish.vercel.app/Coach%20Photo%20Goes%20here/Gemini_Generated_Image_udqeq6udqeq6udqe%20(Edited).webp"

    # 2. Update existing JSON-LD
    scripts = soup.find_all('script', type='application/ld+json')
    for script in scripts:
        try:
            data = json.loads(script.string)
            if data.get('@type') == 'SportsActivityLocation':
                data['url'] = "https://swimwithsatish.vercel.app/"
                data['logo'] = "https://swimwithsatish.vercel.app/swimwithsatish_logo.webp"
                data['image'] = "https://swimwithsatish.vercel.app/Coach%20Photo%20Goes%20here/Gemini_Generated_Image_udqeq6udqeq6udqe%20(Edited).webp"
                data['address'] = {
                    "@type": "PostalAddress",
                    "streetAddress": "Dr. Sampurnanand Sports Complex, Vidyapeeth Rd, Sigra",
                    "addressLocality": "Varanasi",
                    "addressRegion": "UP",
                    "addressCountry": "IN"
                }
                data['geo'] = {
                    "@type": "GeoCoordinates",
                    "latitude": "25.3176",
                    "longitude": "82.9739"
                }
                data['telephone'] = "+919999999999"  # placeholder or use actual if present
                data['openingHours'] = ["Mo-Su 06:00-09:00", "Mo-Su 18:00-21:00"]
                data['sameAs'] = [
                    "https://instagram.com/swimwithsatish",
                    "https://facebook.com/swimwithsatish"
                ]
                script.string = json.dumps(data, indent=2)
        except:
            pass
            
    # 3. Add FAQ JSON-LD
    faq_json = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": "Where can I learn swimming in Varanasi?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "You can learn swimming with Coach Satish Kumar at the Dr. Sampurnanand Sports Complex in Sigra, Varanasi. We offer professional training for all skill levels."
                }
            },
            {
                "@type": "Question",
                "name": "What is the fee for swimming classes in Varanasi?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Our fees vary depending on the chosen tier (Goldfish, Mermaid, or Shark). Please contact us directly or view our courses section for detailed pricing information."
                }
            },
            {
                "@type": "Question",
                "name": "Is Satish Kumar NSNIS certified?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Yes, Coach Satish Kumar is an NSNIS Certified Swimming Coach with over 16 years of professional coaching excellence."
                }
            },
            {
                "@type": "Question",
                "name": "What age groups do you train?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "We train all age groups, from young beginners starting at age 4 to adults and competitive swimmers."
                }
            },
            {
                "@type": "Question",
                "name": "Do you offer online swimming coaching?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Yes, we offer online swimming coaching sessions covering technique analysis, dryland workouts, and mental conditioning for swimmers."
                }
            }
        ]
    }
    new_script = soup.new_tag('script', type='application/ld+json')
    new_script.string = json.dumps(faq_json, indent=2)
    soup.head.append(new_script)

    # 4. H1 change
    h1 = soup.find('h1', class_='hero-h1')
    if h1:
        # Keep internal span but change text
        h1.clear()
        h1.append("Transform Your ")
        br1 = soup.new_tag('br')
        h1.append(br1)
        span = soup.new_tag('span', attrs={'class': 'accent'})
        span.string = "Swimming"
        h1.append(span)
        br2 = soup.new_tag('br')
        h1.append(br2)
        h1.append(" Journey in Varanasi")

    # 5. Add FAQ Section before footer
    faq_html = """
    <section id="faq" style="background: var(--black); border-top: 1px solid rgba(14,165,233,0.1); padding-bottom: 80px;">
        <div style="max-width: 800px; margin: 0 auto;">
            <div style="text-align: center; margin-bottom: 3rem;">
                <span class="section-label">Questions?</span>
                <h2 class="section-title">Frequently Asked <em class="accent">Questions</em></h2>
                <div class="divider" style="margin: 1.2rem auto 2rem;"></div>
            </div>
            <div class="faq-list" style="display: flex; flex-direction: column; gap: 1rem;">
                <!-- FAQ 1 -->
                <div style="background: var(--card-bg); border: 1px solid var(--border); border-radius: 16px; padding: 1.5rem;">
                    <h3 style="color: var(--white); font-family: var(--font-display); font-size: 1.4rem; letter-spacing: 0.04em; margin-bottom: 0.5rem;">Where can I learn swimming in Varanasi?</h3>
                    <p style="color: var(--muted); font-family: var(--font-dm); font-size: 0.95rem; line-height: 1.6;">You can learn swimming with Coach Satish Kumar at the Dr. Sampurnanand Sports Complex in Sigra, Varanasi. We offer professional swim training in Varanasi for all skill levels.</p>
                </div>
                <!-- FAQ 2 -->
                <div style="background: var(--card-bg); border: 1px solid var(--border); border-radius: 16px; padding: 1.5rem;">
                    <h3 style="color: var(--white); font-family: var(--font-display); font-size: 1.4rem; letter-spacing: 0.04em; margin-bottom: 0.5rem;">What is the fee for swimming classes in Varanasi?</h3>
                    <p style="color: var(--muted); font-family: var(--font-dm); font-size: 0.95rem; line-height: 1.6;">Our fees vary depending on the chosen tier (Goldfish, Mermaid, or Shark). Please contact us directly or view our courses section for detailed pricing information on our Varanasi swimming academy.</p>
                </div>
                <!-- FAQ 3 -->
                <div style="background: var(--card-bg); border: 1px solid var(--border); border-radius: 16px; padding: 1.5rem;">
                    <h3 style="color: var(--white); font-family: var(--font-display); font-size: 1.4rem; letter-spacing: 0.04em; margin-bottom: 0.5rem;">Is Satish Kumar NSNIS certified?</h3>
                    <p style="color: var(--muted); font-family: var(--font-dm); font-size: 0.95rem; line-height: 1.6;">Yes, Coach Satish Kumar is an NSNIS Certified Swimming Coach with over 16 years of professional coaching excellence. He is recognized as one of the best swimming coaches in Varanasi.</p>
                </div>
                <!-- FAQ 4 -->
                <div style="background: var(--card-bg); border: 1px solid var(--border); border-radius: 16px; padding: 1.5rem;">
                    <h3 style="color: var(--white); font-family: var(--font-display); font-size: 1.4rem; letter-spacing: 0.04em; margin-bottom: 0.5rem;">What age groups do you train?</h3>
                    <p style="color: var(--muted); font-family: var(--font-dm); font-size: 0.95rem; line-height: 1.6;">We train all age groups, from young beginners starting at age 4 to adults and competitive swimmers. Our swim training in Varanasi caters to everyone.</p>
                </div>
                <!-- FAQ 5 -->
                <div style="background: var(--card-bg); border: 1px solid var(--border); border-radius: 16px; padding: 1.5rem;">
                    <h3 style="color: var(--white); font-family: var(--font-display); font-size: 1.4rem; letter-spacing: 0.04em; margin-bottom: 0.5rem;">Do you offer online swimming coaching?</h3>
                    <p style="color: var(--muted); font-family: var(--font-dm); font-size: 0.95rem; line-height: 1.6;">Yes, alongside our local Varanasi classes, we offer online swimming coaching sessions covering technique analysis, dryland workouts, and mental conditioning for swimmers globally.</p>
                </div>
            </div>
        </div>
    </section>
    """
    footer = soup.find('footer', id='contact')
    if footer:
        faq_soup = BeautifulSoup(faq_html, 'html.parser')
        footer.insert_before(faq_soup)

    # 6. Image Optimization
    for img in soup.find_all('img'):
        src = img.get('src')
        if src and not src.startswith('http') and not src.startswith('data:'):
            # Convert to webp
            # Keep original path to see if it exists
            # Unquote in case of %20
            import urllib.parse
            local_path = urllib.parse.unquote(src)
            # Remove leading slash if any
            if local_path.startswith('/'):
                local_path = local_path[1:]
            
            webp_path = convert_to_webp(local_path)
            if webp_path:
                img['src'] = urllib.parse.quote(webp_path)
                
            # Add alt text
            alt = img.get('alt', '')
            if not alt or 'coach' not in alt.lower():
                img['alt'] = (alt + " - Swimming coach Varanasi").strip(' -')
            
            # Add loading="lazy" if not hero image
            parent_classes = []
            p = img.parent
            while p:
                if p.name == 'section':
                    parent_classes.extend(p.get('class', []))
                    if p.get('id'):
                        parent_classes.append(p.get('id'))
                p = p.parent
            
            if 'hero' not in parent_classes and img.get('class') != ['shop-kit-img']:
                img['loading'] = 'lazy'

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == "__main__":
    update_seo()

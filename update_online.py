import json
from bs4 import BeautifulSoup
import re

def update_online_coaching():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # 1. NEW SECTION ON HOMEPAGE
    # Find the existing courses grid
    courses_grid = soup.find('div', class_='courses-grid')
    if courses_grid:
        # Create a new course card for Online Coaching
        online_card_html = """
        <div class="course-card featured" style="border-color: var(--sky); background: linear-gradient(160deg, rgba(14,165,233,0.08) 0%, rgba(13,27,62,0.6) 100%);">
            <div class="course-emoji">💻</div>
            <div class="course-level">REMOTE TRAINING</div>
            <h3 class="course-name" style="font-size: 1.6rem;">Live Online Swimming Coaching</h3>
            <div class="course-age">Available Anywhere</div>
            <p style="font-family: var(--font-dm); font-size: 0.85rem; color: var(--muted); margin-bottom: 1.5rem; line-height: 1.6;">Live 1-on-1 video coaching calls with Coach Satish Kumar, open to students anywhere — ideal for those who've moved away from Varanasi, students in other cities, or anyone wanting personalized remote coaching.</p>
            <div class="course-price">
                <span class="price-from">STARTING AT</span>
                <span class="price-num">₹[PRICE_PER_SESSION]</span>
                <span class="price-period">/ session</span>
            </div>
            <a href="#contact" class="btn btn-primary" style="width: 100%; justify-content: center; margin-top: auto;">Book a Session</a>
        </div>
        """
        online_soup = BeautifulSoup(online_card_html, 'html.parser')
        courses_grid.append(online_soup)
    
    # 2. UPDATE EXISTING FAQ ANSWER
    faq_section = soup.find('section', id='faq')
    if faq_section:
        for faq in faq_section.find_all('div', style=re.compile("background: var\(--card-bg\);")):
            h3 = faq.find('h3')
            if h3 and "Do you offer online swimming coaching?" in h3.text:
                p = faq.find('p')
                if p:
                    p.string = "Yes! We offer live 1-on-1 video coaching calls with Coach Satish Kumar. Sessions are available to students anywhere, not just Varanasi/Lucknow, and are priced per-session starting at ₹[PRICE_PER_SESSION]."
                break

    # 3. UPDATE JSON-LD SCHEMA
    # First, find the FAQ JSON-LD schema to update its answer as well to match
    scripts = soup.find_all('script', type='application/ld+json')
    for script in scripts:
        try:
            data = json.loads(script.string)
            # Check if this is the SportsActivityLocation schema
            if data.get('@type') == 'SportsActivityLocation':
                if 'hasOfferCatalog' not in data:
                    data['hasOfferCatalog'] = {
                        "@type": "OfferCatalog",
                        "name": "Swimming Coaching Programs",
                        "itemListElement": []
                    }
                # Add online coaching offer
                offers = data['hasOfferCatalog'].get('itemListElement', [])
                offers.append({
                    "@type": "Offer",
                    "itemOffered": {
                        "@type": "Service",
                        "name": "Online Swimming Coaching",
                        "description": "Live 1-on-1 video coaching calls, available to students anywhere."
                    },
                    "price": "[PRICE_PER_SESSION]",
                    "priceCurrency": "INR",
                    "availableAtOrFrom": {
                        "@type": "Place",
                        "name": "Remote / Online"
                    }
                })
                data['hasOfferCatalog']['itemListElement'] = offers
                script.string = json.dumps(data, indent=2)
            
            # Check if this is the FAQ schema
            elif data.get('@type') == 'FAQPage':
                for qa in data.get('mainEntity', []):
                    if qa.get('name') == "Do you offer online swimming coaching?":
                        qa['acceptedAnswer']['text'] = "Yes! We offer live 1-on-1 video coaching calls with Coach Satish Kumar. Sessions are available to students anywhere, not just Varanasi/Lucknow, and are priced per-session starting at ₹[PRICE_PER_SESSION]."
                script.string = json.dumps(data, indent=2)
        except Exception as e:
            pass

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == "__main__":
    update_online_coaching()

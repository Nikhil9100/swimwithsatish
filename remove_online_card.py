from bs4 import BeautifulSoup

def remove_online_card():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # Find the newly added online coaching card and remove it
    for h3 in soup.find_all('h3', class_='course-name'):
        if 'Live Online Swimming Coaching' in h3.text:
            # The card is the parent of this h3
            card = h3.find_parent('div', class_='course-card')
            if card:
                card.decompose()

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == "__main__":
    remove_online_card()

import requests
from bs4 import BeautifulSoup
from datetime import datetime

def extract_data():
    product_list = []
    base_url = "https://fashion-studio.dicoding.dev"

    for page_num in range(1, 51):
        url = base_url if page_num == 1 else f"{base_url}/page{page_num}"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"[Request Error] Page {page_num}: {e}")
            continue

        try:
            soup = BeautifulSoup(response.text, "html.parser")
            cards = soup.select(".collection-card")

            for card in cards:
                title = card.find("h3", class_="product-title")
                price = card.find("span", class_="price") or card.find("p", class_="price")

                data = {
                    "title": title.text.strip() if title else None,
                    "price": price.text.strip().replace("$", "") if price else None,
                    "rating": None,
                    "colors": None,
                    "size": None,
                    "gender": None,
                    "timestamp": datetime.now().isoformat()
                }

                for p in card.find_all("p"):
                    content = p.text.strip()
                    if "Rating" in content:
                        data["rating"] = content
                    elif "Colors" in content:
                        data["colors"] = content
                    elif "Size:" in content:
                        data["size"] = content
                    elif "Gender:" in content:
                        data["gender"] = content

                product_list.append(data)
        except Exception as e:
            print(f"[Parse Error] Page {page_num}: {e}")
            continue

    return product_list

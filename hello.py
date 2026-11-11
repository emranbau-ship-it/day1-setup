import requests

r = requests.get("https://books.toscrape.com/", timeout=10)
print("Status code:", r.status_code)
print("Page size:", len(r.text), "characters")
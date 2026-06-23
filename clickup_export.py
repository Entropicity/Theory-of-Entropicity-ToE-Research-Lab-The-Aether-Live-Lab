import os
import requests
import json

API_TOKEN = "pk_120178091_3UNRKZA9TUWZNQRY56Z4QIQTB1631TF1"
TEAM_ID = "9011914914"

HEADERS = {
    "Authorization": API_TOKEN
}

BASE_URL = "https://api.clickup.com/api/v2"

EXPORT_DIR = "clickup_docs_export"
os.makedirs(EXPORT_DIR, exist_ok=True)

def get_docs():
    url = f"{BASE_URL}/team/{TEAM_ID}/doc"
    response = requests.get(url, headers=HEADERS)
    return response.json().get("docs", [])

def download_doc(doc):
    doc_id = doc["id"]
    title = doc["name"].replace("/", "_")

    print(f"Downloading: {title}")

    # Markdown export
    md_url = f"{BASE_URL}/doc/{doc_id}/export?format=markdown"
    md_response = requests.get(md_url, headers=HEADERS)
    with open(f"{EXPORT_DIR}/{title}.md", "wb") as f:
        f.write(md_response.content)

    # HTML export
    html_url = f"{BASE_URL}/doc/{doc_id}/export?format=html"
    html_response = requests.get(html_url, headers=HEADERS)
    with open(f"{EXPORT_DIR}/{title}.html", "wb") as f:
        f.write(html_response.content)

def main():
    docs = get_docs()
    print(f"Found {len(docs)} docs.")

    for doc in docs:
        download_doc(doc)

    print("Export complete!")

if __name__ == "__main__":
    main()

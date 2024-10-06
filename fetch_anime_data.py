import requests

# Endpoint API
api_url = "https://api.jikan.moe/v4/seasons/now"

# Fetch data dari API
response = requests.get(api_url)
if response.status_code == 200:
    data = response.json()
else:
    print(f"Error: Unable to fetch data from API. Status code: {response.status_code}")
    exit()

# Ambil data anime yang diinginkan
anime_list = data.get("data", [])

# Format string untuk README.md
readme_content = "# Current Anime Season Data\n\n"
readme_content += "<style>\n.card {\n  display: inline-block;\n  width: 45%;\n  margin: 1%;\n  padding: 10px;\n  border: 1px solid #ddd;\n  border-radius: 8px;\n}\n.card img {\n  width: 100%;\n  border-radius: 8px;\n}\n.card-title {\n  text-align: center;\n  font-size: 1.2em;\n  margin-top: 10px;\n}\n</style>\n\n"
readme_content += "<div style='display: flex; flex-wrap: wrap;'>\n"

for anime in anime_list:
    # Ambil gambar dan judul anime
    image_url = anime.get("images", {}).get("webp", {}).get("large_image_url", "")
    title = anime.get("title", "N/A")

    # Tambahkan kartu untuk setiap anime
    if image_url:
        readme_content += f"<div class='card'>\n"
        readme_content += f"<img src='{image_url}' alt='{title}'>\n"
        readme_content += f"<div class='card-title'>{title}</div>\n"
        readme_content += "</div>\n"

readme_content += "</div>"

# Tulis ke README.md
with open("README.md", "w", encoding='utf-8') as file:
    file.write(readme_content)
    print("Data successfully written to README.md")

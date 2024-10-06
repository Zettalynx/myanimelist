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
readme_content = "# Current Anime Season\n\n"
readme_content += "Berikut ini adalah daftar anime yang sedang tayang pada musim ini.\n\n"

# Header tabel dengan dua kolom
readme_content += "| Anime | Anime |\n"
readme_content += "|-------|-------|\n"

# Buat daftar dalam format dua kolom
for i in range(0, len(anime_list), 2):
    # Ambil dua item anime per baris
    anime1 = anime_list[i]
    anime2 = anime_list[i + 1] if i + 1 < len(anime_list) else None

    # Ambil detail anime 1
    title1 = anime1.get("title", "N/A")
    image_url1 = anime1.get("images", {}).get("webp", {}).get("image_url", "")

    # Format kolom untuk anime 1
    col1 = f"![{title1}]({image_url1})<br>{title1}" if image_url1 else title1

    # Ambil detail anime 2 jika ada
    if anime2:
        title2 = anime2.get("title", "N/A")
        image_url2 = anime2.get("images", {}).get("webp", {}).get("image_url", "")
        col2 = f"![{title2}]({image_url2})<br>{title2}" if image_url2 else title2
    else:
        col2 = ""  # Jika tidak ada anime kedua, biarkan kolom kosong

    # Tambahkan baris dengan dua kolom
    readme_content += f"| {col1} | {col2} |\n"

# Tulis ke README.md
with open("README.md", "w", encoding='utf-8') as file:
    file.write(readme_content)
    print("Data successfully written to README.md")

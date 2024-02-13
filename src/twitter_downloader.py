import requests
import bs4

def download_video(url, output_filename) -> None:
    response = requests.get(url, stream=True)
    block_size = 1024

    with open(output_filename, "wb") as file:
        for data in response.iter_content(block_size):
            file.write(data)
        file.flush()

def download_twitter_video(url, file_name):
    api_url = f"https://twitsave.com/info?url={url}"

    response = requests.get(api_url)
    data = bs4.BeautifulSoup(response.text, "html.parser")
    download_button = data.find_all("div", class_="origin-top-right")[0]
    quality_buttons = download_button.find_all("a")
    highest_quality_url = quality_buttons[0].get("href") # Highest quality video url
    
    download_video(highest_quality_url, file_name)
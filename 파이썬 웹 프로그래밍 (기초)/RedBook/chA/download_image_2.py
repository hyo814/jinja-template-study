from pathlib import Path
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup


def parse_image(data):
    soup = BeautifulSoup(data, 'html.parser')
    imgTagList = soup.find_all('img')
    dataSet = set(x.attrs['src'] for x in imgTagList)
    return dataSet


def download_image(url, dataSet):
    downDir = Path('DOWNLOAD')
    downDir.mkdir(exist_ok=True)

    for x in sorted(dataSet):
        imageUrl = urljoin(url, x)
        basename = Path(imageUrl).name
        targetFile = downDir / basename

        print("Downloading...", imageUrl)
        res = requests.get(imageUrl)
        with open(targetFile, 'wb') as f:
            f.write(res.content)


def main():

    url = "http://www.google.co.kr"

    res = requests.get(url)
    charset = res.encoding
    data = res.content.decode(charset)

    dataSet = parse_image(data)

    print("\n>>>>>>>>> Download Images from", url)
    download_image(url, dataSet)


if __name__ == '__main__':
    main()

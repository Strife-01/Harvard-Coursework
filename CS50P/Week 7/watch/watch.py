import re


def main():
    print(parse(input("HTML: ")))


def parse(html):
    if yt_embedded_url := re.match(r'^.*(?:src=")?(?:(?:https?://)?(?:www.)?youtube.com/embed/(\w+))"?.*', html):
        return "https://youtu.be/" + yt_embedded_url.group(1)
    else:
        return None


if __name__ == "__main__":
    main()

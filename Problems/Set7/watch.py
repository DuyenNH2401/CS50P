import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if re.search(r"<iframe(.+)><\/iframe>", s):
        pattern = r"src=\"(http[s]?://)(www\.)?(youtube\.com)*(/embed)*(\S+)\""
        match = re.search(pattern, s)
        if match:
            mid_url = str(match.group(3))
            end_url = str(match.group(5))
            if "youtube.com" not in mid_url:
                return
            mid_url = mid_url.replace("youtube.com", "youtu.be")
            url = 'https://'+mid_url+end_url
            return url
        else:
            return
    return

if __name__ == "__main__":
    main()
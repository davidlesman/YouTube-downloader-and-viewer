from pytube import YouTube


def download(link: str):
    yt = YouTube(link)
    yd = yt.streams.get_highest_resolution()

    if yd.resolution != "1080p":
        yd = yt.streams.get_by_resolution("1080p")

        if yd is None:
            yd = yt.streams.get_by_resolution("720p")

    yd.download("./static/vids")

    return yt, yd


if __name__ == "__main__":
    yt, _ = download(input("link: "))
    print(f"Title: {yt.title}")
    print(f"Views: {yt.views}")

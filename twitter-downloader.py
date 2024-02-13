import src.twitter_downloader as tvdl
import argparse
import re

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Download a video from a URL into a file"
    )

    parser.add_argument(
        "twitter_url",
        type=str,
        help="The video URL to download"
    )

    parser.add_argument(
        "file_name",
        type=str,
        help="The file name or path to save the video to"
    )

    args = parser.parse_args()

    file_name = args.file_name if args.file_name.endswith(".mp4") else args.file_name + ".mp4"

    tvdl.download_twitter_video(args.twitter_url, file_name)
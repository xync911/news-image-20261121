"""Entry for make.fun news-image-20261121.

Writes the front-page image summing up Saturday 21 November 2026's
world news to /output/entry.png. The image is held in this repository
as news.png (1024x1024, under 1 MiB); this program only copies it, so
both runs write exactly the same bytes and no network is used.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
# Deterministic by design: a plain file copy, same bytes on every run.

def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "news.png"), "/output/entry.png")

if __name__ == "__main__":
    main()

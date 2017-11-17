# evernote-url2clip
Clip webpages to Evernote from a text file. Using this file I automatically clipped hundreds of webpages from Chrome and Pocket. The only thing I couldn't automate is enabling shortcuts for Web Clipper extension (see #demo).

## Demo
![](img/demo.gif)

## How to install

Install dependencies
```bash
pip install -r requirements.txt
```
Download driver for Chrome [here](https://sites.google.com/a/chromium.org/chromedriver/downloads)
and make sure its location is added to PATH (or copy to `/usr/bin/` or `/usr/local/bin/`)

Next download Evernote Clip extension by typing its ID (go `chrome://extensions/`, check Developer mode, and find out ID)
https://chrome-extension-downloader.com and put in current directory.

## How to migrate from Chrome (bookmarks)
Simply select and copy-paste links from Chrome bookmark manager to a text file.

## How to migrate from Pocket
Go to
```
Settings > Export > Export to HTML file
```
download HTML file (`fil_export.html` by default) and run (install `lynx`)
```bash
lynx -dump fil_export.html | awk '/http/{print $2}' > links.txt
```
to create desired text file.

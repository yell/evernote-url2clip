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

## How to migrate from Pocket
Go to
```
Settings > Export > Export to HTML file
```
download `fil_export.html` after that run (install `lynx`)
```bash
lynx -dump fil_export.html | awk '/http/{print $2}' > links.txt
```
to create desired text file.

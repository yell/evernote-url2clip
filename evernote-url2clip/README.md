# evernote-url2clip
Clip webpages to Evernote from a text file. Using this program I successfully clipped hundreds of webpages from Chrome and Pocket automatically. The only thing I couldn't automate is enabling shortcuts for Web Clipper extension (see [demo](#demo)). Tested on Ubuntu 16.04 and Chrome. With minimal changes this should also work on Windows.

## Demo
![](img/demo.gif)

## How to install
### Linux (tested on Ubuntu 16.04, Python 2.7.12)
* Download source
```bash
git clone https://github.com/monsta-hd/scripts
cd scripts/evernote-url2clip/
```
* Install dependencies
```bash
pip install -r requirements.txt
```
* Download driver for Chrome [here](https://sites.google.com/a/chromium.org/chromedriver/downloads)
and make sure its location is added to PATH (or copy to `/usr/bin/` or `/usr/local/bin/`)

* I tested program using extension (`.crx`) provided in the current directory. Also you can download newer one from https://chrome-extension-downloader.com by typing its ID (go `chrome://extensions/`, check Developer mode, and find out ID) and put in the root directory of this project.

### Windows (tested on Windows 8.1, Anaconda 4.4.11)
* Download source (e.g. as zip and unzip somewhere)
* Download and install [Anaconda](https://www.anaconda.com/download/#windows)
* Version can be checked from Anaconda prompt:
```bash
conda -V
# conda 4.4.11
```
* Run Anaconda prompt and explicitly install requirements (note that tildes such as `selenium~=3.9.0` does not work with `conda install`):
```bash
conda install selenium=3.9.0
conda install tqdm=4.14.0
```
* Download [chrome driver](https://sites.google.com/a/chromium.org/chromedriver/downloads) and unzip it to `X:/Windows/System32`
* Run script in conda prompt by navigating to root folder of the project and use directions from the next section

## How to run
* Fill `config.yml` file with evernote credentials.
* Run program:
```bash
usage: evernote_url2clip.py [-h] [--clip-type TYPE] [--clip-timeout SEC]
                            FILEPATH

positional arguments:
  FILEPATH            file path with urls

optional arguments:
  -h, --help          show this help message and exit
  --clip-type TYPE    how to clip content: 'A' - article, 'B' - bookmark, 'C'
                      - simplified article, 'E' - email, 'F' - full page, 'M'
                      - screenshot, 'P' - pdf, ... [see extension for more]
                      (default: A)
  --clip-timeout SEC  default timeout (in seconds) to clip pages (default:
                      120)
```

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

# Simple Beautiful Soup Program to scrape the current NPR All Things Considered Stories

## Why?

https://twitter.com/MissingPlaylist

### Setup

#### One time Setup
1. clone this repo
1. `cd VerySimplePlaylistSorta`
1. `python3 -m venv le-env`
1. `source le-env/bin/activate`
1. `pip install -r requirements.txt`

#### Daily Use
1. `python 1.py > atc.sh # get rid of the stuff you don't want to hear`
1. `vim atc.sh`
1. `mkdir out; cd out; . ../atc.sh`
1. `mp3wrap ../big.mp3 *.mp3`
1. `cd ..; rm -rf out`
1. Put big.mp3 in a webserver and enjoy your playlist


#Gisty

*Gisty* is a clone of [sheet](https://github.com/oscardelben/sheet) made in pure python

A small command line that lets you create small gists with text for things to remember

Personally, I use it to save commands I use a lot but can't remember

## Usage

```
gisty			# Lists all your gistys
gisty new git	# Creates a new gisty called git
gisty edit git	# Edits (or creates) a gisty called git
gisty git		# Prints out your git gisty
```
## Installation
In order to install this you can just create a symlink to the gisty script

```sudo ln -s `pwd`/gisty /usr/bin/gisty```

## Notes
- Each gisty is actually a file saved at `~/.config/gisty/`

- For editing the files, right now it executes vim

- I've only tested *Gisty* on OSX Lion with python 2.7

## TODO
- Upload gists to gist.github.com
- Change editor to something more portable or to using $editor

#Gisty

*Gisty* is a clone of [sheet](https://github.com/oscardelben/sheet) made in pure python

A small command line that lets you create small gists with text for things to remember

Personally, I used it to save commands I use a lot but can't remember

Examples:

```
gisty list		# Lists all your gistys
gisty git		# Prints out your git gisty
gisty new git	# Creates a new gisty called git
gisty edit git	# Edits (or creates) a gisty called git
```

- Each gisty is actually a file saved at `~/.config/gisty/`

- For editing the files, right now it executes vim. I need to fix this to something more portable (or maybe to execute the $editor)

- I've only tested Gisty on OSX

## Installation
In order to install this you can just create a symlink to the gisty script

```sudo ln -s `pwd`/gisty /usr/bin/gisty```
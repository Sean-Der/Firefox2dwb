Firefox2dwb
===========

Python Script to convert Firefox bookmarks to dwb's format

Make sure to install BeautifulSoup4 first. You may need to change
the import name in line 1. ex(bs4 => BeautifulSoup)

In Firefox export all your bookmarks as HTML, then move that HTML 
into the same directory as this script

This scripts prints to stdin so you will probably want to do 

pythonn firefox2dwb.py >> ~/.config/dwb/default/bookmarks

This will append your exported Firefox bookmarks to your current
dwb bookmarks

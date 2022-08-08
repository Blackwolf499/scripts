#!/bin/bash
web_url=$1
wordlist="/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt" 
gobuster dir -u $web_url -w $wordlist -t 60 -x html,php -t 60 


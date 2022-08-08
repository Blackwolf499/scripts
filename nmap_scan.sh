#!/bin/bash
# This is a nmap scan shortcut
ip_addr=$1
nmap -sT -sV -sC -A -oN nmapscan $ip_addr

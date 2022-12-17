#!/bin/sh

gnome-terminal --tab -t "Synthesis log" -- lnav -c ':goto 100%' $1
gnome-terminal --tab -t "Synthesis warnings" -- lnav -c ':filter-in WARNING' $1

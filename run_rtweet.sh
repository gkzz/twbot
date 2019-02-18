#!/bin/bash

cd $HOME/twbot
source 36/bin/activate
python3.6 rtweet.py

#write on crontab bellow
#35 */1 * * * cd $HOME/twbot;$HOME/twbot/36/bin/python3.6 rtweet.py

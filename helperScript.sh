#!/bin/bash

### Do not do the following it will not work ###
#source activate AVirtualEnvironment 
#python mypythonscript.py
#source deactivate AVirtual Environment

#requsts-html install
## adv requests-html tut https://www.youtube.com/watch?v=a6fIbtFB46g&t=726s

## pip3 install requests-html
## workaround to get requests working on my system:
##sudo apt-get install  gconf-service libasound2 libatk1.0-0 libatk-bridge2.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils wget

##multi threading made easy
#https://www.youtube.com/watch?v=vJwcW2gCCE4

### Do this instead ###
/home/csadmin/code/python/currencyServer/venv/bin/python /home/csadmin/code/python/currencyServer/app.py

##Crontab is: 45 9 * * 1-5 /home/csadmin/code/python/currencyServer/helperScript.sh
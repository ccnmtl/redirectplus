MANAGE=./manage.py
APP=redirectplus
JS_FILES=media
MAX_COMPLEXITY=6

all: jenkins

include *.mk

makemessages: ./ve/bin/python
	$(MANAGE) makemessages -l es --ignore="ve" --ignore="login.html" --ignore="password*.html"

compilemessages: ./ve/bin/python
	$(MANAGE) compilemessages

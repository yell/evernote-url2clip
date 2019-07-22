install:
	cp evernote_url2clip.py evernote-url2clip
	chmod a+x evernote-url2clip
	sudo mv evernote-url2clip /usr/local/bin/

.PHONY: install

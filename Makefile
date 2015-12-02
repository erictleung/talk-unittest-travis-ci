FILE=unittest-travis

all: unittest-travis.pdf

clean:
	rm unittest-travis.pdf

.PHONY: all clean

%.pdf: %.md
	pandoc -t beamer -s $< -o $@

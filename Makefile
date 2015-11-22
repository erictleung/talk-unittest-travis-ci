FILE=unittest-travis

edit : $(FILE).md
	pandoc -t beamer -s $(FILE).md -o $(FILE).pdf

beamer : $(FILE).md
	pandoc -t beamer -s $(FILE).md -o $(FILE).pdf

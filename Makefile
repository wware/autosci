view: bar.pdf
	evince bar.pdf

foo.n3: foo.tex
	./tangle.py rdf foo.tex > foo.n3

bar.tex: foo.tex
	./weave.py foo.tex > bar.tex

bar.pdf: bar.tex
	pdflatex bar.tex
	pdflatex bar.tex
	pdflatex bar.tex

README.md: foo.md
	./weave.py foo.md > README.md

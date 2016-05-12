view: bar.pdf
	evince bar.pdf

foo.tex: foo.md
	./md2latex.py < foo.md > foo.tex

foo.n3: foo.tex
	./tangle.py rdf foo.tex > foo.n3

bar.tex: foo.tex
	./weave.py foo.tex > bar.tex

bar.pdf: bar.tex
	pdflatex bar.tex
	pdflatex bar.tex
	pdflatex bar.tex

README.md: foo.md
	echo "Semantic markup of LaTeX and Markdown documents" > README.md
	./weave.py foo.md | tail --lines=+2 >> README.md

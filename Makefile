.SUFFIXES: .md .tex .n3 .pdf ;

TITLE = Embedding semantic markup in LaTeX and Markdown documents

.tex.pdf:
	pdflatex $(@:.pdf=.tex)
	pdflatex $(@:.pdf=.tex)
	pdflatex $(@:.pdf=.tex)

.tex.n3:
	./tangle.py rdf $(@:.n3=.tex) > $@

.md.n3:
	./tangle.py rdf $(@:.n3=.md) > $@

all: README.md bar.pdf foo.n3

clean:
	rm -f README.md bar.pdf foo.n3 foo.tex bar.tex

view: bar.pdf
	evince bar.pdf

foo.tex: foo.md
	./md2latex.py -t "$(TITLE)" < foo.md > foo.tex

foo.n3: foo.tex

bar.tex: foo.tex
	./weave.py foo.tex > bar.tex

bar.pdf: bar.tex

README.md: foo.md
	echo "$(TITLE)" > README.md
	./weave.py foo.md | tail --lines=+2 >> README.md

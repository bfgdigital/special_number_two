# Simple build for special_number_two paper

.PHONY: all tables pdf clean

TEX= special_number_two.tex
OUT_PDF= special_number_two.pdf

all: pdf

tables:
	python3 -m special_number_two.python.generate_tables 256

pdf: tables
	pdflatex -halt-on-error $(TEX)
	pdflatex -halt-on-error $(TEX)

clean:
	rm -f *.aux *.log *.out *.toc *.synctex.gz *.lof *.lot


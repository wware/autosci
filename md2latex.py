#!/usr/bin/env python

import logging
import re
import sys

logging.getLogger().setLevel(logging.DEBUG)

R = sys.stdin.read()

# Sections and subsections
R = re.sub(r"([^\n]+)\n===+", r'\\section{\1}', R)
R = re.sub(r"([^\n]+)\n---+", r'\\subsection{\1}', R)

# Italics, except anything inside semantic blocks
Rnew = ""
r = re.compile(r"<<[^>]+>> =")
r2 = re.compile(r"\n@\n")
while True:
    s = r.search(R)
    if s is None:
        R = re.sub(r"\"([^\"]+)\"", r'\\textit{\1}', R)
        break
    m, n = s.start(), s.end()
    S, T, R = R[:m], R[m:n], R[n:]
    logging.debug(T)
    Rnew += re.sub(r"\"([^\"]+)\"", r'\\textit{\1}', S) + T
    s = r2.search(R)
    assert s is not None, 'Semantic block does not end correctly.'
    logging.debug(R[s.end()-8:s.end()])
    Rnew += R[:s.end()]
    R = R[s.end():]
R = Rnew + R

# Quotation blocks
Rnew = ""
r = re.compile(r"\n\n> ([^\n]+(\n> [^\n]+)*\n)\n")
while True:
    s = r.search(R)
    if s is None:
        break
    m, n = s.start(), s.end()
    Rnew += R[:m]
    Rnew += '\n\n\\begin{quotation}\n'
    # quotetext = ''.join(R[m:n].split('> '))
    quotetext = s.group(1).replace('> ', '')
    Rnew += quotetext
    Rnew += '\\end{quotation}\n\n'
    R = R[n:]
R = Rnew + R

# Handle unordered lists
Rnew = ""
r = re.compile(r"\n\n\* ([^\n]+)\n")
r2 = re.compile(r"^\* ([^\n]+)\n")
while True:
    s = r.search(R)
    if s is None:
        break
    m, n = s.start(), s.end()
    Rnew, R = Rnew + R[:m], R[n:]
    Rnew += '\n\n\\begin{itemize}\n\\item{' + s.group(1) + '}\n'
    while True:
        s = r2.match(R)
        if s is None:
            break
        m, n = s.start(), s.end()
        Rnew, R = Rnew + R[:m], R[n:]
        Rnew += '\\item{' + s.group(1) + '}\n'
    Rnew += '\\end{itemize}\n'
R = Rnew + R

# Links are tricky because parentheses may be nested.
Rnew = ""
r = re.compile(r"\[([^\]]+)\]\(")
while True:
    s = r.search(R)
    if s is None:
        break
    m, n = s.start(), s.end()
    linkname = s.group(1)
    parenlevel = 1
    linktarget = ""
    Rnew += R[:m]
    R = R[n:]
    while parenlevel > 0:
        c, R = R[:1], R[1:]
        linktarget += c
        if c == "(":
            parenlevel += 1
        elif c == ")":
            parenlevel -= 1
    linktarget = linktarget[:-1]
    Rnew += '\\href{' + linktarget + '}{'
    Rnew += linkname
    Rnew += '}'
R = Rnew + R

print """\\documentclass{article}
\\usepackage[colorlinks=true,urlcolor=blue,linkcolor=blue]{hyperref}
\\title{Semantic markup of \\LaTeX and Markdown documents}
\\author{Will Ware}
\\date{24 February 2016}
\\begin{document}
\\maketitle
"""
print R.rstrip()
print '\n\n\\end{document}'

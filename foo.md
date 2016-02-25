Semantic markup of LaTeX and Markdown documents
====

Overview
----

My goal here is to figure out what I call a "machine-tractable" scientific literature:
a nice clean way to embed machine-processable semantic information in the source of LaTeX
and Markdown documents, such software pre-processors can extract the information in
machine-tractable form and can also generate (ideally publication-ready) HTML or PDF output.

This idea is part of a larger
[group of ideas](http://willware.blogspot.com/2013/10/bar-camp-boston-2013-talk-on-automation.html)
that I have been thinking about since around 2010.

> ...to formulate a linked language of science that machines can understand. Publish
> papers in formats like RDF/Turtle or JSON or JSON-LD or YAML. Link scientific
> literature to existing semantic networks (DBpedia, Freebase, Google Knowledge Graph,
> LinkedData.org, Schema.org etc). Create schemas for scientific domains and for the
> scientific method (hypotheses, predictions, experiments, data). Provide tutorials,
> tools and incentives to encourage researchers to publish machine-tractable papers.
> Create a distributed graph or database of these papers, in the role of scientific
> journals, accessible to people and machines everywhere. Maybe use Stackoverflow as
> a model for peer review.

My immediate concern is with the task of comfortably embedding such formats in LaTeX or
Markdown source. I say "comfortably" because I hope for eventual wide adoption by the
authors of scientific literature, and that is unlikely if semantic markup presents any
significant additional burden to publication. Consequently the syntax for such markup must
be simple and its meaning obvious.

In particular it should not be necessary to specify the same idea twice, once in English
and again in machine-tractable form. As with mathematical equations, the machine-tractable
representation should be readable and expressive to the human audience as well as the
machine.

Machine representations
----

There have been huge advances in machine learning in recent years, fueled by large
investments from Google, Facebook, and other organizations. I have not kept up with
this work as well as I would like, and no doubt my ideas in this area will seem
antiquated to those who have.

I have tried not to commit this approach to any particular representation, but I've
tended to use [RDF/Turtle](https://www.w3.org/TR/turtle/) because first-order logic
doesn't sound like a bad place to start for machine reasoning about science. The notion
of specifying information or knowledge as a semantic network seems to me a useful one.

Notation
----

These considerations led me to adopt a
[literate programming](https://en.wikipedia.org/wiki/Literate_programming) approach,
borrowing notationally from Norman Ramsey's [noweb](http://www.cs.tufts.edu/~nr/noweb/).
I am [not the first](https://github.com/JonathanAquino/noweb.py) to rewrite noweb in
Python.

In literate programming, one writes a program in small pieces, discussing each in turn.
Likewise, a semantic network can be specified in pieces, with discussion. Here the first
line gives a name to this piece so that it can be referenced elsewhere. The remaining
lines are in the RDF/Turtle language. They tell us that, in the world of Marvel comics
superheros, Spiderman is a person named "Spiderman" who has an enemy (the Green Goblin,
to be discussed shortly).

<<semantic info about spiderman>> =
<#spiderman>
    a foaf:Person ;
    foaf:name "Spiderman" ;
    rel:enemyOf <#green-goblin> .
@

Terms like "foaf:Person" refer to [FOAF](http://xmlns.com/foaf/spec/), or "friend of a
friend", a library of semantic relationships between people. Another similar library is
[Relationship](http://vocab.org/relationship/), which include the "rel:enemyOf" term.

The components of a semantic network are triplets. Blah blah blah triplets....
semicolons... commans... period.

The Green Goblin is another character in the Marvel comics universe, not so different
from Spiderman in some ways.

<<semantic info about the green goblin>> =
<#green-goblin>
    a foaf:Person ;
    foaf:name "Green Goblin" ;
    rel:enemyOf <#spiderman> .
@

Finally we have a wrapper for the two pieces of semantic network above. Here we
provide referents for the prefixes "foaf" and "rel", and other prefixes that are
commonly used in RDF.

<<rdf>> =
@base <http://example.org/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix rel: <http://vocab.org/relationship/> .
<<semantic info about spiderman>>
<<semantic info about the green goblin>>
@

Still left to do
----

Whip up some little machine-tractable notation for reasoning about hypotheses, predictions,
the design and execution of experiments, and the interpretation of their results. It is not
necessary that a machine should be able to do all these things, but it should be able to
"understand" them, to the extent a formal semantic network represents understanding.

It would be a big plus if a RDF reasoner could perform some interesting piece of inference
in this domain. Obviously Ross King was able to accomplish that.

http://www.ncbi.nlm.nih.gov/pmc/articles/PMC1978088/

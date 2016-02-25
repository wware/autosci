Semantic markup of LaTeX and Markdown documents
====

Preliminaries
----

My goal here is to figure out a nice clean way to embed RDF information in the source
of LaTeX and Markdown documents, such that a pre-processor can either extract the RDF
in a suitable format (e.g. Turtle) or do any cleanup that the document source needs
before being processed to HTML or PDF.

This idea is part of a larger
[group of ideas](http://willware.blogspot.com/2013/10/bar-camp-boston-2013-talk-on-automation.html)
that I have been thinking about since around 2010. In the blog post linked above, I
laid out the following agenda:

> to formulate a linked language of science that machines can understand. Publish
> papers in formats like RDF/Turtle or JSON or JSON-LD or YAML. Link scientific
> literature to existing semantic networks (DBpedia, Freebase, Google Knowledge Graph,
> LinkedData.org, Schema.org etc). Create schemas for scientific domains and for the
> scientific method (hypotheses, predictions, experiments, data). Provide tutorials,
> tools and incentives to encourage researchers to publish machine-tractable papers.
> Create a distributed graph or database of these papers, in the role of scientific
> journals, accessible to people and machines everywhere. Maybe use Stackoverflow as
> a model for peer review.

This is an attempt not to publish papers in RDF serialization formats, but to embed
those formats gracefully in better-known and more useful contexts like LaTex source
or Markdown source. Ideally the final result would be a pre-processor that could
accommodate these and any future formats that might arise in the future.

It would be good not to ask the paper's author to write his reasoning twice,
in \LaTeX and in RDF, where preferably, ideas would be expressed just once,
in some format that is easily translatable to RDF and to LaTeX or Markdown source.

<a name="rdf"></a>
```
<<rdf>> =
@base <http://example.org/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix rel: <http://www.perceive.net/schemas/relationship/> .
<<rdf-green-goblin>>
<<rdf-spiderman>>
```
*Refers to: [rdf-green-goblin](#rdf-green-goblin), [rdf-spiderman](#rdf-spiderman)*

Let's give some information about the Green Goblin

<a name="rdf-green-goblin"></a>
```
<<rdf-green-goblin>> =
<#green-goblin>
    rel:enemyOf <#spiderman> ;
    a foaf:Person ;    # in the context of the Marvel universe
    foaf:name "Green Goblin" .
```

and also about Spiderman.

<a name="rdf-spiderman"></a>
```
<<rdf-spiderman>> =
<#spiderman>
    rel:enemyOf <#green-goblin> ;
    a foaf:Person ;
    foaf:name "Spiderman" .
```

Now let's try that with plain text.

<a name="*"></a>
```
<<*>> =
  <<abc>>
  <<def>>
```
*Refers to: [abc](#abc), [def](#def)*

<a name="abc"></a>
```
<<abc>> =
  Here is the first line.
  And the second line.
```

<a name="def"></a>
```
<<def>> =
  Here is the third line.
  And the fourth line.
```

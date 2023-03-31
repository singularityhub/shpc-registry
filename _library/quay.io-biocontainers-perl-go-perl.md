---
layout: container
name:  "quay.io/biocontainers/perl-go-perl"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-go-perl/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-go-perl/container.yaml"
updated_at: "2023-03-31 03:13:49.153988"
latest: "0.15--pl5321hdfd78af_4"
container_url: "https://biocontainers.pro/tools/perl-go-perl"
aliases:
 - "go-apply-xslt"
 - "go-dag-summary.pl"
 - "go-export-graph.pl"
 - "go-export-prolog.pl"
 - "go-filter-subset.pl"
 - "go-show-assocs-by-node.pl"
 - "go-show-paths-to-root.pl"
 - "go2chadoxml"
 - "go2error_report"
 - "go2fmt.pl"
 - "go2godb_prestore"
 - "go2obo"
 - "go2obo_html"
 - "go2obo_text"
 - "go2obo_xml"
 - "go2owl"
 - "go2pathlist"
 - "go2prolog"
 - "go2rdf"
 - "go2rdfxml"
 - "go2summary"
 - "go2sxpr"
 - "go2tbl"
 - "go2text_html"
 - "go2xml"
 - "map2slim"
 - "stag-autoschema.pl"
 - "stag-db.pl"
 - "stag-diff.pl"
 - "stag-drawtree.pl"
 - "stag-filter.pl"
 - "stag-findsubtree.pl"
 - "stag-flatten.pl"
 - "stag-grep.pl"
 - "stag-handle.pl"
 - "stag-itext2simple.pl"
versions:
 - "0.15--pl5321hdfd78af_4"
description: "shpc-registry automated BioContainers addition for perl-go-perl"
config: {"url": "https://biocontainers.pro/tools/perl-go-perl", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-go-perl", "latest": {"0.15--pl5321hdfd78af_4": "sha256:a26833552505f2ab397197787908f1a13905eebf9082d3fc20316670bcac0eaf"}, "tags": {"0.15--pl5321hdfd78af_4": "sha256:a26833552505f2ab397197787908f1a13905eebf9082d3fc20316670bcac0eaf"}, "docker": "quay.io/biocontainers/perl-go-perl", "aliases": {"go-apply-xslt": "/usr/local/bin/go-apply-xslt", "go-dag-summary.pl": "/usr/local/bin/go-dag-summary.pl", "go-export-graph.pl": "/usr/local/bin/go-export-graph.pl", "go-export-prolog.pl": "/usr/local/bin/go-export-prolog.pl", "go-filter-subset.pl": "/usr/local/bin/go-filter-subset.pl", "go-show-assocs-by-node.pl": "/usr/local/bin/go-show-assocs-by-node.pl", "go-show-paths-to-root.pl": "/usr/local/bin/go-show-paths-to-root.pl", "go2chadoxml": "/usr/local/bin/go2chadoxml", "go2error_report": "/usr/local/bin/go2error_report", "go2fmt.pl": "/usr/local/bin/go2fmt.pl", "go2godb_prestore": "/usr/local/bin/go2godb_prestore", "go2obo": "/usr/local/bin/go2obo", "go2obo_html": "/usr/local/bin/go2obo_html", "go2obo_text": "/usr/local/bin/go2obo_text", "go2obo_xml": "/usr/local/bin/go2obo_xml", "go2owl": "/usr/local/bin/go2owl", "go2pathlist": "/usr/local/bin/go2pathlist", "go2prolog": "/usr/local/bin/go2prolog", "go2rdf": "/usr/local/bin/go2rdf", "go2rdfxml": "/usr/local/bin/go2rdfxml", "go2summary": "/usr/local/bin/go2summary", "go2sxpr": "/usr/local/bin/go2sxpr", "go2tbl": "/usr/local/bin/go2tbl", "go2text_html": "/usr/local/bin/go2text_html", "go2xml": "/usr/local/bin/go2xml", "map2slim": "/usr/local/bin/map2slim", "stag-autoschema.pl": "/usr/local/bin/stag-autoschema.pl", "stag-db.pl": "/usr/local/bin/stag-db.pl", "stag-diff.pl": "/usr/local/bin/stag-diff.pl", "stag-drawtree.pl": "/usr/local/bin/stag-drawtree.pl", "stag-filter.pl": "/usr/local/bin/stag-filter.pl", "stag-findsubtree.pl": "/usr/local/bin/stag-findsubtree.pl", "stag-flatten.pl": "/usr/local/bin/stag-flatten.pl", "stag-grep.pl": "/usr/local/bin/stag-grep.pl", "stag-handle.pl": "/usr/local/bin/stag-handle.pl", "stag-itext2simple.pl": "/usr/local/bin/stag-itext2simple.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-go-perl.
shpc-registry automated BioContainers addition for perl-go-perl
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-go-perl
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-go-perl:0.15--pl5321hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-go-perl/0.15--pl5321hdfd78af_4
$ module help quay.io/biocontainers/perl-go-perl/0.15--pl5321hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-go-perl-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-go-perl-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-go-perl-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-go-perl-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-go-perl-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-go-perl-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### go-apply-xslt

```bash
$ singularity exec <container> /usr/local/bin/go-apply-xslt
$ podman run --it --rm --entrypoint /usr/local/bin/go-apply-xslt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go-apply-xslt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go-dag-summary.pl

```bash
$ singularity exec <container> /usr/local/bin/go-dag-summary.pl
$ podman run --it --rm --entrypoint /usr/local/bin/go-dag-summary.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go-dag-summary.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go-export-graph.pl

```bash
$ singularity exec <container> /usr/local/bin/go-export-graph.pl
$ podman run --it --rm --entrypoint /usr/local/bin/go-export-graph.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go-export-graph.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go-export-prolog.pl

```bash
$ singularity exec <container> /usr/local/bin/go-export-prolog.pl
$ podman run --it --rm --entrypoint /usr/local/bin/go-export-prolog.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go-export-prolog.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go-filter-subset.pl

```bash
$ singularity exec <container> /usr/local/bin/go-filter-subset.pl
$ podman run --it --rm --entrypoint /usr/local/bin/go-filter-subset.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go-filter-subset.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go-show-assocs-by-node.pl

```bash
$ singularity exec <container> /usr/local/bin/go-show-assocs-by-node.pl
$ podman run --it --rm --entrypoint /usr/local/bin/go-show-assocs-by-node.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go-show-assocs-by-node.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go-show-paths-to-root.pl

```bash
$ singularity exec <container> /usr/local/bin/go-show-paths-to-root.pl
$ podman run --it --rm --entrypoint /usr/local/bin/go-show-paths-to-root.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go-show-paths-to-root.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go2chadoxml

```bash
$ singularity exec <container> /usr/local/bin/go2chadoxml
$ podman run --it --rm --entrypoint /usr/local/bin/go2chadoxml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go2chadoxml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go2error_report

```bash
$ singularity exec <container> /usr/local/bin/go2error_report
$ podman run --it --rm --entrypoint /usr/local/bin/go2error_report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go2error_report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go2fmt.pl

```bash
$ singularity exec <container> /usr/local/bin/go2fmt.pl
$ podman run --it --rm --entrypoint /usr/local/bin/go2fmt.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go2fmt.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go2godb_prestore

```bash
$ singularity exec <container> /usr/local/bin/go2godb_prestore
$ podman run --it --rm --entrypoint /usr/local/bin/go2godb_prestore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go2godb_prestore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go2obo

```bash
$ singularity exec <container> /usr/local/bin/go2obo
$ podman run --it --rm --entrypoint /usr/local/bin/go2obo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go2obo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go2obo_html

```bash
$ singularity exec <container> /usr/local/bin/go2obo_html
$ podman run --it --rm --entrypoint /usr/local/bin/go2obo_html   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go2obo_html   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go2obo_text

```bash
$ singularity exec <container> /usr/local/bin/go2obo_text
$ podman run --it --rm --entrypoint /usr/local/bin/go2obo_text   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go2obo_text   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go2obo_xml

```bash
$ singularity exec <container> /usr/local/bin/go2obo_xml
$ podman run --it --rm --entrypoint /usr/local/bin/go2obo_xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go2obo_xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go2owl

```bash
$ singularity exec <container> /usr/local/bin/go2owl
$ podman run --it --rm --entrypoint /usr/local/bin/go2owl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go2owl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go2pathlist

```bash
$ singularity exec <container> /usr/local/bin/go2pathlist
$ podman run --it --rm --entrypoint /usr/local/bin/go2pathlist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go2pathlist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go2prolog

```bash
$ singularity exec <container> /usr/local/bin/go2prolog
$ podman run --it --rm --entrypoint /usr/local/bin/go2prolog   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go2prolog   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go2rdf

```bash
$ singularity exec <container> /usr/local/bin/go2rdf
$ podman run --it --rm --entrypoint /usr/local/bin/go2rdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go2rdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go2rdfxml

```bash
$ singularity exec <container> /usr/local/bin/go2rdfxml
$ podman run --it --rm --entrypoint /usr/local/bin/go2rdfxml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go2rdfxml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go2summary

```bash
$ singularity exec <container> /usr/local/bin/go2summary
$ podman run --it --rm --entrypoint /usr/local/bin/go2summary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go2summary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go2sxpr

```bash
$ singularity exec <container> /usr/local/bin/go2sxpr
$ podman run --it --rm --entrypoint /usr/local/bin/go2sxpr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go2sxpr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go2tbl

```bash
$ singularity exec <container> /usr/local/bin/go2tbl
$ podman run --it --rm --entrypoint /usr/local/bin/go2tbl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go2tbl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go2text_html

```bash
$ singularity exec <container> /usr/local/bin/go2text_html
$ podman run --it --rm --entrypoint /usr/local/bin/go2text_html   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go2text_html   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go2xml

```bash
$ singularity exec <container> /usr/local/bin/go2xml
$ podman run --it --rm --entrypoint /usr/local/bin/go2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### map2slim

```bash
$ singularity exec <container> /usr/local/bin/map2slim
$ podman run --it --rm --entrypoint /usr/local/bin/map2slim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/map2slim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stag-autoschema.pl

```bash
$ singularity exec <container> /usr/local/bin/stag-autoschema.pl
$ podman run --it --rm --entrypoint /usr/local/bin/stag-autoschema.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stag-autoschema.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stag-db.pl

```bash
$ singularity exec <container> /usr/local/bin/stag-db.pl
$ podman run --it --rm --entrypoint /usr/local/bin/stag-db.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stag-db.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stag-diff.pl

```bash
$ singularity exec <container> /usr/local/bin/stag-diff.pl
$ podman run --it --rm --entrypoint /usr/local/bin/stag-diff.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stag-diff.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stag-drawtree.pl

```bash
$ singularity exec <container> /usr/local/bin/stag-drawtree.pl
$ podman run --it --rm --entrypoint /usr/local/bin/stag-drawtree.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stag-drawtree.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stag-filter.pl

```bash
$ singularity exec <container> /usr/local/bin/stag-filter.pl
$ podman run --it --rm --entrypoint /usr/local/bin/stag-filter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stag-filter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stag-findsubtree.pl

```bash
$ singularity exec <container> /usr/local/bin/stag-findsubtree.pl
$ podman run --it --rm --entrypoint /usr/local/bin/stag-findsubtree.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stag-findsubtree.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stag-flatten.pl

```bash
$ singularity exec <container> /usr/local/bin/stag-flatten.pl
$ podman run --it --rm --entrypoint /usr/local/bin/stag-flatten.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stag-flatten.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stag-grep.pl

```bash
$ singularity exec <container> /usr/local/bin/stag-grep.pl
$ podman run --it --rm --entrypoint /usr/local/bin/stag-grep.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stag-grep.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stag-handle.pl

```bash
$ singularity exec <container> /usr/local/bin/stag-handle.pl
$ podman run --it --rm --entrypoint /usr/local/bin/stag-handle.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stag-handle.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stag-itext2simple.pl

```bash
$ singularity exec <container> /usr/local/bin/stag-itext2simple.pl
$ podman run --it --rm --entrypoint /usr/local/bin/stag-itext2simple.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stag-itext2simple.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)
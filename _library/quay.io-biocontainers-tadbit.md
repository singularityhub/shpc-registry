---
layout: container
name:  "quay.io/biocontainers/tadbit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tadbit/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/tadbit/container.yaml"
updated_at: "2022-10-29 05:32:32.895900"
latest: "1.0.1--py36h4aaaa08_1"
container_url: "https://biocontainers.pro/tools/tadbit"
aliases:
 - "gem-indexer"
 - "gem-mapper"
 - "gem-retriever"
 - "normalize_oneD.R"
 - "tadbit"
 - "2to3-3.6"
 - "accn-at-a-time"
 - "ace2sam"
 - "align-columns"
 - "amino-acid-composition"
 - "archive-pubmed"
 - "asn2xml"
 - "between-two-genes"
 - "blast2sam.pl"
 - "blast_formatter"
versions:
 - "1.0.1--py36h4aaaa08_1"
description: "shpc-registry automated BioContainers addition for tadbit"
config: {"url": "https://biocontainers.pro/tools/tadbit", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tadbit", "latest": {"1.0.1--py36h4aaaa08_1": "sha256:c3c69e45f09ff844de670fb2204610268bab04c181f495c45cc810268d468897"}, "tags": {"1.0.1--py36h4aaaa08_1": "sha256:c3c69e45f09ff844de670fb2204610268bab04c181f495c45cc810268d468897"}, "docker": "quay.io/biocontainers/tadbit", "aliases": {"gem-indexer": "/usr/local/bin/gem-indexer", "gem-mapper": "/usr/local/bin/gem-mapper", "gem-retriever": "/usr/local/bin/gem-retriever", "normalize_oneD.R": "/usr/local/bin/normalize_oneD.R", "tadbit": "/usr/local/bin/tadbit", "2to3-3.6": "/usr/local/bin/2to3-3.6", "accn-at-a-time": "/usr/local/bin/accn-at-a-time", "ace2sam": "/usr/local/bin/ace2sam", "align-columns": "/usr/local/bin/align-columns", "amino-acid-composition": "/usr/local/bin/amino-acid-composition", "archive-pubmed": "/usr/local/bin/archive-pubmed", "asn2xml": "/usr/local/bin/asn2xml", "between-two-genes": "/usr/local/bin/between-two-genes", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "blast_formatter": "/usr/local/bin/blast_formatter"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tadbit.
shpc-registry automated BioContainers addition for tadbit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tadbit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tadbit:1.0.1--py36h4aaaa08_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tadbit/1.0.1--py36h4aaaa08_1
$ module help quay.io/biocontainers/tadbit/1.0.1--py36h4aaaa08_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tadbit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tadbit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tadbit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tadbit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tadbit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tadbit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gem-indexer

```bash
$ singularity exec <container> /usr/local/bin/gem-indexer
$ podman run --it --rm --entrypoint /usr/local/bin/gem-indexer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gem-indexer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gem-mapper

```bash
$ singularity exec <container> /usr/local/bin/gem-mapper
$ podman run --it --rm --entrypoint /usr/local/bin/gem-mapper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gem-mapper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gem-retriever

```bash
$ singularity exec <container> /usr/local/bin/gem-retriever
$ podman run --it --rm --entrypoint /usr/local/bin/gem-retriever   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gem-retriever   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalize_oneD.R

```bash
$ singularity exec <container> /usr/local/bin/normalize_oneD.R
$ podman run --it --rm --entrypoint /usr/local/bin/normalize_oneD.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalize_oneD.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tadbit

```bash
$ singularity exec <container> /usr/local/bin/tadbit
$ podman run --it --rm --entrypoint /usr/local/bin/tadbit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tadbit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### accn-at-a-time

```bash
$ singularity exec <container> /usr/local/bin/accn-at-a-time
$ podman run --it --rm --entrypoint /usr/local/bin/accn-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/accn-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### align-columns

```bash
$ singularity exec <container> /usr/local/bin/align-columns
$ podman run --it --rm --entrypoint /usr/local/bin/align-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/align-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amino-acid-composition

```bash
$ singularity exec <container> /usr/local/bin/amino-acid-composition
$ podman run --it --rm --entrypoint /usr/local/bin/amino-acid-composition   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amino-acid-composition   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-pubmed

```bash
$ singularity exec <container> /usr/local/bin/archive-pubmed
$ podman run --it --rm --entrypoint /usr/local/bin/archive-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asn2xml

```bash
$ singularity exec <container> /usr/local/bin/asn2xml
$ podman run --it --rm --entrypoint /usr/local/bin/asn2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asn2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### between-two-genes

```bash
$ singularity exec <container> /usr/local/bin/between-two-genes
$ podman run --it --rm --entrypoint /usr/local/bin/between-two-genes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/between-two-genes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/blast2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast_formatter

```bash
$ singularity exec <container> /usr/local/bin/blast_formatter
$ podman run --it --rm --entrypoint /usr/local/bin/blast_formatter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast_formatter   -v ${PWD} -w ${PWD} <container> -c " $@"
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
---
layout: container
name:  "quay.io/biocontainers/amap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/amap/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/amap/container.yaml"
updated_at: "2022-10-29 05:52:29.449390"
latest: "2.2--h9f5acd7_3"
container_url: "https://biocontainers.pro/tools/amap"
aliases:
 - "amap"
 - "accn-at-a-time"
 - "align-columns"
 - "amino-acid-composition"
 - "archive-pubmed"
 - "asn2xml"
 - "between-two-genes"
 - "blast_formatter"
 - "blastdb_aliastool"
 - "blastdbcheck"
 - "blastdbcmd"
versions:
 - "2.2--h9f5acd7_3"
description: "shpc-registry automated BioContainers addition for amap"
config: {"url": "https://biocontainers.pro/tools/amap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for amap", "latest": {"2.2--h9f5acd7_3": "sha256:a8da46fa423d674823ebfbbb084fd60add0c135c73799dd960f88e33f8e7ef5a"}, "tags": {"2.2--h9f5acd7_3": "sha256:a8da46fa423d674823ebfbbb084fd60add0c135c73799dd960f88e33f8e7ef5a"}, "docker": "quay.io/biocontainers/amap", "aliases": {"amap": "/usr/local/bin/amap", "accn-at-a-time": "/usr/local/bin/accn-at-a-time", "align-columns": "/usr/local/bin/align-columns", "amino-acid-composition": "/usr/local/bin/amino-acid-composition", "archive-pubmed": "/usr/local/bin/archive-pubmed", "asn2xml": "/usr/local/bin/asn2xml", "between-two-genes": "/usr/local/bin/between-two-genes", "blast_formatter": "/usr/local/bin/blast_formatter", "blastdb_aliastool": "/usr/local/bin/blastdb_aliastool", "blastdbcheck": "/usr/local/bin/blastdbcheck", "blastdbcmd": "/usr/local/bin/blastdbcmd"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/amap.
shpc-registry automated BioContainers addition for amap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/amap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/amap:2.2--h9f5acd7_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/amap/2.2--h9f5acd7_3
$ module help quay.io/biocontainers/amap/2.2--h9f5acd7_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### amap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### amap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### amap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### amap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### amap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### amap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### amap

```bash
$ singularity exec <container> /usr/local/bin/amap
$ podman run --it --rm --entrypoint /usr/local/bin/amap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### accn-at-a-time

```bash
$ singularity exec <container> /usr/local/bin/accn-at-a-time
$ podman run --it --rm --entrypoint /usr/local/bin/accn-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/accn-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### blast_formatter

```bash
$ singularity exec <container> /usr/local/bin/blast_formatter
$ podman run --it --rm --entrypoint /usr/local/bin/blast_formatter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast_formatter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdb_aliastool

```bash
$ singularity exec <container> /usr/local/bin/blastdb_aliastool
$ podman run --it --rm --entrypoint /usr/local/bin/blastdb_aliastool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdb_aliastool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdbcheck

```bash
$ singularity exec <container> /usr/local/bin/blastdbcheck
$ podman run --it --rm --entrypoint /usr/local/bin/blastdbcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdbcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdbcmd

```bash
$ singularity exec <container> /usr/local/bin/blastdbcmd
$ podman run --it --rm --entrypoint /usr/local/bin/blastdbcmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdbcmd   -v ${PWD} -w ${PWD} <container> -c " $@"
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
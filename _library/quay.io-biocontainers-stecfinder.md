---
layout: container
name:  "quay.io/biocontainers/stecfinder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/stecfinder/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/stecfinder/container.yaml"
updated_at: "2022-10-29 05:55:21.161352"
latest: "1.1.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/stecfinder"
aliases:
 - "stecfinder"
 - "2to3-3.10"
 - "accn-at-a-time"
 - "align-columns"
 - "amino-acid-composition"
 - "archive-pubmed"
 - "asn2xml"
 - "between-two-genes"
 - "blast_formatter"
 - "blastdb_aliastool"
 - "blastdbcheck"
versions:
 - "1.1.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for stecfinder"
config: {"url": "https://biocontainers.pro/tools/stecfinder", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for stecfinder", "latest": {"1.1.0--pyhdfd78af_0": "sha256:dadf3e030539a5df63721596346b54fff590ec8eb7fab0a16a42e8620c27372d"}, "tags": {"1.1.0--pyhdfd78af_0": "sha256:dadf3e030539a5df63721596346b54fff590ec8eb7fab0a16a42e8620c27372d"}, "docker": "quay.io/biocontainers/stecfinder", "aliases": {"stecfinder": "/usr/local/bin/stecfinder", "2to3-3.10": "/usr/local/bin/2to3-3.10", "accn-at-a-time": "/usr/local/bin/accn-at-a-time", "align-columns": "/usr/local/bin/align-columns", "amino-acid-composition": "/usr/local/bin/amino-acid-composition", "archive-pubmed": "/usr/local/bin/archive-pubmed", "asn2xml": "/usr/local/bin/asn2xml", "between-two-genes": "/usr/local/bin/between-two-genes", "blast_formatter": "/usr/local/bin/blast_formatter", "blastdb_aliastool": "/usr/local/bin/blastdb_aliastool", "blastdbcheck": "/usr/local/bin/blastdbcheck"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/stecfinder.
shpc-registry automated BioContainers addition for stecfinder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/stecfinder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/stecfinder:1.1.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/stecfinder/1.1.0--pyhdfd78af_0
$ module help quay.io/biocontainers/stecfinder/1.1.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### stecfinder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### stecfinder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### stecfinder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### stecfinder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### stecfinder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### stecfinder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### stecfinder

```bash
$ singularity exec <container> /usr/local/bin/stecfinder
$ podman run --it --rm --entrypoint /usr/local/bin/stecfinder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stecfinder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
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
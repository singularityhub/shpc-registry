---
layout: container
name:  "quay.io/biocontainers/pairtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pairtools/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/pairtools/container.yaml"
updated_at: "2022-10-29 05:30:05.104674"
latest: "1.0.1--py37h9f12aac_0"
container_url: "https://biocontainers.pro/tools/pairtools"
aliases:
 - "pairtools"
 - "pbgzip"
 - "2to3-3.7"
 - "ace2sam"
 - "b2sum"
 - "bam2pairs"
 - "base32"
 - "base64"
 - "basename"
 - "basenc"
 - "bgzip"
 - "blast2sam.pl"
versions:
 - "1.0.1--py37h9f12aac_0"
description: "shpc-registry automated BioContainers addition for pairtools"
config: {"url": "https://biocontainers.pro/tools/pairtools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pairtools", "latest": {"1.0.1--py37h9f12aac_0": "sha256:656044fea9e722c2a9189e3134f65949b7ee76644d3b8008bf5dd478c5846408"}, "tags": {"1.0.1--py37h9f12aac_0": "sha256:656044fea9e722c2a9189e3134f65949b7ee76644d3b8008bf5dd478c5846408"}, "docker": "quay.io/biocontainers/pairtools", "aliases": {"pairtools": "/usr/local/bin/pairtools", "pbgzip": "/usr/local/bin/pbgzip", "2to3-3.7": "/usr/local/bin/2to3-3.7", "ace2sam": "/usr/local/bin/ace2sam", "b2sum": "/usr/local/bin/b2sum", "bam2pairs": "/usr/local/bin/bam2pairs", "base32": "/usr/local/bin/base32", "base64": "/usr/local/bin/base64", "basename": "/usr/local/bin/basename", "basenc": "/usr/local/bin/basenc", "bgzip": "/usr/local/bin/bgzip", "blast2sam.pl": "/usr/local/bin/blast2sam.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pairtools.
shpc-registry automated BioContainers addition for pairtools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pairtools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pairtools:1.0.1--py37h9f12aac_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pairtools/1.0.1--py37h9f12aac_0
$ module help quay.io/biocontainers/pairtools/1.0.1--py37h9f12aac_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pairtools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pairtools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pairtools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pairtools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pairtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pairtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pairtools

```bash
$ singularity exec <container> /usr/local/bin/pairtools
$ podman run --it --rm --entrypoint /usr/local/bin/pairtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pairtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbgzip

```bash
$ singularity exec <container> /usr/local/bin/pbgzip
$ podman run --it --rm --entrypoint /usr/local/bin/pbgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### b2sum

```bash
$ singularity exec <container> /usr/local/bin/b2sum
$ podman run --it --rm --entrypoint /usr/local/bin/b2sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/b2sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2pairs

```bash
$ singularity exec <container> /usr/local/bin/bam2pairs
$ podman run --it --rm --entrypoint /usr/local/bin/bam2pairs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2pairs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### base32

```bash
$ singularity exec <container> /usr/local/bin/base32
$ podman run --it --rm --entrypoint /usr/local/bin/base32   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/base32   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### base64

```bash
$ singularity exec <container> /usr/local/bin/base64
$ podman run --it --rm --entrypoint /usr/local/bin/base64   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/base64   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### basename

```bash
$ singularity exec <container> /usr/local/bin/basename
$ podman run --it --rm --entrypoint /usr/local/bin/basename   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basename   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### basenc

```bash
$ singularity exec <container> /usr/local/bin/basenc
$ podman run --it --rm --entrypoint /usr/local/bin/basenc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basenc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/blast2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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
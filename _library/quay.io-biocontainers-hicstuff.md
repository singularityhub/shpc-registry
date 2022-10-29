---
layout: container
name:  "quay.io/biocontainers/hicstuff"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hicstuff/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/hicstuff/container.yaml"
updated_at: "2022-10-29 05:50:43.334235"
latest: "3.1.5--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/hicstuff"
aliases:
 - "hicstuff"
 - "2to3-3.7"
 - "ace2sam"
 - "blast2sam.pl"
 - "bowtie2"
 - "bowtie2-align-l"
 - "bowtie2-align-s"
 - "bowtie2-build"
 - "bowtie2-build-l"
 - "bowtie2-build-s"
 - "bowtie2-inspect"
versions:
 - "3.1.5--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for hicstuff"
config: {"url": "https://biocontainers.pro/tools/hicstuff", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hicstuff", "latest": {"3.1.5--pyhdfd78af_0": "sha256:fed76d89a1c0460bbb9066c99383e14e67068f89a908879e2cc9bd6fb955c9d9"}, "tags": {"3.1.5--pyhdfd78af_0": "sha256:fed76d89a1c0460bbb9066c99383e14e67068f89a908879e2cc9bd6fb955c9d9"}, "docker": "quay.io/biocontainers/hicstuff", "aliases": {"hicstuff": "/usr/local/bin/hicstuff", "2to3-3.7": "/usr/local/bin/2to3-3.7", "ace2sam": "/usr/local/bin/ace2sam", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2": "/usr/local/bin/bowtie2", "bowtie2-align-l": "/usr/local/bin/bowtie2-align-l", "bowtie2-align-s": "/usr/local/bin/bowtie2-align-s", "bowtie2-build": "/usr/local/bin/bowtie2-build", "bowtie2-build-l": "/usr/local/bin/bowtie2-build-l", "bowtie2-build-s": "/usr/local/bin/bowtie2-build-s", "bowtie2-inspect": "/usr/local/bin/bowtie2-inspect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hicstuff.
shpc-registry automated BioContainers addition for hicstuff
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hicstuff
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hicstuff:3.1.5--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hicstuff/3.1.5--pyhdfd78af_0
$ module help quay.io/biocontainers/hicstuff/3.1.5--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hicstuff-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hicstuff-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hicstuff-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hicstuff-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hicstuff-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hicstuff-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hicstuff

```bash
$ singularity exec <container> /usr/local/bin/hicstuff
$ podman run --it --rm --entrypoint /usr/local/bin/hicstuff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicstuff   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### blast2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/blast2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2

```bash
$ singularity exec <container> /usr/local/bin/bowtie2
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-align-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-align-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-align-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-align-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-build

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-build
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-build-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-build-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-build-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-build-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-inspect

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
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
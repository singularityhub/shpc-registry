---
layout: container
name:  "quay.io/biocontainers/abyss"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/abyss/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/abyss/container.yaml"
updated_at: "2022-10-27 01:04:27.814280"
latest: "2.3.5--h41cdee2_1"
container_url: "https://biocontainers.pro/tools/abyss"
aliases:
 - "abyss-rresolver-short"
 - "abyss-stack-size"
 - "irqtop"
 - "lsirq"
 - "nsenter"
 - "prlimit"
 - "scriptlive"
versions:
 - "2.3.5--h41cdee2_1"
description: "shpc-registry automated BioContainers addition for abyss"
config: {"url": "https://biocontainers.pro/tools/abyss", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for abyss", "latest": {"2.3.5--h41cdee2_1": "sha256:bed6c7d2dad58b24b3e8c1927b61c92c846772c9f77db51eb7f9d3f543030c4d"}, "tags": {"2.3.5--h41cdee2_1": "sha256:bed6c7d2dad58b24b3e8c1927b61c92c846772c9f77db51eb7f9d3f543030c4d"}, "docker": "quay.io/biocontainers/abyss", "aliases": {"abyss-rresolver-short": "/usr/local/bin/abyss-rresolver-short", "abyss-stack-size": "/usr/local/bin/abyss-stack-size", "irqtop": "/usr/local/bin/irqtop", "lsirq": "/usr/local/bin/lsirq", "nsenter": "/usr/local/bin/nsenter", "prlimit": "/usr/local/bin/prlimit", "scriptlive": "/usr/local/bin/scriptlive"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/abyss.
shpc-registry automated BioContainers addition for abyss
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/abyss
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/abyss:2.3.5--h41cdee2_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/abyss/2.3.5--h41cdee2_1
$ module help quay.io/biocontainers/abyss/2.3.5--h41cdee2_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### abyss-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### abyss-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### abyss-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### abyss-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### abyss-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### abyss-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### abyss-rresolver-short

```bash
$ singularity exec <container> /usr/local/bin/abyss-rresolver-short
$ podman run --it --rm --entrypoint /usr/local/bin/abyss-rresolver-short   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abyss-rresolver-short   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-stack-size

```bash
$ singularity exec <container> /usr/local/bin/abyss-stack-size
$ podman run --it --rm --entrypoint /usr/local/bin/abyss-stack-size   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abyss-stack-size   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### irqtop

```bash
$ singularity exec <container> /usr/local/bin/irqtop
$ podman run --it --rm --entrypoint /usr/local/bin/irqtop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/irqtop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lsirq

```bash
$ singularity exec <container> /usr/local/bin/lsirq
$ podman run --it --rm --entrypoint /usr/local/bin/lsirq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lsirq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nsenter

```bash
$ singularity exec <container> /usr/local/bin/nsenter
$ podman run --it --rm --entrypoint /usr/local/bin/nsenter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nsenter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prlimit

```bash
$ singularity exec <container> /usr/local/bin/prlimit
$ podman run --it --rm --entrypoint /usr/local/bin/prlimit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prlimit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scriptlive

```bash
$ singularity exec <container> /usr/local/bin/scriptlive
$ podman run --it --rm --entrypoint /usr/local/bin/scriptlive   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scriptlive   -v ${PWD} -w ${PWD} <container> -c " $@"
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
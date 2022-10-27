---
layout: container
name:  "quay.io/biocontainers/ntlink"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ntlink/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ntlink/container.yaml"
updated_at: "2022-10-27 01:14:07.337712"
latest: "1.3.4--py39h6935b12_0"
container_url: "https://biocontainers.pro/tools/ntlink"
aliases:
 - "abyss-rresolver-short"
 - "indexlr"
 - "irqtop"
 - "lrunzip"
 - "lrzcat"
 - "lrzip"
 - "lrztar"
 - "lrzuntar"
 - "lsirq"
 - "nsenter"
 - "ntLink"
 - "ntLink_rounds"
 - "prlimit"
versions:
 - "1.3.4--py39h6935b12_0"
description: "shpc-registry automated BioContainers addition for ntlink"
config: {"url": "https://biocontainers.pro/tools/ntlink", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ntlink", "latest": {"1.3.4--py39h6935b12_0": "sha256:afce9184978c9c93e6d58986630145fff8f2212bebf24c73a6b4c3bb79abdbea"}, "tags": {"1.3.4--py39h6935b12_0": "sha256:afce9184978c9c93e6d58986630145fff8f2212bebf24c73a6b4c3bb79abdbea"}, "docker": "quay.io/biocontainers/ntlink", "aliases": {"abyss-rresolver-short": "/usr/local/bin/abyss-rresolver-short", "indexlr": "/usr/local/bin/indexlr", "irqtop": "/usr/local/bin/irqtop", "lrunzip": "/usr/local/bin/lrunzip", "lrzcat": "/usr/local/bin/lrzcat", "lrzip": "/usr/local/bin/lrzip", "lrztar": "/usr/local/bin/lrztar", "lrzuntar": "/usr/local/bin/lrzuntar", "lsirq": "/usr/local/bin/lsirq", "nsenter": "/usr/local/bin/nsenter", "ntLink": "/usr/local/bin/ntLink", "ntLink_rounds": "/usr/local/bin/ntLink_rounds", "prlimit": "/usr/local/bin/prlimit"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ntlink.
shpc-registry automated BioContainers addition for ntlink
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ntlink
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ntlink:1.3.4--py39h6935b12_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ntlink/1.3.4--py39h6935b12_0
$ module help quay.io/biocontainers/ntlink/1.3.4--py39h6935b12_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ntlink-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ntlink-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ntlink-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ntlink-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ntlink-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ntlink-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### abyss-rresolver-short

```bash
$ singularity exec <container> /usr/local/bin/abyss-rresolver-short
$ podman run --it --rm --entrypoint /usr/local/bin/abyss-rresolver-short   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abyss-rresolver-short   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### indexlr

```bash
$ singularity exec <container> /usr/local/bin/indexlr
$ podman run --it --rm --entrypoint /usr/local/bin/indexlr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/indexlr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### irqtop

```bash
$ singularity exec <container> /usr/local/bin/irqtop
$ podman run --it --rm --entrypoint /usr/local/bin/irqtop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/irqtop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrunzip

```bash
$ singularity exec <container> /usr/local/bin/lrunzip
$ podman run --it --rm --entrypoint /usr/local/bin/lrunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrzcat

```bash
$ singularity exec <container> /usr/local/bin/lrzcat
$ podman run --it --rm --entrypoint /usr/local/bin/lrzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrzip

```bash
$ singularity exec <container> /usr/local/bin/lrzip
$ podman run --it --rm --entrypoint /usr/local/bin/lrzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrztar

```bash
$ singularity exec <container> /usr/local/bin/lrztar
$ podman run --it --rm --entrypoint /usr/local/bin/lrztar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrztar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrzuntar

```bash
$ singularity exec <container> /usr/local/bin/lrzuntar
$ podman run --it --rm --entrypoint /usr/local/bin/lrzuntar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrzuntar   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### ntLink

```bash
$ singularity exec <container> /usr/local/bin/ntLink
$ podman run --it --rm --entrypoint /usr/local/bin/ntLink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ntLink   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ntLink_rounds

```bash
$ singularity exec <container> /usr/local/bin/ntLink_rounds
$ podman run --it --rm --entrypoint /usr/local/bin/ntLink_rounds   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ntLink_rounds   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prlimit

```bash
$ singularity exec <container> /usr/local/bin/prlimit
$ podman run --it --rm --entrypoint /usr/local/bin/prlimit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prlimit   -v ${PWD} -w ${PWD} <container> -c " $@"
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
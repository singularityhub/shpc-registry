---
layout: container
name:  "quay.io/biocontainers/ldblockshow"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ldblockshow/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ldblockshow/container.yaml"
updated_at: "2023-10-25 03:15:44.869780"
latest: "1.40--pl5321hdcf5f25_3"
container_url: "https://biocontainers.pro/tools/ldblockshow"
aliases:
 - "LDBlockShow"
 - "ShowLDSVG"
 - "plink"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.40--pl5321hd03093a_2"
 - "1.40--pl5321hdcf5f25_3"
description: "shpc-registry automated BioContainers addition for ldblockshow"
config: {"url": "https://biocontainers.pro/tools/ldblockshow", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ldblockshow", "latest": {"1.40--pl5321hdcf5f25_3": "sha256:4658b8eeda5aac52691f625bc0e6eea7d97dd7bf85ebbee0570ff23673d3827e"}, "tags": {"1.40--pl5321hd03093a_2": "sha256:0780e7d3e35e4977859a316e8797c61993390d6c9880ff6ad339affdeba91be2", "1.40--pl5321hdcf5f25_3": "sha256:4658b8eeda5aac52691f625bc0e6eea7d97dd7bf85ebbee0570ff23673d3827e"}, "docker": "quay.io/biocontainers/ldblockshow", "aliases": {"LDBlockShow": "/usr/local/bin/LDBlockShow", "ShowLDSVG": "/usr/local/bin/ShowLDSVG", "plink": "/usr/local/bin/plink", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ldblockshow.
shpc-registry automated BioContainers addition for ldblockshow
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ldblockshow
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ldblockshow:1.40--pl5321hdcf5f25_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ldblockshow/1.40--pl5321hdcf5f25_3
$ module help quay.io/biocontainers/ldblockshow/1.40--pl5321hdcf5f25_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ldblockshow-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ldblockshow-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ldblockshow-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ldblockshow-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ldblockshow-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ldblockshow-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### LDBlockShow

```bash
$ singularity exec <container> /usr/local/bin/LDBlockShow
$ podman run --it --rm --entrypoint /usr/local/bin/LDBlockShow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LDBlockShow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ShowLDSVG

```bash
$ singularity exec <container> /usr/local/bin/ShowLDSVG
$ podman run --it --rm --entrypoint /usr/local/bin/ShowLDSVG   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ShowLDSVG   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plink

```bash
$ singularity exec <container> /usr/local/bin/plink
$ podman run --it --rm --entrypoint /usr/local/bin/plink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plink   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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
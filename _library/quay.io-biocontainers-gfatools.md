---
layout: container
name:  "quay.io/biocontainers/gfatools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gfatools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gfatools/container.yaml"
updated_at: "2025-03-20 03:29:55.443766"
latest: "0.5--h577a1d6_5"
container_url: "https://biocontainers.pro/tools/gfatools"
aliases:
 - "gfatools"
 - "paf2gfa"
versions:
 - "0.5--h7132678_2"
 - "0.5--he4a0461_4"
 - "0.5--h577a1d6_5"
description: "shpc-registry automated BioContainers addition for gfatools"
config: {"url": "https://biocontainers.pro/tools/gfatools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gfatools", "latest": {"0.5--h577a1d6_5": "sha256:cdb1a77adaab3a25de0a57d36b219d3c30a98c3d9b6932b5755fbd73c15b3141"}, "tags": {"0.5--h7132678_2": "sha256:77e9c818a3cb314c50b2ed086aa3e3054dedac0eab3f7d7b3338d8dfa66ddbdd", "0.5--he4a0461_4": "sha256:64a4f8e6838e2d259ea5da2d3c4001d1254adab364c87a0ee3e75966751810c4", "0.5--h577a1d6_5": "sha256:cdb1a77adaab3a25de0a57d36b219d3c30a98c3d9b6932b5755fbd73c15b3141"}, "docker": "quay.io/biocontainers/gfatools", "aliases": {"gfatools": "/usr/local/bin/gfatools", "paf2gfa": "/usr/local/bin/paf2gfa"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gfatools.
shpc-registry automated BioContainers addition for gfatools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gfatools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gfatools:0.5--h577a1d6_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gfatools/0.5--h577a1d6_5
$ module help quay.io/biocontainers/gfatools/0.5--h577a1d6_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gfatools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gfatools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gfatools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gfatools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gfatools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gfatools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gfatools

```bash
$ singularity exec <container> /usr/local/bin/gfatools
$ podman run --it --rm --entrypoint /usr/local/bin/gfatools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfatools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paf2gfa

```bash
$ singularity exec <container> /usr/local/bin/paf2gfa
$ podman run --it --rm --entrypoint /usr/local/bin/paf2gfa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paf2gfa   -v ${PWD} -w ${PWD} <container> -c " $@"
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
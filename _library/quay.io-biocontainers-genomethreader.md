---
layout: container
name:  "quay.io/biocontainers/genomethreader"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/genomethreader/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/genomethreader/container.yaml"
updated_at: "2024-06-04 03:15:43.305563"
latest: "1.7.1--hdbdd923_6"
container_url: "https://biocontainers.pro/tools/genomethreader"
aliases:
 - "gth"
 - "gthclean.sh"
 - "gthcleanrec.sh"
 - "gthconsensus"
 - "gthfilestat"
 - "gthgetseq"
 - "gthsplit"
 - "gthsplit2dim.sh"
versions:
 - "1.7.1--h87f3376_4"
 - "1.7.1--hdbdd923_6"
description: "shpc-registry automated BioContainers addition for genomethreader"
config: {"url": "https://biocontainers.pro/tools/genomethreader", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for genomethreader", "latest": {"1.7.1--hdbdd923_6": "sha256:589ce1701c351f4e40a1dcf9ac4894ab6b65444bd17d3e78ec1f55c4c53bf20e"}, "tags": {"1.7.1--h87f3376_4": "sha256:7b18c7d28f81a7ffbe7c864c7130a896fb6bf887347a212d5feb3d1dbf33bcb2", "1.7.1--hdbdd923_6": "sha256:589ce1701c351f4e40a1dcf9ac4894ab6b65444bd17d3e78ec1f55c4c53bf20e"}, "docker": "quay.io/biocontainers/genomethreader", "aliases": {"gth": "/usr/local/bin/gth", "gthclean.sh": "/usr/local/bin/gthclean.sh", "gthcleanrec.sh": "/usr/local/bin/gthcleanrec.sh", "gthconsensus": "/usr/local/bin/gthconsensus", "gthfilestat": "/usr/local/bin/gthfilestat", "gthgetseq": "/usr/local/bin/gthgetseq", "gthsplit": "/usr/local/bin/gthsplit", "gthsplit2dim.sh": "/usr/local/bin/gthsplit2dim.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/genomethreader.
shpc-registry automated BioContainers addition for genomethreader
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/genomethreader
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/genomethreader:1.7.1--hdbdd923_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/genomethreader/1.7.1--hdbdd923_6
$ module help quay.io/biocontainers/genomethreader/1.7.1--hdbdd923_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### genomethreader-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### genomethreader-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### genomethreader-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### genomethreader-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### genomethreader-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### genomethreader-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gth

```bash
$ singularity exec <container> /usr/local/bin/gth
$ podman run --it --rm --entrypoint /usr/local/bin/gth   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gth   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gthclean.sh

```bash
$ singularity exec <container> /usr/local/bin/gthclean.sh
$ podman run --it --rm --entrypoint /usr/local/bin/gthclean.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gthclean.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gthcleanrec.sh

```bash
$ singularity exec <container> /usr/local/bin/gthcleanrec.sh
$ podman run --it --rm --entrypoint /usr/local/bin/gthcleanrec.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gthcleanrec.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gthconsensus

```bash
$ singularity exec <container> /usr/local/bin/gthconsensus
$ podman run --it --rm --entrypoint /usr/local/bin/gthconsensus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gthconsensus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gthfilestat

```bash
$ singularity exec <container> /usr/local/bin/gthfilestat
$ podman run --it --rm --entrypoint /usr/local/bin/gthfilestat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gthfilestat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gthgetseq

```bash
$ singularity exec <container> /usr/local/bin/gthgetseq
$ podman run --it --rm --entrypoint /usr/local/bin/gthgetseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gthgetseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gthsplit

```bash
$ singularity exec <container> /usr/local/bin/gthsplit
$ podman run --it --rm --entrypoint /usr/local/bin/gthsplit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gthsplit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gthsplit2dim.sh

```bash
$ singularity exec <container> /usr/local/bin/gthsplit2dim.sh
$ podman run --it --rm --entrypoint /usr/local/bin/gthsplit2dim.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gthsplit2dim.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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
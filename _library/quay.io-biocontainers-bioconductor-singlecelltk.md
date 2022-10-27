---
layout: container
name:  "quay.io/biocontainers/bioconductor-singlecelltk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-singlecelltk/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-singlecelltk/container.yaml"
updated_at: "2022-10-27 00:21:55.911731"
latest: "2.4.0--r41hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-singlecelltk"
aliases:
 - ".bioconductor-celldex-post-link.sh"
 - ".bioconductor-celldex-pre-unlink.sh"
 - ".bioconductor-gsvadata-post-link.sh"
 - ".bioconductor-gsvadata-pre-unlink.sh"
 - ".bioconductor-hgu95a.db-post-link.sh"
 - ".bioconductor-hgu95a.db-pre-unlink.sh"
 - ".bioconductor-scrnaseq-post-link.sh"
 - ".bioconductor-scrnaseq-pre-unlink.sh"
 - ".bioconductor-tenxpbmcdata-post-link.sh"
 - ".bioconductor-tenxpbmcdata-pre-unlink.sh"
versions:
 - "2.4.0--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-singlecelltk"
config: {"url": "https://biocontainers.pro/tools/bioconductor-singlecelltk", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-singlecelltk", "latest": {"2.4.0--r41hdfd78af_0": "sha256:56fed3da5c6d8756dc1f7fe7fa9b904bf2ca44c31c286d4dd37a46c993e847df"}, "tags": {"2.4.0--r41hdfd78af_0": "sha256:56fed3da5c6d8756dc1f7fe7fa9b904bf2ca44c31c286d4dd37a46c993e847df"}, "docker": "quay.io/biocontainers/bioconductor-singlecelltk", "aliases": {".bioconductor-celldex-post-link.sh": "/usr/local/bin/.bioconductor-celldex-post-link.sh", ".bioconductor-celldex-pre-unlink.sh": "/usr/local/bin/.bioconductor-celldex-pre-unlink.sh", ".bioconductor-gsvadata-post-link.sh": "/usr/local/bin/.bioconductor-gsvadata-post-link.sh", ".bioconductor-gsvadata-pre-unlink.sh": "/usr/local/bin/.bioconductor-gsvadata-pre-unlink.sh", ".bioconductor-hgu95a.db-post-link.sh": "/usr/local/bin/.bioconductor-hgu95a.db-post-link.sh", ".bioconductor-hgu95a.db-pre-unlink.sh": "/usr/local/bin/.bioconductor-hgu95a.db-pre-unlink.sh", ".bioconductor-scrnaseq-post-link.sh": "/usr/local/bin/.bioconductor-scrnaseq-post-link.sh", ".bioconductor-scrnaseq-pre-unlink.sh": "/usr/local/bin/.bioconductor-scrnaseq-pre-unlink.sh", ".bioconductor-tenxpbmcdata-post-link.sh": "/usr/local/bin/.bioconductor-tenxpbmcdata-post-link.sh", ".bioconductor-tenxpbmcdata-pre-unlink.sh": "/usr/local/bin/.bioconductor-tenxpbmcdata-pre-unlink.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-singlecelltk.
shpc-registry automated BioContainers addition for bioconductor-singlecelltk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-singlecelltk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-singlecelltk:2.4.0--r41hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-singlecelltk/2.4.0--r41hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-singlecelltk/2.4.0--r41hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-singlecelltk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-singlecelltk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-singlecelltk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-singlecelltk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-singlecelltk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-singlecelltk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .bioconductor-celldex-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-celldex-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-celldex-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-celldex-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-celldex-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-celldex-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-celldex-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-celldex-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-gsvadata-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-gsvadata-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-gsvadata-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-gsvadata-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-gsvadata-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-gsvadata-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-gsvadata-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-gsvadata-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-hgu95a.db-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-hgu95a.db-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-hgu95a.db-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-hgu95a.db-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-hgu95a.db-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-hgu95a.db-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-hgu95a.db-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-hgu95a.db-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-scrnaseq-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-scrnaseq-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-scrnaseq-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-scrnaseq-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-scrnaseq-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-scrnaseq-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-scrnaseq-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-scrnaseq-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-tenxpbmcdata-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-tenxpbmcdata-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-tenxpbmcdata-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-tenxpbmcdata-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-tenxpbmcdata-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-tenxpbmcdata-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-tenxpbmcdata-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-tenxpbmcdata-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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
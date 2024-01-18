---
layout: container
name:  "quay.io/biocontainers/pbwt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pbwt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pbwt/container.yaml"
updated_at: "2024-01-18 02:33:25.004801"
latest: "3.0--h6141fd1_9"
container_url: "https://biocontainers.pro/tools/pbwt"
aliases:
 - "pbwt"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "3.0--hb0d9459_7"
 - "3.0--hc88714e_8"
 - "3.0--h6141fd1_9"
description: "shpc-registry automated BioContainers addition for pbwt"
config: {"url": "https://biocontainers.pro/tools/pbwt", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pbwt", "latest": {"3.0--h6141fd1_9": "sha256:9d3ac9ea8f38d6b755a052f38cc6450c8342ebdd1fff42b9e65b2c094f156ca9"}, "tags": {"3.0--hb0d9459_7": "sha256:7bb9e6d57c8010f3f6c654f0f67aad48f43db3e1dcdb2cf71f3414f67126ef75", "3.0--hc88714e_8": "sha256:0da5d9e94130efdc90cd02ecaca856a0d9ed9cf4ae02d268c60bfce65d663a6a", "3.0--h6141fd1_9": "sha256:9d3ac9ea8f38d6b755a052f38cc6450c8342ebdd1fff42b9e65b2c094f156ca9"}, "docker": "quay.io/biocontainers/pbwt", "aliases": {"pbwt": "/usr/local/bin/pbwt", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pbwt.
shpc-registry automated BioContainers addition for pbwt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pbwt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pbwt:3.0--h6141fd1_9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pbwt/3.0--h6141fd1_9
$ module help quay.io/biocontainers/pbwt/3.0--h6141fd1_9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pbwt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pbwt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pbwt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pbwt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pbwt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pbwt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pbwt

```bash
$ singularity exec <container> /usr/local/bin/pbwt
$ podman run --it --rm --entrypoint /usr/local/bin/pbwt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbwt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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
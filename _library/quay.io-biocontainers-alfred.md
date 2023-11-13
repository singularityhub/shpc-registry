---
layout: container
name:  "quay.io/biocontainers/alfred"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/alfred/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/alfred/container.yaml"
updated_at: "2023-11-13 02:46:09.575105"
latest: "0.2.7--hd8a7f93_2"
container_url: "https://biocontainers.pro/tools/alfred"
aliases:
 - "alfred"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.2.6--ha41ced6_1"
 - "0.2.6--h2af1cb8_2"
 - "0.2.7--h96c1cfd_0"
 - "0.2.7--hd8a7f93_2"
description: "shpc-registry automated BioContainers addition for alfred"
config: {"url": "https://biocontainers.pro/tools/alfred", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for alfred", "latest": {"0.2.7--hd8a7f93_2": "sha256:de55488ae9fe185437ac57dc506d47f135efdc0bb6bf54fa064963309ac5a07e"}, "tags": {"0.2.6--ha41ced6_1": "sha256:f5421a70045aed56fa245214c31ad2a121160121e2d7b4f8230371c03e98fa51", "0.2.6--h2af1cb8_2": "sha256:187d8576ef798284c6047b2346ca42d88332b0953b0be7b8bc983ef386fbb7ef", "0.2.7--h96c1cfd_0": "sha256:f329e3cd2271dc595d3fb7c2b0ca935c9ce893e50a0f193831dd31679bf30443", "0.2.7--hd8a7f93_2": "sha256:de55488ae9fe185437ac57dc506d47f135efdc0bb6bf54fa064963309ac5a07e"}, "docker": "quay.io/biocontainers/alfred", "aliases": {"alfred": "/usr/local/bin/alfred", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/alfred.
shpc-registry automated BioContainers addition for alfred
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/alfred
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/alfred:0.2.7--hd8a7f93_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/alfred/0.2.7--hd8a7f93_2
$ module help quay.io/biocontainers/alfred/0.2.7--hd8a7f93_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### alfred-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### alfred-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### alfred-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### alfred-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### alfred-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### alfred-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### alfred

```bash
$ singularity exec <container> /usr/local/bin/alfred
$ podman run --it --rm --entrypoint /usr/local/bin/alfred   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alfred   -v ${PWD} -w ${PWD} <container> -c " $@"
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
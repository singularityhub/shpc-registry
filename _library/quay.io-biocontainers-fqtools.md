---
layout: container
name:  "quay.io/biocontainers/fqtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fqtools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fqtools/container.yaml"
updated_at: "2024-01-06 02:32:29.463903"
latest: "2.0--h6141fd1_12"
container_url: "https://biocontainers.pro/tools/fqtools"
aliases:
 - "fqtools"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "2.0--h6233b05_9"
 - "2.0--hb0d9459_10"
 - "2.0--hc88714e_11"
 - "2.0--h6141fd1_12"
description: "shpc-registry automated BioContainers addition for fqtools"
config: {"url": "https://biocontainers.pro/tools/fqtools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fqtools", "latest": {"2.0--h6141fd1_12": "sha256:4dd3e5cd351498433db5ea6f7e369e91e21dc518c8ef06a9c864e35c52cb111b"}, "tags": {"2.0--h6233b05_9": "sha256:63710e23819216691604b249a89cb54957d02ec0446b458c6964fc5d4e87e0eb", "2.0--hb0d9459_10": "sha256:390708c9dca3cd02d36f6acde16bed1699b405c4a4de6680aa85eba74b1d7b8d", "2.0--hc88714e_11": "sha256:35f340a42e631f8bf049cb222bcbb66cd70746ae20d1546d17fb26ab7bab57c9", "2.0--h6141fd1_12": "sha256:4dd3e5cd351498433db5ea6f7e369e91e21dc518c8ef06a9c864e35c52cb111b"}, "docker": "quay.io/biocontainers/fqtools", "aliases": {"fqtools": "/usr/local/bin/fqtools", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fqtools.
shpc-registry automated BioContainers addition for fqtools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fqtools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fqtools:2.0--h6141fd1_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fqtools/2.0--h6141fd1_12
$ module help quay.io/biocontainers/fqtools/2.0--h6141fd1_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fqtools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fqtools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fqtools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fqtools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fqtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fqtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fqtools

```bash
$ singularity exec <container> /usr/local/bin/fqtools
$ podman run --it --rm --entrypoint /usr/local/bin/fqtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fqtools   -v ${PWD} -w ${PWD} <container> -c " $@"
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
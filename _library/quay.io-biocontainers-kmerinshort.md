---
layout: container
name:  "quay.io/biocontainers/kmerinshort"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kmerinshort/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kmerinshort/container.yaml"
updated_at: "2023-03-30 03:32:39.084167"
latest: "1.0.1--0"
container_url: "https://biocontainers.pro/tools/kmerinshort"
aliases:
 - "KmerInShort"
versions:
 - "1.0.1--0"
description: "shpc-registry automated BioContainers addition for kmerinshort"
config: {"url": "https://biocontainers.pro/tools/kmerinshort", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kmerinshort", "latest": {"1.0.1--0": "sha256:056e3de6174c48a7b342c8f91541896c39d2e30a64e62d62e51ae43227c36278"}, "tags": {"1.0.1--0": "sha256:056e3de6174c48a7b342c8f91541896c39d2e30a64e62d62e51ae43227c36278"}, "docker": "quay.io/biocontainers/kmerinshort", "aliases": {"KmerInShort": "/usr/local/bin/KmerInShort"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kmerinshort.
shpc-registry automated BioContainers addition for kmerinshort
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kmerinshort
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kmerinshort:1.0.1--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kmerinshort/1.0.1--0
$ module help quay.io/biocontainers/kmerinshort/1.0.1--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kmerinshort-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kmerinshort-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kmerinshort-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kmerinshort-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kmerinshort-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kmerinshort-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### KmerInShort

```bash
$ singularity exec <container> /usr/local/bin/KmerInShort
$ podman run --it --rm --entrypoint /usr/local/bin/KmerInShort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/KmerInShort   -v ${PWD} -w ${PWD} <container> -c " $@"
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
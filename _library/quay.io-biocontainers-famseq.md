---
layout: container
name:  "quay.io/biocontainers/famseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/famseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/famseq/container.yaml"
updated_at: "2023-05-10 02:33:59.888191"
latest: "1.0.3--h9f5acd7_4"
container_url: "https://biocontainers.pro/tools/famseq"
aliases:
 - "FamSeq"
versions:
 - "1.0.3--h9f5acd7_4"
description: "shpc-registry automated BioContainers addition for famseq"
config: {"url": "https://biocontainers.pro/tools/famseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for famseq", "latest": {"1.0.3--h9f5acd7_4": "sha256:e5dd767e9ebc277efc6bc621b15a7d792298a7d0ee57a2c6409c03a0197ff564"}, "tags": {"1.0.3--h9f5acd7_4": "sha256:e5dd767e9ebc277efc6bc621b15a7d792298a7d0ee57a2c6409c03a0197ff564"}, "docker": "quay.io/biocontainers/famseq", "aliases": {"FamSeq": "/usr/local/bin/FamSeq"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/famseq.
shpc-registry automated BioContainers addition for famseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/famseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/famseq:1.0.3--h9f5acd7_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/famseq/1.0.3--h9f5acd7_4
$ module help quay.io/biocontainers/famseq/1.0.3--h9f5acd7_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### famseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### famseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### famseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### famseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### famseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### famseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### FamSeq

```bash
$ singularity exec <container> /usr/local/bin/FamSeq
$ podman run --it --rm --entrypoint /usr/local/bin/FamSeq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FamSeq   -v ${PWD} -w ${PWD} <container> -c " $@"
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
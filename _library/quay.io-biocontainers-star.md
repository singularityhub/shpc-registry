---
layout: container
name:  "quay.io/biocontainers/star"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/star/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/star/container.yaml"
updated_at: "2024-02-17 02:53:13.780469"
latest: "2.7.11a--h0033a41_0"
container_url: "https://biocontainers.pro/tools/star"
aliases:
 - "STAR"
versions:
 - "2.7.10a--h9ee0642_0"
 - "2.7.10b--h6b7c446_1"
 - "2.7.11a--h0033a41_0"
description: "shpc-registry automated BioContainers addition for star"
config: {"url": "https://biocontainers.pro/tools/star", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for star", "latest": {"2.7.11a--h0033a41_0": "sha256:91530a1e0a30d859645f075fbdb4bf73e2a92c3e2b890e154dfbee4b3f3356a4"}, "tags": {"2.7.10a--h9ee0642_0": "sha256:8e4a22498462f54b924cec7dd28dc53b3f277b736497e7105036f63361aad1f4", "2.7.10b--h6b7c446_1": "sha256:99c71999731d3d66581a689641bca050a646076c9d85748cb4420d070dd73fc5", "2.7.11a--h0033a41_0": "sha256:91530a1e0a30d859645f075fbdb4bf73e2a92c3e2b890e154dfbee4b3f3356a4"}, "docker": "quay.io/biocontainers/star", "aliases": {"STAR": "/usr/local/bin/STAR"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/star.
shpc-registry automated BioContainers addition for star
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/star
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/star:2.7.11a--h0033a41_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/star/2.7.11a--h0033a41_0
$ module help quay.io/biocontainers/star/2.7.11a--h0033a41_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### star-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### star-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### star-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### star-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### star-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### star-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### STAR

```bash
$ singularity exec <container> /usr/local/bin/STAR
$ podman run --it --rm --entrypoint /usr/local/bin/STAR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STAR   -v ${PWD} -w ${PWD} <container> -c " $@"
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
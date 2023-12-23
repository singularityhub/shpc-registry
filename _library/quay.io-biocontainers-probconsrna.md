---
layout: container
name:  "quay.io/biocontainers/probconsrna"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/probconsrna/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/probconsrna/container.yaml"
updated_at: "2023-12-23 03:04:24.565249"
latest: "1.10--h9f5acd7_3"
container_url: "https://biocontainers.pro/tools/probconsrna"
aliases:
 - "probconsRNA"
versions:
 - "1.10--h9f5acd7_2"
 - "1.10--h9f5acd7_3"
description: "shpc-registry automated BioContainers addition for probconsrna"
config: {"url": "https://biocontainers.pro/tools/probconsrna", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for probconsrna", "latest": {"1.10--h9f5acd7_3": "sha256:e1a08a1ef6de014c8fb949d3eb4adfe8ca44ede30817c8a9dbcc8b30e9b74647"}, "tags": {"1.10--h9f5acd7_2": "sha256:6377f2f6ee7bf2a440a33e2de61e6d6533647cea8c369810c8d13d993e87f1a2", "1.10--h9f5acd7_3": "sha256:e1a08a1ef6de014c8fb949d3eb4adfe8ca44ede30817c8a9dbcc8b30e9b74647"}, "docker": "quay.io/biocontainers/probconsrna", "aliases": {"probconsRNA": "/usr/local/bin/probconsRNA"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/probconsrna.
shpc-registry automated BioContainers addition for probconsrna
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/probconsrna
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/probconsrna:1.10--h9f5acd7_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/probconsrna/1.10--h9f5acd7_3
$ module help quay.io/biocontainers/probconsrna/1.10--h9f5acd7_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### probconsrna-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### probconsrna-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### probconsrna-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### probconsrna-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### probconsrna-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### probconsrna-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### probconsRNA

```bash
$ singularity exec <container> /usr/local/bin/probconsRNA
$ podman run --it --rm --entrypoint /usr/local/bin/probconsRNA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/probconsRNA   -v ${PWD} -w ${PWD} <container> -c " $@"
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
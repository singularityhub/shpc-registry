---
layout: container
name:  "quay.io/biocontainers/peptide-shaker"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/peptide-shaker/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/peptide-shaker/container.yaml"
updated_at: "2022-10-27 01:15:20.209702"
latest: "1.16.4--py27_0"
container_url: "https://biocontainers.pro/tools/peptide-shaker"
aliases:
 - "peptide-shaker"
versions:
 - "1.16.4--py27_0"
description: "shpc-registry automated BioContainers addition for peptide-shaker"
config: {"url": "https://biocontainers.pro/tools/peptide-shaker", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for peptide-shaker", "latest": {"1.16.4--py27_0": "sha256:1ee91304befdc6a6b3573eadfd25ff59ec64f4f08c909b0e95a3edfa4e3d0617"}, "tags": {"1.16.4--py27_0": "sha256:1ee91304befdc6a6b3573eadfd25ff59ec64f4f08c909b0e95a3edfa4e3d0617"}, "docker": "quay.io/biocontainers/peptide-shaker", "aliases": {"peptide-shaker": "/usr/local/bin/peptide-shaker"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/peptide-shaker.
shpc-registry automated BioContainers addition for peptide-shaker
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/peptide-shaker
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/peptide-shaker:1.16.4--py27_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/peptide-shaker/1.16.4--py27_0
$ module help quay.io/biocontainers/peptide-shaker/1.16.4--py27_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### peptide-shaker-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### peptide-shaker-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### peptide-shaker-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### peptide-shaker-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### peptide-shaker-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### peptide-shaker-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### peptide-shaker

```bash
$ singularity exec <container> /usr/local/bin/peptide-shaker
$ podman run --it --rm --entrypoint /usr/local/bin/peptide-shaker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/peptide-shaker   -v ${PWD} -w ${PWD} <container> -c " $@"
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
---
layout: container
name:  "quay.io/biocontainers/rfmix"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rfmix/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rfmix/container.yaml"
updated_at: "2024-01-17 03:13:58.019851"
latest: "2.03.r0.9505bfa--hdbdd923_5"
container_url: "https://biocontainers.pro/tools/rfmix"
aliases:
 - "rfmix"
 - "simulate"
versions:
 - "2.03.r0.9505bfa--h87f3376_3"
 - "2.03.r0.9505bfa--hdbdd923_5"
description: "shpc-registry automated BioContainers addition for rfmix"
config: {"url": "https://biocontainers.pro/tools/rfmix", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rfmix", "latest": {"2.03.r0.9505bfa--hdbdd923_5": "sha256:b2c59b85ebe24f9518ae88aa1e6364184da5da4d5941e238d5bc404d64d452d8"}, "tags": {"2.03.r0.9505bfa--h87f3376_3": "sha256:d86bf897af37bd05d4b933597ee9e6b07117e76d946f65439986f0a5609eb005", "2.03.r0.9505bfa--hdbdd923_5": "sha256:b2c59b85ebe24f9518ae88aa1e6364184da5da4d5941e238d5bc404d64d452d8"}, "docker": "quay.io/biocontainers/rfmix", "aliases": {"rfmix": "/usr/local/bin/rfmix", "simulate": "/usr/local/bin/simulate"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rfmix.
shpc-registry automated BioContainers addition for rfmix
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rfmix
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rfmix:2.03.r0.9505bfa--hdbdd923_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rfmix/2.03.r0.9505bfa--hdbdd923_5
$ module help quay.io/biocontainers/rfmix/2.03.r0.9505bfa--hdbdd923_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rfmix-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rfmix-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rfmix-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rfmix-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rfmix-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rfmix-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rfmix

```bash
$ singularity exec <container> /usr/local/bin/rfmix
$ podman run --it --rm --entrypoint /usr/local/bin/rfmix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rfmix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simulate

```bash
$ singularity exec <container> /usr/local/bin/simulate
$ podman run --it --rm --entrypoint /usr/local/bin/simulate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simulate   -v ${PWD} -w ${PWD} <container> -c " $@"
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
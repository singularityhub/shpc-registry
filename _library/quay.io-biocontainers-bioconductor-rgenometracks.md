---
layout: container
name:  "quay.io/biocontainers/bioconductor-rgenometracks"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rgenometracks/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rgenometracks/container.yaml"
updated_at: "2025-01-19 03:09:28.133894"
latest: "1.12.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rgenometracks"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.12.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rgenometracks"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rgenometracks", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rgenometracks", "latest": {"1.12.0--r44hdfd78af_0": "sha256:84850e766bc595e2ad953c6976e09099f5d978e3f59180030ea2beed71ed6eb4"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:e5d3c687d59af5894c636267cc0b423a2d97c7583aa876e96ee32e69ffd9f790", "1.4.0--r42hdfd78af_0": "sha256:8f1439ea42c2d6539c0112a752fe6578e522eea0e2cc0bed0e579347af694dfc", "1.6.0--r43hdfd78af_0": "sha256:f2ce043730bc1bfcd4e80acb1e6c5e6c58193bbe9951239a5c14202860677923", "1.8.0--r43hdfd78af_0": "sha256:f275c2e4026ac17b5e47576ef67386291662912934d05caf1795c7a09c0e7745", "1.12.0--r44hdfd78af_0": "sha256:84850e766bc595e2ad953c6976e09099f5d978e3f59180030ea2beed71ed6eb4"}, "docker": "quay.io/biocontainers/bioconductor-rgenometracks"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rgenometracks.
shpc-registry automated BioContainers addition for bioconductor-rgenometracks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rgenometracks
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rgenometracks:1.12.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rgenometracks/1.12.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rgenometracks/1.12.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rgenometracks-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rgenometracks-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rgenometracks-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rgenometracks-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rgenometracks-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rgenometracks-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rgenometracks

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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
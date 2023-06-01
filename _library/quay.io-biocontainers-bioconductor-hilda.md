---
layout: container
name:  "quay.io/biocontainers/bioconductor-hilda"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hilda/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hilda/container.yaml"
updated_at: "2023-06-01 03:46:58.092881"
latest: "1.12.0--r42hf17093f_1"
container_url: "https://biocontainers.pro/tools/bioconductor-hilda"
aliases:
 - "jags"
versions:
 - "1.8.0--r41hc247a5b_2"
 - "1.12.0--r42hc247a5b_0"
 - "1.12.0--r42hf17093f_1"
description: "shpc-registry automated BioContainers addition for bioconductor-hilda"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hilda", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hilda", "latest": {"1.12.0--r42hf17093f_1": "sha256:2d183dc032e991c60a18cb5a997f049d2a30c87e390162e1eec0ab564113cf1c"}, "tags": {"1.8.0--r41hc247a5b_2": "sha256:e046c215a105ac93a409fc6292321bdcaad87c5c9e4fe8c47b58e0e30652414a", "1.12.0--r42hc247a5b_0": "sha256:6e244037e7e6563d1d1ca446f82e0a0fbbf4b36f2e2daf731dd93b4d072c42fd", "1.12.0--r42hf17093f_1": "sha256:2d183dc032e991c60a18cb5a997f049d2a30c87e390162e1eec0ab564113cf1c"}, "docker": "quay.io/biocontainers/bioconductor-hilda", "aliases": {"jags": "/usr/local/bin/jags"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hilda.
shpc-registry automated BioContainers addition for bioconductor-hilda
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hilda
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hilda:1.12.0--r42hf17093f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hilda/1.12.0--r42hf17093f_1
$ module help quay.io/biocontainers/bioconductor-hilda/1.12.0--r42hf17093f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hilda-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hilda-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hilda-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hilda-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hilda-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hilda-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### jags

```bash
$ singularity exec <container> /usr/local/bin/jags
$ podman run --it --rm --entrypoint /usr/local/bin/jags   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jags   -v ${PWD} -w ${PWD} <container> -c " $@"
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
---
layout: container
name:  "quay.io/biocontainers/bioconductor-epivizrstandalone"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-epivizrstandalone/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-epivizrstandalone/container.yaml"
updated_at: "2022-11-09 00:36:43.789327"
latest: "1.8.0--r351_0"
container_url: "https://biocontainers.pro/tools/bioconductor-epivizrstandalone"
aliases:
 - "wget"
versions:
 - "1.8.0--r351_0"
description: "shpc-registry automated BioContainers addition for bioconductor-epivizrstandalone"
config: {"url": "https://biocontainers.pro/tools/bioconductor-epivizrstandalone", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-epivizrstandalone", "latest": {"1.8.0--r351_0": "sha256:647b84e1a04542840a1e57d3c1a7970b6b4be62f2c37eb393a8a004a87951183"}, "tags": {"1.8.0--r351_0": "sha256:647b84e1a04542840a1e57d3c1a7970b6b4be62f2c37eb393a8a004a87951183"}, "docker": "quay.io/biocontainers/bioconductor-epivizrstandalone", "aliases": {"wget": "/usr/local/bin/wget"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-epivizrstandalone.
shpc-registry automated BioContainers addition for bioconductor-epivizrstandalone
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-epivizrstandalone
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-epivizrstandalone:1.8.0--r351_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-epivizrstandalone/1.8.0--r351_0
$ module help quay.io/biocontainers/bioconductor-epivizrstandalone/1.8.0--r351_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-epivizrstandalone-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-epivizrstandalone-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-epivizrstandalone-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-epivizrstandalone-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-epivizrstandalone-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-epivizrstandalone-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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
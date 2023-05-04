---
layout: container
name:  "quay.io/biocontainers/bioconductor-singler"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-singler/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-singler/container.yaml"
updated_at: "2023-05-04 02:49:57.333726"
latest: "2.0.0--r42hc247a5b_0"
container_url: "https://biocontainers.pro/tools/bioconductor-singler"

versions:
 - "1.8.1--r41hc247a5b_1"
 - "2.0.0--r42hc247a5b_0"
description: "shpc-registry automated BioContainers addition for bioconductor-singler"
config: {"url": "https://biocontainers.pro/tools/bioconductor-singler", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-singler", "latest": {"2.0.0--r42hc247a5b_0": "sha256:5e594b755c2c673ab61134db3e70de49b03166df100ead8bf0cf2e793ebacaf5"}, "tags": {"1.8.1--r41hc247a5b_1": "sha256:975b3f41bd94a141dcce611a08c76bfde66df15e9ae466360fe5faa750ace46c", "2.0.0--r42hc247a5b_0": "sha256:5e594b755c2c673ab61134db3e70de49b03166df100ead8bf0cf2e793ebacaf5"}, "docker": "quay.io/biocontainers/bioconductor-singler"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-singler.
shpc-registry automated BioContainers addition for bioconductor-singler
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-singler
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-singler:2.0.0--r42hc247a5b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-singler/2.0.0--r42hc247a5b_0
$ module help quay.io/biocontainers/bioconductor-singler/2.0.0--r42hc247a5b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-singler-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-singler-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-singler-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-singler-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-singler-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-singler-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-singler

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
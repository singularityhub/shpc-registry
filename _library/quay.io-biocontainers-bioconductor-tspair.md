---
layout: container
name:  "quay.io/biocontainers/bioconductor-tspair"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tspair/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tspair/container.yaml"
updated_at: "2026-01-06 04:02:27.101051"
latest: "1.52.0--r41hc0cfd56_2"
container_url: "https://biocontainers.pro/tools/bioconductor-tspair"

versions:
 - "1.52.0--r41hc0cfd56_2"
description: "shpc-registry automated BioContainers addition for bioconductor-tspair"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tspair", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tspair", "latest": {"1.52.0--r41hc0cfd56_2": "sha256:f9fa00157be67a4c8b8fe04fe2ec2c058ea8a8792cc3848894168a9293f15e44"}, "tags": {"1.52.0--r41hc0cfd56_2": "sha256:f9fa00157be67a4c8b8fe04fe2ec2c058ea8a8792cc3848894168a9293f15e44"}, "docker": "quay.io/biocontainers/bioconductor-tspair"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tspair.
shpc-registry automated BioContainers addition for bioconductor-tspair
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tspair
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tspair:1.52.0--r41hc0cfd56_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tspair/1.52.0--r41hc0cfd56_2
$ module help quay.io/biocontainers/bioconductor-tspair/1.52.0--r41hc0cfd56_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tspair-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tspair-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tspair-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tspair-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tspair-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tspair-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tspair

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
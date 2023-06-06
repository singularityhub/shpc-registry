---
layout: container
name:  "quay.io/biocontainers/bioconductor-puma"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-puma/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-puma/container.yaml"
updated_at: "2023-06-06 03:40:29.879716"
latest: "3.40.0--r42ha9d7317_1"
container_url: "https://biocontainers.pro/tools/bioconductor-puma"

versions:
 - "3.36.0--r41hc0cfd56_2"
 - "3.40.0--r42hc0cfd56_0"
 - "3.40.0--r42ha9d7317_1"
description: "shpc-registry automated BioContainers addition for bioconductor-puma"
config: {"url": "https://biocontainers.pro/tools/bioconductor-puma", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-puma", "latest": {"3.40.0--r42ha9d7317_1": "sha256:b1a92ff98d5a46b34edfa2941a7abfef10b906b496a61ca1001169c8d89fbd1e"}, "tags": {"3.36.0--r41hc0cfd56_2": "sha256:77f41aba9551cad89fe3cc372ff9d7e376f8613e293edc58201cc3a31e964578", "3.40.0--r42hc0cfd56_0": "sha256:dad776e858c2d9f8f42b660cd0c79d52f83f2508d2c5882733b78f239a9a1a6d", "3.40.0--r42ha9d7317_1": "sha256:b1a92ff98d5a46b34edfa2941a7abfef10b906b496a61ca1001169c8d89fbd1e"}, "docker": "quay.io/biocontainers/bioconductor-puma"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-puma.
shpc-registry automated BioContainers addition for bioconductor-puma
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-puma
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-puma:3.40.0--r42ha9d7317_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-puma/3.40.0--r42ha9d7317_1
$ module help quay.io/biocontainers/bioconductor-puma/3.40.0--r42ha9d7317_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-puma-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-puma-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-puma-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-puma-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-puma-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-puma-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-puma

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
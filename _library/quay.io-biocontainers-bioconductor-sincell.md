---
layout: container
name:  "quay.io/biocontainers/bioconductor-sincell"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sincell/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sincell/container.yaml"
updated_at: "2023-03-18 02:45:02.382116"
latest: "1.30.0--r42hc247a5b_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sincell"
aliases:
 - "glpsol"
versions:
 - "1.26.0--r41hc247a5b_2"
 - "1.30.0--r42hc247a5b_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sincell"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sincell", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sincell", "latest": {"1.30.0--r42hc247a5b_0": "sha256:30f35c52d0aa9dbd975842fedaae58183221afd3dedeef05fd6d5d09c6c80936"}, "tags": {"1.26.0--r41hc247a5b_2": "sha256:a09c3465a040bc9e6e0c205e2efb52bc769f7ab2bc6c124f906fd50737db2124", "1.30.0--r42hc247a5b_0": "sha256:30f35c52d0aa9dbd975842fedaae58183221afd3dedeef05fd6d5d09c6c80936"}, "docker": "quay.io/biocontainers/bioconductor-sincell", "aliases": {"glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sincell.
shpc-registry automated BioContainers addition for bioconductor-sincell
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sincell
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sincell:1.30.0--r42hc247a5b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sincell/1.30.0--r42hc247a5b_0
$ module help quay.io/biocontainers/bioconductor-sincell/1.30.0--r42hc247a5b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sincell-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sincell-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sincell-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sincell-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sincell-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sincell-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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
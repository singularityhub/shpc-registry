---
layout: container
name:  "quay.io/biocontainers/bioconductor-mmpalatemirna"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mmpalatemirna/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mmpalatemirna/container.yaml"
updated_at: "2022-10-27 01:02:33.970858"
latest: "1.37.0--r40_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mmpalatemirna"

versions:
 - "1.37.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mmpalatemirna"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mmpalatemirna", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mmpalatemirna", "latest": {"1.37.0--r40_0": "sha256:7eb07695862c38f956934344d94074a5903b580834e67e464ef76cf7b5221609"}, "tags": {"1.37.0--r40_0": "sha256:7eb07695862c38f956934344d94074a5903b580834e67e464ef76cf7b5221609"}, "docker": "quay.io/biocontainers/bioconductor-mmpalatemirna"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mmpalatemirna.
shpc-registry automated BioContainers addition for bioconductor-mmpalatemirna
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mmpalatemirna
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mmpalatemirna:1.37.0--r40_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mmpalatemirna/1.37.0--r40_0
$ module help quay.io/biocontainers/bioconductor-mmpalatemirna/1.37.0--r40_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mmpalatemirna-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mmpalatemirna-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mmpalatemirna-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mmpalatemirna-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mmpalatemirna-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mmpalatemirna-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mmpalatemirna

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
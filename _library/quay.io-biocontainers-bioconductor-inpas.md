---
layout: container
name:  "quay.io/biocontainers/bioconductor-inpas"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-inpas/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-inpas/container.yaml"
updated_at: "2024-09-22 03:08:54.085996"
latest: "2.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-inpas"

versions:
 - "2.2.0--r41hdfd78af_0"
 - "2.6.0--r42hdfd78af_0"
 - "2.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-inpas"
config: {"url": "https://biocontainers.pro/tools/bioconductor-inpas", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-inpas", "latest": {"2.8.0--r43hdfd78af_0": "sha256:c492a2d8feb80f0e1980e32b1610ad3a140f239ebeab61229be4656f571a4c11"}, "tags": {"2.2.0--r41hdfd78af_0": "sha256:8e2d2e3418f6fcb41c346f34e119cf85284816ec3468b9c7d62fa4a347299b9c", "2.6.0--r42hdfd78af_0": "sha256:2be17c4f4f35aeeffdefde5d0bacba0b7d9e5fdcbf2b6a302efe59624d55ffc4", "2.8.0--r43hdfd78af_0": "sha256:c492a2d8feb80f0e1980e32b1610ad3a140f239ebeab61229be4656f571a4c11"}, "docker": "quay.io/biocontainers/bioconductor-inpas"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-inpas.
shpc-registry automated BioContainers addition for bioconductor-inpas
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-inpas
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-inpas:2.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-inpas/2.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-inpas/2.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-inpas-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-inpas-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-inpas-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-inpas-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-inpas-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-inpas-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-inpas

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
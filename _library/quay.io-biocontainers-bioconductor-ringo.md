---
layout: container
name:  "quay.io/biocontainers/bioconductor-ringo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ringo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ringo/container.yaml"
updated_at: "2025-08-26 03:11:25.129908"
latest: "1.66.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ringo"

versions:
 - "1.58.0--r41hc247a5b_2"
 - "1.62.0--r42hc247a5b_0"
 - "1.62.0--r42hf17093f_1"
 - "1.64.0--r43hf17093f_0"
 - "1.66.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ringo"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ringo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ringo", "latest": {"1.66.0--r43hf17093f_0": "sha256:88562c01c4824b671b578349d7400817fcd13262e1ce01eadf4fb073b9bc0e51"}, "tags": {"1.58.0--r41hc247a5b_2": "sha256:8f603485d5b697eaddf87c843a3178ab7755af338d54320b8497a15555be81b8", "1.62.0--r42hc247a5b_0": "sha256:021f05a4eb178943a1b1ce1477b4edf5b6bf1898e8968bbd276ca1c1a15f2455", "1.62.0--r42hf17093f_1": "sha256:53b0f8204c500f93926b92691a369cba901db0abedce20457ab4980e0e00fbe1", "1.64.0--r43hf17093f_0": "sha256:664ad1ca10445aa099849b93dd0867b35c21b11c4942bcd877a78732d72f427c", "1.66.0--r43hf17093f_0": "sha256:88562c01c4824b671b578349d7400817fcd13262e1ce01eadf4fb073b9bc0e51"}, "docker": "quay.io/biocontainers/bioconductor-ringo"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ringo.
shpc-registry automated BioContainers addition for bioconductor-ringo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ringo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ringo:1.66.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ringo/1.66.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-ringo/1.66.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ringo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ringo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ringo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ringo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ringo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ringo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ringo

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
---
layout: container
name:  "quay.io/biocontainers/bioconductor-fishpond"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-fishpond/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-fishpond/container.yaml"
updated_at: "2024-01-11 02:52:02.205875"
latest: "2.6.2--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-fishpond"

versions:
 - "2.0.1--r41hc247a5b_1"
 - "2.4.0--r42hdfd78af_0"
 - "2.6.2--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-fishpond"
config: {"url": "https://biocontainers.pro/tools/bioconductor-fishpond", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-fishpond", "latest": {"2.6.2--r43hdfd78af_0": "sha256:58d7f84aad34a6a7d9b6fa19bd2b87b4a126c0d172758778f1463baf67d332d9"}, "tags": {"2.0.1--r41hc247a5b_1": "sha256:16356fe078eb835b961a12cfa226a28d26d9fd8cd7e300fa4da0198b51acf89c", "2.4.0--r42hdfd78af_0": "sha256:6e2a764e61c28f52fcfc4ffd20c112d6b490244113c423fafc5fc7bd5c33ebf3", "2.6.2--r43hdfd78af_0": "sha256:58d7f84aad34a6a7d9b6fa19bd2b87b4a126c0d172758778f1463baf67d332d9"}, "docker": "quay.io/biocontainers/bioconductor-fishpond"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-fishpond.
shpc-registry automated BioContainers addition for bioconductor-fishpond
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-fishpond
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-fishpond:2.6.2--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-fishpond/2.6.2--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-fishpond/2.6.2--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-fishpond-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fishpond-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fishpond-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-fishpond-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-fishpond-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-fishpond-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-fishpond

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
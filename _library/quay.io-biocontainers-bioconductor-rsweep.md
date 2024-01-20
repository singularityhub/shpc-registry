---
layout: container
name:  "quay.io/biocontainers/bioconductor-rsweep"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rsweep/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rsweep/container.yaml"
updated_at: "2024-01-20 02:33:05.100935"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rsweep"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rsweep"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rsweep", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rsweep", "latest": {"1.14.0--r43hdfd78af_0": "sha256:ce01e91cdb41dcb2d767d57e069529722a4ae97cf5b3cd176afcbaf1a5715bc9"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:7c73f2f4899d32f930b6ba4fbc24d29dbed46cd12e11208f3bd3e95984bce978", "1.10.0--r42hdfd78af_0": "sha256:3749ca4e28251ea7015c326214faba69e887c488e37cb82791f86d8f541575c9", "1.12.0--r43hdfd78af_0": "sha256:9ca16be396bc98a3f2cb8b7f97628729032baffa0f8642aa5a858cb77a82dbdd", "1.14.0--r43hdfd78af_0": "sha256:ce01e91cdb41dcb2d767d57e069529722a4ae97cf5b3cd176afcbaf1a5715bc9"}, "docker": "quay.io/biocontainers/bioconductor-rsweep"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rsweep.
shpc-registry automated BioContainers addition for bioconductor-rsweep
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rsweep
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rsweep:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rsweep/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rsweep/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rsweep-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rsweep-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rsweep-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rsweep-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rsweep-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rsweep-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rsweep

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
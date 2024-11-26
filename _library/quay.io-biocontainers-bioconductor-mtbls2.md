---
layout: container
name:  "quay.io/biocontainers/bioconductor-mtbls2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mtbls2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mtbls2/container.yaml"
updated_at: "2024-11-26 03:18:40.152856"
latest: "1.32.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mtbls2"

versions:
 - "1.24.0--r41hdfd78af_1"
 - "1.27.0--r42hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mtbls2"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mtbls2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mtbls2", "latest": {"1.32.0--r43hdfd78af_0": "sha256:a9921a49d99b6ede93de8e5946b3b0c5b19af49949ef39521528be7b35e2afa1"}, "tags": {"1.24.0--r41hdfd78af_1": "sha256:5ead4a41a3a83906366dc0c1c4701007e406f6755902dfacba38dc9936146244", "1.27.0--r42hdfd78af_0": "sha256:c071c5387e096b47589cbd34184e15945b25deb471ce89c8b1e17ab60d104ba2", "1.30.0--r43hdfd78af_0": "sha256:66fe897b13a3f18124cfe67a2e637f04e919b721f765f19350cac62ae6221c80", "1.32.0--r43hdfd78af_0": "sha256:a9921a49d99b6ede93de8e5946b3b0c5b19af49949ef39521528be7b35e2afa1"}, "docker": "quay.io/biocontainers/bioconductor-mtbls2"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mtbls2.
shpc-registry automated BioContainers addition for bioconductor-mtbls2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mtbls2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mtbls2:1.32.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mtbls2/1.32.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mtbls2/1.32.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mtbls2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mtbls2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mtbls2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mtbls2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mtbls2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mtbls2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mtbls2

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
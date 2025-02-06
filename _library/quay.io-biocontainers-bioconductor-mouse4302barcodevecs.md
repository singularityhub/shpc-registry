---
layout: container
name:  "quay.io/biocontainers/bioconductor-mouse4302barcodevecs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mouse4302barcodevecs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mouse4302barcodevecs/container.yaml"
updated_at: "2025-02-06 03:02:18.931690"
latest: "1.44.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mouse4302barcodevecs"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.35.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.44.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mouse4302barcodevecs"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mouse4302barcodevecs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mouse4302barcodevecs", "latest": {"1.44.0--r44hdfd78af_0": "sha256:a2c6562eca149866dcce128e09f0675efaf635c2d0bfa6d14b6ee06df405d948"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:8cc27544dd1919b5126545af2b56f4ee8c4d5b74edc7cc0bb5a33cace25c930d", "1.35.0--r42hdfd78af_0": "sha256:fa66abbf48cb27283fb6d681b8d4e126381ca712d1e8ffd36af9ffcc97ec6bc1", "1.38.0--r43hdfd78af_0": "sha256:8d0c3a30eafd661c4f0af493397d65d0fab572ffd3752a0be0a0104a58d9f972", "1.40.0--r43hdfd78af_0": "sha256:3558dbf49ffb5f8971c57456f90f14eb76ea277c278713c828e5b5738c4d7272", "1.44.0--r44hdfd78af_0": "sha256:a2c6562eca149866dcce128e09f0675efaf635c2d0bfa6d14b6ee06df405d948"}, "docker": "quay.io/biocontainers/bioconductor-mouse4302barcodevecs"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mouse4302barcodevecs.
shpc-registry automated BioContainers addition for bioconductor-mouse4302barcodevecs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mouse4302barcodevecs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mouse4302barcodevecs:1.44.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mouse4302barcodevecs/1.44.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mouse4302barcodevecs/1.44.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mouse4302barcodevecs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mouse4302barcodevecs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mouse4302barcodevecs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mouse4302barcodevecs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mouse4302barcodevecs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mouse4302barcodevecs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mouse4302barcodevecs

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
---
layout: container
name:  "quay.io/biocontainers/bioconductor-pcan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pcan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pcan/container.yaml"
updated_at: "2024-03-28 02:50:19.091514"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pcan"

versions:
 - "1.8.0--r351_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r40hdfd78af_1"
 - "1.16.0--r40_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pcan"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pcan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pcan", "latest": {"1.30.0--r43hdfd78af_0": "sha256:20892624fb2f5c870ad796f8a1a621709963d5e18d6ce7db6aec361525305ad9"}, "tags": {"1.8.0--r351_0": "sha256:8a6805edbc77d7a895b9365cf3553bcb622282814805a2f4e84447be6f05a4df", "1.26.0--r42hdfd78af_0": "sha256:77978c99b81f65c91b92150e219f7500af57a408a0218fc352173cfa7b6d461c", "1.22.0--r41hdfd78af_0": "sha256:197c22bfed5e491dcbf880004704c078b9accd13a82e9e097ea88c066a9f1ac7", "1.20.0--r41hdfd78af_0": "sha256:ac4c9b35a2198c53aa8b704934f66c9c8f1fdb4fed6688eb4c371c8ff9b82fd4", "1.18.0--r40hdfd78af_1": "sha256:9c049b50776ea9d9fe3b739068c1fe9da814328070b9f638599044429f8ada5c", "1.16.0--r40_0": "sha256:b652cba9cd6f789e3b3a669183eea3d997da910d8eec17cae3486e3e9fde98a6", "1.28.0--r43hdfd78af_0": "sha256:6b466ca6c39605b3d296dbddee21a32e10666a22f6fc24da970c958eb772446f", "1.30.0--r43hdfd78af_0": "sha256:20892624fb2f5c870ad796f8a1a621709963d5e18d6ce7db6aec361525305ad9"}, "docker": "quay.io/biocontainers/bioconductor-pcan"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pcan.
shpc-registry automated BioContainers addition for bioconductor-pcan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pcan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pcan:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pcan/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pcan/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pcan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pcan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pcan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pcan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pcan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pcan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-pcan

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
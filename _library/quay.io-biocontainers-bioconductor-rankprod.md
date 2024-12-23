---
layout: container
name:  "quay.io/biocontainers/bioconductor-rankprod"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rankprod/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rankprod/container.yaml"
updated_at: "2024-12-23 03:31:00.366974"
latest: "3.32.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rankprod"

versions:
 - "3.8.0--r351_0"
 - "3.24.0--r42hdfd78af_0"
 - "3.20.0--r41hdfd78af_0"
 - "3.18.0--r41hdfd78af_0"
 - "3.16.0--r40hdfd78af_1"
 - "3.14.0--r40_0"
 - "3.26.0--r43hdfd78af_0"
 - "3.28.0--r43hdfd78af_0"
 - "3.32.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rankprod"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rankprod", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rankprod", "latest": {"3.32.0--r44hdfd78af_0": "sha256:3e0796e9dd8ea17c6c381fc3afac98c27dce4601b2bbfadb23ea92b991179c24"}, "tags": {"3.8.0--r351_0": "sha256:81b558de4430f097f5f8fbb380db046f9691b9bcd2e0c7944ee73b22b98438e1", "3.24.0--r42hdfd78af_0": "sha256:2efe64732ac923bff952677a0ade57e5e0ebb8c1052c956c58356ac17f46a9cf", "3.20.0--r41hdfd78af_0": "sha256:3319f7d21416a961432ebb7c53727c4b57f5e19153ecc303258da27829cc86cf", "3.18.0--r41hdfd78af_0": "sha256:0207736b0528cf55f465e32f0bb38e29e745c06dc37b04777652960e9215756c", "3.16.0--r40hdfd78af_1": "sha256:dd719bd9751b2857b21ef92213a50d1d8a2c3462a33326434b752d803f65cf6a", "3.14.0--r40_0": "sha256:c6f7f945d00a580a0760e036c2731f9647b0b3bd445645e4ec0886170b9d2e73", "3.26.0--r43hdfd78af_0": "sha256:6d7db716e3d22e9a976836c6d661ce47dd2879c5daa52036b11959f90dc7deb0", "3.28.0--r43hdfd78af_0": "sha256:23cb4b52c498a7f4410de81ef403e4e589bc39681cedc64efcb89c37d77a423e", "3.32.0--r44hdfd78af_0": "sha256:3e0796e9dd8ea17c6c381fc3afac98c27dce4601b2bbfadb23ea92b991179c24"}, "docker": "quay.io/biocontainers/bioconductor-rankprod"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rankprod.
shpc-registry automated BioContainers addition for bioconductor-rankprod
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rankprod
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rankprod:3.32.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rankprod/3.32.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rankprod/3.32.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rankprod-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rankprod-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rankprod-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rankprod-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rankprod-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rankprod-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rankprod

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
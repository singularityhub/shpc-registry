---
layout: container
name:  "quay.io/biocontainers/bioconductor-asics"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-asics/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-asics/container.yaml"
updated_at: "2024-03-25 03:09:12.408813"
latest: "2.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-asics"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "2.8.0--r41hdfd78af_0"
 - "2.14.0--r42hdfd78af_0"
 - "2.10.0--r41hdfd78af_0"
 - "2.16.0--r43hdfd78af_0"
 - "2.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-asics"
config: {"url": "https://biocontainers.pro/tools/bioconductor-asics", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-asics", "latest": {"2.18.0--r43hdfd78af_0": "sha256:d2950cbd9b189087f4c44b46b8081ff66092c3714ec0b81ad351f3bfbe7cd453"}, "tags": {"2.8.0--r41hdfd78af_0": "sha256:a60ab0f921e328cf0fec906822a08f52c6d94d2c8ddb640bc53480b1b46a7a58", "2.14.0--r42hdfd78af_0": "sha256:2a4b748e72f3a54e608402063ab9ab9ff4630ea63b43204c0b3c4c8335eb4559", "2.10.0--r41hdfd78af_0": "sha256:6474301cfe4fa2c3e78e978056ddeb0705d44068df6b027b1447188e94586970", "2.16.0--r43hdfd78af_0": "sha256:f35c2ab0040941f0c3e7a4ab0ce325e939897fe118f5e7c191d317df2b79a13d", "2.18.0--r43hdfd78af_0": "sha256:d2950cbd9b189087f4c44b46b8081ff66092c3714ec0b81ad351f3bfbe7cd453"}, "docker": "quay.io/biocontainers/bioconductor-asics", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-asics.
shpc-registry automated BioContainers addition for bioconductor-asics
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-asics
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-asics:2.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-asics/2.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-asics/2.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-asics-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-asics-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-asics-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-asics-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-asics-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-asics-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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
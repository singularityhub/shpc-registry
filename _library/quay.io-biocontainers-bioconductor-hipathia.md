---
layout: container
name:  "quay.io/biocontainers/bioconductor-hipathia"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hipathia/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hipathia/container.yaml"
updated_at: "2023-02-23 03:16:28.805587"
latest: "2.14.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-hipathia"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "2.8.0--r41hdfd78af_0"
 - "2.10.0--r41hdfd78af_0"
 - "2.14.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-hipathia"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hipathia", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hipathia", "latest": {"2.14.0--r42hdfd78af_0": "sha256:11b75a66656a73bad2a1937b3c48ae7324c7a554d5d76d32779056657b6b9afc"}, "tags": {"2.8.0--r41hdfd78af_0": "sha256:380c13f6b01b78ab19ba86f7e94643bbb4eddb4328009d209d52ddead94d5c28", "2.10.0--r41hdfd78af_0": "sha256:dbebc41e22d18f18bd94b65ff3f54a40100ea02835452ed764eec1afebf770c3", "2.14.0--r42hdfd78af_0": "sha256:11b75a66656a73bad2a1937b3c48ae7324c7a554d5d76d32779056657b6b9afc"}, "docker": "quay.io/biocontainers/bioconductor-hipathia", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hipathia.
shpc-registry automated BioContainers addition for bioconductor-hipathia
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hipathia
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hipathia:2.14.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hipathia/2.14.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-hipathia/2.14.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hipathia-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hipathia-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hipathia-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hipathia-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hipathia-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hipathia-inspect-deffile:

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
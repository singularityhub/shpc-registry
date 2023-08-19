---
layout: container
name:  "quay.io/biocontainers/bioconductor-xvector"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-xvector/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-xvector/container.yaml"
updated_at: "2023-08-19 03:08:44.838609"
latest: "0.40.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-xvector"

versions:
 - "0.34.0--r41hc0cfd56_2"
 - "0.38.0--r42hc0cfd56_0"
 - "0.38.0--r42ha9d7317_1"
 - "0.40.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-xvector"
config: {"url": "https://biocontainers.pro/tools/bioconductor-xvector", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-xvector", "latest": {"0.40.0--r43ha9d7317_0": "sha256:af59873c0d7855e6372204ee64ee4d7f84d1898370af12dccff6d6eb042b23b9"}, "tags": {"0.34.0--r41hc0cfd56_2": "sha256:0d5fa322944c3a1c44b9c19cb5c5f817666a438f3abc6c1c6d99671ec26ae39c", "0.38.0--r42hc0cfd56_0": "sha256:72131b05741c1ec091bc34e0d6d709f7315ae09b5c674b597d492cfa89ed3623", "0.38.0--r42ha9d7317_1": "sha256:ec58e9a9766ad375e50cd29687ff49c7adac9bf23e5cdd623c8366b24fb04fdc", "0.40.0--r43ha9d7317_0": "sha256:af59873c0d7855e6372204ee64ee4d7f84d1898370af12dccff6d6eb042b23b9"}, "docker": "quay.io/biocontainers/bioconductor-xvector"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-xvector.
shpc-registry automated BioContainers addition for bioconductor-xvector
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-xvector
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-xvector:0.40.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-xvector/0.40.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-xvector/0.40.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-xvector-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-xvector-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-xvector-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-xvector-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-xvector-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-xvector-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-xvector

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
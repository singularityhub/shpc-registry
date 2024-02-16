---
layout: container
name:  "quay.io/biocontainers/bioconductor-gcsscore"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gcsscore/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gcsscore/container.yaml"
updated_at: "2024-02-16 02:24:25.335210"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gcsscore"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gcsscore"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gcsscore", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gcsscore", "latest": {"1.14.0--r43hdfd78af_0": "sha256:64dcd9609d608d562f88ae123e5a9da689f7051634194ecfeca4d3fce8e9df21"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:73528548613d36b1c4bdba34b3da925040ebe8195830fb79a076a3941218cd4e", "1.12.0--r42hdfd78af_0": "sha256:d196102813b69b4a910531b14b4aaee7e9eb5960cf5816c3d6542d5271b312f8", "1.14.0--r43hdfd78af_0": "sha256:64dcd9609d608d562f88ae123e5a9da689f7051634194ecfeca4d3fce8e9df21"}, "docker": "quay.io/biocontainers/bioconductor-gcsscore"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gcsscore.
shpc-registry automated BioContainers addition for bioconductor-gcsscore
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gcsscore
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gcsscore:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gcsscore/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gcsscore/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gcsscore-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gcsscore-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gcsscore-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gcsscore-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gcsscore-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gcsscore-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gcsscore

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
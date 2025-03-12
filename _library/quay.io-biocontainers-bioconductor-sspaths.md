---
layout: container
name:  "quay.io/biocontainers/bioconductor-sspaths"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sspaths/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sspaths/container.yaml"
updated_at: "2025-03-12 03:17:09.370609"
latest: "1.20.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sspaths"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.20.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sspaths"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sspaths", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sspaths", "latest": {"1.20.0--r44hdfd78af_0": "sha256:0fa6db8c918840037b0ddc1127617480ba8aeb9c6f13099de11c61e0816b6c50"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:941229e821828b672531173483658d6f42180592b04c27707ef9e5a05dde0aad", "1.12.0--r42hdfd78af_0": "sha256:b66a13d563985da6922298b5d9e99d5619c886888302f67d1d402ea0ddf57d7d", "1.14.0--r43hdfd78af_0": "sha256:2fde753702e64f7bca31f512e86d7970b9dcb0f6174ac5a94a24668c0f8ff8ad", "1.16.0--r43hdfd78af_0": "sha256:a0b4c8452e4a9ffe767101d3436ee27724557d71c17857f17618d89797e8fba1", "1.20.0--r44hdfd78af_0": "sha256:0fa6db8c918840037b0ddc1127617480ba8aeb9c6f13099de11c61e0816b6c50"}, "docker": "quay.io/biocontainers/bioconductor-sspaths"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sspaths.
shpc-registry automated BioContainers addition for bioconductor-sspaths
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sspaths
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sspaths:1.20.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sspaths/1.20.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-sspaths/1.20.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sspaths-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sspaths-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sspaths-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sspaths-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sspaths-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sspaths-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-sspaths

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
---
layout: container
name:  "quay.io/biocontainers/bioconductor-nnnorm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-nnnorm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-nnnorm/container.yaml"
updated_at: "2024-03-25 03:06:28.442926"
latest: "2.66.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-nnnorm"

versions:
 - "2.58.0--r41hdfd78af_0"
 - "2.62.0--r42hdfd78af_0"
 - "2.64.0--r43hdfd78af_0"
 - "2.66.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-nnnorm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-nnnorm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-nnnorm", "latest": {"2.66.0--r43hdfd78af_0": "sha256:0e9f8a4d45ca53fc23f42d5074a3b45d10e3fb24757058407d5cb94be9ca1a10"}, "tags": {"2.58.0--r41hdfd78af_0": "sha256:29eb36c4803fa35a8b8e01df27562352af70510117960f26551fd09d9aa671ec", "2.62.0--r42hdfd78af_0": "sha256:3cb4cd6ac7de2ae4b4adc62972459f4c812b91b5a5e4ab309523b6e1673696b6", "2.64.0--r43hdfd78af_0": "sha256:aa1df4b4d4d248ccc0b9d85fdde851b890e4c450a7c47fb9a481e12af03e2168", "2.66.0--r43hdfd78af_0": "sha256:0e9f8a4d45ca53fc23f42d5074a3b45d10e3fb24757058407d5cb94be9ca1a10"}, "docker": "quay.io/biocontainers/bioconductor-nnnorm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-nnnorm.
shpc-registry automated BioContainers addition for bioconductor-nnnorm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-nnnorm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-nnnorm:2.66.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-nnnorm/2.66.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-nnnorm/2.66.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-nnnorm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nnnorm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nnnorm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-nnnorm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-nnnorm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-nnnorm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-nnnorm

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
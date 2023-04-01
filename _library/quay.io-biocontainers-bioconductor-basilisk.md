---
layout: container
name:  "quay.io/biocontainers/bioconductor-basilisk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-basilisk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-basilisk/container.yaml"
updated_at: "2023-04-01 03:11:12.022749"
latest: "1.10.2--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-basilisk"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.2--r42hdfd78af_0"
 - "1.9.12--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-basilisk"
config: {"url": "https://biocontainers.pro/tools/bioconductor-basilisk", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-basilisk", "latest": {"1.10.2--r42hdfd78af_0": "sha256:4bb0a9d93f833e2f8cb0cc6e52dbbccf28470626c98178e0abefe1b2f2d07bcd"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:5b39ad6bf15ce80d073c4628e2a4a8fef1b0128834688b27cb98becc172b179d", "1.10.2--r42hdfd78af_0": "sha256:4bb0a9d93f833e2f8cb0cc6e52dbbccf28470626c98178e0abefe1b2f2d07bcd", "1.9.12--r42hdfd78af_0": "sha256:d6cdc743a4284ba1de1e2be3effa70e5273fe2cc3349af6f797f1402372a12f4"}, "docker": "quay.io/biocontainers/bioconductor-basilisk"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-basilisk.
shpc-registry automated BioContainers addition for bioconductor-basilisk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-basilisk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-basilisk:1.10.2--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-basilisk/1.10.2--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-basilisk/1.10.2--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-basilisk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-basilisk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-basilisk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-basilisk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-basilisk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-basilisk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-basilisk

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
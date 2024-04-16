---
layout: container
name:  "quay.io/biocontainers/bioconductor-arrayquality"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-arrayquality/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-arrayquality/container.yaml"
updated_at: "2024-04-16 02:48:00.582898"
latest: "1.80.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-arrayquality"

versions:
 - "1.72.0--r41hdfd78af_0"
 - "1.76.0--r42hdfd78af_0"
 - "1.78.0--r43hdfd78af_0"
 - "1.80.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-arrayquality"
config: {"url": "https://biocontainers.pro/tools/bioconductor-arrayquality", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-arrayquality", "latest": {"1.80.0--r43hdfd78af_0": "sha256:48a580c9411dccd657d4530a5cdd3467f79271288b052f6577f0a86afca2bbba"}, "tags": {"1.72.0--r41hdfd78af_0": "sha256:8bd66fdac9aca46503289a4082916ffa13b77a4dc7716c7776a4eed9d0597286", "1.76.0--r42hdfd78af_0": "sha256:f8ef453e7bdcd88c5f433314f464b1b20368f663d297bb919a170eb5658688c8", "1.78.0--r43hdfd78af_0": "sha256:c3891f488169ed40929a06bfad55c12fa0b3233a377f8ba71aca9350ed75a0d1", "1.80.0--r43hdfd78af_0": "sha256:48a580c9411dccd657d4530a5cdd3467f79271288b052f6577f0a86afca2bbba"}, "docker": "quay.io/biocontainers/bioconductor-arrayquality"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-arrayquality.
shpc-registry automated BioContainers addition for bioconductor-arrayquality
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-arrayquality
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-arrayquality:1.80.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-arrayquality/1.80.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-arrayquality/1.80.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-arrayquality-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-arrayquality-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-arrayquality-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-arrayquality-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-arrayquality-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-arrayquality-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-arrayquality

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
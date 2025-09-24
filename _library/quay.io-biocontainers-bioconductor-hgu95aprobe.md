---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgu95aprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgu95aprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgu95aprobe/container.yaml"
updated_at: "2025-09-24 03:15:28.485446"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-hgu95aprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-hgu95aprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgu95aprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgu95aprobe", "latest": {"2.18.0--r44hdfd78af_13": "sha256:45374fa12b6fff0c4e1c4153498ea6eb08a935a500f63078203eaacb4f1e9fdf"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:a7eca36660a615e1429c1e32213176fc5d72d954c536578f301524a00cfa9e05", "2.18.0--r42hdfd78af_10": "sha256:0f3613fde4e50a77dd533c3569faa3b870ae0a779a026b91724be7524b5f6696", "2.18.0--r43hdfd78af_11": "sha256:95479ee9da4acec9493e81e5c3e7990ebe3a49fdb49d6035c0c8730bb65a12a7", "2.18.0--r43hdfd78af_12": "sha256:5c522c4e15a71dedd7cddf25998d2a42c66c856c68e9c2b11b8b32cbebdefbca", "2.18.0--r44hdfd78af_13": "sha256:45374fa12b6fff0c4e1c4153498ea6eb08a935a500f63078203eaacb4f1e9fdf"}, "docker": "quay.io/biocontainers/bioconductor-hgu95aprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgu95aprobe.
shpc-registry automated BioContainers addition for bioconductor-hgu95aprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu95aprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu95aprobe:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgu95aprobe/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-hgu95aprobe/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgu95aprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu95aprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu95aprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgu95aprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgu95aprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgu95aprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hgu95aprobe

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
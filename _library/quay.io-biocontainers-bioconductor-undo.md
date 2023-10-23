---
layout: container
name:  "quay.io/biocontainers/bioconductor-undo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-undo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-undo/container.yaml"
updated_at: "2023-10-23 02:52:13.502000"
latest: "1.42.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-undo"

versions:
 - "1.36.0--r41hdfd78af_0"
 - "1.40.0--r42hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-undo"
config: {"url": "https://biocontainers.pro/tools/bioconductor-undo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-undo", "latest": {"1.42.0--r43hdfd78af_0": "sha256:6836444f08ee172867ace677f7ad58da59090f974569fbc4932c224ea65e4c77"}, "tags": {"1.36.0--r41hdfd78af_0": "sha256:59829ff2fb8c48ae429a37d8cb98313fe7dbdbfe8435ab5a789adc611d1afc0c", "1.40.0--r42hdfd78af_0": "sha256:2024059b861d96c5c7e2398ef8e2c6de7227eaf5e7a0cbdf797299e9e9652753", "1.42.0--r43hdfd78af_0": "sha256:6836444f08ee172867ace677f7ad58da59090f974569fbc4932c224ea65e4c77"}, "docker": "quay.io/biocontainers/bioconductor-undo"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-undo.
shpc-registry automated BioContainers addition for bioconductor-undo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-undo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-undo:1.42.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-undo/1.42.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-undo/1.42.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-undo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-undo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-undo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-undo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-undo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-undo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-undo

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
---
layout: container
name:  "quay.io/biocontainers/bioconductor-verso"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-verso/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-verso/container.yaml"
updated_at: "2024-08-08 03:10:30.073271"
latest: "1.12.0--r43hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-verso"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-verso"
config: {"url": "https://biocontainers.pro/tools/bioconductor-verso", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-verso", "latest": {"1.12.0--r43hdfd78af_1": "sha256:9561e2ebb4b3da3cf0632eb24809b203b477bb13d6f71eb3adb8be9afd09f503"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:51a1d4fc455f787f00f1f6002c3e534d291926272cadfddb64a30a97515dfef7", "1.8.0--r42hdfd78af_0": "sha256:cf0a614d049e8756e577c7511ed85907cc6d03175828eab5b8ef32a07a72f837", "1.10.0--r43hdfd78af_0": "sha256:0f0c1b3510014a39424f4e34173830f469859344a48bf4e541955064ae5846d9", "1.12.0--r43hdfd78af_1": "sha256:9561e2ebb4b3da3cf0632eb24809b203b477bb13d6f71eb3adb8be9afd09f503"}, "docker": "quay.io/biocontainers/bioconductor-verso"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-verso.
shpc-registry automated BioContainers addition for bioconductor-verso
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-verso
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-verso:1.12.0--r43hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-verso/1.12.0--r43hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-verso/1.12.0--r43hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-verso-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-verso-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-verso-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-verso-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-verso-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-verso-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-verso

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
---
layout: container
name:  "quay.io/biocontainers/bioconductor-gwascat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gwascat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gwascat/container.yaml"
updated_at: "2024-05-13 02:58:45.704719"
latest: "2.34.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gwascat"

versions:
 - "2.26.0--r41hdfd78af_0"
 - "2.30.0--r42hdfd78af_0"
 - "2.32.0--r43hdfd78af_0"
 - "2.34.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gwascat"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gwascat", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gwascat", "latest": {"2.34.0--r43hdfd78af_0": "sha256:a48a97ca9e32e868d9a0713b0f1a623b0d6c6050798cf6e8a12234c2d830d3f8"}, "tags": {"2.26.0--r41hdfd78af_0": "sha256:8e41b2299d783021f0f4b1154580aecf34624358644c2ec50ba5085b6a1c4724", "2.30.0--r42hdfd78af_0": "sha256:c6522167541242cdf087237b420be6ee10c52d4b829bcd9649858336af866a14", "2.32.0--r43hdfd78af_0": "sha256:fb4b120ca6371d669a0b93c08a518928dcf964d3b146adc2a26ff965272cee1e", "2.34.0--r43hdfd78af_0": "sha256:a48a97ca9e32e868d9a0713b0f1a623b0d6c6050798cf6e8a12234c2d830d3f8"}, "docker": "quay.io/biocontainers/bioconductor-gwascat"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gwascat.
shpc-registry automated BioContainers addition for bioconductor-gwascat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gwascat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gwascat:2.34.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gwascat/2.34.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gwascat/2.34.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gwascat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gwascat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gwascat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gwascat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gwascat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gwascat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gwascat

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
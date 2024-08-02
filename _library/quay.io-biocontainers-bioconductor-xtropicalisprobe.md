---
layout: container
name:  "quay.io/biocontainers/bioconductor-xtropicalisprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-xtropicalisprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-xtropicalisprobe/container.yaml"
updated_at: "2024-08-02 02:56:46.275039"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-xtropicalisprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-xtropicalisprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-xtropicalisprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-xtropicalisprobe", "latest": {"2.18.0--r43hdfd78af_12": "sha256:83b28e9a7989c68a2a1b607e19190659a517e51aabe85ed70014fa01f73f527b"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:90fdb5003798999168126ca59c1dd4496e4534a72bc1bfef891f4a86d61f6977", "2.18.0--r42hdfd78af_10": "sha256:f0a6cc1986c9e203d520adcdaff4bba24c9e57e8d31701fc44336b917b6a03fe", "2.18.0--r43hdfd78af_11": "sha256:a251f2d4a82b7ca51fb532308f802ab1889f1be6b0d1ec703afbe8b373392793", "2.18.0--r43hdfd78af_12": "sha256:83b28e9a7989c68a2a1b607e19190659a517e51aabe85ed70014fa01f73f527b"}, "docker": "quay.io/biocontainers/bioconductor-xtropicalisprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-xtropicalisprobe.
shpc-registry automated BioContainers addition for bioconductor-xtropicalisprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-xtropicalisprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-xtropicalisprobe:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-xtropicalisprobe/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-xtropicalisprobe/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-xtropicalisprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-xtropicalisprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-xtropicalisprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-xtropicalisprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-xtropicalisprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-xtropicalisprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-xtropicalisprobe

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
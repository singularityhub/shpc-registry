---
layout: container
name:  "quay.io/biocontainers/bioconductor-u133x3pprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-u133x3pprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-u133x3pprobe/container.yaml"
updated_at: "2024-07-12 03:16:12.008710"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-u133x3pprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-u133x3pprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-u133x3pprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-u133x3pprobe", "latest": {"2.18.0--r43hdfd78af_12": "sha256:9cc87e39b4e99e2d79f8cef7212b14b70c75be1f9d43027b0daaab340b62d3aa"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:f86f0465972f0d01170f7028a9361f4e0c9e5aa1da45c72f13e3d14ec94d98c6", "2.18.0--r42hdfd78af_10": "sha256:d0ff40c9ca06a76fed9fc1704ca839a2fc74b06b6127e4b2a802c02d59ed28d8", "2.18.0--r43hdfd78af_11": "sha256:0d7db423d91fe3bf0ceb003ad840e0146618d37f1d331d9eb3d280f35388f30a", "2.18.0--r43hdfd78af_12": "sha256:9cc87e39b4e99e2d79f8cef7212b14b70c75be1f9d43027b0daaab340b62d3aa"}, "docker": "quay.io/biocontainers/bioconductor-u133x3pprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-u133x3pprobe.
shpc-registry automated BioContainers addition for bioconductor-u133x3pprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-u133x3pprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-u133x3pprobe:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-u133x3pprobe/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-u133x3pprobe/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-u133x3pprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-u133x3pprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-u133x3pprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-u133x3pprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-u133x3pprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-u133x3pprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-u133x3pprobe

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
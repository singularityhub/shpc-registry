---
layout: container
name:  "quay.io/biocontainers/bioconductor-rtopper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rtopper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rtopper/container.yaml"
updated_at: "2025-12-29 04:26:34.434505"
latest: "1.52.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rtopper"

versions:
 - "1.40.0--r41hdfd78af_0"
 - "1.44.0--r42hdfd78af_0"
 - "1.46.0--r43hdfd78af_0"
 - "1.48.0--r43hdfd78af_0"
 - "1.52.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rtopper"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rtopper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rtopper", "latest": {"1.52.0--r44hdfd78af_0": "sha256:0fb6ac669151c4afdfb064796051641d84b48a51e5edf789bcff717c650059d9"}, "tags": {"1.40.0--r41hdfd78af_0": "sha256:f919f93b0789c688f78313a37d5572c1abb9dbd35d305c20998e565d150a6c43", "1.44.0--r42hdfd78af_0": "sha256:689d12843900d1798cf159733a174caaeaed3fed97f2c85884a7fb11abb7c920", "1.46.0--r43hdfd78af_0": "sha256:eebf5ef9211ed020447aee6cf60358139990271cd7f5f6eec2bde79be6386dd9", "1.48.0--r43hdfd78af_0": "sha256:ee4c25f3378e8608536fffa6206da8acbfe50eb70e8f1d29298f9b9b6dc03b8b", "1.52.0--r44hdfd78af_0": "sha256:0fb6ac669151c4afdfb064796051641d84b48a51e5edf789bcff717c650059d9"}, "docker": "quay.io/biocontainers/bioconductor-rtopper"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rtopper.
shpc-registry automated BioContainers addition for bioconductor-rtopper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rtopper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rtopper:1.52.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rtopper/1.52.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rtopper/1.52.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rtopper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rtopper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rtopper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rtopper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rtopper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rtopper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rtopper

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
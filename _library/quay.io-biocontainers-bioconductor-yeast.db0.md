---
layout: container
name:  "quay.io/biocontainers/bioconductor-yeast.db0"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-yeast.db0/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-yeast.db0/container.yaml"
updated_at: "2025-12-01 04:05:48.356829"
latest: "3.20.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-yeast.db0"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "3.8.2--r36_1"
 - "3.16.0--r42hdfd78af_0"
 - "3.14.0--r41hdfd78af_1"
 - "3.13.0--r41hdfd78af_0"
 - "3.12.0--r40hdfd78af_1"
 - "3.11.2--r40_0"
 - "3.17.0--r43hdfd78af_0"
 - "3.18.0--r43hdfd78af_0"
 - "3.20.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-yeast.db0"
config: {"url": "https://biocontainers.pro/tools/bioconductor-yeast.db0", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-yeast.db0", "latest": {"3.20.0--r44hdfd78af_0": "sha256:6d9ad7d55e6bd76f66edf0e118d5aa9add67b91cbc0d5739b13a3af454a43cce"}, "tags": {"3.8.2--r36_1": "sha256:99c73eac7f81af831c9f4766d5825d2c4ea2591a38b0c21ffc5aba7478f66945", "3.16.0--r42hdfd78af_0": "sha256:cd148f84bab4e2035d62c1becb4f1a7df9423286494d277e36f3332b16debad1", "3.14.0--r41hdfd78af_1": "sha256:c6c03c528272d2d701b2dad2884e27fad6ff67e1d1887fa8c9c9b4fae2f72b4b", "3.13.0--r41hdfd78af_0": "sha256:cc64a87d6b81d5c672ad0a8b3732e793191cfe7519aa9fc128dc6fe6445f0832", "3.12.0--r40hdfd78af_1": "sha256:04c62750c4ec2972d40df1eed57600f9d3a1c8f27b1c2ef54a4b48e6d174b7dd", "3.11.2--r40_0": "sha256:cb4eeb62fa2be4439127a51f4988a29dea66e4706c45ac3f9afd7341374cecb9", "3.17.0--r43hdfd78af_0": "sha256:182e8a0f57164ba271ce87e6bc8fa0b29054a6d5d0a154da5c5e2a88bdd4973b", "3.18.0--r43hdfd78af_0": "sha256:1264806aa06cf1966e3377d50f5c3a18a12c7f3bd5311f212133c605e97f3be9", "3.20.0--r44hdfd78af_0": "sha256:6d9ad7d55e6bd76f66edf0e118d5aa9add67b91cbc0d5739b13a3af454a43cce"}, "docker": "quay.io/biocontainers/bioconductor-yeast.db0", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-yeast.db0.
shpc-registry automated BioContainers addition for bioconductor-yeast.db0
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-yeast.db0
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-yeast.db0:3.20.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-yeast.db0/3.20.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-yeast.db0/3.20.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-yeast.db0-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-yeast.db0-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-yeast.db0-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-yeast.db0-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-yeast.db0-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-yeast.db0-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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
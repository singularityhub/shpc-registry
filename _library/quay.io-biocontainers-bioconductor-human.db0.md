---
layout: container
name:  "quay.io/biocontainers/bioconductor-human.db0"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-human.db0/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-human.db0/container.yaml"
updated_at: "2024-03-06 02:25:15.462614"
latest: "3.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-human.db0"
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
description: "shpc-registry automated BioContainers addition for bioconductor-human.db0"
config: {"url": "https://biocontainers.pro/tools/bioconductor-human.db0", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-human.db0", "latest": {"3.18.0--r43hdfd78af_0": "sha256:40804bcbd225b7036b70df65a00dc8c7ade3847652e39bb1da07f84f5b56f3f8"}, "tags": {"3.8.2--r36_1": "sha256:f55f8d7a997962a5f6a26930877f12dd240ef610ddeb3ed82749f0e352bb52db", "3.16.0--r42hdfd78af_0": "sha256:5b4d4a90db5aaeb1091483103dc9a8076b58cc7cb63f3771cf9984377ce89ff9", "3.14.0--r41hdfd78af_1": "sha256:83788b09536821dbf14c5efd8ae8d4b90dc16513410034b11d73b05ac7b262ac", "3.13.0--r41hdfd78af_0": "sha256:38ca98e02bf92f4e0458938e2d63ef45763cc8cab3b0f9d9c82719ffc3548a05", "3.12.0--r40hdfd78af_1": "sha256:68ebf853fef54c88ad0c7057b77e4c1aff539f65c99a1583beebb361fa1e2f23", "3.11.2--r40_0": "sha256:5169f74689dddeccc9d93eef85bc67e6e96820485b6b216474b4722ed8fd8ad0", "3.17.0--r43hdfd78af_0": "sha256:420fe8f8910fdfa8152168b0073da8c6d90f41ff122ad3bc8a61d084bf3c571c", "3.18.0--r43hdfd78af_0": "sha256:40804bcbd225b7036b70df65a00dc8c7ade3847652e39bb1da07f84f5b56f3f8"}, "docker": "quay.io/biocontainers/bioconductor-human.db0", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-human.db0.
shpc-registry automated BioContainers addition for bioconductor-human.db0
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-human.db0
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-human.db0:3.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-human.db0/3.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-human.db0/3.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-human.db0-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-human.db0-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-human.db0-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-human.db0-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-human.db0-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-human.db0-inspect-deffile:

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
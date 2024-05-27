---
layout: container
name:  "quay.io/biocontainers/bioconductor-ndexr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ndexr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ndexr/container.yaml"
updated_at: "2024-05-27 03:18:35.504105"
latest: "1.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ndexr"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
 - "1.20.0--r42hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.1--r40hdfd78af_0"
 - "1.10.0--r40_0"
 - "1.22.0--r43hdfd78af_0"
 - "1.24.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ndexr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ndexr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ndexr", "latest": {"1.24.0--r43hdfd78af_0": "sha256:afaa69eac896debf3f000587c550f760636475da6dae327100cf9e0f5371deb8"}, "tags": {"1.8.0--r36_0": "sha256:4cd424f708975aa07e765954ca6a04323c48a4c5f8cd7b4cc1f443ee1960825e", "1.20.0--r42hdfd78af_0": "sha256:3ce31f98746d5f821203f15a226791561a2ddb28ea89dfc9f9fbcf9c120fbb62", "1.16.0--r41hdfd78af_0": "sha256:7807ad549277c802fbaef47acd89a80244b1d1c464711cd4567b4d5c2e78435d", "1.14.0--r41hdfd78af_0": "sha256:f816fe4904266e5f01fa73cba5296c6d43acdbd298304c9330e4e292ecf81655", "1.12.1--r40hdfd78af_0": "sha256:e64408d5f6084004faa04a10826c382192d8a2502bf1900cfd881ac6a840f741", "1.10.0--r40_0": "sha256:c27b56840cc44eddbb11c479002a9689d91da80ef130ec8b1899a3dd417ef79a", "1.22.0--r43hdfd78af_0": "sha256:1367642e581272483c80ce0aecee5cb86cb8c854e1a56f9fb1efd62218fc774c", "1.24.0--r43hdfd78af_0": "sha256:afaa69eac896debf3f000587c550f760636475da6dae327100cf9e0f5371deb8"}, "docker": "quay.io/biocontainers/bioconductor-ndexr", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ndexr.
shpc-registry automated BioContainers addition for bioconductor-ndexr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ndexr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ndexr:1.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ndexr/1.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ndexr/1.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ndexr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ndexr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ndexr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ndexr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ndexr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ndexr-inspect-deffile:

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
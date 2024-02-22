---
layout: container
name:  "quay.io/biocontainers/bioconductor-jaspar2020"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-jaspar2020/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-jaspar2020/container.yaml"
updated_at: "2024-02-22 04:42:11.905032"
latest: "0.99.10--r43hdfd78af_7"
container_url: "https://biocontainers.pro/tools/bioconductor-jaspar2020"

versions:
 - "0.99.10--r41hdfd78af_4"
 - "0.99.10--r42hdfd78af_5"
 - "0.99.10--r43hdfd78af_6"
 - "0.99.10--r43hdfd78af_7"
description: "shpc-registry automated BioContainers addition for bioconductor-jaspar2020"
config: {"url": "https://biocontainers.pro/tools/bioconductor-jaspar2020", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-jaspar2020", "latest": {"0.99.10--r43hdfd78af_7": "sha256:d6586e2994aad3e4a8af098e5194f27b3b433f4d660e3900254f637d1f480541"}, "tags": {"0.99.10--r41hdfd78af_4": "sha256:0ce7d0582f5ff3b87b857cdc05d14373bc93cd14f80406f29c5851f952c0de6d", "0.99.10--r42hdfd78af_5": "sha256:f0589285f0dc193fe82043013297cb58f160abdadb41404aea23137eec21c923", "0.99.10--r43hdfd78af_6": "sha256:dff8fc78f54ec060c593b16ed0228d334718c9f0c26ddc9592ab8afa85959ec0", "0.99.10--r43hdfd78af_7": "sha256:d6586e2994aad3e4a8af098e5194f27b3b433f4d660e3900254f637d1f480541"}, "docker": "quay.io/biocontainers/bioconductor-jaspar2020"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-jaspar2020.
shpc-registry automated BioContainers addition for bioconductor-jaspar2020
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-jaspar2020
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-jaspar2020:0.99.10--r43hdfd78af_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-jaspar2020/0.99.10--r43hdfd78af_7
$ module help quay.io/biocontainers/bioconductor-jaspar2020/0.99.10--r43hdfd78af_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-jaspar2020-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-jaspar2020-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-jaspar2020-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-jaspar2020-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-jaspar2020-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-jaspar2020-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-jaspar2020

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
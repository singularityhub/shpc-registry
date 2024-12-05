---
layout: container
name:  "quay.io/biocontainers/bioconductor-coveb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-coveb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-coveb/container.yaml"
updated_at: "2024-12-05 03:36:09.738215"
latest: "1.28.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-coveb"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.1--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-coveb"
config: {"url": "https://biocontainers.pro/tools/bioconductor-coveb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-coveb", "latest": {"1.28.0--r43hdfd78af_0": "sha256:3bd5a1155a4fea93577297ea13b4185961500e68b7d3cf3bbf1c60ee12a3f10a"}, "tags": {"1.8.1--r351_0": "sha256:b64f0f261733ca9d882eb91e2dd83decd673960360b3d57d8a3e3ab85ccabcfa", "1.24.0--r42hdfd78af_0": "sha256:e609a80f7bd9588c484da9766cbb0c492012de05616059533fda818b3a1f3d69", "1.20.0--r41hdfd78af_0": "sha256:11046a4e221b55515bf1d7fd539b5d6c868c4a873bb3d11bc122faa1f726f2df", "1.18.0--r41hdfd78af_0": "sha256:e32a47bbda2a2841030846ada74fc10ae56a9e0fad34d741b89d2f34afd6f0f6", "1.16.0--r40hdfd78af_1": "sha256:88e7ad6fd22207bf0bf9a41f1df685256b016e7d4e98e654fd54ff4b3564932e", "1.14.0--r40_0": "sha256:adc1dc61cc822a28ef6cfaf2eb2bf4b749e559ee51f5cb3a68ac5d793b7252c7", "1.26.0--r43hdfd78af_0": "sha256:265770ca4840ff5ce0e4ac0d2739e8d9be8c9ba279aa01a829c5193731232526", "1.28.0--r43hdfd78af_0": "sha256:3bd5a1155a4fea93577297ea13b4185961500e68b7d3cf3bbf1c60ee12a3f10a"}, "docker": "quay.io/biocontainers/bioconductor-coveb", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-coveb.
shpc-registry automated BioContainers addition for bioconductor-coveb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-coveb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-coveb:1.28.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-coveb/1.28.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-coveb/1.28.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-coveb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-coveb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-coveb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-coveb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-coveb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-coveb-inspect-deffile:

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
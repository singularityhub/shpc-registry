---
layout: container
name:  "quay.io/biocontainers/bioconductor-scale4c"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scale4c/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scale4c/container.yaml"
updated_at: "2025-10-22 03:34:28.439394"
latest: "1.28.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scale4c"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.0--r40hdfd78af_1"
 - "1.10.0--r40_0"
 - "1.20.0--r42hdfd78af_0"
 - "1.22.0--r43hdfd78af_0"
 - "1.24.0--r43hdfd78af_0"
 - "1.28.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-scale4c"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scale4c", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scale4c", "latest": {"1.28.0--r44hdfd78af_0": "sha256:a781ac56c9e1400d0c4c9d88f4916de579493a00acab0a11456a2543de41f943"}, "tags": {"1.8.0--r36_0": "sha256:64b075eeaa1607853e9c21d9d240ccde4289d772b3edd76691493765fbe68bea", "1.16.0--r41hdfd78af_0": "sha256:5a54ccb85d28b5eddf9f17fd87bef283bf68cc8507129691c057dc5d2cca4c72", "1.14.0--r41hdfd78af_0": "sha256:aadf465dbd20470b70acaf7d879b7627adb2a3f84f406377879fe18e11ae3271", "1.12.0--r40hdfd78af_1": "sha256:e847fdac70cd3c69f7179f89828096a92aa33b35e79fa52172a1182de51bb17c", "1.10.0--r40_0": "sha256:5e49fb0cd007219f87670e1621b0cd8a06f135b450a4b6346b431a27229338b0", "1.20.0--r42hdfd78af_0": "sha256:eed36875605304332b460b611d1c309bb4f0fc4647dfeafb7273b619e43a6b44", "1.22.0--r43hdfd78af_0": "sha256:afc47d86695dd19addf39082ba0fceeef20eea5537c4d699e81ff3e47cee5dbf", "1.24.0--r43hdfd78af_0": "sha256:65115a70c1c6390e0175525801f3f35a12e65643a8ccae4fa11bab311b87644f", "1.28.0--r44hdfd78af_0": "sha256:a781ac56c9e1400d0c4c9d88f4916de579493a00acab0a11456a2543de41f943"}, "docker": "quay.io/biocontainers/bioconductor-scale4c", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scale4c.
shpc-registry automated BioContainers addition for bioconductor-scale4c
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scale4c
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scale4c:1.28.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scale4c/1.28.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-scale4c/1.28.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scale4c-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scale4c-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scale4c-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scale4c-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scale4c-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scale4c-inspect-deffile:

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
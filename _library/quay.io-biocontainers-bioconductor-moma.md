---
layout: container
name:  "quay.io/biocontainers/bioconductor-moma"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-moma/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-moma/container.yaml"
updated_at: "2025-05-08 05:23:35.553003"
latest: "1.18.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-moma"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.18.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-moma"
config: {"url": "https://biocontainers.pro/tools/bioconductor-moma", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-moma", "latest": {"1.18.0--r44hdfd78af_0": "sha256:8ddcae908ae5cd96f7eec0ed651d1637de1c5c7bd049eb68d1189ced09fafad6"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:0c03fb25867e4db9793ac1a482b4eff5763b1f2e7de898dc5029c506a907b249", "1.10.0--r42hdfd78af_0": "sha256:279ed54eb9ac3a77f5cadd3b566a02185b5f1f348ed7d3b16c25258e1da4c79e", "1.12.0--r43hdfd78af_0": "sha256:bd52815817771338a979143108e7a8a04dd07062a1204e4cb5fc1f732ea35771", "1.14.0--r43hdfd78af_0": "sha256:ef269cc2aad76e2fe9d434545584dda51462c3b0bcde3f7115550db37c24167d", "1.18.0--r44hdfd78af_0": "sha256:8ddcae908ae5cd96f7eec0ed651d1637de1c5c7bd049eb68d1189ced09fafad6"}, "docker": "quay.io/biocontainers/bioconductor-moma"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-moma.
shpc-registry automated BioContainers addition for bioconductor-moma
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-moma
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-moma:1.18.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-moma/1.18.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-moma/1.18.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-moma-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-moma-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-moma-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-moma-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-moma-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-moma-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-moma

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
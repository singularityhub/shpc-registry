---
layout: container
name:  "quay.io/biocontainers/bioconductor-r4rna"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-r4rna/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-r4rna/container.yaml"
updated_at: "2024-11-14 04:39:43.573857"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-r4rna"

versions:
 - "1.8.0--r351_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r40hdfd78af_1"
 - "1.16.0--r40_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-r4rna"
config: {"url": "https://biocontainers.pro/tools/bioconductor-r4rna", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-r4rna", "latest": {"1.30.0--r43hdfd78af_0": "sha256:395e3a8f63a22dfcd6020d64b0014fc67a392fa47cbb7f816f31f060abcb711e"}, "tags": {"1.8.0--r351_0": "sha256:be2f058a061dd685c12cff9e339521d15162fff97217032ae5b6684ca8bd144c", "1.26.0--r42hdfd78af_0": "sha256:27d61714ed25334386803cc1f02e4f28d56736f48a5d6b0d5632b98af771690f", "1.22.0--r41hdfd78af_0": "sha256:9add2f6ece2d5b88922b86ad44d44bb415ca964206d8c9e74e4061fc481e93e7", "1.20.0--r41hdfd78af_0": "sha256:805df30143babe9003b2fb83f5c329ac1b72fa336ca6143f9471a15ac3a64ee3", "1.18.0--r40hdfd78af_1": "sha256:8f944e089a9f422430f5ed598dbdeab74f3f8cada81f52533add43251ce15c6f", "1.16.0--r40_0": "sha256:959727ff43fe3e00785b351873486eff2e6112caae30b502189f16358ea347d6", "1.28.0--r43hdfd78af_0": "sha256:278bedc7aad243946fc19622f5590a93b0cddd14a6a365b922d8bc2531197717", "1.30.0--r43hdfd78af_0": "sha256:395e3a8f63a22dfcd6020d64b0014fc67a392fa47cbb7f816f31f060abcb711e"}, "docker": "quay.io/biocontainers/bioconductor-r4rna"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-r4rna.
shpc-registry automated BioContainers addition for bioconductor-r4rna
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-r4rna
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-r4rna:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-r4rna/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-r4rna/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-r4rna-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-r4rna-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-r4rna-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-r4rna-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-r4rna-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-r4rna-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-r4rna

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
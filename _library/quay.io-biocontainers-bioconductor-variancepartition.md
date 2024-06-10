---
layout: container
name:  "quay.io/biocontainers/bioconductor-variancepartition"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-variancepartition/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-variancepartition/container.yaml"
updated_at: "2024-06-10 03:19:59.215431"
latest: "1.32.2--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-variancepartition"
aliases:
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.1--r3.4.1_0"
 - "1.28.0--r42hdfd78af_0"
 - "1.24.0--r41hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r40hdfd78af_1"
 - "1.18.0--r40_0"
 - "1.30.2--r43hdfd78af_0"
 - "1.32.2--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-variancepartition"
config: {"url": "https://biocontainers.pro/tools/bioconductor-variancepartition", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-variancepartition", "latest": {"1.32.2--r43hdfd78af_0": "sha256:95c5c2f1d6229be81dd30fcb6a4fe745872fbe2d0494e2e294dc85054a77a9d5"}, "tags": {"1.8.1--r3.4.1_0": "sha256:21a528b07a13d6e0a9f59f967bac45eac9adfcdbfa55c63723f091b0fedd0ef4", "1.28.0--r42hdfd78af_0": "sha256:ba9f64ba8fb73c88c433672c6b0a8cb76a54f4411c18841dcdf87b1453f40829", "1.24.0--r41hdfd78af_0": "sha256:96087dab7d8ebe09c66c1e7c532839285731939923388ebd4b4f900e1cd4324d", "1.22.0--r41hdfd78af_0": "sha256:fd3b843151eb534889323dec2a9c387ec172a6fb9861696a1f8883c2179f7c3d", "1.20.0--r40hdfd78af_1": "sha256:02df9ecda0a2282d38877a12381bd9e96e2870cd04a090c3f0e1e1b3bd2dddaa", "1.18.0--r40_0": "sha256:a93409035516a2d785174dc194060b08d3c148b2ef20fcdce56e4d24f7f806d1", "1.30.2--r43hdfd78af_0": "sha256:a9a8a7be36161b07920326c3769889c627a13f6df50ea61ba36025a3fc88a08f", "1.32.2--r43hdfd78af_0": "sha256:95c5c2f1d6229be81dd30fcb6a4fe745872fbe2d0494e2e294dc85054a77a9d5"}, "docker": "quay.io/biocontainers/bioconductor-variancepartition", "aliases": {"ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-variancepartition.
shpc-registry automated BioContainers addition for bioconductor-variancepartition
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-variancepartition
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-variancepartition:1.32.2--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-variancepartition/1.32.2--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-variancepartition/1.32.2--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-variancepartition-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-variancepartition-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-variancepartition-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-variancepartition-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-variancepartition-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-variancepartition-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ncurses5-config

```bash
$ singularity exec <container> /usr/local/bin/ncurses5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncursesw5-config

```bash
$ singularity exec <container> /usr/local/bin/ncursesw5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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
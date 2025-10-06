---
layout: container
name:  "quay.io/biocontainers/bioconductor-derfinderhelper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-derfinderhelper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-derfinderhelper/container.yaml"
updated_at: "2025-10-06 06:38:17.999217"
latest: "1.40.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-derfinderhelper"

versions:
 - "1.28.0--r41hdfd78af_0"
 - "1.32.0--r42hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.40.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-derfinderhelper"
config: {"url": "https://biocontainers.pro/tools/bioconductor-derfinderhelper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-derfinderhelper", "latest": {"1.40.0--r44hdfd78af_0": "sha256:f855572330a89345be22925533cc0d2b3ca2707a0cdfa895313a1627f8453e84"}, "tags": {"1.28.0--r41hdfd78af_0": "sha256:0acb46969279e7a03686928a608ad058c517a39bea879e5ea509879a631d0a85", "1.32.0--r42hdfd78af_0": "sha256:8650c25318359ba5d6e73de7932d4ea430928239c6ce2e881833020ae314684f", "1.34.0--r43hdfd78af_0": "sha256:e13bad311ab1083317a054a6f12bfbd0a8dd124962be6751a062d104d117915b", "1.36.0--r43hdfd78af_0": "sha256:bc69f54686524ec677ba7dbb6f2fdc7b5a2490f768af3817c9d98f6dee58da98", "1.40.0--r44hdfd78af_0": "sha256:f855572330a89345be22925533cc0d2b3ca2707a0cdfa895313a1627f8453e84"}, "docker": "quay.io/biocontainers/bioconductor-derfinderhelper"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-derfinderhelper.
shpc-registry automated BioContainers addition for bioconductor-derfinderhelper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-derfinderhelper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-derfinderhelper:1.40.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-derfinderhelper/1.40.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-derfinderhelper/1.40.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-derfinderhelper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-derfinderhelper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-derfinderhelper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-derfinderhelper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-derfinderhelper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-derfinderhelper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-derfinderhelper

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
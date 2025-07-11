---
layout: container
name:  "quay.io/biocontainers/bioconductor-estrogen"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-estrogen/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-estrogen/container.yaml"
updated_at: "2025-07-11 15:11:23.267915"
latest: "1.52.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-estrogen"

versions:
 - "1.40.0--r41hdfd78af_1"
 - "1.43.0--r42hdfd78af_0"
 - "1.46.0--r43hdfd78af_0"
 - "1.48.0--r43hdfd78af_0"
 - "1.52.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-estrogen"
config: {"url": "https://biocontainers.pro/tools/bioconductor-estrogen", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-estrogen", "latest": {"1.52.0--r44hdfd78af_0": "sha256:89927aa38b560203bf5744f296c496b4c61bcec968fe78a6933b2c97eb9ba256"}, "tags": {"1.40.0--r41hdfd78af_1": "sha256:6ac882777f9ddd07a2a089d857adc991a55c2205e5511861456e2118e10c3f11", "1.43.0--r42hdfd78af_0": "sha256:e63c5ad46fe9784396cd2c9214a37c2140da117b440b4276f7718685ca3e8047", "1.46.0--r43hdfd78af_0": "sha256:72e443c57a75610c4b71e574f288c0ce364fe1c62146cdc940b32e2bc18bad7a", "1.48.0--r43hdfd78af_0": "sha256:292e59d161887e76c21ae352db52731f9ea0ee07d0d33d5ec98db1f6d2c9a655", "1.52.0--r44hdfd78af_0": "sha256:89927aa38b560203bf5744f296c496b4c61bcec968fe78a6933b2c97eb9ba256"}, "docker": "quay.io/biocontainers/bioconductor-estrogen"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-estrogen.
shpc-registry automated BioContainers addition for bioconductor-estrogen
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-estrogen
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-estrogen:1.52.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-estrogen/1.52.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-estrogen/1.52.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-estrogen-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-estrogen-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-estrogen-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-estrogen-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-estrogen-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-estrogen-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-estrogen

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
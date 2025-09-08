---
layout: container
name:  "quay.io/biocontainers/r-genomictools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-genomictools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-genomictools/container.yaml"
updated_at: "2025-09-08 03:41:29.967989"
latest: "0.2.9.7--r44h40dc89f_7"
container_url: "https://biocontainers.pro/tools/r-genomictools"

versions:
 - "0.2.9.7--r41hecf12ef_3"
 - "0.2.9.7--r42hecf12ef_4"
 - "0.2.9.7--r42h21a89ab_5"
 - "0.2.9.7--r43h21a89ab_6"
 - "0.2.9.7--r44h40dc89f_7"
description: "shpc-registry automated BioContainers addition for r-genomictools"
config: {"url": "https://biocontainers.pro/tools/r-genomictools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-genomictools", "latest": {"0.2.9.7--r44h40dc89f_7": "sha256:6ba4c8d614bf485fc80876f410eccd2c1014292b14c95602474a3f62b7d45d17"}, "tags": {"0.2.9.7--r41hecf12ef_3": "sha256:ba6ebb2ba3850901156dc063def734a0c598ff9ee7ebd95e2b1a65568b9274a1", "0.2.9.7--r42hecf12ef_4": "sha256:32cfdb044774b7e10cc1b28259f6226b76bd8fe06aca7f223bf3e8c8449c2633", "0.2.9.7--r42h21a89ab_5": "sha256:1a94022fc0820fc989bfa8f35c0014d129a0f312b7c165983530ec15553aea13", "0.2.9.7--r43h21a89ab_6": "sha256:36a94ab551abaad0fa82cbb67dc55dc8075e8f1833059fafe711b51aa98654b4", "0.2.9.7--r44h40dc89f_7": "sha256:6ba4c8d614bf485fc80876f410eccd2c1014292b14c95602474a3f62b7d45d17"}, "docker": "quay.io/biocontainers/r-genomictools"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-genomictools.
shpc-registry automated BioContainers addition for r-genomictools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-genomictools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-genomictools:0.2.9.7--r44h40dc89f_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-genomictools/0.2.9.7--r44h40dc89f_7
$ module help quay.io/biocontainers/r-genomictools/0.2.9.7--r44h40dc89f_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-genomictools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-genomictools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-genomictools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-genomictools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-genomictools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-genomictools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-genomictools

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
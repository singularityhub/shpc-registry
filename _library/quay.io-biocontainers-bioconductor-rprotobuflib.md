---
layout: container
name:  "quay.io/biocontainers/bioconductor-rprotobuflib"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rprotobuflib/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rprotobuflib/container.yaml"
updated_at: "2023-06-12 03:07:15.805074"
latest: "2.10.0--r42hc247a5b_1"
container_url: "https://biocontainers.pro/tools/bioconductor-rprotobuflib"

versions:
 - "2.6.0--r41hc247a5b_2"
 - "2.10.0--r42hc247a5b_0"
 - "2.10.0--r42hc247a5b_1"
description: "shpc-registry automated BioContainers addition for bioconductor-rprotobuflib"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rprotobuflib", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rprotobuflib", "latest": {"2.10.0--r42hc247a5b_1": "sha256:007b29961e4a315659bf4972390431343bb7fb3a1d2a1b1ac13e3154e3afc894"}, "tags": {"2.6.0--r41hc247a5b_2": "sha256:084c42539d35c7c11ddfb19a722748d933bb7f3a599f2ad30e17771d09379762", "2.10.0--r42hc247a5b_0": "sha256:438593ee009dc1e1b821444f4576e4a56bac6755587b9b301a9c6d6ba91afd75", "2.10.0--r42hc247a5b_1": "sha256:007b29961e4a315659bf4972390431343bb7fb3a1d2a1b1ac13e3154e3afc894"}, "docker": "quay.io/biocontainers/bioconductor-rprotobuflib"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rprotobuflib.
shpc-registry automated BioContainers addition for bioconductor-rprotobuflib
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rprotobuflib
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rprotobuflib:2.10.0--r42hc247a5b_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rprotobuflib/2.10.0--r42hc247a5b_1
$ module help quay.io/biocontainers/bioconductor-rprotobuflib/2.10.0--r42hc247a5b_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rprotobuflib-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rprotobuflib-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rprotobuflib-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rprotobuflib-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rprotobuflib-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rprotobuflib-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rprotobuflib

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
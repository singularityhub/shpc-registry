---
layout: container
name:  "quay.io/biocontainers/bioconductor-geneselectmmd"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-geneselectmmd/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-geneselectmmd/container.yaml"
updated_at: "2023-03-26 02:49:42.283028"
latest: "2.42.0--r42hefde4a7_0"
container_url: "https://biocontainers.pro/tools/bioconductor-geneselectmmd"

versions:
 - "2.38.0--r41hefde4a7_2"
 - "2.42.0--r42hefde4a7_0"
description: "shpc-registry automated BioContainers addition for bioconductor-geneselectmmd"
config: {"url": "https://biocontainers.pro/tools/bioconductor-geneselectmmd", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-geneselectmmd", "latest": {"2.42.0--r42hefde4a7_0": "sha256:09e187892d0719335fa33858989f38028264cabb6ed404e4c65cb648e3f760c3"}, "tags": {"2.38.0--r41hefde4a7_2": "sha256:c026841908538cef63e573b92c066440f73543d1d41a8912dbfc245404479851", "2.42.0--r42hefde4a7_0": "sha256:09e187892d0719335fa33858989f38028264cabb6ed404e4c65cb648e3f760c3"}, "docker": "quay.io/biocontainers/bioconductor-geneselectmmd"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-geneselectmmd.
shpc-registry automated BioContainers addition for bioconductor-geneselectmmd
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-geneselectmmd
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-geneselectmmd:2.42.0--r42hefde4a7_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-geneselectmmd/2.42.0--r42hefde4a7_0
$ module help quay.io/biocontainers/bioconductor-geneselectmmd/2.42.0--r42hefde4a7_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-geneselectmmd-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-geneselectmmd-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-geneselectmmd-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-geneselectmmd-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-geneselectmmd-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-geneselectmmd-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-geneselectmmd

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
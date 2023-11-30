---
layout: container
name:  "quay.io/biocontainers/r-tcga2stat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-tcga2stat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-tcga2stat/container.yaml"
updated_at: "2023-11-30 02:30:51.102115"
latest: "1.2--r43h3121a25_10"
container_url: "https://biocontainers.pro/tools/r-tcga2stat"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.2--r41h3121a25_8"
 - "1.2--r42h3121a25_9"
 - "1.2--r43h3121a25_10"
description: "shpc-registry automated BioContainers addition for r-tcga2stat"
config: {"url": "https://biocontainers.pro/tools/r-tcga2stat", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-tcga2stat", "latest": {"1.2--r43h3121a25_10": "sha256:81823a41be22e0c66f4afccea1b12dfac4f8ec4123a81fdf5b2ea7e0cb2d7e61"}, "tags": {"1.2--r41h3121a25_8": "sha256:aad507daf828a3d31654ccbc3cea3471d1df564f9d3aa56cf0ba96bc06f2892f", "1.2--r42h3121a25_9": "sha256:61da1c9fc25af48c5100dcb2b8acf00efccb85d50e537cfd42f133494ede86f1", "1.2--r43h3121a25_10": "sha256:81823a41be22e0c66f4afccea1b12dfac4f8ec4123a81fdf5b2ea7e0cb2d7e61"}, "docker": "quay.io/biocontainers/r-tcga2stat", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-tcga2stat.
shpc-registry automated BioContainers addition for r-tcga2stat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-tcga2stat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-tcga2stat:1.2--r43h3121a25_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-tcga2stat/1.2--r43h3121a25_10
$ module help quay.io/biocontainers/r-tcga2stat/1.2--r43h3121a25_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-tcga2stat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-tcga2stat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-tcga2stat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-tcga2stat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-tcga2stat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-tcga2stat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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
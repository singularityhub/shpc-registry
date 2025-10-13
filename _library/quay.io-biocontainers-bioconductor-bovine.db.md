---
layout: container
name:  "quay.io/biocontainers/bioconductor-bovine.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bovine.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bovine.db/container.yaml"
updated_at: "2025-10-13 04:17:55.260432"
latest: "3.13.0--r44hdfd78af_5"
container_url: "https://biocontainers.pro/tools/bioconductor-bovine.db"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.2.3--r41hdfd78af_7"
 - "3.13.0--r42hdfd78af_2"
 - "3.13.0--r43hdfd78af_3"
 - "3.13.0--r43hdfd78af_4"
 - "3.13.0--r44hdfd78af_5"
description: "shpc-registry automated BioContainers addition for bioconductor-bovine.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bovine.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bovine.db", "latest": {"3.13.0--r44hdfd78af_5": "sha256:1bde4f996e629971f50a5f08ad954bfb6c21273b32112acffc4bcf279b11a990"}, "tags": {"3.2.3--r41hdfd78af_7": "sha256:ffe2bb76898826183c854b12e4dd628561989f5c7869c7bc8d2e66224acf629a", "3.13.0--r42hdfd78af_2": "sha256:456906fd17e0206fef3bd82dbd4825777e66e76b437ceeb8f63190a855915ef3", "3.13.0--r43hdfd78af_3": "sha256:b3e6e407d3ada2498fcbd192798fbbc37f85ce5130c9a4504713ed5b2586382d", "3.13.0--r43hdfd78af_4": "sha256:bb4851a94ea32805009ab1f9a9e11ce1461e4e6dcc507783a1881698b8f72b0f", "3.13.0--r44hdfd78af_5": "sha256:1bde4f996e629971f50a5f08ad954bfb6c21273b32112acffc4bcf279b11a990"}, "docker": "quay.io/biocontainers/bioconductor-bovine.db", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bovine.db.
shpc-registry automated BioContainers addition for bioconductor-bovine.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bovine.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bovine.db:3.13.0--r44hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bovine.db/3.13.0--r44hdfd78af_5
$ module help quay.io/biocontainers/bioconductor-bovine.db/3.13.0--r44hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bovine.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bovine.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bovine.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bovine.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bovine.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bovine.db-inspect-deffile:

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
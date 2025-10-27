---
layout: container
name:  "quay.io/biocontainers/bioconductor-corral"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-corral/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-corral/container.yaml"
updated_at: "2025-10-27 03:36:04.936359"
latest: "1.16.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-corral"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.16.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-corral"
config: {"url": "https://biocontainers.pro/tools/bioconductor-corral", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-corral", "latest": {"1.16.0--r44hdfd78af_0": "sha256:9541f12d36136056a847ac4cdcbda14c8a78106eddee18a9f984a70439b93460"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:79e19c0a9dfffb9b3b311defcaa11286dab3cbde94d08c8e5ddf9c60ca804cbf", "1.8.0--r42hdfd78af_0": "sha256:48f58dbb86e0f4151246da5285793db64c87dfe32383d9a423f34087718b038f", "1.10.0--r43hdfd78af_0": "sha256:8dbb1131753f153594353172819126cd8912332fe4537adbd1bb94c10cd846f4", "1.12.0--r43hdfd78af_0": "sha256:7ea1bf960ff586f5528e3159cba18b0e0f69f6af4e126f6100ef4bbe15373519", "1.16.0--r44hdfd78af_0": "sha256:9541f12d36136056a847ac4cdcbda14c8a78106eddee18a9f984a70439b93460"}, "docker": "quay.io/biocontainers/bioconductor-corral", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-corral.
shpc-registry automated BioContainers addition for bioconductor-corral
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-corral
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-corral:1.16.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-corral/1.16.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-corral/1.16.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-corral-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-corral-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-corral-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-corral-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-corral-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-corral-inspect-deffile:

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
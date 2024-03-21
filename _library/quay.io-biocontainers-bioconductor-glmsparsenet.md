---
layout: container
name:  "quay.io/biocontainers/bioconductor-glmsparsenet"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-glmsparsenet/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-glmsparsenet/container.yaml"
updated_at: "2024-03-21 02:44:10.461883"
latest: "1.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-glmsparsenet"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-glmsparsenet"
config: {"url": "https://biocontainers.pro/tools/bioconductor-glmsparsenet", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-glmsparsenet", "latest": {"1.20.0--r43hdfd78af_0": "sha256:2de0c9ba2a186fc3ea65c1f87198a53de012eeb67b76b912ea36377b13781429"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:ee7d0efd8232b46685afd3607548df7c2c37e664a5eaf02cde394ec0e7917225", "1.16.0--r42hdfd78af_0": "sha256:d3d238348cabf3cbfac86219ac98dd7628104468d1e58cdbcbe301e171389016", "1.12.0--r41hdfd78af_0": "sha256:19b8ef8e573331afebcc92bf863d43e6c842e39e02fd3dabe830f69afe3375f7", "1.10.0--r41hdfd78af_0": "sha256:0a77b7878c0c0cb2b32e9e28cf22ce4b474c3a57f743729be4a3aab452c713b6", "1.18.0--r43hdfd78af_0": "sha256:fd922d816db5ffc308fec3f5e1bb391d09855c3244a35f631c778f6b5fb4569a", "1.20.0--r43hdfd78af_0": "sha256:2de0c9ba2a186fc3ea65c1f87198a53de012eeb67b76b912ea36377b13781429"}, "docker": "quay.io/biocontainers/bioconductor-glmsparsenet", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-glmsparsenet.
shpc-registry automated BioContainers addition for bioconductor-glmsparsenet
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-glmsparsenet
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-glmsparsenet:1.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-glmsparsenet/1.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-glmsparsenet/1.20.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-glmsparsenet-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-glmsparsenet-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-glmsparsenet-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-glmsparsenet-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-glmsparsenet-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-glmsparsenet-inspect-deffile:

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
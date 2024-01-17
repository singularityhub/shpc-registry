---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgu133atagcdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgu133atagcdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgu133atagcdf/container.yaml"
updated_at: "2024-01-17 02:40:45.960461"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-hgu133atagcdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-hgu133atagcdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgu133atagcdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgu133atagcdf", "latest": {"2.18.0--r43hdfd78af_12": "sha256:d02d3304eb357c0dc1c8dc5bf772a9ce74c33a09d4cc836497a5e4ba3dd21c8d"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:1d8a6a33c2a1087afcc1d97a3081c2ef131723378db97ca731f7118a44fc3e15", "2.18.0--r42hdfd78af_10": "sha256:2ac5e262e42c65a32099186ad125d6b9b0f76b35737f22732d12ecd17ae8af94", "2.18.0--r43hdfd78af_11": "sha256:ee21f14b44b12046e72278a3f5af13a22f02b6cc9c55e4e3f2f5098e79dc02c6", "2.18.0--r43hdfd78af_12": "sha256:d02d3304eb357c0dc1c8dc5bf772a9ce74c33a09d4cc836497a5e4ba3dd21c8d"}, "docker": "quay.io/biocontainers/bioconductor-hgu133atagcdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgu133atagcdf.
shpc-registry automated BioContainers addition for bioconductor-hgu133atagcdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu133atagcdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu133atagcdf:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgu133atagcdf/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-hgu133atagcdf/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgu133atagcdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu133atagcdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu133atagcdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgu133atagcdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgu133atagcdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgu133atagcdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hgu133atagcdf

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
---
layout: container
name:  "quay.io/biocontainers/bioconductor-tenxbusdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tenxbusdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tenxbusdata/container.yaml"
updated_at: "2024-06-08 02:42:35.383531"
latest: "1.16.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tenxbusdata"

versions:
 - "1.8.0--r41hdfd78af_1"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tenxbusdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tenxbusdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tenxbusdata", "latest": {"1.16.0--r43hdfd78af_0": "sha256:0fba18f0f77437368d641a368ae614a90367b76cbc6bf7f3eea6dca7be2c8798"}, "tags": {"1.8.0--r41hdfd78af_1": "sha256:50c5643a32be5d5544a3d6e4b288ef94e550e9e10535f25c76bcce22eed27946", "1.12.0--r42hdfd78af_0": "sha256:7c3c5a2d309e69315a0370e057663cf299111cca342d5648cdf70df7f1769b68", "1.14.0--r43hdfd78af_0": "sha256:e3963b90fe8774b273b99f22dfe38b1b4b6804e8ca0c699b2b6503e2951d1199", "1.16.0--r43hdfd78af_0": "sha256:0fba18f0f77437368d641a368ae614a90367b76cbc6bf7f3eea6dca7be2c8798"}, "docker": "quay.io/biocontainers/bioconductor-tenxbusdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tenxbusdata.
shpc-registry automated BioContainers addition for bioconductor-tenxbusdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tenxbusdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tenxbusdata:1.16.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tenxbusdata/1.16.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tenxbusdata/1.16.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tenxbusdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tenxbusdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tenxbusdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tenxbusdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tenxbusdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tenxbusdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tenxbusdata

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
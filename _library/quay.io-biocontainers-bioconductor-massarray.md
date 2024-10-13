---
layout: container
name:  "quay.io/biocontainers/bioconductor-massarray"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-massarray/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-massarray/container.yaml"
updated_at: "2024-10-13 11:02:47.394242"
latest: "1.54.0--r43hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-massarray"

versions:
 - "1.46.0--r41hdfd78af_0"
 - "1.50.0--r42hdfd78af_0"
 - "1.52.0--r43hdfd78af_0"
 - "1.54.0--r43hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-massarray"
config: {"url": "https://biocontainers.pro/tools/bioconductor-massarray", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-massarray", "latest": {"1.54.0--r43hdfd78af_1": "sha256:0ffe5dc4ccc5cc0f1c52f8aa4dde1472eb2d1d22717579a93f0a618e968052f5"}, "tags": {"1.46.0--r41hdfd78af_0": "sha256:20747a2d7aa4032e5f51aca8c6175dd512c47be519ad0dc35c06984535ab443b", "1.50.0--r42hdfd78af_0": "sha256:34145b3900f59b939f65e395176430414939e89fa064be23eee2e1eb21adf60d", "1.52.0--r43hdfd78af_0": "sha256:cb77379dd24d78206d1db21f42c1bc61525fdc1c4453758f4ebad8b8dba93711", "1.54.0--r43hdfd78af_1": "sha256:0ffe5dc4ccc5cc0f1c52f8aa4dde1472eb2d1d22717579a93f0a618e968052f5"}, "docker": "quay.io/biocontainers/bioconductor-massarray"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-massarray.
shpc-registry automated BioContainers addition for bioconductor-massarray
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-massarray
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-massarray:1.54.0--r43hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-massarray/1.54.0--r43hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-massarray/1.54.0--r43hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-massarray-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-massarray-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-massarray-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-massarray-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-massarray-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-massarray-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-massarray

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
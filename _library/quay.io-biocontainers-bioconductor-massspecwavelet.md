---
layout: container
name:  "quay.io/biocontainers/bioconductor-massspecwavelet"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-massspecwavelet/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-massspecwavelet/container.yaml"
updated_at: "2024-08-25 03:16:25.086530"
latest: "1.68.0--r43ha9d7317_1"
container_url: "https://biocontainers.pro/tools/bioconductor-massspecwavelet"

versions:
 - "1.60.1--r41hc0cfd56_0"
 - "1.64.0--r42hc0cfd56_0"
 - "1.64.0--r42ha9d7317_1"
 - "1.66.0--r43ha9d7317_0"
 - "1.68.0--r43ha9d7317_0"
 - "1.68.0--r43ha9d7317_1"
description: "shpc-registry automated BioContainers addition for bioconductor-massspecwavelet"
config: {"url": "https://biocontainers.pro/tools/bioconductor-massspecwavelet", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-massspecwavelet", "latest": {"1.68.0--r43ha9d7317_1": "sha256:04477ecd11a321352b48a543ead20e3bcde0f432ab422c8aee66c7080d8e067b"}, "tags": {"1.60.1--r41hc0cfd56_0": "sha256:2512be2726fc609d5fb75f41e717d5cfa9a103540c6a25a140b44d7476e005f9", "1.64.0--r42hc0cfd56_0": "sha256:f654755894fd79d737ee2f288e4e259550314c41560cbebc625fd77600befa07", "1.64.0--r42ha9d7317_1": "sha256:40957a143d02721b9043a7e7f90e51103bae5f06f655ce4922f6f64bff845839", "1.66.0--r43ha9d7317_0": "sha256:f3ae352ea7c92a5ce67adf7a2a1aacf850d139f4e999c4c372b2556da1d8b233", "1.68.0--r43ha9d7317_0": "sha256:eb3c182de5f60652d0427a35ee56925ca7eb002e9e4e5613515ffa43eadd9726", "1.68.0--r43ha9d7317_1": "sha256:04477ecd11a321352b48a543ead20e3bcde0f432ab422c8aee66c7080d8e067b"}, "docker": "quay.io/biocontainers/bioconductor-massspecwavelet"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-massspecwavelet.
shpc-registry automated BioContainers addition for bioconductor-massspecwavelet
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-massspecwavelet
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-massspecwavelet:1.68.0--r43ha9d7317_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-massspecwavelet/1.68.0--r43ha9d7317_1
$ module help quay.io/biocontainers/bioconductor-massspecwavelet/1.68.0--r43ha9d7317_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-massspecwavelet-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-massspecwavelet-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-massspecwavelet-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-massspecwavelet-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-massspecwavelet-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-massspecwavelet-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-massspecwavelet

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
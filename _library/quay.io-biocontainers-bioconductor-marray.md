---
layout: container
name:  "quay.io/biocontainers/bioconductor-marray"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-marray/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-marray/container.yaml"
updated_at: "2024-12-09 04:24:05.804091"
latest: "1.80.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-marray"

versions:
 - "1.72.0--r41hdfd78af_0"
 - "1.76.0--r42hdfd78af_0"
 - "1.78.0--r43hdfd78af_0"
 - "1.80.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-marray"
config: {"url": "https://biocontainers.pro/tools/bioconductor-marray", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-marray", "latest": {"1.80.0--r43hdfd78af_0": "sha256:7221d0f1f16ee7ae2b7a5a2262beb5a59cea06fc2b7ef5ad6cc1a527bd899dac"}, "tags": {"1.72.0--r41hdfd78af_0": "sha256:bb2b868330759250b7e81819bfea134b4e18508836a67c85b7c200d9415f7427", "1.76.0--r42hdfd78af_0": "sha256:18fc58bb48d1f92aced2614e0b40d3598b9c5c1df688ab38a3da5244d7883f2e", "1.78.0--r43hdfd78af_0": "sha256:35b7689ca986dcc0c6f720feb3a12d1d674298bd2fcce2db803493dceebde4d9", "1.80.0--r43hdfd78af_0": "sha256:7221d0f1f16ee7ae2b7a5a2262beb5a59cea06fc2b7ef5ad6cc1a527bd899dac"}, "docker": "quay.io/biocontainers/bioconductor-marray"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-marray.
shpc-registry automated BioContainers addition for bioconductor-marray
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-marray
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-marray:1.80.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-marray/1.80.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-marray/1.80.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-marray-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-marray-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-marray-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-marray-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-marray-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-marray-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-marray

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
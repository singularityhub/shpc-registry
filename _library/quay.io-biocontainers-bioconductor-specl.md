---
layout: container
name:  "quay.io/biocontainers/bioconductor-specl"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-specl/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-specl/container.yaml"
updated_at: "2025-09-28 03:24:33.369474"
latest: "1.40.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-specl"

versions:
 - "1.28.0--r41hdfd78af_0"
 - "1.32.0--r42hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.40.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-specl"
config: {"url": "https://biocontainers.pro/tools/bioconductor-specl", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-specl", "latest": {"1.40.0--r44hdfd78af_0": "sha256:5d70a3efe4e7480220fac63c9f054fb70283793d8d433a2cd3adca12db09201d"}, "tags": {"1.28.0--r41hdfd78af_0": "sha256:fb954288febd70853e5cd2d5015011dc91132d9305b8c458026a0be50426ec27", "1.32.0--r42hdfd78af_0": "sha256:ac60f7bccd3204239bfc45364815b91a47ec53186174eef6c16265ab02e86616", "1.34.0--r43hdfd78af_0": "sha256:0f112f41a3a69d2b0d51c75c3bf927509b4dd41dd350454bd315c8365e992584", "1.36.0--r43hdfd78af_0": "sha256:578b1c5078719fd52159e44c6cbf1bda57b64bd3f83afff01c82e2142ef704f8", "1.40.0--r44hdfd78af_0": "sha256:5d70a3efe4e7480220fac63c9f054fb70283793d8d433a2cd3adca12db09201d"}, "docker": "quay.io/biocontainers/bioconductor-specl"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-specl.
shpc-registry automated BioContainers addition for bioconductor-specl
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-specl
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-specl:1.40.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-specl/1.40.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-specl/1.40.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-specl-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-specl-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-specl-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-specl-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-specl-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-specl-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-specl

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
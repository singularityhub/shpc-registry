---
layout: container
name:  "quay.io/biocontainers/bioconductor-dlbcl"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dlbcl/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dlbcl/container.yaml"
updated_at: "2025-02-12 03:19:28.095448"
latest: "1.46.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dlbcl"

versions:
 - "1.34.0--r41hdfd78af_1"
 - "1.38.0--r42hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.42.1--r43hdfd78af_0"
 - "1.46.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-dlbcl"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dlbcl", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dlbcl", "latest": {"1.46.0--r44hdfd78af_0": "sha256:b8ebc7d8dc630e039063816cf7b2a9b764949889ef42ead2f9b4c8729e9732a3"}, "tags": {"1.34.0--r41hdfd78af_1": "sha256:6d8fd4abbb310ca4571df6f998a9b4b43d208708222ffcd870f202d0638e9721", "1.38.0--r42hdfd78af_0": "sha256:5f259abb69241ce882f53c50ad69de43fa8d0bf4bb108290b35cb29186600d9e", "1.40.0--r43hdfd78af_0": "sha256:f40490ebaba859ca42fa684768d2c9efc9f5e08e1d7ae48335a3be0436cafc1e", "1.42.1--r43hdfd78af_0": "sha256:615aa8a437e3d4bc2808a1b6badc19291b21d1106a049880e8bfc1141b601fb6", "1.46.0--r44hdfd78af_0": "sha256:b8ebc7d8dc630e039063816cf7b2a9b764949889ef42ead2f9b4c8729e9732a3"}, "docker": "quay.io/biocontainers/bioconductor-dlbcl"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dlbcl.
shpc-registry automated BioContainers addition for bioconductor-dlbcl
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dlbcl
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dlbcl:1.46.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dlbcl/1.46.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-dlbcl/1.46.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dlbcl-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dlbcl-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dlbcl-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dlbcl-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dlbcl-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dlbcl-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-dlbcl

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
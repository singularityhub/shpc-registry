---
layout: container
name:  "quay.io/biocontainers/bioconductor-gpaexample"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gpaexample/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gpaexample/container.yaml"
updated_at: "2024-02-20 02:57:37.285833"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gpaexample"

versions:
 - "1.6.0--r41hdfd78af_1"
 - "1.9.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gpaexample"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gpaexample", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gpaexample", "latest": {"1.14.0--r43hdfd78af_0": "sha256:e56a8986c9b30ba00e2a6b3020282247a69721d202ee4043ec358d9a97350a52"}, "tags": {"1.6.0--r41hdfd78af_1": "sha256:5cbe9805e6dbd801fc71821d03c3705f8202fe6949bfb37223a952132f0e05e3", "1.9.0--r42hdfd78af_0": "sha256:7943d7e8d3beaa5c4462e186e259f7e6de2b4ae2530c7b46b70004b260ba0b68", "1.12.0--r43hdfd78af_0": "sha256:5d25b616e3a74981e0ed934fb616bdcdc122a4feda0391c0ac30a29f58cadb63", "1.14.0--r43hdfd78af_0": "sha256:e56a8986c9b30ba00e2a6b3020282247a69721d202ee4043ec358d9a97350a52"}, "docker": "quay.io/biocontainers/bioconductor-gpaexample"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gpaexample.
shpc-registry automated BioContainers addition for bioconductor-gpaexample
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gpaexample
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gpaexample:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gpaexample/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gpaexample/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gpaexample-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gpaexample-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gpaexample-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gpaexample-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gpaexample-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gpaexample-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gpaexample

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
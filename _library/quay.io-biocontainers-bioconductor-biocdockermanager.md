---
layout: container
name:  "quay.io/biocontainers/bioconductor-biocdockermanager"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biocdockermanager/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biocdockermanager/container.yaml"
updated_at: "2023-08-18 03:17:23.477530"
latest: "1.11.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-biocdockermanager"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.11.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-biocdockermanager"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biocdockermanager", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-biocdockermanager", "latest": {"1.11.0--r43hdfd78af_0": "sha256:04025faa13c7e9883b52eb436ab2f96d99caee9118dc1a179536161c8e048f4f"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:efecde61010b335dfb710204f55798034d70830d344e77ea071d0f52cee7ca64", "1.10.0--r42hdfd78af_0": "sha256:0fd71298b43931ecd9c8ac5f5da669451235dea52f6672f9b72719d2e4816f31", "1.11.0--r43hdfd78af_0": "sha256:04025faa13c7e9883b52eb436ab2f96d99caee9118dc1a179536161c8e048f4f"}, "docker": "quay.io/biocontainers/bioconductor-biocdockermanager"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biocdockermanager.
shpc-registry automated BioContainers addition for bioconductor-biocdockermanager
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biocdockermanager
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biocdockermanager:1.11.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biocdockermanager/1.11.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-biocdockermanager/1.11.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biocdockermanager-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocdockermanager-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocdockermanager-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biocdockermanager-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biocdockermanager-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biocdockermanager-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-biocdockermanager

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
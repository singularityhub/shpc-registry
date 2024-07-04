---
layout: container
name:  "quay.io/biocontainers/bioconductor-factdesign"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-factdesign/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-factdesign/container.yaml"
updated_at: "2024-07-04 02:59:40.526753"
latest: "1.78.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-factdesign"

versions:
 - "1.70.0--r41hdfd78af_0"
 - "1.74.0--r42hdfd78af_0"
 - "1.76.0--r43hdfd78af_0"
 - "1.78.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-factdesign"
config: {"url": "https://biocontainers.pro/tools/bioconductor-factdesign", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-factdesign", "latest": {"1.78.0--r43hdfd78af_0": "sha256:1316015f187a62d7b7927fa7da99eccc9510ece8c3feac9c3557e682c9ae2ea3"}, "tags": {"1.70.0--r41hdfd78af_0": "sha256:8992262852d6969d1bfec1d6a22a36141b5d45de9efdc8d550059333f99ec53c", "1.74.0--r42hdfd78af_0": "sha256:a25582545665cfa0b00de2c87b7f12f75ab339d5a107d67cf2d9238e8a616c5a", "1.76.0--r43hdfd78af_0": "sha256:728aef1af6fabb6bfbb2ea70abae64cf951fe0e74f546946c51bad81392c12e4", "1.78.0--r43hdfd78af_0": "sha256:1316015f187a62d7b7927fa7da99eccc9510ece8c3feac9c3557e682c9ae2ea3"}, "docker": "quay.io/biocontainers/bioconductor-factdesign"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-factdesign.
shpc-registry automated BioContainers addition for bioconductor-factdesign
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-factdesign
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-factdesign:1.78.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-factdesign/1.78.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-factdesign/1.78.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-factdesign-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-factdesign-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-factdesign-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-factdesign-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-factdesign-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-factdesign-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-factdesign

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
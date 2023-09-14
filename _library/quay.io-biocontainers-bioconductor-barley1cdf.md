---
layout: container
name:  "quay.io/biocontainers/bioconductor-barley1cdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-barley1cdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-barley1cdf/container.yaml"
updated_at: "2023-09-14 03:24:25.326768"
latest: "2.18.0--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-barley1cdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-barley1cdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-barley1cdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-barley1cdf", "latest": {"2.18.0--r43hdfd78af_11": "sha256:ed8212ea592e43ff09fbc81609741736f199496895404cd4ea074ff1ef202307"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:0b2d0be3e4a2d1984bcbe54c57e902452a7c69d09186037a9eb1899a0e166ed9", "2.18.0--r42hdfd78af_10": "sha256:8322642e3a5caea1dd2cfafc945d940d4a0e0d0425236f325b16aea1514a5257", "2.18.0--r43hdfd78af_11": "sha256:ed8212ea592e43ff09fbc81609741736f199496895404cd4ea074ff1ef202307"}, "docker": "quay.io/biocontainers/bioconductor-barley1cdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-barley1cdf.
shpc-registry automated BioContainers addition for bioconductor-barley1cdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-barley1cdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-barley1cdf:2.18.0--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-barley1cdf/2.18.0--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-barley1cdf/2.18.0--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-barley1cdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-barley1cdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-barley1cdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-barley1cdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-barley1cdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-barley1cdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-barley1cdf

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
---
layout: container
name:  "quay.io/biocontainers/bioconductor-gostats"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gostats/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gostats/container.yaml"
updated_at: "2023-12-20 03:13:24.671590"
latest: "2.66.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gostats"

versions:
 - "2.60.0--r41hdfd78af_0"
 - "2.64.0--r42hdfd78af_0"
 - "2.66.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gostats"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gostats", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gostats", "latest": {"2.66.0--r43hdfd78af_0": "sha256:87bcc33eb5933a98889c782908a88cc8106af0c13e35db69ae5b110aaceb4144"}, "tags": {"2.60.0--r41hdfd78af_0": "sha256:dac96483e0dfbdfef1d60039f2694a4fa4a989baa9a3b671f6eafaf88557fad9", "2.64.0--r42hdfd78af_0": "sha256:ebcbe21a8a4867a7641b4140f067825c414e77f0fdfe085d06ea3a960857329d", "2.66.0--r43hdfd78af_0": "sha256:87bcc33eb5933a98889c782908a88cc8106af0c13e35db69ae5b110aaceb4144"}, "docker": "quay.io/biocontainers/bioconductor-gostats"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gostats.
shpc-registry automated BioContainers addition for bioconductor-gostats
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gostats
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gostats:2.66.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gostats/2.66.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gostats/2.66.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gostats-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gostats-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gostats-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gostats-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gostats-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gostats-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gostats

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
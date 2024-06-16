---
layout: container
name:  "quay.io/biocontainers/bioconductor-biotip"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biotip/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biotip/container.yaml"
updated_at: "2024-06-16 03:14:13.765624"
latest: "1.16.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-biotip"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-biotip"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biotip", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-biotip", "latest": {"1.16.0--r43hdfd78af_0": "sha256:7fa68ff6bb54618266b787f747a5e76985ef8804721e14ab9e582e7fc735280b"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:92b1d18197cd73c1e21b1dff548467ba5af1400ab8293a402e645599904e9696", "1.12.0--r42hdfd78af_0": "sha256:87fbfa51912ba6f8ae5770b2f5f6b7030882632a5fba0385aa31fe4f2a963bd3", "1.14.0--r43hdfd78af_0": "sha256:f83564d10db366beab06f0e1168d51b9f898c6aed544bea571aa8764801d4008", "1.16.0--r43hdfd78af_0": "sha256:7fa68ff6bb54618266b787f747a5e76985ef8804721e14ab9e582e7fc735280b"}, "docker": "quay.io/biocontainers/bioconductor-biotip"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biotip.
shpc-registry automated BioContainers addition for bioconductor-biotip
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biotip
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biotip:1.16.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biotip/1.16.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-biotip/1.16.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biotip-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biotip-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biotip-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biotip-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biotip-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biotip-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-biotip

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
---
layout: container
name:  "quay.io/biocontainers/bioconductor-randpack"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-randpack/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-randpack/container.yaml"
updated_at: "2023-07-23 03:01:08.279683"
latest: "1.46.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-randpack"

versions:
 - "1.40.0--r41hdfd78af_0"
 - "1.44.0--r42hdfd78af_0"
 - "1.46.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-randpack"
config: {"url": "https://biocontainers.pro/tools/bioconductor-randpack", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-randpack", "latest": {"1.46.0--r43hdfd78af_0": "sha256:984263645739ab4719d76ff3221d8f63402cd2208de08aa2f0fb14e795738f18"}, "tags": {"1.40.0--r41hdfd78af_0": "sha256:c87a95aa0339cd2c2f57969f178bbbf1ee9f68d0feec666d0db8b6e428735192", "1.44.0--r42hdfd78af_0": "sha256:c94e5cb8fe7eaebcd67b92f631e3f98de88b4f2f04b19ea31b18f5915a8d5e85", "1.46.0--r43hdfd78af_0": "sha256:984263645739ab4719d76ff3221d8f63402cd2208de08aa2f0fb14e795738f18"}, "docker": "quay.io/biocontainers/bioconductor-randpack"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-randpack.
shpc-registry automated BioContainers addition for bioconductor-randpack
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-randpack
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-randpack:1.46.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-randpack/1.46.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-randpack/1.46.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-randpack-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-randpack-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-randpack-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-randpack-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-randpack-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-randpack-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-randpack

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
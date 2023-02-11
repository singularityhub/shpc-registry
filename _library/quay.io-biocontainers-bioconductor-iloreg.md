---
layout: container
name:  "quay.io/biocontainers/bioconductor-iloreg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-iloreg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-iloreg/container.yaml"
updated_at: "2023-02-11 02:48:12.899721"
latest: "1.8.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-iloreg"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-iloreg"
config: {"url": "https://biocontainers.pro/tools/bioconductor-iloreg", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-iloreg", "latest": {"1.8.0--r42hdfd78af_0": "sha256:ae83eff7fb9113c4855bfd1c998c2b19fc0546a570091e97a1b94ff29dbe21bd"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:1c023cc65f2f3996fbc60f856af57b78cfe06a005406562b433369a1c1685ab1", "1.8.0--r42hdfd78af_0": "sha256:ae83eff7fb9113c4855bfd1c998c2b19fc0546a570091e97a1b94ff29dbe21bd"}, "docker": "quay.io/biocontainers/bioconductor-iloreg"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-iloreg.
shpc-registry automated BioContainers addition for bioconductor-iloreg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-iloreg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-iloreg:1.8.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-iloreg/1.8.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-iloreg/1.8.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-iloreg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-iloreg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-iloreg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-iloreg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-iloreg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-iloreg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-iloreg

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
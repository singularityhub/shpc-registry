---
layout: container
name:  "quay.io/biocontainers/bioconductor-msprep"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-msprep/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-msprep/container.yaml"
updated_at: "2023-06-10 03:17:29.182316"
latest: "1.8.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-msprep"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-msprep"
config: {"url": "https://biocontainers.pro/tools/bioconductor-msprep", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-msprep", "latest": {"1.8.0--r42hdfd78af_0": "sha256:dbe83d27a83a459b597d4a331743a013f2aac9aa3619edb92ea3a0c9bc5ae3b5"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:c8730bb17f4620830e270fa110911380d137838598ce4cf0a7bfc40a7a8a6847", "1.8.0--r42hdfd78af_0": "sha256:dbe83d27a83a459b597d4a331743a013f2aac9aa3619edb92ea3a0c9bc5ae3b5"}, "docker": "quay.io/biocontainers/bioconductor-msprep"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-msprep.
shpc-registry automated BioContainers addition for bioconductor-msprep
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-msprep
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-msprep:1.8.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-msprep/1.8.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-msprep/1.8.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-msprep-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msprep-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msprep-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-msprep-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-msprep-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-msprep-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-msprep

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
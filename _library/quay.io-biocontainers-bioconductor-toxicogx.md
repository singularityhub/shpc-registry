---
layout: container
name:  "quay.io/biocontainers/bioconductor-toxicogx"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-toxicogx/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-toxicogx/container.yaml"
updated_at: "2023-06-06 03:05:25.736612"
latest: "2.2.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-toxicogx"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "2.2.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-toxicogx"
config: {"url": "https://biocontainers.pro/tools/bioconductor-toxicogx", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-toxicogx", "latest": {"2.2.0--r42hdfd78af_0": "sha256:1c8959a50f7c68507fd0e5ffa4f5c2dd1cbdf9d8b9ab2150c73c2c9b2c15fa7b"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:5f6559c9440b94724333799267a664af69dec234ac8db4535d67db427c958f40", "2.2.0--r42hdfd78af_0": "sha256:1c8959a50f7c68507fd0e5ffa4f5c2dd1cbdf9d8b9ab2150c73c2c9b2c15fa7b"}, "docker": "quay.io/biocontainers/bioconductor-toxicogx"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-toxicogx.
shpc-registry automated BioContainers addition for bioconductor-toxicogx
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-toxicogx
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-toxicogx:2.2.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-toxicogx/2.2.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-toxicogx/2.2.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-toxicogx-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-toxicogx-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-toxicogx-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-toxicogx-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-toxicogx-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-toxicogx-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-toxicogx

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
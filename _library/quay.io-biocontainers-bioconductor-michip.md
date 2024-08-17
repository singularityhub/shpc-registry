---
layout: container
name:  "quay.io/biocontainers/bioconductor-michip"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-michip/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-michip/container.yaml"
updated_at: "2024-08-17 03:22:09.138671"
latest: "1.56.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-michip"

versions:
 - "1.48.0--r41hdfd78af_0"
 - "1.52.0--r42hdfd78af_0"
 - "1.54.0--r43hdfd78af_0"
 - "1.56.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-michip"
config: {"url": "https://biocontainers.pro/tools/bioconductor-michip", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-michip", "latest": {"1.56.0--r43hdfd78af_0": "sha256:951529f026a9e16b176b80de9e15f5ec7567e8f53976d1f7ab4fba2a28ca0eb3"}, "tags": {"1.48.0--r41hdfd78af_0": "sha256:05d205e5bb5f8b4956575cef017a258fa541620091bd9ead6df0dcbc0c346a8d", "1.52.0--r42hdfd78af_0": "sha256:2d8f5a200f07974d7958266545e403ff99ac166f6ef2415fcd34befe40e7d794", "1.54.0--r43hdfd78af_0": "sha256:430d934a238c79e5616129949303d8d0d3df7db37942c616b504f8620390d74f", "1.56.0--r43hdfd78af_0": "sha256:951529f026a9e16b176b80de9e15f5ec7567e8f53976d1f7ab4fba2a28ca0eb3"}, "docker": "quay.io/biocontainers/bioconductor-michip"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-michip.
shpc-registry automated BioContainers addition for bioconductor-michip
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-michip
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-michip:1.56.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-michip/1.56.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-michip/1.56.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-michip-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-michip-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-michip-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-michip-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-michip-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-michip-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-michip

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
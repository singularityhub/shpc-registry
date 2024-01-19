---
layout: container
name:  "quay.io/biocontainers/bioconductor-agdex"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-agdex/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-agdex/container.yaml"
updated_at: "2024-01-19 03:07:08.897822"
latest: "1.50.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-agdex"

versions:
 - "1.42.0--r41hdfd78af_0"
 - "1.46.0--r42hdfd78af_0"
 - "1.48.0--r43hdfd78af_0"
 - "1.50.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-agdex"
config: {"url": "https://biocontainers.pro/tools/bioconductor-agdex", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-agdex", "latest": {"1.50.0--r43hdfd78af_0": "sha256:6afb0b6b66f4818af62955b673b5424c10e750496e7befb2206cdfe27ffe96a8"}, "tags": {"1.42.0--r41hdfd78af_0": "sha256:41ad00b61d704ccd367fa9952874931bb5b7cb0291edad7a3e9d44b2d90fbf09", "1.46.0--r42hdfd78af_0": "sha256:633cbc789d58de7b9b60a7a574088437b974fe1c3edffb8b2304025e2384e109", "1.48.0--r43hdfd78af_0": "sha256:43908b41c16fefb83c290b6eab2406b1ccd09eb00b57d765240eaea39ed71f61", "1.50.0--r43hdfd78af_0": "sha256:6afb0b6b66f4818af62955b673b5424c10e750496e7befb2206cdfe27ffe96a8"}, "docker": "quay.io/biocontainers/bioconductor-agdex"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-agdex.
shpc-registry automated BioContainers addition for bioconductor-agdex
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-agdex
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-agdex:1.50.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-agdex/1.50.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-agdex/1.50.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-agdex-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-agdex-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-agdex-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-agdex-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-agdex-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-agdex-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-agdex

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
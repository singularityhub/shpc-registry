---
layout: container
name:  "quay.io/biocontainers/bioconductor-flowclean"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-flowclean/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-flowclean/container.yaml"
updated_at: "2024-05-06 02:32:34.749437"
latest: "1.40.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-flowclean"

versions:
 - "1.32.0--r41hdfd78af_0"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-flowclean"
config: {"url": "https://biocontainers.pro/tools/bioconductor-flowclean", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-flowclean", "latest": {"1.40.0--r43hdfd78af_0": "sha256:6fcc3c5ed9dadead21d62e8a2dde15289b146bd68431b6f5f1fda84112be87e7"}, "tags": {"1.32.0--r41hdfd78af_0": "sha256:ac763a3fe7dd6ae089154550ae63aafd80ec21c96512640c48191f55e0fc2abb", "1.36.0--r42hdfd78af_0": "sha256:044499447d9153a61727d1f6b032fe7ce95bf0ab2621c2198eb2b387514cf4e7", "1.38.0--r43hdfd78af_0": "sha256:1611807dd9c2fb648fd931db721ee249befa975f23c1bf314b3e91245e605175", "1.40.0--r43hdfd78af_0": "sha256:6fcc3c5ed9dadead21d62e8a2dde15289b146bd68431b6f5f1fda84112be87e7"}, "docker": "quay.io/biocontainers/bioconductor-flowclean"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-flowclean.
shpc-registry automated BioContainers addition for bioconductor-flowclean
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-flowclean
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-flowclean:1.40.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-flowclean/1.40.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-flowclean/1.40.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-flowclean-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowclean-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowclean-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-flowclean-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-flowclean-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-flowclean-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-flowclean

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
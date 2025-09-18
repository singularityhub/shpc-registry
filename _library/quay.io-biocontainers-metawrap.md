---
layout: container
name:  "quay.io/biocontainers/metawrap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metawrap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metawrap/container.yaml"
updated_at: "2025-09-18 03:13:18.090921"
latest: "1.2--hdfd78af_2"
container_url: "https://biocontainers.pro/tools/metawrap"

versions:
 - "1.2--hdfd78af_2"
description: "shpc-registry automated BioContainers addition for metawrap"
config: {"url": "https://biocontainers.pro/tools/metawrap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metawrap", "latest": {"1.2--hdfd78af_2": "sha256:b767a2ec6928618496fa7dc78fe84265ae7029cf28f2a82093694f55f2f35e85"}, "tags": {"1.2--hdfd78af_2": "sha256:b767a2ec6928618496fa7dc78fe84265ae7029cf28f2a82093694f55f2f35e85"}, "docker": "quay.io/biocontainers/metawrap"}
---

This module is a singularity container wrapper for quay.io/biocontainers/metawrap.
shpc-registry automated BioContainers addition for metawrap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metawrap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metawrap:1.2--hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metawrap/1.2--hdfd78af_2
$ module help quay.io/biocontainers/metawrap/1.2--hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metawrap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metawrap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metawrap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metawrap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metawrap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metawrap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### metawrap

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
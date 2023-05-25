---
layout: container
name:  "quay.io/biocontainers/bioconductor-rain"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rain/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rain/container.yaml"
updated_at: "2023-05-25 03:16:01.946160"
latest: "1.32.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rain"

versions:
 - "1.28.0--r41hdfd78af_0"
 - "1.32.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rain"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rain", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rain", "latest": {"1.32.0--r42hdfd78af_0": "sha256:1bd8655d2187edfb11c57861e048a684975099fcd8260d797597316421e26b54"}, "tags": {"1.28.0--r41hdfd78af_0": "sha256:ff8aed56ca0057a586c46523bfb576fb8fc502cbafcd9d51928dc61885a5e8a3", "1.32.0--r42hdfd78af_0": "sha256:1bd8655d2187edfb11c57861e048a684975099fcd8260d797597316421e26b54"}, "docker": "quay.io/biocontainers/bioconductor-rain"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rain.
shpc-registry automated BioContainers addition for bioconductor-rain
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rain
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rain:1.32.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rain/1.32.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rain/1.32.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rain-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rain-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rain-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rain-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rain-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rain-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rain

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
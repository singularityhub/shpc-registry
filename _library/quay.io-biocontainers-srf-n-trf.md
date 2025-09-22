---
layout: container
name:  "quay.io/biocontainers/srf-n-trf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/srf-n-trf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/srf-n-trf/container.yaml"
updated_at: "2025-09-22 03:27:40.641059"
latest: "0.1.1--h4349ce8_0"
container_url: "https://biocontainers.pro/tools/srf-n-trf"
aliases:
 - "srf-n-trf"
versions:
 - "0.1.1--h4349ce8_0"
description: "singularity registry hpc automated addition for srf-n-trf"
config: {"url": "https://biocontainers.pro/tools/srf-n-trf", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for srf-n-trf", "latest": {"0.1.1--h4349ce8_0": "sha256:dd242691f5c1899f4efa24a7fea54bcec70a3d26767b523c88db29cd94db07ad"}, "tags": {"0.1.1--h4349ce8_0": "sha256:dd242691f5c1899f4efa24a7fea54bcec70a3d26767b523c88db29cd94db07ad"}, "docker": "quay.io/biocontainers/srf-n-trf", "aliases": {"srf-n-trf": "/usr/local/bin/srf-n-trf"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/srf-n-trf.
singularity registry hpc automated addition for srf-n-trf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/srf-n-trf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/srf-n-trf:0.1.1--h4349ce8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/srf-n-trf/0.1.1--h4349ce8_0
$ module help quay.io/biocontainers/srf-n-trf/0.1.1--h4349ce8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### srf-n-trf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### srf-n-trf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### srf-n-trf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### srf-n-trf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### srf-n-trf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### srf-n-trf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### srf-n-trf

```bash
$ singularity exec <container> /usr/local/bin/srf-n-trf
$ podman run --it --rm --entrypoint /usr/local/bin/srf-n-trf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/srf-n-trf   -v ${PWD} -w ${PWD} <container> -c " $@"
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
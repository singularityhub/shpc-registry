---
layout: container
name:  "quay.io/biocontainers/baysor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/baysor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/baysor/container.yaml"
updated_at: "2026-06-21 07:43:45.887210"
latest: "0.7.1--h467016e_2"
container_url: "https://biocontainers.pro/tools/baysor"
aliases:
 - "baysor"
versions:
 - "0.7.1--hab16a5f_0"
 - "0.7.1--h467016e_2"
description: "singularity registry hpc automated addition for baysor"
config: {"url": "https://biocontainers.pro/tools/baysor", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for baysor", "latest": {"0.7.1--h467016e_2": "sha256:4bd9546d1e63ce8e4b052faac1df0ce76f0ca1305802bd9fba8760f5cdf3ec7b"}, "tags": {"0.7.1--hab16a5f_0": "sha256:8b9e10762e23fedf6420fc415cddac1549ffa807ef98bebfc109c0df68723dd7", "0.7.1--h467016e_2": "sha256:4bd9546d1e63ce8e4b052faac1df0ce76f0ca1305802bd9fba8760f5cdf3ec7b"}, "docker": "quay.io/biocontainers/baysor", "aliases": {"baysor": "/usr/local/bin/baysor"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/baysor.
singularity registry hpc automated addition for baysor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/baysor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/baysor:0.7.1--h467016e_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/baysor/0.7.1--h467016e_2
$ module help quay.io/biocontainers/baysor/0.7.1--h467016e_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### baysor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### baysor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### baysor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### baysor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### baysor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### baysor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### baysor

```bash
$ singularity exec <container> /usr/local/bin/baysor
$ podman run --it --rm --entrypoint /usr/local/bin/baysor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/baysor   -v ${PWD} -w ${PWD} <container> -c " $@"
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
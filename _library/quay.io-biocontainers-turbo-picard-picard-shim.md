---
layout: container
name:  "quay.io/biocontainers/turbo-picard-picard-shim"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/turbo-picard-picard-shim/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/turbo-picard-picard-shim/container.yaml"
updated_at: "2026-10-10 19:06:59.512702"
latest: "0.1.15--hf5b135f_0"
container_url: "https://biocontainers.pro/tools/turbo-picard-picard-shim"
aliases:
 - "turbo-picard"
 - "picard"
versions:
 - "0.1.15--hf5b135f_0"
description: "singularity registry hpc automated addition for turbo-picard-picard-shim"
config: {"url": "https://biocontainers.pro/tools/turbo-picard-picard-shim", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for turbo-picard-picard-shim", "latest": {"0.1.15--hf5b135f_0": "sha256:618e6b7a2be3b015711cb0523e7667aeab716a29a334f8db55b2cdece132df1d"}, "tags": {"0.1.15--hf5b135f_0": "sha256:618e6b7a2be3b015711cb0523e7667aeab716a29a334f8db55b2cdece132df1d"}, "docker": "quay.io/biocontainers/turbo-picard-picard-shim", "aliases": {"turbo-picard": "/usr/local/bin/turbo-picard", "picard": "/usr/local/bin/picard"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/turbo-picard-picard-shim.
singularity registry hpc automated addition for turbo-picard-picard-shim
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/turbo-picard-picard-shim
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/turbo-picard-picard-shim:0.1.15--hf5b135f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/turbo-picard-picard-shim/0.1.15--hf5b135f_0
$ module help quay.io/biocontainers/turbo-picard-picard-shim/0.1.15--hf5b135f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### turbo-picard-picard-shim-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### turbo-picard-picard-shim-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### turbo-picard-picard-shim-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### turbo-picard-picard-shim-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### turbo-picard-picard-shim-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### turbo-picard-picard-shim-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### turbo-picard

```bash
$ singularity exec <container> /usr/local/bin/turbo-picard
$ podman run --it --rm --entrypoint /usr/local/bin/turbo-picard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/turbo-picard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### picard

```bash
$ singularity exec <container> /usr/local/bin/picard
$ podman run --it --rm --entrypoint /usr/local/bin/picard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/picard   -v ${PWD} -w ${PWD} <container> -c " $@"
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
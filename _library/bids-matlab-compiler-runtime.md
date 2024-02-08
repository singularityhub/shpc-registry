---
layout: container
name:  "bids/matlab-compiler-runtime"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/bids/matlab-compiler-runtime/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/bids/matlab-compiler-runtime/container.yaml"
updated_at: "2024-02-08 03:05:54.306348"
latest: "R2016b"
container_url: "https://hub.docker.com/r/bids/matlab-compiler-runtime"

versions:
 - "R2016b"
description: "Base image with Matlab compiler runtime (https://github.com/BIDS-Apps/matlab-compiler-runtime)"
config: {"docker": "bids/matlab-compiler-runtime", "latest": {"R2016b": "sha256:cd3170ac40fe8c00e84f69963a3cf8a5c39e2c9c25bb9df899754c3d31252bd1"}, "tags": {"R2016b": "sha256:cd3170ac40fe8c00e84f69963a3cf8a5c39e2c9c25bb9df899754c3d31252bd1"}, "filter": ["R2016b"], "maintainer": "@vsoch", "description": "Base image with Matlab compiler runtime (https://github.com/BIDS-Apps/matlab-compiler-runtime)", "url": "https://hub.docker.com/r/bids/matlab-compiler-runtime"}
---

This module is a singularity container wrapper for bids/matlab-compiler-runtime.
Base image with Matlab compiler runtime (https://github.com/BIDS-Apps/matlab-compiler-runtime)
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install bids/matlab-compiler-runtime
```

Or a specific version:

```bash
$ shpc install bids/matlab-compiler-runtime:R2016b
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load bids/matlab-compiler-runtime/R2016b
$ module help bids/matlab-compiler-runtime/R2016b
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### matlab-compiler-runtime-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### matlab-compiler-runtime-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### matlab-compiler-runtime-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### matlab-compiler-runtime-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### matlab-compiler-runtime-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### matlab-compiler-runtime-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### matlab-compiler-runtime

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
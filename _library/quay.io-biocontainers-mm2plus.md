---
layout: container
name:  "quay.io/biocontainers/mm2plus"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mm2plus/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mm2plus/container.yaml"
updated_at: "2025-03-28 03:20:22.334131"
latest: "1.0--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/mm2plus"
aliases:
 - "mm2plus"
 - "mm2plus.avx"
 - "mm2plus.avx2"
 - "mm2plus.avx512"
 - "mm2plus.sse4.1"
 - "mm2plus.sse4.2"
versions:
 - "1.0--h9ee0642_0"
description: "singularity registry hpc automated addition for mm2plus"
config: {"url": "https://biocontainers.pro/tools/mm2plus", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mm2plus", "latest": {"1.0--h9ee0642_0": "sha256:6b3d32f44b8a530b97267fd5e4a6889210ba9daaceef49b7a5224f29830a7c4e"}, "tags": {"1.0--h9ee0642_0": "sha256:6b3d32f44b8a530b97267fd5e4a6889210ba9daaceef49b7a5224f29830a7c4e"}, "docker": "quay.io/biocontainers/mm2plus", "aliases": {"mm2plus": "/usr/local/bin/mm2plus", "mm2plus.avx": "/usr/local/bin/mm2plus.avx", "mm2plus.avx2": "/usr/local/bin/mm2plus.avx2", "mm2plus.avx512": "/usr/local/bin/mm2plus.avx512", "mm2plus.sse4.1": "/usr/local/bin/mm2plus.sse4.1", "mm2plus.sse4.2": "/usr/local/bin/mm2plus.sse4.2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mm2plus.
singularity registry hpc automated addition for mm2plus
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mm2plus
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mm2plus:1.0--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mm2plus/1.0--h9ee0642_0
$ module help quay.io/biocontainers/mm2plus/1.0--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mm2plus-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mm2plus-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mm2plus-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mm2plus-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mm2plus-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mm2plus-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mm2plus

```bash
$ singularity exec <container> /usr/local/bin/mm2plus
$ podman run --it --rm --entrypoint /usr/local/bin/mm2plus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mm2plus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mm2plus.avx

```bash
$ singularity exec <container> /usr/local/bin/mm2plus.avx
$ podman run --it --rm --entrypoint /usr/local/bin/mm2plus.avx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mm2plus.avx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mm2plus.avx2

```bash
$ singularity exec <container> /usr/local/bin/mm2plus.avx2
$ podman run --it --rm --entrypoint /usr/local/bin/mm2plus.avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mm2plus.avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mm2plus.avx512

```bash
$ singularity exec <container> /usr/local/bin/mm2plus.avx512
$ podman run --it --rm --entrypoint /usr/local/bin/mm2plus.avx512   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mm2plus.avx512   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mm2plus.sse4.1

```bash
$ singularity exec <container> /usr/local/bin/mm2plus.sse4.1
$ podman run --it --rm --entrypoint /usr/local/bin/mm2plus.sse4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mm2plus.sse4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mm2plus.sse4.2

```bash
$ singularity exec <container> /usr/local/bin/mm2plus.sse4.2
$ podman run --it --rm --entrypoint /usr/local/bin/mm2plus.sse4.2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mm2plus.sse4.2   -v ${PWD} -w ${PWD} <container> -c " $@"
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
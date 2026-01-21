---
layout: container
name:  "quay.io/biocontainers/fastmd5"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastmd5/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastmd5/container.yaml"
updated_at: "2026-01-21 04:23:33.760355"
latest: "1.0.0--h3ab6199_0"
container_url: "https://biocontainers.pro/tools/fastmd5"
aliases:
 - "fastmd5"
versions:
 - "1.0.0--h3ab6199_0"
description: "singularity registry hpc automated addition for fastmd5"
config: {"url": "https://biocontainers.pro/tools/fastmd5", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for fastmd5", "latest": {"1.0.0--h3ab6199_0": "sha256:77174d0332ac5a0fe338b629df526f775e2049b58539e6250cbdf6577c411ac7"}, "tags": {"1.0.0--h3ab6199_0": "sha256:77174d0332ac5a0fe338b629df526f775e2049b58539e6250cbdf6577c411ac7"}, "docker": "quay.io/biocontainers/fastmd5", "aliases": {"fastmd5": "/usr/local/bin/fastmd5"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastmd5.
singularity registry hpc automated addition for fastmd5
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastmd5
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastmd5:1.0.0--h3ab6199_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastmd5/1.0.0--h3ab6199_0
$ module help quay.io/biocontainers/fastmd5/1.0.0--h3ab6199_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastmd5-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastmd5-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastmd5-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastmd5-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastmd5-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastmd5-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastmd5

```bash
$ singularity exec <container> /usr/local/bin/fastmd5
$ podman run --it --rm --entrypoint /usr/local/bin/fastmd5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastmd5   -v ${PWD} -w ${PWD} <container> -c " $@"
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
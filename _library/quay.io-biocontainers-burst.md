---
layout: container
name:  "quay.io/biocontainers/burst"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/burst/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/burst/container.yaml"
updated_at: "2022-11-08 00:32:16.783353"
latest: "v1.0--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/burst"
aliases:
 - "bcov2-strip"
 - "burst_linux_DB12"
 - "burst_linux_DB15"
 - "lingenome"
 - "t2gg"
versions:
 - "v1.0--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for burst"
config: {"url": "https://biocontainers.pro/tools/burst", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for burst", "latest": {"v1.0--hdfd78af_1": "sha256:18940befe4320d7b01cff71eff828661e40cae55aa5c5d7c2ec833c3c08f0fde"}, "tags": {"v1.0--hdfd78af_1": "sha256:18940befe4320d7b01cff71eff828661e40cae55aa5c5d7c2ec833c3c08f0fde"}, "docker": "quay.io/biocontainers/burst", "aliases": {"bcov2-strip": "/usr/local/bin/bcov2-strip", "burst_linux_DB12": "/usr/local/bin/burst_linux_DB12", "burst_linux_DB15": "/usr/local/bin/burst_linux_DB15", "lingenome": "/usr/local/bin/lingenome", "t2gg": "/usr/local/bin/t2gg"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/burst.
shpc-registry automated BioContainers addition for burst
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/burst
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/burst:v1.0--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/burst/v1.0--hdfd78af_1
$ module help quay.io/biocontainers/burst/v1.0--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### burst-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### burst-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### burst-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### burst-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### burst-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### burst-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bcov2-strip

```bash
$ singularity exec <container> /usr/local/bin/bcov2-strip
$ podman run --it --rm --entrypoint /usr/local/bin/bcov2-strip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcov2-strip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### burst_linux_DB12

```bash
$ singularity exec <container> /usr/local/bin/burst_linux_DB12
$ podman run --it --rm --entrypoint /usr/local/bin/burst_linux_DB12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/burst_linux_DB12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### burst_linux_DB15

```bash
$ singularity exec <container> /usr/local/bin/burst_linux_DB15
$ podman run --it --rm --entrypoint /usr/local/bin/burst_linux_DB15   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/burst_linux_DB15   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lingenome

```bash
$ singularity exec <container> /usr/local/bin/lingenome
$ podman run --it --rm --entrypoint /usr/local/bin/lingenome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lingenome   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### t2gg

```bash
$ singularity exec <container> /usr/local/bin/t2gg
$ podman run --it --rm --entrypoint /usr/local/bin/t2gg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/t2gg   -v ${PWD} -w ${PWD} <container> -c " $@"
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
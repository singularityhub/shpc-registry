---
layout: container
name:  "quay.io/biocontainers/reaper-trim"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/reaper-trim/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/reaper-trim/container.yaml"
updated_at: "2026-07-01 15:34:19.526021"
latest: "17.257--h118bc1c_0"
container_url: "https://biocontainers.pro/tools/reaper-trim"
aliases:
 - "minion"
 - "reaper"
 - "swan"
 - "tally"
versions:
 - "17.257--h118bc1c_0"
description: "singularity registry hpc automated addition for reaper-trim"
config: {"url": "https://biocontainers.pro/tools/reaper-trim", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for reaper-trim", "latest": {"17.257--h118bc1c_0": "sha256:d124302115aadcb2cc8d70c68f2a0a0f21569feaed323fdb97d6e328cda87027"}, "tags": {"17.257--h118bc1c_0": "sha256:d124302115aadcb2cc8d70c68f2a0a0f21569feaed323fdb97d6e328cda87027"}, "docker": "quay.io/biocontainers/reaper-trim", "aliases": {"minion": "/usr/local/bin/minion", "reaper": "/usr/local/bin/reaper", "swan": "/usr/local/bin/swan", "tally": "/usr/local/bin/tally"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/reaper-trim.
singularity registry hpc automated addition for reaper-trim
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/reaper-trim
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/reaper-trim:17.257--h118bc1c_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/reaper-trim/17.257--h118bc1c_0
$ module help quay.io/biocontainers/reaper-trim/17.257--h118bc1c_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### reaper-trim-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### reaper-trim-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### reaper-trim-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### reaper-trim-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### reaper-trim-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### reaper-trim-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### minion

```bash
$ singularity exec <container> /usr/local/bin/minion
$ podman run --it --rm --entrypoint /usr/local/bin/minion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minion   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reaper

```bash
$ singularity exec <container> /usr/local/bin/reaper
$ podman run --it --rm --entrypoint /usr/local/bin/reaper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reaper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### swan

```bash
$ singularity exec <container> /usr/local/bin/swan
$ podman run --it --rm --entrypoint /usr/local/bin/swan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/swan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tally

```bash
$ singularity exec <container> /usr/local/bin/tally
$ podman run --it --rm --entrypoint /usr/local/bin/tally   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tally   -v ${PWD} -w ${PWD} <container> -c " $@"
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
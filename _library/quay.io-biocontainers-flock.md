---
layout: container
name:  "quay.io/biocontainers/flock"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/flock/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/flock/container.yaml"
updated_at: "2025-08-19 03:28:16.482807"
latest: "1.0--h470a237_2"
container_url: "https://biocontainers.pro/tools/flock"
aliases:
 - "cent_adjust"
 - "flock1"
 - "flock2"
versions:
 - "1.0--h470a237_2"
description: "shpc-registry automated BioContainers addition for flock"
config: {"url": "https://biocontainers.pro/tools/flock", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for flock", "latest": {"1.0--h470a237_2": "sha256:13a9138efa512c2936d34eb5f5a5b191302e45a25892c8a89a5ce5c828908cf4"}, "tags": {"1.0--h470a237_2": "sha256:13a9138efa512c2936d34eb5f5a5b191302e45a25892c8a89a5ce5c828908cf4"}, "docker": "quay.io/biocontainers/flock", "aliases": {"cent_adjust": "/usr/local/bin/cent_adjust", "flock1": "/usr/local/bin/flock1", "flock2": "/usr/local/bin/flock2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/flock.
shpc-registry automated BioContainers addition for flock
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/flock
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/flock:1.0--h470a237_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/flock/1.0--h470a237_2
$ module help quay.io/biocontainers/flock/1.0--h470a237_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### flock-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### flock-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### flock-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### flock-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### flock-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### flock-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cent_adjust

```bash
$ singularity exec <container> /usr/local/bin/cent_adjust
$ podman run --it --rm --entrypoint /usr/local/bin/cent_adjust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cent_adjust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flock1

```bash
$ singularity exec <container> /usr/local/bin/flock1
$ podman run --it --rm --entrypoint /usr/local/bin/flock1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flock1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flock2

```bash
$ singularity exec <container> /usr/local/bin/flock2
$ podman run --it --rm --entrypoint /usr/local/bin/flock2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flock2   -v ${PWD} -w ${PWD} <container> -c " $@"
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
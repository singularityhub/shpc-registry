---
layout: container
name:  "quay.io/biocontainers/bramble"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bramble/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bramble/container.yaml"
updated_at: "2026-08-21 18:45:01.286642"
latest: "0.1.8--hdb859ee_0"
container_url: "https://biocontainers.pro/tools/bramble"
aliases:
 - "bramble"
 - "bramble-rs"
versions:
 - "0.1.8--hdb859ee_0"
description: "singularity registry hpc automated addition for bramble"
config: {"url": "https://biocontainers.pro/tools/bramble", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bramble", "latest": {"0.1.8--hdb859ee_0": "sha256:2d9b543d18517493576b0c60f7e70f902af618249528b7cdd634dae7a1499259"}, "tags": {"0.1.8--hdb859ee_0": "sha256:2d9b543d18517493576b0c60f7e70f902af618249528b7cdd634dae7a1499259"}, "docker": "quay.io/biocontainers/bramble", "aliases": {"bramble": "/usr/local/bin/bramble", "bramble-rs": "/usr/local/bin/bramble-rs"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bramble.
singularity registry hpc automated addition for bramble
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bramble
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bramble:0.1.8--hdb859ee_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bramble/0.1.8--hdb859ee_0
$ module help quay.io/biocontainers/bramble/0.1.8--hdb859ee_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bramble-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bramble-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bramble-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bramble-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bramble-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bramble-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bramble

```bash
$ singularity exec <container> /usr/local/bin/bramble
$ podman run --it --rm --entrypoint /usr/local/bin/bramble   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bramble   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bramble-rs

```bash
$ singularity exec <container> /usr/local/bin/bramble-rs
$ podman run --it --rm --entrypoint /usr/local/bin/bramble-rs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bramble-rs   -v ${PWD} -w ${PWD} <container> -c " $@"
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
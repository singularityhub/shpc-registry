---
layout: container
name:  "quay.io/biocontainers/sshash"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sshash/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sshash/container.yaml"
updated_at: "2025-12-18 03:47:23.982340"
latest: "4.0.0--haf24da9_0"
container_url: "https://biocontainers.pro/tools/sshash"
aliases:
 - "sshash"
versions:
 - "4.0.0--haf24da9_0"
description: "singularity registry hpc automated addition for sshash"
config: {"url": "https://biocontainers.pro/tools/sshash", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for sshash", "latest": {"4.0.0--haf24da9_0": "sha256:83d971cf857b249dd2227c84a63028289a1a24afffdc6e8c38c9003c8dd2800a"}, "tags": {"4.0.0--haf24da9_0": "sha256:83d971cf857b249dd2227c84a63028289a1a24afffdc6e8c38c9003c8dd2800a"}, "docker": "quay.io/biocontainers/sshash", "aliases": {"sshash": "/usr/local/bin/sshash"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sshash.
singularity registry hpc automated addition for sshash
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sshash
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sshash:4.0.0--haf24da9_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sshash/4.0.0--haf24da9_0
$ module help quay.io/biocontainers/sshash/4.0.0--haf24da9_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sshash-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sshash-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sshash-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sshash-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sshash-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sshash-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sshash

```bash
$ singularity exec <container> /usr/local/bin/sshash
$ podman run --it --rm --entrypoint /usr/local/bin/sshash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sshash   -v ${PWD} -w ${PWD} <container> -c " $@"
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
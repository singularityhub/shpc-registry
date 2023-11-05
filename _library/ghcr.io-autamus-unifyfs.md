---
layout: container
name:  "ghcr.io/autamus/unifyfs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/unifyfs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/unifyfs/container.yaml"
updated_at: "2023-11-05 03:09:50.890785"
latest: "1.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/unifyfs"
aliases:
 - "unifyfs"
 - "unifyfs-config"
 - "unifyfsd"
versions:
 - "0.9.2"
 - "latest"
 - "1.0"
description: "User level file system that enables applications to use node-local storage as burst buffers for shared files."
config: {"docker": "ghcr.io/autamus/unifyfs", "url": "https://github.com/orgs/autamus/packages/container/package/unifyfs", "maintainer": "@vsoch", "description": "User level file system that enables applications to use node-local storage as burst buffers for shared files.", "latest": {"1.0": "sha256:338c2aa13db3dd72b6cc4294b02663af630560ccda28c59cd9a35403b2420684"}, "tags": {"0.9.2": "sha256:2b2a925b3e1d7fec92bdcf74f93d0e9e2aa278a3e778283ec7d7d7230da83fde", "latest": "sha256:338c2aa13db3dd72b6cc4294b02663af630560ccda28c59cd9a35403b2420684", "1.0": "sha256:338c2aa13db3dd72b6cc4294b02663af630560ccda28c59cd9a35403b2420684"}, "aliases": {"unifyfs": "/opt/view/bin/unifyfs", "unifyfs-config": "/opt/view/bin/unifyfs-config", "unifyfsd": "/opt/view/bin/unifyfsd"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/unifyfs.
User level file system that enables applications to use node-local storage as burst buffers for shared files.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/unifyfs
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/unifyfs:1.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/unifyfs/1.0
$ module help ghcr.io/autamus/unifyfs/1.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### unifyfs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### unifyfs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### unifyfs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### unifyfs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### unifyfs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### unifyfs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### unifyfs

```bash
$ singularity exec <container> /opt/view/bin/unifyfs
$ podman run --it --rm --entrypoint /opt/view/bin/unifyfs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/unifyfs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unifyfs-config

```bash
$ singularity exec <container> /opt/view/bin/unifyfs-config
$ podman run --it --rm --entrypoint /opt/view/bin/unifyfs-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/unifyfs-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unifyfsd

```bash
$ singularity exec <container> /opt/view/bin/unifyfsd
$ podman run --it --rm --entrypoint /opt/view/bin/unifyfsd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/unifyfsd   -v ${PWD} -w ${PWD} <container> -c " $@"
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
---
layout: container
name:  "hashicorp/consul"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/hashicorp/consul/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/hashicorp/consul/container.yaml"
updated_at: "2024-02-28 02:21:49.086300"
latest: "1.18.0-rc1"
container_url: "https://hub.docker.com/r/hashicorp/consul"
aliases:
 - "consul"
 - "docker-entrypoint.sh"
versions:
 - "1.16"
 - "1.17.0-rc1"
 - "1.17"
 - "1.18.0-rc1"
description: "Automatic build of consul based on the current release."
config: {"docker": "hashicorp/consul", "maintainer": "@vsoch", "url": "https://hub.docker.com/r/hashicorp/consul", "description": "Automatic build of consul based on the current release.", "latest": {"1.18.0-rc1": "sha256:0e20dd2d4cc42b7efd888334432e5524c58acc37f7fd6541269c61c15afe5328"}, "tags": {"1.16": "sha256:e4c674e01776d5bd8c6d85462c7fb057b2c5ec46256e2d0ac2737caf122decd7", "1.17.0-rc1": "sha256:a44a99380b89e66caa4a6511212bff40fa1f4b89d62374bd4ebcf3897c05976b", "1.17": "sha256:fa5020e2307bc941e4317207de1ab55f2c7a8cd6b02c0592cce1cd20ec8a7f87", "1.18.0-rc1": "sha256:0e20dd2d4cc42b7efd888334432e5524c58acc37f7fd6541269c61c15afe5328"}, "aliases": {"consul": "/bin/consul", "docker-entrypoint.sh": "/usr/local/bin/docker-entrypoint.sh"}}
---

This module is a singularity container wrapper for hashicorp/consul.
Automatic build of consul based on the current release.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install hashicorp/consul
```

Or a specific version:

```bash
$ shpc install hashicorp/consul:1.18.0-rc1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load hashicorp/consul/1.18.0-rc1
$ module help hashicorp/consul/1.18.0-rc1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### consul-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### consul-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### consul-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### consul-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### consul-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### consul-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### consul

```bash
$ singularity exec <container> /bin/consul
$ podman run --it --rm --entrypoint /bin/consul   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /bin/consul   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### docker-entrypoint.sh

```bash
$ singularity exec <container> /usr/local/bin/docker-entrypoint.sh
$ podman run --it --rm --entrypoint /usr/local/bin/docker-entrypoint.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/docker-entrypoint.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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
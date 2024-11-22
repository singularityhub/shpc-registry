---
layout: container
name:  "ghcr.io/autamus/caliper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/caliper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/caliper/container.yaml"
updated_at: "2024-11-22 03:53:08.538068"
latest: "2.7.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/caliper"
aliases:
 - "cali-query"
 - "cali-stat"
versions:
 - "2.6.0"
 - "2.7.0"
 - "latest"
description: "Caliper is a program instrumentation and performance measurement framework."
config: {"docker": "ghcr.io/autamus/caliper", "url": "https://github.com/orgs/autamus/packages/container/package/caliper", "maintainer": "@vsoch", "description": "Caliper is a program instrumentation and performance measurement framework.", "latest": {"2.7.0": "sha256:fa18e4ad79b34e701713ed964cf766036b77bf120b7416aa826ad6d64e632a1e"}, "tags": {"2.6.0": "sha256:f6dce0cfbd6149dc02ec59916a40d8d841224cd79d03f2fd76b33264ae660fe5", "2.7.0": "sha256:fa18e4ad79b34e701713ed964cf766036b77bf120b7416aa826ad6d64e632a1e", "latest": "sha256:fa18e4ad79b34e701713ed964cf766036b77bf120b7416aa826ad6d64e632a1e"}, "aliases": {"cali-query": "/opt/view/bin/cali-query", "cali-stat": "/opt/view/bin/cali-stat"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/caliper.
Caliper is a program instrumentation and performance measurement framework.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/caliper
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/caliper:2.7.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/caliper/2.7.0
$ module help ghcr.io/autamus/caliper/2.7.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### caliper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### caliper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### caliper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### caliper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### caliper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### caliper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cali-query

```bash
$ singularity exec <container> /opt/view/bin/cali-query
$ podman run --it --rm --entrypoint /opt/view/bin/cali-query   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/cali-query   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cali-stat

```bash
$ singularity exec <container> /opt/view/bin/cali-stat
$ podman run --it --rm --entrypoint /opt/view/bin/cali-stat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/cali-stat   -v ${PWD} -w ${PWD} <container> -c " $@"
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
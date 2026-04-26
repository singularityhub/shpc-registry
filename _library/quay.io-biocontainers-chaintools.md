---
layout: container
name:  "quay.io/biocontainers/chaintools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/chaintools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/chaintools/container.yaml"
updated_at: "2026-04-26 05:49:57.449384"
latest: "0.0.2--hd612981_0"
container_url: "https://biocontainers.pro/tools/chaintools"
aliases:
 - "benchmark"
 - "chaintools"
versions:
 - "0.0.2--hd612981_0"
description: "singularity registry hpc automated addition for chaintools"
config: {"url": "https://biocontainers.pro/tools/chaintools", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for chaintools", "latest": {"0.0.2--hd612981_0": "sha256:c9a0e07475aeac8498d885606d140cf12dcebaf37763dc3fc8753fd2ac7a9b1e"}, "tags": {"0.0.2--hd612981_0": "sha256:c9a0e07475aeac8498d885606d140cf12dcebaf37763dc3fc8753fd2ac7a9b1e"}, "docker": "quay.io/biocontainers/chaintools", "aliases": {"benchmark": "/usr/local/bin/benchmark", "chaintools": "/usr/local/bin/chaintools"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/chaintools.
singularity registry hpc automated addition for chaintools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/chaintools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/chaintools:0.0.2--hd612981_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/chaintools/0.0.2--hd612981_0
$ module help quay.io/biocontainers/chaintools/0.0.2--hd612981_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### chaintools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### chaintools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### chaintools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### chaintools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### chaintools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### chaintools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### benchmark

```bash
$ singularity exec <container> /usr/local/bin/benchmark
$ podman run --it --rm --entrypoint /usr/local/bin/benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chaintools

```bash
$ singularity exec <container> /usr/local/bin/chaintools
$ podman run --it --rm --entrypoint /usr/local/bin/chaintools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chaintools   -v ${PWD} -w ${PWD} <container> -c " $@"
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
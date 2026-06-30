---
layout: container
name:  "quay.io/biocontainers/r-teddy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-teddy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-teddy/container.yaml"
updated_at: "2026-06-30 06:48:45.114889"
latest: "1.1.8--r41hcf09f9e_0"
container_url: "https://biocontainers.pro/tools/r-teddy"
aliases:
 - "x86_64-conda-linux-gnu.cfg"
versions:
 - "1.0.3--r41hcf09f9e_0"
 - "1.1.8--r41hcf09f9e_0"
description: "singularity registry hpc automated addition for r-teddy"
config: {"url": "https://biocontainers.pro/tools/r-teddy", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for r-teddy", "latest": {"1.1.8--r41hcf09f9e_0": "sha256:1c58e474ac37c50658c0b764db72218360f789652d3df5cc4735915e99194797"}, "tags": {"1.0.3--r41hcf09f9e_0": "sha256:fd9f0915fa0db0f05a6dc47aad203739f15af9b8801473ecccd8a1d39902a70c", "1.1.8--r41hcf09f9e_0": "sha256:1c58e474ac37c50658c0b764db72218360f789652d3df5cc4735915e99194797"}, "docker": "quay.io/biocontainers/r-teddy", "aliases": {"x86_64-conda-linux-gnu.cfg": "/usr/local/bin/x86_64-conda-linux-gnu.cfg"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-teddy.
singularity registry hpc automated addition for r-teddy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-teddy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-teddy:1.1.8--r41hcf09f9e_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-teddy/1.1.8--r41hcf09f9e_0
$ module help quay.io/biocontainers/r-teddy/1.1.8--r41hcf09f9e_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-teddy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-teddy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-teddy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-teddy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-teddy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-teddy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu.cfg

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu.cfg
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
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
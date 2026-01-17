---
layout: container
name:  "quay.io/biocontainers/r-rspectral"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-rspectral/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-rspectral/container.yaml"
updated_at: "2026-01-17 04:11:56.424959"
latest: "1.0.0.14--r44h40dc89f_0"
container_url: "https://biocontainers.pro/tools/r-rspectral"
aliases:
 - "glpsol"
versions:
 - "1.0.0.9--r42hecf12ef_0"
 - "1.0.0.10--r42hecf12ef_0"
 - "1.0.0.10--r42h21a89ab_1"
 - "1.0.0.10--r43h21a89ab_2"
 - "1.0.0.10--r44h40dc89f_3"
 - "1.0.0.14--r44h40dc89f_0"
description: "singularity registry hpc automated addition for r-rspectral"
config: {"url": "https://biocontainers.pro/tools/r-rspectral", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for r-rspectral", "latest": {"1.0.0.14--r44h40dc89f_0": "sha256:c36dbc0271f93bc9979fc69ab0c6c80c44501f24da301cc4ca9f3924593f1b38"}, "tags": {"1.0.0.9--r42hecf12ef_0": "sha256:51bcbb0ef8be98a4d7e7cf66c01748023d15960eb8e2cf1e56f85cd215dfb38c", "1.0.0.10--r42hecf12ef_0": "sha256:81c0e7f0ff02c61e0a7c02b5da1aae3780ae1ce8e01fa6edd13c66f05bf34767", "1.0.0.10--r42h21a89ab_1": "sha256:7dcddd2c7c2efa6b720170755464c06e2176721831da98a022ca242c444a34e0", "1.0.0.10--r43h21a89ab_2": "sha256:a322994baf921f4c26bd2932350f548cf1c83326c8c5d53ea4e3df6d38413a23", "1.0.0.10--r44h40dc89f_3": "sha256:535fdbfc8f2cbca9dd1c515863034a05b3beb6f144d1573ed4ec20c2cb9098e5", "1.0.0.14--r44h40dc89f_0": "sha256:c36dbc0271f93bc9979fc69ab0c6c80c44501f24da301cc4ca9f3924593f1b38"}, "docker": "quay.io/biocontainers/r-rspectral", "aliases": {"glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-rspectral.
singularity registry hpc automated addition for r-rspectral
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-rspectral
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-rspectral:1.0.0.14--r44h40dc89f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-rspectral/1.0.0.14--r44h40dc89f_0
$ module help quay.io/biocontainers/r-rspectral/1.0.0.14--r44h40dc89f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-rspectral-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-rspectral-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-rspectral-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-rspectral-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-rspectral-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-rspectral-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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
---
layout: container
name:  "quay.io/biocontainers/eagle"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/eagle/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/eagle/container.yaml"
updated_at: "2022-10-27 00:50:13.057077"
latest: "0.9.4.6--pyh5ca1d4c_0"
container_url: "https://biocontainers.pro/tools/eagle"
aliases:
 - "eagle"
 - "sqt"
versions:
 - "0.9.4.6--pyh5ca1d4c_0"
description: "shpc-registry automated BioContainers addition for eagle"
config: {"url": "https://biocontainers.pro/tools/eagle", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for eagle", "latest": {"0.9.4.6--pyh5ca1d4c_0": "sha256:4fa74d66cc6dc1274361a3e8e85a0e1c6182766e038994b48eab05e0d0a19220"}, "tags": {"0.9.4.6--pyh5ca1d4c_0": "sha256:4fa74d66cc6dc1274361a3e8e85a0e1c6182766e038994b48eab05e0d0a19220"}, "docker": "quay.io/biocontainers/eagle", "aliases": {"eagle": "/usr/local/bin/eagle", "sqt": "/usr/local/bin/sqt"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/eagle.
shpc-registry automated BioContainers addition for eagle
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/eagle
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/eagle:0.9.4.6--pyh5ca1d4c_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/eagle/0.9.4.6--pyh5ca1d4c_0
$ module help quay.io/biocontainers/eagle/0.9.4.6--pyh5ca1d4c_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### eagle-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### eagle-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### eagle-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### eagle-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### eagle-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### eagle-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### eagle

```bash
$ singularity exec <container> /usr/local/bin/eagle
$ podman run --it --rm --entrypoint /usr/local/bin/eagle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eagle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sqt

```bash
$ singularity exec <container> /usr/local/bin/sqt
$ podman run --it --rm --entrypoint /usr/local/bin/sqt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sqt   -v ${PWD} -w ${PWD} <container> -c " $@"
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
---
layout: container
name:  "quay.io/biocontainers/rapmap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rapmap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rapmap/container.yaml"
updated_at: "2023-12-30 04:16:06.948446"
latest: "0.6.0--h6a68c12_5"
container_url: "https://biocontainers.pro/tools/rapmap"
aliases:
 - "rapmap"
versions:
 - "v0.2.1--hfc679d8_2"
 - "0.6.0--hf1761c0_3"
 - "0.5.0--hfc679d8_0"
 - "0.6.0--h6a68c12_5"
description: "shpc-registry automated BioContainers addition for rapmap"
config: {"url": "https://biocontainers.pro/tools/rapmap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rapmap", "latest": {"0.6.0--h6a68c12_5": "sha256:21023f8d6f723c403237be0812ec8f43cc223c3a00d557ec20e943634071d7d0"}, "tags": {"v0.2.1--hfc679d8_2": "sha256:b17abbee8b67810c8291d09721a3d982edf74800ce5d4879e9d265391a5756c4", "0.6.0--hf1761c0_3": "sha256:863de1f30d00960140a1df9b7ee69672f1afef7e6346805dddb6d4e307d8e58f", "0.5.0--hfc679d8_0": "sha256:a973b5c35e2343084e603fd576e8a2043f655c4b9a93da776f2601b72dfa48c0", "0.6.0--h6a68c12_5": "sha256:21023f8d6f723c403237be0812ec8f43cc223c3a00d557ec20e943634071d7d0"}, "docker": "quay.io/biocontainers/rapmap", "aliases": {"rapmap": "/usr/local/bin/rapmap"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rapmap.
shpc-registry automated BioContainers addition for rapmap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rapmap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rapmap:0.6.0--h6a68c12_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rapmap/0.6.0--h6a68c12_5
$ module help quay.io/biocontainers/rapmap/0.6.0--h6a68c12_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rapmap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rapmap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rapmap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rapmap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rapmap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rapmap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rapmap

```bash
$ singularity exec <container> /usr/local/bin/rapmap
$ podman run --it --rm --entrypoint /usr/local/bin/rapmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rapmap   -v ${PWD} -w ${PWD} <container> -c " $@"
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
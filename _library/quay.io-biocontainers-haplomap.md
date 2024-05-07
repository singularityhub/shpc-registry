---
layout: container
name:  "quay.io/biocontainers/haplomap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/haplomap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/haplomap/container.yaml"
updated_at: "2024-05-07 02:44:31.968404"
latest: "0.1.0--h8cec121_2"
container_url: "https://biocontainers.pro/tools/haplomap"
aliases:
 - "haplomap"
versions:
 - "0.1.0--hb5289fc_0"
 - "0.1.0--h8cec121_2"
description: "singularity registry hpc automated addition for haplomap"
config: {"url": "https://biocontainers.pro/tools/haplomap", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for haplomap", "latest": {"0.1.0--h8cec121_2": "sha256:66d41ba8edb455fbb1851328025c285b16ffe460caba74cdbf178fd83776b968"}, "tags": {"0.1.0--hb5289fc_0": "sha256:b9e6e7325db8b1abd95c2ce0235ff282477ab154292b35e95dfeffcaf102e05b", "0.1.0--h8cec121_2": "sha256:66d41ba8edb455fbb1851328025c285b16ffe460caba74cdbf178fd83776b968"}, "docker": "quay.io/biocontainers/haplomap", "aliases": {"haplomap": "/usr/local/bin/haplomap"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/haplomap.
singularity registry hpc automated addition for haplomap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/haplomap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/haplomap:0.1.0--h8cec121_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/haplomap/0.1.0--h8cec121_2
$ module help quay.io/biocontainers/haplomap/0.1.0--h8cec121_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### haplomap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### haplomap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### haplomap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### haplomap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### haplomap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### haplomap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### haplomap

```bash
$ singularity exec <container> /usr/local/bin/haplomap
$ podman run --it --rm --entrypoint /usr/local/bin/haplomap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/haplomap   -v ${PWD} -w ${PWD} <container> -c " $@"
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
---
layout: container
name:  "quay.io/biocontainers/haplomap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/haplomap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/haplomap/container.yaml"
updated_at: "2025-11-04 03:34:46.159200"
latest: "0.1.2--h4656aac_1"
container_url: "https://biocontainers.pro/tools/haplomap"
aliases:
 - "haplomap"
versions:
 - "0.1.0--hb5289fc_0"
 - "0.1.0--h8cec121_2"
 - "0.1.1--h8cec121_0"
 - "0.1.2--h8cec121_0"
 - "0.1.2--h4656aac_1"
description: "singularity registry hpc automated addition for haplomap"
config: {"url": "https://biocontainers.pro/tools/haplomap", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for haplomap", "latest": {"0.1.2--h4656aac_1": "sha256:f43f72befb10c310b7c30574df16bc4a3d0d67bfe33b142e531dd136f53d78d4"}, "tags": {"0.1.0--hb5289fc_0": "sha256:b9e6e7325db8b1abd95c2ce0235ff282477ab154292b35e95dfeffcaf102e05b", "0.1.0--h8cec121_2": "sha256:66d41ba8edb455fbb1851328025c285b16ffe460caba74cdbf178fd83776b968", "0.1.1--h8cec121_0": "sha256:98d6ff8df596f7d5b569134e520e892e28337410513b2953b0f64808ff43452b", "0.1.2--h8cec121_0": "sha256:748b287c7f9f4a2629c4a8bab4fc4f4dae0161615657b92ba08a0c49089f66b8", "0.1.2--h4656aac_1": "sha256:f43f72befb10c310b7c30574df16bc4a3d0d67bfe33b142e531dd136f53d78d4"}, "docker": "quay.io/biocontainers/haplomap", "aliases": {"haplomap": "/usr/local/bin/haplomap"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/haplomap.
singularity registry hpc automated addition for haplomap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/haplomap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/haplomap:0.1.2--h4656aac_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/haplomap/0.1.2--h4656aac_1
$ module help quay.io/biocontainers/haplomap/0.1.2--h4656aac_1
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
---
layout: container
name:  "quay.io/biocontainers/ksw"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ksw/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ksw/container.yaml"
updated_at: "2024-09-14 02:44:28.613204"
latest: "0.2.3--h43eeafb_0"
container_url: "https://biocontainers.pro/tools/ksw"
aliases:
 - "ksw"
versions:
 - "0.2.1--h5b5514e_3"
 - "0.2.2--h5b5514e_0"
 - "0.2.2--h43eeafb_2"
 - "0.2.3--h43eeafb_0"
description: "shpc-registry automated BioContainers addition for ksw"
config: {"url": "https://biocontainers.pro/tools/ksw", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ksw", "latest": {"0.2.3--h43eeafb_0": "sha256:d03eaa94451c56f2aff84395aac6d37ed3c9b483b8a7aae9224786c50ae8dd2a"}, "tags": {"0.2.1--h5b5514e_3": "sha256:77a4585738abd15335b3265c70ebfc744670cc874793c6332dd495fec3a7e262", "0.2.2--h5b5514e_0": "sha256:97029f48195f9a33ae194b2fd8f46429e347b52f78f712577f3c3d41355b1e60", "0.2.2--h43eeafb_2": "sha256:12acb54954a0ec5a052d21d84695af470934b1b34b196d0b9573f66b5b70a3c2", "0.2.3--h43eeafb_0": "sha256:d03eaa94451c56f2aff84395aac6d37ed3c9b483b8a7aae9224786c50ae8dd2a"}, "docker": "quay.io/biocontainers/ksw", "aliases": {"ksw": "/usr/local/bin/ksw"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ksw.
shpc-registry automated BioContainers addition for ksw
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ksw
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ksw:0.2.3--h43eeafb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ksw/0.2.3--h43eeafb_0
$ module help quay.io/biocontainers/ksw/0.2.3--h43eeafb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ksw-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ksw-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ksw-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ksw-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ksw-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ksw-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ksw

```bash
$ singularity exec <container> /usr/local/bin/ksw
$ podman run --it --rm --entrypoint /usr/local/bin/ksw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ksw   -v ${PWD} -w ${PWD} <container> -c " $@"
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
---
layout: container
name:  "quay.io/biocontainers/minirmd"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/minirmd/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/minirmd/container.yaml"
updated_at: "2025-10-13 04:06:56.804404"
latest: "1.1--h077b44d_5"
container_url: "https://biocontainers.pro/tools/minirmd"
aliases:
 - "minirmd"
versions:
 - "1.1--hd03093a_2"
 - "1.1--hdcf5f25_4"
 - "1.1--h077b44d_5"
description: "shpc-registry automated BioContainers addition for minirmd"
config: {"url": "https://biocontainers.pro/tools/minirmd", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for minirmd", "latest": {"1.1--h077b44d_5": "sha256:6570d46ebf9fcfd0c78aca1599dce73fbe864871290d1cf230d057981e47da22"}, "tags": {"1.1--hd03093a_2": "sha256:874389f8e3335703781c6cb976b2bb1d9937ef6b9b22959b9efef0bb17dbb6a5", "1.1--hdcf5f25_4": "sha256:b1e96b1aaf8e78d11c847058e8ca253acb46d02833d43e1cf285383bab9af0a1", "1.1--h077b44d_5": "sha256:6570d46ebf9fcfd0c78aca1599dce73fbe864871290d1cf230d057981e47da22"}, "docker": "quay.io/biocontainers/minirmd", "aliases": {"minirmd": "/usr/local/bin/minirmd"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/minirmd.
shpc-registry automated BioContainers addition for minirmd
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/minirmd
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/minirmd:1.1--h077b44d_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/minirmd/1.1--h077b44d_5
$ module help quay.io/biocontainers/minirmd/1.1--h077b44d_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### minirmd-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### minirmd-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### minirmd-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### minirmd-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### minirmd-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### minirmd-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### minirmd

```bash
$ singularity exec <container> /usr/local/bin/minirmd
$ podman run --it --rm --entrypoint /usr/local/bin/minirmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minirmd   -v ${PWD} -w ${PWD} <container> -c " $@"
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
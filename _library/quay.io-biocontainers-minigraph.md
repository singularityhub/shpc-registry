---
layout: container
name:  "quay.io/biocontainers/minigraph"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/minigraph/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/minigraph/container.yaml"
updated_at: "2024-03-11 03:06:09.961464"
latest: "0.20--he4a0461_2"
container_url: "https://biocontainers.pro/tools/minigraph"
aliases:
 - "minigraph"
versions:
 - "0.19--h7132678_1"
 - "0.20--h7132678_0"
 - "0.20--he4a0461_2"
description: "shpc-registry automated BioContainers addition for minigraph"
config: {"url": "https://biocontainers.pro/tools/minigraph", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for minigraph", "latest": {"0.20--he4a0461_2": "sha256:530228e3e79a97454e1d852e5b866353d6a8148dc8cd2ba08c7ebc01f2d04f63"}, "tags": {"0.19--h7132678_1": "sha256:724ed20de63a1b0e6ce756719edcf53c0df06885a640101cdd6fd5769e8d6a88", "0.20--h7132678_0": "sha256:e41e5ae2793d0b47165223220e06567566860e01b795900356a2513e5ff48e1d", "0.20--he4a0461_2": "sha256:530228e3e79a97454e1d852e5b866353d6a8148dc8cd2ba08c7ebc01f2d04f63"}, "docker": "quay.io/biocontainers/minigraph", "aliases": {"minigraph": "/usr/local/bin/minigraph"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/minigraph.
shpc-registry automated BioContainers addition for minigraph
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/minigraph
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/minigraph:0.20--he4a0461_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/minigraph/0.20--he4a0461_2
$ module help quay.io/biocontainers/minigraph/0.20--he4a0461_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### minigraph-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### minigraph-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### minigraph-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### minigraph-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### minigraph-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### minigraph-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### minigraph

```bash
$ singularity exec <container> /usr/local/bin/minigraph
$ podman run --it --rm --entrypoint /usr/local/bin/minigraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minigraph   -v ${PWD} -w ${PWD} <container> -c " $@"
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
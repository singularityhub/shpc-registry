---
layout: container
name:  "quay.io/biocontainers/lca"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lca/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/lca/container.yaml"
updated_at: "2025-06-06 12:07:31.485037"
latest: "0.25--h077b44d_1"
container_url: "https://biocontainers.pro/tools/lca"
aliases:
 - "LCA"
versions:
 - "0.23--hd03093a_1"
 - "0.24--hdcf5f25_2"
 - "0.25--hdcf5f25_0"
 - "0.25--h077b44d_1"
description: "shpc-registry automated BioContainers addition for lca"
config: {"url": "https://biocontainers.pro/tools/lca", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for lca", "latest": {"0.25--h077b44d_1": "sha256:82b0159a2fc848233cbfd037c8a98038b54c5cecb13ae7c290260ac1259c5772"}, "tags": {"0.23--hd03093a_1": "sha256:914333ec6aedc403748387c136645c0db05125b4b2571b74eafb00e67df49ab5", "0.24--hdcf5f25_2": "sha256:74a8caf952ed34e1e6fd2e0bfda1a744b50fbaffb07695853b57afb9633d64a0", "0.25--hdcf5f25_0": "sha256:e3705ddb09867d75f041a26f165f5961fc9576b12c9fe44513aed5d7c07c5d18", "0.25--h077b44d_1": "sha256:82b0159a2fc848233cbfd037c8a98038b54c5cecb13ae7c290260ac1259c5772"}, "docker": "quay.io/biocontainers/lca", "aliases": {"LCA": "/usr/local/bin/LCA"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/lca.
shpc-registry automated BioContainers addition for lca
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lca
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lca:0.25--h077b44d_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lca/0.25--h077b44d_1
$ module help quay.io/biocontainers/lca/0.25--h077b44d_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lca-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lca-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lca-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lca-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lca-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lca-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### LCA

```bash
$ singularity exec <container> /usr/local/bin/LCA
$ podman run --it --rm --entrypoint /usr/local/bin/LCA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LCA   -v ${PWD} -w ${PWD} <container> -c " $@"
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
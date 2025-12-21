---
layout: container
name:  "quay.io/biocontainers/rabbittclust"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rabbittclust/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rabbittclust/container.yaml"
updated_at: "2025-12-21 04:08:56.270952"
latest: "2.3.0--h43eeafb_0"
container_url: "https://biocontainers.pro/tools/rabbittclust"
aliases:
 - "clust-greedy"
 - "clust-mst"
versions:
 - "2.3.0--h43eeafb_0"
description: "singularity registry hpc automated addition for rabbittclust"
config: {"url": "https://biocontainers.pro/tools/rabbittclust", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for rabbittclust", "latest": {"2.3.0--h43eeafb_0": "sha256:feeaa2726438a1397e73513c99469d77a09eb55a7b97612f0f599e1c4763c145"}, "tags": {"2.3.0--h43eeafb_0": "sha256:feeaa2726438a1397e73513c99469d77a09eb55a7b97612f0f599e1c4763c145"}, "docker": "quay.io/biocontainers/rabbittclust", "aliases": {"clust-greedy": "/usr/local/bin/clust-greedy", "clust-mst": "/usr/local/bin/clust-mst"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rabbittclust.
singularity registry hpc automated addition for rabbittclust
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rabbittclust
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rabbittclust:2.3.0--h43eeafb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rabbittclust/2.3.0--h43eeafb_0
$ module help quay.io/biocontainers/rabbittclust/2.3.0--h43eeafb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rabbittclust-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rabbittclust-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rabbittclust-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rabbittclust-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rabbittclust-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rabbittclust-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### clust-greedy

```bash
$ singularity exec <container> /usr/local/bin/clust-greedy
$ podman run --it --rm --entrypoint /usr/local/bin/clust-greedy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clust-greedy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clust-mst

```bash
$ singularity exec <container> /usr/local/bin/clust-mst
$ podman run --it --rm --entrypoint /usr/local/bin/clust-mst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clust-mst   -v ${PWD} -w ${PWD} <container> -c " $@"
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
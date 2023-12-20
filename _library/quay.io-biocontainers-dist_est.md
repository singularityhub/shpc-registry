---
layout: container
name:  "quay.io/biocontainers/dist_est"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dist_est/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dist_est/container.yaml"
updated_at: "2023-12-20 02:42:10.118638"
latest: "1.1--hdbdd923_2"
container_url: "https://biocontainers.pro/tools/dist_est"
aliases:
 - "dist_est"
versions:
 - "1.1--h87f3376_0"
 - "1.1--hdbdd923_2"
description: "singularity registry hpc automated addition for dist_est"
config: {"url": "https://biocontainers.pro/tools/dist_est", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for dist_est", "latest": {"1.1--hdbdd923_2": "sha256:97d8af66966553592b0c5053c19953f45055b152c3f743597766993ed1916511"}, "tags": {"1.1--h87f3376_0": "sha256:86d5415907e2ba76c890f72efcaef9b555158c3b2ca2e4e029dfaf5231209bcc", "1.1--hdbdd923_2": "sha256:97d8af66966553592b0c5053c19953f45055b152c3f743597766993ed1916511"}, "docker": "quay.io/biocontainers/dist_est", "aliases": {"dist_est": "/usr/local/bin/dist_est"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dist_est.
singularity registry hpc automated addition for dist_est
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dist_est
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dist_est:1.1--hdbdd923_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dist_est/1.1--hdbdd923_2
$ module help quay.io/biocontainers/dist_est/1.1--hdbdd923_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dist_est-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dist_est-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dist_est-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dist_est-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dist_est-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dist_est-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dist_est

```bash
$ singularity exec <container> /usr/local/bin/dist_est
$ podman run --it --rm --entrypoint /usr/local/bin/dist_est   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dist_est   -v ${PWD} -w ${PWD} <container> -c " $@"
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
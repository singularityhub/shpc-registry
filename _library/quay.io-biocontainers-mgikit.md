---
layout: container
name:  "quay.io/biocontainers/mgikit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mgikit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mgikit/container.yaml"
updated_at: "2025-02-07 03:40:50.116788"
latest: "0.1.7--h3ab6199_1"
container_url: "https://biocontainers.pro/tools/mgikit"
aliases:
 - "mgikit"
versions:
 - "0.1.5--h4c94732_0"
 - "0.1.5--h4c94732_1"
 - "0.1.6--h4c94732_0"
 - "0.1.7--h4c94732_0"
 - "0.1.7--h3ab6199_1"
description: "singularity registry hpc automated addition for mgikit"
config: {"url": "https://biocontainers.pro/tools/mgikit", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mgikit", "latest": {"0.1.7--h3ab6199_1": "sha256:42c9b20b7103cab6327458d39a833d3db81381bec0605c03665f29a7a52c4e38"}, "tags": {"0.1.5--h4c94732_0": "sha256:499811e979978077987761492c5d9d7c3af468b2caaf4ad501035e60580a9bf2", "0.1.5--h4c94732_1": "sha256:d38b38c49bae810c354d70b40f481c1574ebbcc96927a3091c8ed7e71c08d471", "0.1.6--h4c94732_0": "sha256:80054ccc61bbd83aeb21fe7c41dafb896ef7ac93af84de109a36594908d993e4", "0.1.7--h4c94732_0": "sha256:5435e10072dfe3f17d375e750889c0ef4de1a745682049f0079b1eada73c469f", "0.1.7--h3ab6199_1": "sha256:42c9b20b7103cab6327458d39a833d3db81381bec0605c03665f29a7a52c4e38"}, "docker": "quay.io/biocontainers/mgikit", "aliases": {"mgikit": "/usr/local/bin/mgikit"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mgikit.
singularity registry hpc automated addition for mgikit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mgikit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mgikit:0.1.7--h3ab6199_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mgikit/0.1.7--h3ab6199_1
$ module help quay.io/biocontainers/mgikit/0.1.7--h3ab6199_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mgikit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mgikit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mgikit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mgikit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mgikit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mgikit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mgikit

```bash
$ singularity exec <container> /usr/local/bin/mgikit
$ podman run --it --rm --entrypoint /usr/local/bin/mgikit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mgikit   -v ${PWD} -w ${PWD} <container> -c " $@"
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
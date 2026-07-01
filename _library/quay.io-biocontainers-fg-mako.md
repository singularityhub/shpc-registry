---
layout: container
name:  "quay.io/biocontainers/fg-mako"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fg-mako/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fg-mako/container.yaml"
updated_at: "2026-07-01 15:18:35.782054"
latest: "0.1.1--h7296c89_0"
container_url: "https://biocontainers.pro/tools/fg-mako"
aliases:
 - "mako"
versions:
 - "0.1.1--h7296c89_0"
description: "singularity registry hpc automated addition for fg-mako"
config: {"url": "https://biocontainers.pro/tools/fg-mako", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for fg-mako", "latest": {"0.1.1--h7296c89_0": "sha256:960d01aa5477ef82ad2b91739c4e4fa7e8916928882216f2fa7b66bad7e01826"}, "tags": {"0.1.1--h7296c89_0": "sha256:960d01aa5477ef82ad2b91739c4e4fa7e8916928882216f2fa7b66bad7e01826"}, "docker": "quay.io/biocontainers/fg-mako", "aliases": {"mako": "/usr/local/bin/mako"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fg-mako.
singularity registry hpc automated addition for fg-mako
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fg-mako
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fg-mako:0.1.1--h7296c89_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fg-mako/0.1.1--h7296c89_0
$ module help quay.io/biocontainers/fg-mako/0.1.1--h7296c89_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fg-mako-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fg-mako-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fg-mako-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fg-mako-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fg-mako-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fg-mako-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mako

```bash
$ singularity exec <container> /usr/local/bin/mako
$ podman run --it --rm --entrypoint /usr/local/bin/mako   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mako   -v ${PWD} -w ${PWD} <container> -c " $@"
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
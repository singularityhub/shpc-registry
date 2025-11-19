---
layout: container
name:  "quay.io/biocontainers/baypass"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/baypass/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/baypass/container.yaml"
updated_at: "2025-11-19 03:42:23.057596"
latest: "2.31--h1c9e865_2"
container_url: "https://biocontainers.pro/tools/baypass"
aliases:
 - "g_baypass"
versions:
 - "2.31--h1107714_0"
 - "2.31--h1c9e865_2"
description: "singularity registry hpc automated addition for baypass"
config: {"url": "https://biocontainers.pro/tools/baypass", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for baypass", "latest": {"2.31--h1c9e865_2": "sha256:2493bd8cb88902de0769adc67746ebbd6da15fc3b2cea7cbd6110d205001369d"}, "tags": {"2.31--h1107714_0": "sha256:4b189363402b3dc9a10abd287a638bf4e96759f10c4568bdf43c39a50c5f38f9", "2.31--h1c9e865_2": "sha256:2493bd8cb88902de0769adc67746ebbd6da15fc3b2cea7cbd6110d205001369d"}, "docker": "quay.io/biocontainers/baypass", "aliases": {"g_baypass": "/usr/local/bin/g_baypass"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/baypass.
singularity registry hpc automated addition for baypass
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/baypass
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/baypass:2.31--h1c9e865_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/baypass/2.31--h1c9e865_2
$ module help quay.io/biocontainers/baypass/2.31--h1c9e865_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### baypass-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### baypass-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### baypass-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### baypass-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### baypass-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### baypass-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### g_baypass

```bash
$ singularity exec <container> /usr/local/bin/g_baypass
$ podman run --it --rm --entrypoint /usr/local/bin/g_baypass   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g_baypass   -v ${PWD} -w ${PWD} <container> -c " $@"
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
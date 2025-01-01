---
layout: container
name:  "quay.io/biocontainers/strangepg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/strangepg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/strangepg/container.yaml"
updated_at: "2025-01-01 02:58:50.264367"
latest: "0.8.15--h9a53f25_0"
container_url: "https://biocontainers.pro/tools/strangepg"
aliases:
 - "strawk"
 - "strpg"
versions:
 - "0.8.0--h9a53f25_0"
 - "0.8.4--h9a53f25_0"
 - "0.8.8--h9a53f25_0"
 - "0.8.14--h9a53f25_0"
 - "0.8.15--h9a53f25_0"
description: "singularity registry hpc automated addition for strangepg"
config: {"url": "https://biocontainers.pro/tools/strangepg", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for strangepg", "latest": {"0.8.15--h9a53f25_0": "sha256:aad2024368fed2c71369185323441195980a5d5977957e6a1bfe5380d2c19ab9"}, "tags": {"0.8.0--h9a53f25_0": "sha256:8de054f5b9e643465ca172039c84da98bb991d5d8e09fa757dd97eaa5b46b20b", "0.8.4--h9a53f25_0": "sha256:571c482c5c2c3c846345eba9f48d6c3ebc31d8113f554257c28b52783f808c38", "0.8.8--h9a53f25_0": "sha256:c988a26a45d48192a7f08dfe01a64f8942f840b3999376b3fabf63689ec4daaf", "0.8.14--h9a53f25_0": "sha256:6609ba89ba913488bc22cf4db5355243ff9a481e17e5b8e16afefceaefe08e2d", "0.8.15--h9a53f25_0": "sha256:aad2024368fed2c71369185323441195980a5d5977957e6a1bfe5380d2c19ab9"}, "docker": "quay.io/biocontainers/strangepg", "aliases": {"strawk": "/usr/local/bin/strawk", "strpg": "/usr/local/bin/strpg"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/strangepg.
singularity registry hpc automated addition for strangepg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/strangepg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/strangepg:0.8.15--h9a53f25_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/strangepg/0.8.15--h9a53f25_0
$ module help quay.io/biocontainers/strangepg/0.8.15--h9a53f25_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### strangepg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### strangepg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### strangepg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### strangepg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### strangepg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### strangepg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### strawk

```bash
$ singularity exec <container> /usr/local/bin/strawk
$ podman run --it --rm --entrypoint /usr/local/bin/strawk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/strawk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### strpg

```bash
$ singularity exec <container> /usr/local/bin/strpg
$ podman run --it --rm --entrypoint /usr/local/bin/strpg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/strpg   -v ${PWD} -w ${PWD} <container> -c " $@"
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
---
layout: container
name:  "quay.io/biocontainers/sqlitebrowser"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sqlitebrowser/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/sqlitebrowser/container.yaml"
updated_at: "2022-10-27 00:58:10.617413"
latest: "3.8.0--0"
container_url: "https://biocontainers.pro/tools/sqlitebrowser"
aliases:
 - "sqlitebrowser"
versions:
 - "3.8.0--0"
description: "shpc-registry automated BioContainers addition for sqlitebrowser"
config: {"url": "https://biocontainers.pro/tools/sqlitebrowser", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sqlitebrowser", "latest": {"3.8.0--0": "sha256:39e283319207b78e1721934a52c70a929f3bd2070fcd1f7900b920477ca3fd08"}, "tags": {"3.8.0--0": "sha256:39e283319207b78e1721934a52c70a929f3bd2070fcd1f7900b920477ca3fd08"}, "docker": "quay.io/biocontainers/sqlitebrowser", "aliases": {"sqlitebrowser": "/usr/local/bin/sqlitebrowser"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sqlitebrowser.
shpc-registry automated BioContainers addition for sqlitebrowser
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sqlitebrowser
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sqlitebrowser:3.8.0--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sqlitebrowser/3.8.0--0
$ module help quay.io/biocontainers/sqlitebrowser/3.8.0--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sqlitebrowser-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sqlitebrowser-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sqlitebrowser-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sqlitebrowser-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sqlitebrowser-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sqlitebrowser-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sqlitebrowser

```bash
$ singularity exec <container> /usr/local/bin/sqlitebrowser
$ podman run --it --rm --entrypoint /usr/local/bin/sqlitebrowser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sqlitebrowser   -v ${PWD} -w ${PWD} <container> -c " $@"
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
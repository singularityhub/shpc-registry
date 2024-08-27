---
layout: container
name:  "quay.io/biocontainers/grenedalf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/grenedalf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/grenedalf/container.yaml"
updated_at: "2024-08-27 06:56:12.908473"
latest: "0.6.0--h27d5293_0"
container_url: "https://biocontainers.pro/tools/grenedalf"
aliases:
 - "grenedalf"
versions:
 - "0.6.0--h27d5293_0"
description: "singularity registry hpc automated addition for grenedalf"
config: {"url": "https://biocontainers.pro/tools/grenedalf", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for grenedalf", "latest": {"0.6.0--h27d5293_0": "sha256:4dba68a89f6c839edac33bb5844e68ae183f41cb15188475d5ad30a17b0a9a4c"}, "tags": {"0.6.0--h27d5293_0": "sha256:4dba68a89f6c839edac33bb5844e68ae183f41cb15188475d5ad30a17b0a9a4c"}, "docker": "quay.io/biocontainers/grenedalf", "aliases": {"grenedalf": "/usr/local/bin/grenedalf"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/grenedalf.
singularity registry hpc automated addition for grenedalf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/grenedalf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/grenedalf:0.6.0--h27d5293_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/grenedalf/0.6.0--h27d5293_0
$ module help quay.io/biocontainers/grenedalf/0.6.0--h27d5293_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### grenedalf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### grenedalf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### grenedalf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### grenedalf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### grenedalf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### grenedalf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### grenedalf

```bash
$ singularity exec <container> /usr/local/bin/grenedalf
$ podman run --it --rm --entrypoint /usr/local/bin/grenedalf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grenedalf   -v ${PWD} -w ${PWD} <container> -c " $@"
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
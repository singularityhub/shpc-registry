---
layout: container
name:  "quay.io/biocontainers/recontig"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/recontig/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/recontig/container.yaml"
updated_at: "2023-05-05 03:12:02.173119"
latest: "1.5.0--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/recontig"
aliases:
 - "recontig"
versions:
 - "1.5.0--h9ee0642_0"
description: "shpc-registry automated BioContainers addition for recontig"
config: {"url": "https://biocontainers.pro/tools/recontig", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for recontig", "latest": {"1.5.0--h9ee0642_0": "sha256:58ea03b898a3d709b075d796c24d00a98921a44bd335f62ba85c634eaece64e6"}, "tags": {"1.5.0--h9ee0642_0": "sha256:58ea03b898a3d709b075d796c24d00a98921a44bd335f62ba85c634eaece64e6"}, "docker": "quay.io/biocontainers/recontig", "aliases": {"recontig": "/usr/local/bin/recontig"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/recontig.
shpc-registry automated BioContainers addition for recontig
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/recontig
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/recontig:1.5.0--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/recontig/1.5.0--h9ee0642_0
$ module help quay.io/biocontainers/recontig/1.5.0--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### recontig-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### recontig-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### recontig-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### recontig-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### recontig-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### recontig-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### recontig

```bash
$ singularity exec <container> /usr/local/bin/recontig
$ podman run --it --rm --entrypoint /usr/local/bin/recontig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/recontig   -v ${PWD} -w ${PWD} <container> -c " $@"
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
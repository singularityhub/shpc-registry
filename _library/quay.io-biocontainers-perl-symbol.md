---
layout: container
name:  "quay.io/biocontainers/perl-symbol"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-symbol/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-symbol/container.yaml"
updated_at: "2026-02-02 12:57:41.586548"
latest: "1.07--pl526_1"
container_url: "https://biocontainers.pro/tools/perl-symbol"

versions:
 - "1.07--pl526_1"
description: "shpc-registry automated BioContainers addition for perl-symbol"
config: {"url": "https://biocontainers.pro/tools/perl-symbol", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-symbol", "latest": {"1.07--pl526_1": "sha256:288e837e7d32b002e846fc72c41bb39644f3767218397079496d6bf81ca3089e"}, "tags": {"1.07--pl526_1": "sha256:288e837e7d32b002e846fc72c41bb39644f3767218397079496d6bf81ca3089e"}, "docker": "quay.io/biocontainers/perl-symbol"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-symbol.
shpc-registry automated BioContainers addition for perl-symbol
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-symbol
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-symbol:1.07--pl526_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-symbol/1.07--pl526_1
$ module help quay.io/biocontainers/perl-symbol/1.07--pl526_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-symbol-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-symbol-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-symbol-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-symbol-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-symbol-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-symbol-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-symbol

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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
---
layout: container
name:  "quay.io/biocontainers/r-lncpipereporter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-lncpipereporter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-lncpipereporter/container.yaml"
updated_at: "2024-11-25 04:20:25.755527"
latest: "0.1.1--r43h031d066_8"
container_url: "https://biocontainers.pro/tools/r-lncpipereporter"
aliases:
 - "pandoc"
versions:
 - "0.1.1--r41hec16e2b_5"
 - "0.1.1--r42hec16e2b_6"
 - "0.1.1--r42h031d066_7"
 - "0.1.1--r43h031d066_8"
description: "shpc-registry automated BioContainers addition for r-lncpipereporter"
config: {"url": "https://biocontainers.pro/tools/r-lncpipereporter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-lncpipereporter", "latest": {"0.1.1--r43h031d066_8": "sha256:c7c470d15d955a11c95ae2564be894861547013d04b7f531f41b174a09a47833"}, "tags": {"0.1.1--r41hec16e2b_5": "sha256:916d49aaddcb11fffc11fd3cf4b2d44fd9455653b88cca1685eda71ce7d64268", "0.1.1--r42hec16e2b_6": "sha256:a7d6df5d1901e5851f8f6bfc2d0b5bf2249383dc88efcfe3a070fef60b6b823f", "0.1.1--r42h031d066_7": "sha256:45684b08853b2a9bb0549d602e924af601095d1d9b5ac85f42abe51ebe6f74a2", "0.1.1--r43h031d066_8": "sha256:c7c470d15d955a11c95ae2564be894861547013d04b7f531f41b174a09a47833"}, "docker": "quay.io/biocontainers/r-lncpipereporter", "aliases": {"pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-lncpipereporter.
shpc-registry automated BioContainers addition for r-lncpipereporter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-lncpipereporter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-lncpipereporter:0.1.1--r43h031d066_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-lncpipereporter/0.1.1--r43h031d066_8
$ module help quay.io/biocontainers/r-lncpipereporter/0.1.1--r43h031d066_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-lncpipereporter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-lncpipereporter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-lncpipereporter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-lncpipereporter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-lncpipereporter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-lncpipereporter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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
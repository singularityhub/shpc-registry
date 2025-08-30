---
layout: container
name:  "quay.io/biocontainers/suma_package"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/suma_package/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/suma_package/container.yaml"
updated_at: "2025-08-30 03:42:33.061633"
latest: "1.0.00--h577a1d6_8"
container_url: "https://biocontainers.pro/tools/suma_package"
aliases:
 - "sumaclust"
 - "sumatra"
versions:
 - "1.0.00--h7132678_5"
 - "1.0.00--h7132678_6"
 - "1.0.00--he4a0461_7"
 - "1.0.00--h577a1d6_8"
description: "shpc-registry automated BioContainers addition for suma_package"
config: {"url": "https://biocontainers.pro/tools/suma_package", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for suma_package", "latest": {"1.0.00--h577a1d6_8": "sha256:e6a1a7e82159cbf905bfa5de256358c8a792369f48f9581d97e5f40cbdbc5998"}, "tags": {"1.0.00--h7132678_5": "sha256:781cd79ca306b4ed25847f9a095dc97ddce2a2d647e4857ec618082fc2dac600", "1.0.00--h7132678_6": "sha256:b32f17db38efcc209c2c3463dc3f13164b23cc18938622a8198b962c48ad3a50", "1.0.00--he4a0461_7": "sha256:2d288ca6eca16a2c8a6947fca77a4c9093ed5a03ea2d8c1e24cb5bac67a36938", "1.0.00--h577a1d6_8": "sha256:e6a1a7e82159cbf905bfa5de256358c8a792369f48f9581d97e5f40cbdbc5998"}, "docker": "quay.io/biocontainers/suma_package", "aliases": {"sumaclust": "/usr/local/bin/sumaclust", "sumatra": "/usr/local/bin/sumatra"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/suma_package.
shpc-registry automated BioContainers addition for suma_package
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/suma_package
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/suma_package:1.0.00--h577a1d6_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/suma_package/1.0.00--h577a1d6_8
$ module help quay.io/biocontainers/suma_package/1.0.00--h577a1d6_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### suma_package-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### suma_package-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### suma_package-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### suma_package-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### suma_package-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### suma_package-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sumaclust

```bash
$ singularity exec <container> /usr/local/bin/sumaclust
$ podman run --it --rm --entrypoint /usr/local/bin/sumaclust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sumaclust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sumatra

```bash
$ singularity exec <container> /usr/local/bin/sumatra
$ podman run --it --rm --entrypoint /usr/local/bin/sumatra   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sumatra   -v ${PWD} -w ${PWD} <container> -c " $@"
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
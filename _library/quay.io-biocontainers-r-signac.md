---
layout: container
name:  "quay.io/biocontainers/r-signac"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-signac/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-signac/container.yaml"
updated_at: "2024-10-19 03:28:49.818871"
latest: "1.14.0--r43h21a89ab_0"
container_url: "https://biocontainers.pro/tools/r-signac"
aliases:
 - "geosop"
 - "geos-config"
versions:
 - "1.8.0--r41hecf12ef_0"
 - "1.8.0--r42hecf12ef_1"
 - "1.9.0--r42hecf12ef_0"
 - "1.9.0--r42hecf12ef_1"
 - "1.10.0--r42h21a89ab_1"
 - "1.9.0--r42h21a89ab_2"
 - "1.10.0--r43h21a89ab_2"
 - "1.12.0--r43h21a89ab_0"
 - "1.11.0--r43h21a89ab_0"
 - "1.13.0--r43h21a89ab_0"
 - "1.14.0--r43h21a89ab_0"
description: "shpc-registry automated BioContainers addition for r-signac"
config: {"url": "https://biocontainers.pro/tools/r-signac", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-signac", "latest": {"1.14.0--r43h21a89ab_0": "sha256:5bb00a5f5046a2b33eb5a2192f3f60069be76e42a361917595d597215359ce5c"}, "tags": {"1.8.0--r41hecf12ef_0": "sha256:f212100013aac7cf43778f9fa5d9fc9e2aea39ed90d58919ea99c43f99405fb8", "1.8.0--r42hecf12ef_1": "sha256:0e1afe6c0bae43e4b1064710c97d9be7e282f44ea147e1cd1f9e9ebcaa05ff34", "1.9.0--r42hecf12ef_0": "sha256:86a37b689ab590106f0135fe7a30d69314c248d8133f1adda198c2c96044f149", "1.9.0--r42hecf12ef_1": "sha256:99a1b1520ce3a1d16d8147627b78376a30128d90be867a1b6d3f403fabf32a7f", "1.10.0--r42h21a89ab_1": "sha256:f8a5eb595127633eabdbe4b28e5b82df882fcfc1464b1bd521d7e64f2e47dc14", "1.9.0--r42h21a89ab_2": "sha256:ebd890596eda06fc0bd0171b759d4b228cb2a81f8201c57e99fb935ca59d8b3a", "1.10.0--r43h21a89ab_2": "sha256:9f6a7d17c34cb3a61fb47a15867a493ebdbc5d6195c0df601e566c98ce39c59c", "1.12.0--r43h21a89ab_0": "sha256:f8e4b9d4cf685af41360d34319ebbe4de1761dc9b571f1fa71a3ea252f149101", "1.11.0--r43h21a89ab_0": "sha256:1e488297951b5597cd3503a244780cf5f0f592b1168c6e2d947d2a095a0c1cc0", "1.13.0--r43h21a89ab_0": "sha256:ac8c391221f41a988f1d092c42b2a445851e0b5d8cb9bf8674e92e4c359a0912", "1.14.0--r43h21a89ab_0": "sha256:5bb00a5f5046a2b33eb5a2192f3f60069be76e42a361917595d597215359ce5c"}, "docker": "quay.io/biocontainers/r-signac", "aliases": {"geosop": "/usr/local/bin/geosop", "geos-config": "/usr/local/bin/geos-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-signac.
shpc-registry automated BioContainers addition for r-signac
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-signac
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-signac:1.14.0--r43h21a89ab_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-signac/1.14.0--r43h21a89ab_0
$ module help quay.io/biocontainers/r-signac/1.14.0--r43h21a89ab_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-signac-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-signac-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-signac-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-signac-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-signac-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-signac-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### geosop

```bash
$ singularity exec <container> /usr/local/bin/geosop
$ podman run --it --rm --entrypoint /usr/local/bin/geosop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geosop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geos-config

```bash
$ singularity exec <container> /usr/local/bin/geos-config
$ podman run --it --rm --entrypoint /usr/local/bin/geos-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geos-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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
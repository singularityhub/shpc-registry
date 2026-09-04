---
layout: container
name:  "quay.io/biocontainers/te-looker"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/te-looker/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/te-looker/container.yaml"
updated_at: "2026-09-04 07:11:14.762374"
latest: "0.3.0--hfa8f182_0"
container_url: "https://biocontainers.pro/tools/te-looker"
aliases:
 - "abpoa"
 - "dtr"
 - "te-discover"
 - "te-refine"
 - "te-seed"
 - "spoa"
versions:
 - "0.3.0--hfa8f182_0"
description: "singularity registry hpc automated addition for te-looker"
config: {"url": "https://biocontainers.pro/tools/te-looker", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for te-looker", "latest": {"0.3.0--hfa8f182_0": "sha256:79c2a15386bc5d8ee477b50c407e47a7de3cd9f29b83e7e3d4dc8e47633cc3ce"}, "tags": {"0.3.0--hfa8f182_0": "sha256:79c2a15386bc5d8ee477b50c407e47a7de3cd9f29b83e7e3d4dc8e47633cc3ce"}, "docker": "quay.io/biocontainers/te-looker", "aliases": {"abpoa": "/usr/local/bin/abpoa", "dtr": "/usr/local/bin/dtr", "te-discover": "/usr/local/bin/te-discover", "te-refine": "/usr/local/bin/te-refine", "te-seed": "/usr/local/bin/te-seed", "spoa": "/usr/local/bin/spoa"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/te-looker.
singularity registry hpc automated addition for te-looker
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/te-looker
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/te-looker:0.3.0--hfa8f182_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/te-looker/0.3.0--hfa8f182_0
$ module help quay.io/biocontainers/te-looker/0.3.0--hfa8f182_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### te-looker-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### te-looker-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### te-looker-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### te-looker-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### te-looker-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### te-looker-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### abpoa

```bash
$ singularity exec <container> /usr/local/bin/abpoa
$ podman run --it --rm --entrypoint /usr/local/bin/abpoa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abpoa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dtr

```bash
$ singularity exec <container> /usr/local/bin/dtr
$ podman run --it --rm --entrypoint /usr/local/bin/dtr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dtr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### te-discover

```bash
$ singularity exec <container> /usr/local/bin/te-discover
$ podman run --it --rm --entrypoint /usr/local/bin/te-discover   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/te-discover   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### te-refine

```bash
$ singularity exec <container> /usr/local/bin/te-refine
$ podman run --it --rm --entrypoint /usr/local/bin/te-refine   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/te-refine   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### te-seed

```bash
$ singularity exec <container> /usr/local/bin/te-seed
$ podman run --it --rm --entrypoint /usr/local/bin/te-seed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/te-seed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spoa

```bash
$ singularity exec <container> /usr/local/bin/spoa
$ podman run --it --rm --entrypoint /usr/local/bin/spoa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spoa   -v ${PWD} -w ${PWD} <container> -c " $@"
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
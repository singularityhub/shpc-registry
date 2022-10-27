---
layout: container
name:  "quay.io/biocontainers/pairix"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pairix/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/pairix/container.yaml"
updated_at: "2022-10-27 00:56:33.754983"
latest: "0.3.7--py36haf49e46_4"
container_url: "https://biocontainers.pro/tools/pairix"

versions:
 - "0.3.7--py36haf49e46_4"
description: "shpc-registry automated BioContainers addition for pairix"
config: {"url": "https://biocontainers.pro/tools/pairix", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pairix", "latest": {"0.3.7--py36haf49e46_4": "sha256:beeb156ca2c238c3c6b602f20e75bda97b1866df449fcf0f9a552088b6240fa1"}, "tags": {"0.3.7--py36haf49e46_4": "sha256:beeb156ca2c238c3c6b602f20e75bda97b1866df449fcf0f9a552088b6240fa1"}, "docker": "quay.io/biocontainers/pairix"}
---

This module is a singularity container wrapper for quay.io/biocontainers/pairix.
shpc-registry automated BioContainers addition for pairix
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pairix
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pairix:0.3.7--py36haf49e46_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pairix/0.3.7--py36haf49e46_4
$ module help quay.io/biocontainers/pairix/0.3.7--py36haf49e46_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pairix-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pairix-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pairix-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pairix-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pairix-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pairix-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### pairix

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
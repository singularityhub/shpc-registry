---
layout: container
name:  "quay.io/biocontainers/predicthaplo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/predicthaplo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/predicthaplo/container.yaml"
updated_at: "2024-01-11 03:06:14.715795"
latest: "2.1.4--h9b88814_5"
container_url: "https://biocontainers.pro/tools/predicthaplo"
aliases:
 - "predicthaplo"
versions:
 - "2.1.4--h9b88814_3"
 - "2.1.4--h9b88814_4"
 - "2.1.4--h9b88814_5"
description: "shpc-registry automated BioContainers addition for predicthaplo"
config: {"url": "https://biocontainers.pro/tools/predicthaplo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for predicthaplo", "latest": {"2.1.4--h9b88814_5": "sha256:5a9889594b9274038d5cc759389aa77eeb18ee8ff9d0f9277b71cfd4ee7abb9f"}, "tags": {"2.1.4--h9b88814_3": "sha256:89587c8e93a7f2c0035787d80ae508f83c8b77215a1f34f515502a038a69e8e7", "2.1.4--h9b88814_4": "sha256:8790ff4b7a48bb6ec9400abef6fee0ad686b9c1223ffbcfa308050d42bc2b20d", "2.1.4--h9b88814_5": "sha256:5a9889594b9274038d5cc759389aa77eeb18ee8ff9d0f9277b71cfd4ee7abb9f"}, "docker": "quay.io/biocontainers/predicthaplo", "aliases": {"predicthaplo": "/usr/local/bin/predicthaplo"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/predicthaplo.
shpc-registry automated BioContainers addition for predicthaplo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/predicthaplo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/predicthaplo:2.1.4--h9b88814_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/predicthaplo/2.1.4--h9b88814_5
$ module help quay.io/biocontainers/predicthaplo/2.1.4--h9b88814_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### predicthaplo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### predicthaplo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### predicthaplo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### predicthaplo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### predicthaplo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### predicthaplo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### predicthaplo

```bash
$ singularity exec <container> /usr/local/bin/predicthaplo
$ podman run --it --rm --entrypoint /usr/local/bin/predicthaplo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/predicthaplo   -v ${PWD} -w ${PWD} <container> -c " $@"
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
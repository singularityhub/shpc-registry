---
layout: container
name:  "quay.io/biocontainers/hilive2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hilive2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hilive2/container.yaml"
updated_at: "2025-11-15 03:40:46.085651"
latest: "2.0--he629db7_3"
container_url: "https://biocontainers.pro/tools/hilive2"
aliases:
 - "hilive"
 - "hilive-build"
 - "hilive-out"
versions:
 - "2.0a--h2e6a766_2"
 - "2.0--he629db7_3"
description: "shpc-registry automated BioContainers addition for hilive2"
config: {"url": "https://biocontainers.pro/tools/hilive2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hilive2", "latest": {"2.0--he629db7_3": "sha256:35a84cd3b0f5e1ef7dae63ad1cd0693db8c911846eb89d93847ae69c81cad726"}, "tags": {"2.0a--h2e6a766_2": "sha256:8672f9f210bba35b64cee5cebd5610ed03a5acb11ec6df4a9846ed18aa7dfbd6", "2.0--he629db7_3": "sha256:35a84cd3b0f5e1ef7dae63ad1cd0693db8c911846eb89d93847ae69c81cad726"}, "docker": "quay.io/biocontainers/hilive2", "aliases": {"hilive": "/usr/local/bin/hilive", "hilive-build": "/usr/local/bin/hilive-build", "hilive-out": "/usr/local/bin/hilive-out"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hilive2.
shpc-registry automated BioContainers addition for hilive2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hilive2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hilive2:2.0--he629db7_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hilive2/2.0--he629db7_3
$ module help quay.io/biocontainers/hilive2/2.0--he629db7_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hilive2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hilive2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hilive2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hilive2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hilive2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hilive2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hilive

```bash
$ singularity exec <container> /usr/local/bin/hilive
$ podman run --it --rm --entrypoint /usr/local/bin/hilive   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hilive   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hilive-build

```bash
$ singularity exec <container> /usr/local/bin/hilive-build
$ podman run --it --rm --entrypoint /usr/local/bin/hilive-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hilive-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hilive-out

```bash
$ singularity exec <container> /usr/local/bin/hilive-out
$ podman run --it --rm --entrypoint /usr/local/bin/hilive-out   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hilive-out   -v ${PWD} -w ${PWD} <container> -c " $@"
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
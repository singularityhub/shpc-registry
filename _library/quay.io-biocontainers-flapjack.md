---
layout: container
name:  "quay.io/biocontainers/flapjack"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/flapjack/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/flapjack/container.yaml"
updated_at: "2022-10-27 00:30:32.811538"
latest: "1.20.10.07--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/flapjack"
aliases:
 - "flapjack"
versions:
 - "1.20.10.07--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for flapjack"
config: {"url": "https://biocontainers.pro/tools/flapjack", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for flapjack", "latest": {"1.20.10.07--hdfd78af_1": "sha256:7e41296d5324822c6842cb0712d8289f2d4812dc1f78d4b393288033e075c94f"}, "tags": {"1.20.10.07--hdfd78af_1": "sha256:7e41296d5324822c6842cb0712d8289f2d4812dc1f78d4b393288033e075c94f"}, "docker": "quay.io/biocontainers/flapjack", "aliases": {"flapjack": "/usr/local/bin/flapjack"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/flapjack.
shpc-registry automated BioContainers addition for flapjack
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/flapjack
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/flapjack:1.20.10.07--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/flapjack/1.20.10.07--hdfd78af_1
$ module help quay.io/biocontainers/flapjack/1.20.10.07--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### flapjack-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### flapjack-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### flapjack-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### flapjack-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### flapjack-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### flapjack-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### flapjack

```bash
$ singularity exec <container> /usr/local/bin/flapjack
$ podman run --it --rm --entrypoint /usr/local/bin/flapjack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flapjack   -v ${PWD} -w ${PWD} <container> -c " $@"
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
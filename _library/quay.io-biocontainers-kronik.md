---
layout: container
name:  "quay.io/biocontainers/kronik"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kronik/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kronik/container.yaml"
updated_at: "2023-08-20 03:09:41.643500"
latest: "2.20--h4ac6f70_6"
container_url: "https://biocontainers.pro/tools/kronik"
aliases:
 - "kronik"
versions:
 - "2.20--h9f5acd7_4"
 - "2.20--h4ac6f70_6"
description: "shpc-registry automated BioContainers addition for kronik"
config: {"url": "https://biocontainers.pro/tools/kronik", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kronik", "latest": {"2.20--h4ac6f70_6": "sha256:bfb99c879872dd8aef84e4e2664beaac7bd896a3d6707f4ec8f0a249f1db7e88"}, "tags": {"2.20--h9f5acd7_4": "sha256:9291060a2af21a908ce19d62f53c9816549f485904dd689a0f1f8792e1660e9a", "2.20--h4ac6f70_6": "sha256:bfb99c879872dd8aef84e4e2664beaac7bd896a3d6707f4ec8f0a249f1db7e88"}, "docker": "quay.io/biocontainers/kronik", "aliases": {"kronik": "/usr/local/bin/kronik"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kronik.
shpc-registry automated BioContainers addition for kronik
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kronik
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kronik:2.20--h4ac6f70_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kronik/2.20--h4ac6f70_6
$ module help quay.io/biocontainers/kronik/2.20--h4ac6f70_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kronik-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kronik-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kronik-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kronik-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kronik-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kronik-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### kronik

```bash
$ singularity exec <container> /usr/local/bin/kronik
$ podman run --it --rm --entrypoint /usr/local/bin/kronik   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kronik   -v ${PWD} -w ${PWD} <container> -c " $@"
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
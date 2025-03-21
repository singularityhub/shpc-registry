---
layout: container
name:  "quay.io/biocontainers/memopair"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/memopair/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/memopair/container.yaml"
updated_at: "2025-03-21 03:24:22.583687"
latest: "0.1.6--h4349ce8_0"
container_url: "https://biocontainers.pro/tools/memopair"
aliases:
 - "memopair"
versions:
 - "0.1.5--h4349ce8_0"
 - "0.1.6--h4349ce8_0"
description: "singularity registry hpc automated addition for memopair"
config: {"url": "https://biocontainers.pro/tools/memopair", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for memopair", "latest": {"0.1.6--h4349ce8_0": "sha256:fbb586237575957d3986ab38023eb86bbec42b981d88e92b9e74f3cd538ebf8f"}, "tags": {"0.1.5--h4349ce8_0": "sha256:3d23547407241f4dd5c822db78e152e3e220cc8ebc1c424bc35c726f73254ff5", "0.1.6--h4349ce8_0": "sha256:fbb586237575957d3986ab38023eb86bbec42b981d88e92b9e74f3cd538ebf8f"}, "docker": "quay.io/biocontainers/memopair", "aliases": {"memopair": "/usr/local/bin/memopair"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/memopair.
singularity registry hpc automated addition for memopair
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/memopair
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/memopair:0.1.6--h4349ce8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/memopair/0.1.6--h4349ce8_0
$ module help quay.io/biocontainers/memopair/0.1.6--h4349ce8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### memopair-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### memopair-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### memopair-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### memopair-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### memopair-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### memopair-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### memopair

```bash
$ singularity exec <container> /usr/local/bin/memopair
$ podman run --it --rm --entrypoint /usr/local/bin/memopair   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/memopair   -v ${PWD} -w ${PWD} <container> -c " $@"
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
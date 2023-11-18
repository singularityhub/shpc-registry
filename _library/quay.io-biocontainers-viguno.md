---
layout: container
name:  "quay.io/biocontainers/viguno"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/viguno/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/viguno/container.yaml"
updated_at: "2023-11-18 02:30:37.184414"
latest: "0.1.6--h7e29777_0"
container_url: "https://biocontainers.pro/tools/viguno"
aliases:
 - "viguno"
versions:
 - "0.1.1--h7e29777_0"
 - "0.1.6--h7e29777_0"
description: "singularity registry hpc automated addition for viguno"
config: {"url": "https://biocontainers.pro/tools/viguno", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for viguno", "latest": {"0.1.6--h7e29777_0": "sha256:4dce318cf723819840d2fc641e08c4ea3b0877b64ffc47b7fe93ca6b0a81acf5"}, "tags": {"0.1.1--h7e29777_0": "sha256:8a42109d38493410adf689fa56a859c7cec55efe6d85f02b0c3f0a694e02234f", "0.1.6--h7e29777_0": "sha256:4dce318cf723819840d2fc641e08c4ea3b0877b64ffc47b7fe93ca6b0a81acf5"}, "docker": "quay.io/biocontainers/viguno", "aliases": {"viguno": "/usr/local/bin/viguno"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/viguno.
singularity registry hpc automated addition for viguno
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/viguno
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/viguno:0.1.6--h7e29777_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/viguno/0.1.6--h7e29777_0
$ module help quay.io/biocontainers/viguno/0.1.6--h7e29777_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### viguno-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### viguno-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### viguno-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### viguno-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### viguno-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### viguno-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### viguno

```bash
$ singularity exec <container> /usr/local/bin/viguno
$ podman run --it --rm --entrypoint /usr/local/bin/viguno   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/viguno   -v ${PWD} -w ${PWD} <container> -c " $@"
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
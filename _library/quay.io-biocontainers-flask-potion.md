---
layout: container
name:  "quay.io/biocontainers/flask-potion"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/flask-potion/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/flask-potion/container.yaml"
updated_at: "2022-10-27 00:21:05.976709"
latest: "0.12.1--py35_0"
container_url: "https://biocontainers.pro/tools/flask-potion"

versions:
 - "0.12.1--py35_0"
description: "shpc-registry automated BioContainers addition for flask-potion"
config: {"url": "https://biocontainers.pro/tools/flask-potion", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for flask-potion", "latest": {"0.12.1--py35_0": "sha256:e6029aeb1a3e6ef7fb5fb4f369a24aab814e1a7c5781e83c4f7fca0f60936cfe"}, "tags": {"0.12.1--py35_0": "sha256:e6029aeb1a3e6ef7fb5fb4f369a24aab814e1a7c5781e83c4f7fca0f60936cfe"}, "docker": "quay.io/biocontainers/flask-potion"}
---

This module is a singularity container wrapper for quay.io/biocontainers/flask-potion.
shpc-registry automated BioContainers addition for flask-potion
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/flask-potion
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/flask-potion:0.12.1--py35_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/flask-potion/0.12.1--py35_0
$ module help quay.io/biocontainers/flask-potion/0.12.1--py35_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### flask-potion-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### flask-potion-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### flask-potion-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### flask-potion-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### flask-potion-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### flask-potion-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### flask-potion

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
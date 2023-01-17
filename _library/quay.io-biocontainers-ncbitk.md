---
layout: container
name:  "quay.io/biocontainers/ncbitk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ncbitk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ncbitk/container.yaml"
updated_at: "2023-01-17 02:48:27.708291"
latest: "1.0a17--py_0"
container_url: "https://biocontainers.pro/tools/ncbitk"

versions:
 - "1.0a17--py_0"
description: "shpc-registry automated BioContainers addition for ncbitk"
config: {"url": "https://biocontainers.pro/tools/ncbitk", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ncbitk", "latest": {"1.0a17--py_0": "sha256:8d29f445dd6cee4807948cbaf553e52f19a908461d6f656f3423cbc2ba2142b7"}, "tags": {"1.0a17--py_0": "sha256:8d29f445dd6cee4807948cbaf553e52f19a908461d6f656f3423cbc2ba2142b7"}, "docker": "quay.io/biocontainers/ncbitk"}
---

This module is a singularity container wrapper for quay.io/biocontainers/ncbitk.
shpc-registry automated BioContainers addition for ncbitk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ncbitk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ncbitk:1.0a17--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ncbitk/1.0a17--py_0
$ module help quay.io/biocontainers/ncbitk/1.0a17--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ncbitk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ncbitk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ncbitk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ncbitk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ncbitk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ncbitk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### ncbitk

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
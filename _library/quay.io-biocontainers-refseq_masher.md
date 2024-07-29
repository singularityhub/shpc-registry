---
layout: container
name:  "quay.io/biocontainers/refseq_masher"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/refseq_masher/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/refseq_masher/container.yaml"
updated_at: "2024-07-29 17:54:02.109365"
latest: "0.1.2--py_0"
container_url: "https://biocontainers.pro/tools/refseq_masher"

versions:
 - "0.1.2--py_0"
description: "shpc-registry automated BioContainers addition for refseq_masher"
config: {"url": "https://biocontainers.pro/tools/refseq_masher", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for refseq_masher", "latest": {"0.1.2--py_0": "sha256:cc8793c3f4414ae3fa644f9a958fce2af706d2f6c8c21b42bb6c3cd3748d445f"}, "tags": {"0.1.2--py_0": "sha256:cc8793c3f4414ae3fa644f9a958fce2af706d2f6c8c21b42bb6c3cd3748d445f"}, "docker": "quay.io/biocontainers/refseq_masher"}
---

This module is a singularity container wrapper for quay.io/biocontainers/refseq_masher.
shpc-registry automated BioContainers addition for refseq_masher
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/refseq_masher
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/refseq_masher:0.1.2--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/refseq_masher/0.1.2--py_0
$ module help quay.io/biocontainers/refseq_masher/0.1.2--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### refseq_masher-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### refseq_masher-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### refseq_masher-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### refseq_masher-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### refseq_masher-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### refseq_masher-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### refseq_masher

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
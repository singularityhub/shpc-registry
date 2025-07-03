---
layout: container
name:  "quay.io/biocontainers/ra"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ra/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ra/container.yaml"
updated_at: "2025-07-03 03:50:42.162617"
latest: "0.9--hdbdd923_6"
container_url: "https://biocontainers.pro/tools/ra"

versions:
 - "0.9--h87f3376_4"
 - "0.9--hdbdd923_6"
description: "shpc-registry automated BioContainers addition for ra"
config: {"url": "https://biocontainers.pro/tools/ra", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ra", "latest": {"0.9--hdbdd923_6": "sha256:c3c0b88b0d6e614ac048d4231a54538264219f71f1878b14fe8c4e9e1f7fe72f"}, "tags": {"0.9--h87f3376_4": "sha256:d4940148ca1c359931b32a6c7c27181cfa4023bcc9b7b600bef21012d54e4539", "0.9--hdbdd923_6": "sha256:c3c0b88b0d6e614ac048d4231a54538264219f71f1878b14fe8c4e9e1f7fe72f"}, "docker": "quay.io/biocontainers/ra"}
---

This module is a singularity container wrapper for quay.io/biocontainers/ra.
shpc-registry automated BioContainers addition for ra
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ra
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ra:0.9--hdbdd923_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ra/0.9--hdbdd923_6
$ module help quay.io/biocontainers/ra/0.9--hdbdd923_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ra-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ra-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ra-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ra-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ra-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ra-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### ra

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
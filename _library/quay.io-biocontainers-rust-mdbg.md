---
layout: container
name:  "quay.io/biocontainers/rust-mdbg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rust-mdbg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rust-mdbg/container.yaml"
updated_at: "2024-01-21 02:41:02.451762"
latest: "1.0.1--h4ac6f70_3"
container_url: "https://biocontainers.pro/tools/rust-mdbg"
aliases:
 - "rust-mdbg"
 - "to_basespace"
versions:
 - "1.0.1--h9f5acd7_1"
 - "1.0.1--h4ac6f70_3"
description: "shpc-registry automated BioContainers addition for rust-mdbg"
config: {"url": "https://biocontainers.pro/tools/rust-mdbg", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rust-mdbg", "latest": {"1.0.1--h4ac6f70_3": "sha256:ae14fd179734052fbd7552625bd3cecb77ddc91f9e8c6fddadd8d0cebe1b1097"}, "tags": {"1.0.1--h9f5acd7_1": "sha256:c14f965f418e980000d177f861600eb13b5d91cd96466fc1f79f6c5955035b91", "1.0.1--h4ac6f70_3": "sha256:ae14fd179734052fbd7552625bd3cecb77ddc91f9e8c6fddadd8d0cebe1b1097"}, "docker": "quay.io/biocontainers/rust-mdbg", "aliases": {"rust-mdbg": "/usr/local/bin/rust-mdbg", "to_basespace": "/usr/local/bin/to_basespace"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rust-mdbg.
shpc-registry automated BioContainers addition for rust-mdbg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rust-mdbg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rust-mdbg:1.0.1--h4ac6f70_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rust-mdbg/1.0.1--h4ac6f70_3
$ module help quay.io/biocontainers/rust-mdbg/1.0.1--h4ac6f70_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rust-mdbg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rust-mdbg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rust-mdbg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rust-mdbg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rust-mdbg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rust-mdbg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rust-mdbg

```bash
$ singularity exec <container> /usr/local/bin/rust-mdbg
$ podman run --it --rm --entrypoint /usr/local/bin/rust-mdbg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rust-mdbg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### to_basespace

```bash
$ singularity exec <container> /usr/local/bin/to_basespace
$ podman run --it --rm --entrypoint /usr/local/bin/to_basespace   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/to_basespace   -v ${PWD} -w ${PWD} <container> -c " $@"
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
---
layout: container
name:  "quay.io/biocontainers/rpsbproc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rpsbproc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rpsbproc/container.yaml"
updated_at: "2024-09-17 02:59:34.083109"
latest: "0.5.0--h6a68c12_0"
container_url: "https://biocontainers.pro/tools/rpsbproc"
aliases:
 - "rpsbproc"
versions:
 - "0.5.0--h6a68c12_0"
description: "singularity registry hpc automated addition for rpsbproc"
config: {"url": "https://biocontainers.pro/tools/rpsbproc", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for rpsbproc", "latest": {"0.5.0--h6a68c12_0": "sha256:9023c179a44a0dd6056f72f183a5de6fc6b4a8c8dca3a1362e141d858bee285b"}, "tags": {"0.5.0--h6a68c12_0": "sha256:9023c179a44a0dd6056f72f183a5de6fc6b4a8c8dca3a1362e141d858bee285b"}, "docker": "quay.io/biocontainers/rpsbproc", "aliases": {"rpsbproc": "/usr/local/bin/rpsbproc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rpsbproc.
singularity registry hpc automated addition for rpsbproc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rpsbproc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rpsbproc:0.5.0--h6a68c12_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rpsbproc/0.5.0--h6a68c12_0
$ module help quay.io/biocontainers/rpsbproc/0.5.0--h6a68c12_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rpsbproc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rpsbproc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rpsbproc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rpsbproc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rpsbproc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rpsbproc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rpsbproc

```bash
$ singularity exec <container> /usr/local/bin/rpsbproc
$ podman run --it --rm --entrypoint /usr/local/bin/rpsbproc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rpsbproc   -v ${PWD} -w ${PWD} <container> -c " $@"
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
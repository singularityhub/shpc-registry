---
layout: container
name:  "quay.io/biocontainers/vmd"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vmd/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/vmd/container.yaml"
updated_at: "2025-02-11 02:58:42.349174"
latest: "1.9.3"
container_url: "https://biocontainers.pro/tools/vmd"
aliases:
 - "vmd"
versions:
 - "1.9.3"
description: "shpc-registry automated BioContainers addition for vmd"
config: {"url": "https://biocontainers.pro/tools/vmd", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for vmd", "latest": {"1.9.3": "sha256:c8ccfdd9efd621cee192c7b58ee986f030c251b89b203b68dd830938f67b0d28"}, "tags": {"1.9.3": "sha256:c8ccfdd9efd621cee192c7b58ee986f030c251b89b203b68dd830938f67b0d28"}, "docker": "quay.io/biocontainers/vmd", "aliases": {"vmd": "/usr/local/bin/vmd"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vmd.
shpc-registry automated BioContainers addition for vmd
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vmd
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vmd:1.9.3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vmd/1.9.3
$ module help quay.io/biocontainers/vmd/1.9.3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vmd-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vmd-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vmd-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vmd-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vmd-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vmd-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### vmd

```bash
$ singularity exec <container> /usr/local/bin/vmd
$ podman run --it --rm --entrypoint /usr/local/bin/vmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vmd   -v ${PWD} -w ${PWD} <container> -c " $@"
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
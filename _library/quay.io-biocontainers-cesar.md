---
layout: container
name:  "quay.io/biocontainers/cesar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cesar/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cesar/container.yaml"
updated_at: "2023-04-15 02:40:39.369891"
latest: "1.01--h87f3376_0"
container_url: "https://biocontainers.pro/tools/cesar"
aliases:
 - "cesar"
versions:
 - "1.01--h87f3376_0"
description: "singularity registry hpc automated addition for cesar"
config: {"url": "https://biocontainers.pro/tools/cesar", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for cesar", "latest": {"1.01--h87f3376_0": "sha256:0590933a637180c856d18def0a9cdd073bed15093f361608db8a97c6e0fc0089"}, "tags": {"1.01--h87f3376_0": "sha256:0590933a637180c856d18def0a9cdd073bed15093f361608db8a97c6e0fc0089"}, "docker": "quay.io/biocontainers/cesar", "aliases": {"cesar": "/usr/local/bin/cesar"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cesar.
singularity registry hpc automated addition for cesar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cesar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cesar:1.01--h87f3376_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cesar/1.01--h87f3376_0
$ module help quay.io/biocontainers/cesar/1.01--h87f3376_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cesar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cesar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cesar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cesar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cesar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cesar-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cesar

```bash
$ singularity exec <container> /usr/local/bin/cesar
$ podman run --it --rm --entrypoint /usr/local/bin/cesar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cesar   -v ${PWD} -w ${PWD} <container> -c " $@"
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
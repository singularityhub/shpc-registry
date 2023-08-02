---
layout: container
name:  "quay.io/biocontainers/calib"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/calib/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/calib/container.yaml"
updated_at: "2023-08-02 02:44:11.115667"
latest: "0.3.4--hdcf5f25_5"
container_url: "https://biocontainers.pro/tools/calib"
aliases:
 - "calib"
 - "calib_cons"
versions:
 - "0.3.4--hd03093a_3"
 - "0.3.4--hdcf5f25_5"
description: "shpc-registry automated BioContainers addition for calib"
config: {"url": "https://biocontainers.pro/tools/calib", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for calib", "latest": {"0.3.4--hdcf5f25_5": "sha256:31178d7e1c849d9fb68146c1abda0fc11af12ee0c499e0001887c0a694d46162"}, "tags": {"0.3.4--hd03093a_3": "sha256:3c6e3dfd1c7d09da5b9174ae9e4fa2c4d1627ab1366dbe9632e3894790e4a5f0", "0.3.4--hdcf5f25_5": "sha256:31178d7e1c849d9fb68146c1abda0fc11af12ee0c499e0001887c0a694d46162"}, "docker": "quay.io/biocontainers/calib", "aliases": {"calib": "/usr/local/bin/calib", "calib_cons": "/usr/local/bin/calib_cons"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/calib.
shpc-registry automated BioContainers addition for calib
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/calib
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/calib:0.3.4--hdcf5f25_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/calib/0.3.4--hdcf5f25_5
$ module help quay.io/biocontainers/calib/0.3.4--hdcf5f25_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### calib-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### calib-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### calib-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### calib-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### calib-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### calib-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### calib

```bash
$ singularity exec <container> /usr/local/bin/calib
$ podman run --it --rm --entrypoint /usr/local/bin/calib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/calib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### calib_cons

```bash
$ singularity exec <container> /usr/local/bin/calib_cons
$ podman run --it --rm --entrypoint /usr/local/bin/calib_cons   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/calib_cons   -v ${PWD} -w ${PWD} <container> -c " $@"
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
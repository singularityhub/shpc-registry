---
layout: container
name:  "quay.io/biocontainers/scvi-tools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/scvi-tools/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/scvi-tools/container.yaml"
updated_at: "2022-10-27 00:39:47.497713"
latest: "0.9.1--py_0"
container_url: "https://biocontainers.pro/tools/scvi-tools"
aliases:
 - "hyperopt-mongo-worker"
 - "keyring"
 - "pkginfo"
 - "poetry"
versions:
 - "0.9.1--py_0"
description: "shpc-registry automated BioContainers addition for scvi-tools"
config: {"url": "https://biocontainers.pro/tools/scvi-tools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for scvi-tools", "latest": {"0.9.1--py_0": "sha256:0bee7f7bbdc70fc3294f72588a35e06b986f50fcafda73aa009b2acd108d232c"}, "tags": {"0.9.1--py_0": "sha256:0bee7f7bbdc70fc3294f72588a35e06b986f50fcafda73aa009b2acd108d232c"}, "docker": "quay.io/biocontainers/scvi-tools", "aliases": {"hyperopt-mongo-worker": "/usr/local/bin/hyperopt-mongo-worker", "keyring": "/usr/local/bin/keyring", "pkginfo": "/usr/local/bin/pkginfo", "poetry": "/usr/local/bin/poetry"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/scvi-tools.
shpc-registry automated BioContainers addition for scvi-tools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/scvi-tools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/scvi-tools:0.9.1--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/scvi-tools/0.9.1--py_0
$ module help quay.io/biocontainers/scvi-tools/0.9.1--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### scvi-tools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### scvi-tools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### scvi-tools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### scvi-tools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### scvi-tools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### scvi-tools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hyperopt-mongo-worker

```bash
$ singularity exec <container> /usr/local/bin/hyperopt-mongo-worker
$ podman run --it --rm --entrypoint /usr/local/bin/hyperopt-mongo-worker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hyperopt-mongo-worker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### keyring

```bash
$ singularity exec <container> /usr/local/bin/keyring
$ podman run --it --rm --entrypoint /usr/local/bin/keyring   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/keyring   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pkginfo

```bash
$ singularity exec <container> /usr/local/bin/pkginfo
$ podman run --it --rm --entrypoint /usr/local/bin/pkginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pkginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### poetry

```bash
$ singularity exec <container> /usr/local/bin/poetry
$ podman run --it --rm --entrypoint /usr/local/bin/poetry   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/poetry   -v ${PWD} -w ${PWD} <container> -c " $@"
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
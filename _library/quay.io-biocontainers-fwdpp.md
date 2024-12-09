---
layout: container
name:  "quay.io/biocontainers/fwdpp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fwdpp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fwdpp/container.yaml"
updated_at: "2024-12-09 03:57:05.132708"
latest: "0.5.7--2"
container_url: "https://biocontainers.pro/tools/fwdpp"
aliases:
 - "fwdppConfig"
versions:
 - "0.5.7--2"
description: "shpc-registry automated BioContainers addition for fwdpp"
config: {"url": "https://biocontainers.pro/tools/fwdpp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fwdpp", "latest": {"0.5.7--2": "sha256:340ff385d06bf3e5e292c8554a4590ad50f383c38b3e2f408341caa6a0892455"}, "tags": {"0.5.7--2": "sha256:340ff385d06bf3e5e292c8554a4590ad50f383c38b3e2f408341caa6a0892455"}, "docker": "quay.io/biocontainers/fwdpp", "aliases": {"fwdppConfig": "/usr/local/bin/fwdppConfig"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fwdpp.
shpc-registry automated BioContainers addition for fwdpp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fwdpp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fwdpp:0.5.7--2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fwdpp/0.5.7--2
$ module help quay.io/biocontainers/fwdpp/0.5.7--2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fwdpp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fwdpp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fwdpp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fwdpp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fwdpp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fwdpp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fwdppConfig

```bash
$ singularity exec <container> /usr/local/bin/fwdppConfig
$ podman run --it --rm --entrypoint /usr/local/bin/fwdppConfig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fwdppConfig   -v ${PWD} -w ${PWD} <container> -c " $@"
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
---
layout: container
name:  "quay.io/biocontainers/smashpp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/smashpp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/smashpp/container.yaml"
updated_at: "2026-01-06 04:29:42.739537"
latest: "23.09--h9948957_1"
container_url: "https://biocontainers.pro/tools/smashpp"
aliases:
 - "exclude_N"
 - "smashpp"
 - "smashpp-inv-rep"
versions:
 - "22.08--h9f5acd7_0"
 - "22.08--h4ac6f70_2"
 - "23.09--h4ac6f70_0"
 - "23.09--h9948957_1"
description: "shpc-registry automated BioContainers addition for smashpp"
config: {"url": "https://biocontainers.pro/tools/smashpp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for smashpp", "latest": {"23.09--h9948957_1": "sha256:4b214521d55f75f3656dd9d151716b53634a60e21576f529454d8a3edb954650"}, "tags": {"22.08--h9f5acd7_0": "sha256:991a0d84349a12ecef06c176bdcea2424abb140f293d5c041ba9c9b2433adcdd", "22.08--h4ac6f70_2": "sha256:f4d9347fce5907dfff4e015c4ff460f592da981ecb4554415a9f31a43a0e1da9", "23.09--h4ac6f70_0": "sha256:39365dfc11629d21f7bf5934f4b6f6eff205eaa3ccf87700b97863f550984c48", "23.09--h9948957_1": "sha256:4b214521d55f75f3656dd9d151716b53634a60e21576f529454d8a3edb954650"}, "docker": "quay.io/biocontainers/smashpp", "aliases": {"exclude_N": "/usr/local/bin/exclude_N", "smashpp": "/usr/local/bin/smashpp", "smashpp-inv-rep": "/usr/local/bin/smashpp-inv-rep"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/smashpp.
shpc-registry automated BioContainers addition for smashpp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/smashpp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/smashpp:23.09--h9948957_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/smashpp/23.09--h9948957_1
$ module help quay.io/biocontainers/smashpp/23.09--h9948957_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### smashpp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### smashpp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### smashpp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### smashpp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### smashpp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### smashpp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### exclude_N

```bash
$ singularity exec <container> /usr/local/bin/exclude_N
$ podman run --it --rm --entrypoint /usr/local/bin/exclude_N   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exclude_N   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smashpp

```bash
$ singularity exec <container> /usr/local/bin/smashpp
$ podman run --it --rm --entrypoint /usr/local/bin/smashpp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smashpp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smashpp-inv-rep

```bash
$ singularity exec <container> /usr/local/bin/smashpp-inv-rep
$ podman run --it --rm --entrypoint /usr/local/bin/smashpp-inv-rep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smashpp-inv-rep   -v ${PWD} -w ${PWD} <container> -c " $@"
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
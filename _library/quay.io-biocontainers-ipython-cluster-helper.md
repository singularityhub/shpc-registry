---
layout: container
name:  "quay.io/biocontainers/ipython-cluster-helper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ipython-cluster-helper/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ipython-cluster-helper/container.yaml"
updated_at: "2022-10-27 00:54:53.159874"
latest: "0.6.4--pyh864c0ab_1"
container_url: "https://biocontainers.pro/tools/ipython-cluster-helper"
aliases:
 - "ipcluster"
 - "ipcontroller"
 - "ipengine"
versions:
 - "0.6.4--pyh864c0ab_1"
description: "shpc-registry automated BioContainers addition for ipython-cluster-helper"
config: {"url": "https://biocontainers.pro/tools/ipython-cluster-helper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ipython-cluster-helper", "latest": {"0.6.4--pyh864c0ab_1": "sha256:99713d8628a67bb15eebe345b8cfd0121e6a0b879043aa43811ae8d844bf6967"}, "tags": {"0.6.4--pyh864c0ab_1": "sha256:99713d8628a67bb15eebe345b8cfd0121e6a0b879043aa43811ae8d844bf6967"}, "docker": "quay.io/biocontainers/ipython-cluster-helper", "aliases": {"ipcluster": "/usr/local/bin/ipcluster", "ipcontroller": "/usr/local/bin/ipcontroller", "ipengine": "/usr/local/bin/ipengine"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ipython-cluster-helper.
shpc-registry automated BioContainers addition for ipython-cluster-helper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ipython-cluster-helper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ipython-cluster-helper:0.6.4--pyh864c0ab_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ipython-cluster-helper/0.6.4--pyh864c0ab_1
$ module help quay.io/biocontainers/ipython-cluster-helper/0.6.4--pyh864c0ab_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ipython-cluster-helper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ipython-cluster-helper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ipython-cluster-helper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ipython-cluster-helper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ipython-cluster-helper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ipython-cluster-helper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ipcluster

```bash
$ singularity exec <container> /usr/local/bin/ipcluster
$ podman run --it --rm --entrypoint /usr/local/bin/ipcluster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipcluster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipcontroller

```bash
$ singularity exec <container> /usr/local/bin/ipcontroller
$ podman run --it --rm --entrypoint /usr/local/bin/ipcontroller   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipcontroller   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipengine

```bash
$ singularity exec <container> /usr/local/bin/ipengine
$ podman run --it --rm --entrypoint /usr/local/bin/ipengine   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipengine   -v ${PWD} -w ${PWD} <container> -c " $@"
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
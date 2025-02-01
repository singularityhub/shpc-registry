---
layout: container
name:  "quay.io/biocontainers/colorid_bv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/colorid_bv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/colorid_bv/container.yaml"
updated_at: "2025-02-01 02:51:00.586420"
latest: "0.1.0--h3ab6199_2"
container_url: "https://biocontainers.pro/tools/colorid_bv"
aliases:
 - "colorid_bv"
versions:
 - "0.1.0--h4c94732_0"
 - "0.1.0--h4c94732_1"
 - "0.1.0--h3ab6199_2"
description: "singularity registry hpc automated addition for colorid_bv"
config: {"url": "https://biocontainers.pro/tools/colorid_bv", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for colorid_bv", "latest": {"0.1.0--h3ab6199_2": "sha256:384c98f0d282ca57b0fe3a70c573bf9b96d6efe1788b54e09df8f7109533df17"}, "tags": {"0.1.0--h4c94732_0": "sha256:e96b937564b1f40ae5b834163d6737ba95bbb6b0e2b996d34fd385429271fdaa", "0.1.0--h4c94732_1": "sha256:1a808527472f8d37acad643b4f9847683222aaddeb6fdc694437472468fdfc5d", "0.1.0--h3ab6199_2": "sha256:384c98f0d282ca57b0fe3a70c573bf9b96d6efe1788b54e09df8f7109533df17"}, "docker": "quay.io/biocontainers/colorid_bv", "aliases": {"colorid_bv": "/usr/local/bin/colorid_bv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/colorid_bv.
singularity registry hpc automated addition for colorid_bv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/colorid_bv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/colorid_bv:0.1.0--h3ab6199_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/colorid_bv/0.1.0--h3ab6199_2
$ module help quay.io/biocontainers/colorid_bv/0.1.0--h3ab6199_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### colorid_bv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### colorid_bv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### colorid_bv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### colorid_bv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### colorid_bv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### colorid_bv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### colorid_bv

```bash
$ singularity exec <container> /usr/local/bin/colorid_bv
$ podman run --it --rm --entrypoint /usr/local/bin/colorid_bv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/colorid_bv   -v ${PWD} -w ${PWD} <container> -c " $@"
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
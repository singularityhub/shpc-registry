---
layout: container
name:  "bids/freesurfer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/bids/freesurfer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/bids/freesurfer/container.yaml"
updated_at: "2024-11-24 03:50:29.035206"
latest: "V30-a43f1f"
container_url: "https://hub.docker.com/r/bids/freesurfer"

versions:
 - "latest"
 - "v6.0.1-6.1"
 - "V30-a43f1f"
 - "V29-37bf1c"
 - "V28-ae189c"
 - "enh_QA"
 - "7-202309"
 - "7.4.1-202309"
description: "Surface reconstruction using Freesurfer"
config: {"docker": "bids/freesurfer", "url": "https://hub.docker.com/r/bids/freesurfer", "maintainer": "@vsoch", "description": "Surface reconstruction using Freesurfer", "latest": {"V30-a43f1f": "sha256:cb7aee6c7634d7e57530b6b72230009759fe2c020c573aad87e71a523ba075f3"}, "tags": {"latest": "sha256:3a06160de8a1fbaed9b31993b5dee1e7f590f95626754d9a4db493113112ed3e", "v6.0.1-6.1": "sha256:02237eda4a22bb5fd66a50a66d21b13e0f378840fa61a937dab8794ee527cd48", "V30-a43f1f": "sha256:cb7aee6c7634d7e57530b6b72230009759fe2c020c573aad87e71a523ba075f3", "V29-37bf1c": "sha256:513303323f955365d05b5b5d3223a37102c6eb064cc46d2a658db8de33db06c9", "V28-ae189c": "sha256:ebdd94e63210301f277c00ad0e3464f1b1baa5703f5dad19f094f299e74f86c0", "enh_QA": "sha256:b9fe8cf6d6cc2912f1671ab009d8d8805eb22f8b260f598069822807507f02fd", "7-202309": "sha256:720b4365f2bc4c4b787d6a80606a2dc06e5ef88f44f55c06131e829845f3b433", "7.4.1-202309": "sha256:720b4365f2bc4c4b787d6a80606a2dc06e5ef88f44f55c06131e829845f3b433"}, "filter": ["v*"]}
---

This module is a singularity container wrapper for bids/freesurfer.
Surface reconstruction using Freesurfer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install bids/freesurfer
```

Or a specific version:

```bash
$ shpc install bids/freesurfer:V30-a43f1f
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load bids/freesurfer/V30-a43f1f
$ module help bids/freesurfer/V30-a43f1f
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### freesurfer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### freesurfer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### freesurfer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### freesurfer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### freesurfer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### freesurfer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### freesurfer

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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
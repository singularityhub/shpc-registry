---
layout: container
name:  "bids/niak"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/bids/niak/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/bids/niak/container.yaml"
updated_at: "2024-08-26 02:38:29.893935"
latest: "latest"
container_url: "https://hub.docker.com/r/bids/niak"

versions:
 - "latest"
description: "The neuroimaging analysis kit. Pipeline for preprocessing of fMRI and structural MRI scans http://niak.simexp-lab.org/ (https://github.com/BIDS-Apps/niak)"
config: {"docker": "bids/niak", "latest": {"latest": "sha256:b1f6a71a6c440bf94ef6081d1b7a5c9576454ad9c98e629fbda357e702f75b3e"}, "tags": {"latest": "sha256:b1f6a71a6c440bf94ef6081d1b7a5c9576454ad9c98e629fbda357e702f75b3e"}, "filter": ["latest"], "maintainer": "@vsoch", "description": "The neuroimaging analysis kit. Pipeline for preprocessing of fMRI and structural MRI scans http://niak.simexp-lab.org/ (https://github.com/BIDS-Apps/niak)", "url": "https://hub.docker.com/r/bids/niak"}
---

This module is a singularity container wrapper for bids/niak.
The neuroimaging analysis kit. Pipeline for preprocessing of fMRI and structural MRI scans http://niak.simexp-lab.org/ (https://github.com/BIDS-Apps/niak)
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install bids/niak
```

Or a specific version:

```bash
$ shpc install bids/niak:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load bids/niak/latest
$ module help bids/niak/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### niak-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### niak-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### niak-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### niak-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### niak-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### niak-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### niak

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
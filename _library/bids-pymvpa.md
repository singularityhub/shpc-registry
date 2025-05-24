---
layout: container
name:  "bids/pymvpa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/bids/pymvpa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/bids/pymvpa/container.yaml"
updated_at: "2025-05-24 03:09:00.690359"
latest: "v4.0.4"
container_url: "https://hub.docker.com/r/bids/pymvpa"

versions:
 - "latest"
 - "v2.0.2"
 - "v4.0.1"
 - "unstable"
 - "v4.0.3"
 - "v4.0.4"
description: "Take fMRI data and generates ROI based MultiVariate Pattern Analysis (MVPA) outputs (https://github.com/BIDS-Apps/PyMVPA)"
config: {"docker": "bids/pymvpa", "url": "https://hub.docker.com/r/bids/pymvpa", "maintainer": "@vsoch", "description": "Take fMRI data and generates ROI based MultiVariate Pattern Analysis (MVPA) outputs (https://github.com/BIDS-Apps/PyMVPA)", "latest": {"v4.0.4": "sha256:443e6d18df66418bc88acd43fed2e0a3992a979d65f0d50c02596bc6c314ff12"}, "tags": {"latest": "sha256:fd1763835219279f0fca18d880a827cba52b70b014b0f5dd5c62ec6525be45f6", "v2.0.2": "sha256:fd1763835219279f0fca18d880a827cba52b70b014b0f5dd5c62ec6525be45f6", "v4.0.1": "sha256:e29fbce4e72f4dc53fcada1ddeb2e7bfc8ef7f696b5b6ac8492c9d0689ce8e5d", "unstable": "sha256:fd1763835219279f0fca18d880a827cba52b70b014b0f5dd5c62ec6525be45f6", "v4.0.3": "sha256:b9b443b6803ec40e82fd617cb9062641a1c4bbd6a6cd6d77c2a3dc2136e77b57", "v4.0.4": "sha256:443e6d18df66418bc88acd43fed2e0a3992a979d65f0d50c02596bc6c314ff12"}, "filter": ["v*"]}
---

This module is a singularity container wrapper for bids/pymvpa.
Take fMRI data and generates ROI based MultiVariate Pattern Analysis (MVPA) outputs (https://github.com/BIDS-Apps/PyMVPA)
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install bids/pymvpa
```

Or a specific version:

```bash
$ shpc install bids/pymvpa:v4.0.4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load bids/pymvpa/v4.0.4
$ module help bids/pymvpa/v4.0.4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pymvpa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pymvpa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pymvpa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pymvpa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pymvpa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pymvpa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### pymvpa

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
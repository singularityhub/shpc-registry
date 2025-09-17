---
layout: container
name:  "quay.io/biocontainers/leviosam2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/leviosam2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/leviosam2/container.yaml"
updated_at: "2025-09-17 03:45:56.712850"
latest: "0.5.0--h9948957_1"
container_url: "https://biocontainers.pro/tools/leviosam2"
aliases:
 - "leviosam2"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.3.0--h28e74a2_0"
 - "0.3.0--hf77a93e_1"
 - "0.3.0--h84372a0_2"
 - "0.4.0--h4ac6f70_0"
 - "0.4.1--h4ac6f70_0"
 - "0.4.2--h4ac6f70_0"
 - "0.5.0--h4ac6f70_0"
 - "0.5.0--h9948957_1"
description: "singularity registry hpc automated addition for leviosam2"
config: {"url": "https://biocontainers.pro/tools/leviosam2", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for leviosam2", "latest": {"0.5.0--h9948957_1": "sha256:fe0a4fc3b0a1364bfee5e76d3e5da70a84d531695a1150d2fb07c71f176aa5aa"}, "tags": {"0.3.0--h28e74a2_0": "sha256:0f9408d2585fdff469405db33f4fcb7ab6447a3046d97cbc12dc128d8651317d", "0.3.0--hf77a93e_1": "sha256:88ee0e89173512415d5db65f225235c13f306688d66ba90f5c28d8de1f05f10c", "0.3.0--h84372a0_2": "sha256:6d7b299668754cab7d818e00b9fad24a49a3f7af5004f1d4d934e058d67b2454", "0.4.0--h4ac6f70_0": "sha256:0859ddedda456cf599abb862d28ac97f68505f2e3473b04163e784d8047980e6", "0.4.1--h4ac6f70_0": "sha256:480a5726966af496bc33f28df19248b2510e576768679c0d8ca3ef0233b5fdc9", "0.4.2--h4ac6f70_0": "sha256:405aacb46b4b8b2fd62d713638ed6d0b9176ec3c686ea3c30d385fd6bb4abf8c", "0.5.0--h4ac6f70_0": "sha256:2734d84bfe4639bc8ced8fc54967f6fabb7a24ae9ba60b60c9ee61bdf904a9ee", "0.5.0--h9948957_1": "sha256:fe0a4fc3b0a1364bfee5e76d3e5da70a84d531695a1150d2fb07c71f176aa5aa"}, "docker": "quay.io/biocontainers/leviosam2", "aliases": {"leviosam2": "/usr/local/bin/leviosam2", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/leviosam2.
singularity registry hpc automated addition for leviosam2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/leviosam2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/leviosam2:0.5.0--h9948957_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/leviosam2/0.5.0--h9948957_1
$ module help quay.io/biocontainers/leviosam2/0.5.0--h9948957_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### leviosam2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### leviosam2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### leviosam2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### leviosam2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### leviosam2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### leviosam2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### leviosam2

```bash
$ singularity exec <container> /usr/local/bin/leviosam2
$ podman run --it --rm --entrypoint /usr/local/bin/leviosam2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/leviosam2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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
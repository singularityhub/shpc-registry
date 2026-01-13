---
layout: container
name:  "quay.io/biocontainers/nail"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nail/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nail/container.yaml"
updated_at: "2026-01-13 03:55:18.364712"
latest: "0.4.0--h4349ce8_1"
container_url: "https://biocontainers.pro/tools/nail"
aliases:
 - "nail"
versions:
 - "0.3.0--h4349ce8_0"
 - "0.3.0--h4349ce8_1"
 - "0.4.0--h4349ce8_0"
 - "0.4.0--h4349ce8_1"
description: "singularity registry hpc automated addition for nail"
config: {"url": "https://biocontainers.pro/tools/nail", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for nail", "latest": {"0.4.0--h4349ce8_1": "sha256:09bb02327d890f1af81b897ccfb71e5b3f78f526bb8c73295ebe08f21e36ec21"}, "tags": {"0.3.0--h4349ce8_0": "sha256:54e47136c7445593ec40965b74d74f4473a6a6bac447c8364e1c884960f7d43c", "0.3.0--h4349ce8_1": "sha256:f9c8f1bd41f2a0561bb2d4ce640ebffc4a671c5ae52ba140b49225cd72487e6e", "0.4.0--h4349ce8_0": "sha256:fbd4fee71cdf448391cd4dd66100ac33d982775e25ab38e376024c07852e0ed8", "0.4.0--h4349ce8_1": "sha256:09bb02327d890f1af81b897ccfb71e5b3f78f526bb8c73295ebe08f21e36ec21"}, "docker": "quay.io/biocontainers/nail", "aliases": {"nail": "/usr/local/bin/nail"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nail.
singularity registry hpc automated addition for nail
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nail
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nail:0.4.0--h4349ce8_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nail/0.4.0--h4349ce8_1
$ module help quay.io/biocontainers/nail/0.4.0--h4349ce8_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nail-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nail-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nail-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nail-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nail-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nail-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### nail

```bash
$ singularity exec <container> /usr/local/bin/nail
$ podman run --it --rm --entrypoint /usr/local/bin/nail   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nail   -v ${PWD} -w ${PWD} <container> -c " $@"
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
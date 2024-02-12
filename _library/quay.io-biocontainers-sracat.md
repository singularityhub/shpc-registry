---
layout: container
name:  "quay.io/biocontainers/sracat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sracat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sracat/container.yaml"
updated_at: "2024-02-12 03:11:22.366164"
latest: "0.2--hdcf5f25_2"
container_url: "https://biocontainers.pro/tools/sracat"
aliases:
 - "sracat"
versions:
 - "0.2--h9f5acd7_1"
 - "0.2--hdcf5f25_2"
description: "shpc-registry automated BioContainers addition for sracat"
config: {"url": "https://biocontainers.pro/tools/sracat", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sracat", "latest": {"0.2--hdcf5f25_2": "sha256:7670de916b70f3451a20fe0707d1fb20eb29376d27b45c66ac5216ee16fa2fc4"}, "tags": {"0.2--h9f5acd7_1": "sha256:be9c04f036953a0cf20f58ffc8aaa247dae3323e4d2f08e00f2a85ee06222083", "0.2--hdcf5f25_2": "sha256:7670de916b70f3451a20fe0707d1fb20eb29376d27b45c66ac5216ee16fa2fc4"}, "docker": "quay.io/biocontainers/sracat", "aliases": {"sracat": "/usr/local/bin/sracat"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sracat.
shpc-registry automated BioContainers addition for sracat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sracat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sracat:0.2--hdcf5f25_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sracat/0.2--hdcf5f25_2
$ module help quay.io/biocontainers/sracat/0.2--hdcf5f25_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sracat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sracat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sracat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sracat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sracat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sracat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sracat

```bash
$ singularity exec <container> /usr/local/bin/sracat
$ podman run --it --rm --entrypoint /usr/local/bin/sracat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sracat   -v ${PWD} -w ${PWD} <container> -c " $@"
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
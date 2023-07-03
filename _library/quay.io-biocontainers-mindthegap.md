---
layout: container
name:  "quay.io/biocontainers/mindthegap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mindthegap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mindthegap/container.yaml"
updated_at: "2023-07-03 03:57:52.037824"
latest: "2.3.0--hdcf5f25_3"
container_url: "https://biocontainers.pro/tools/mindthegap"
aliases:
 - "MindTheGap"
 - "dbgh5"
 - "dbginfo"
versions:
 - "2.3.0--hd03093a_1"
 - "2.3.0--hd03093a_2"
 - "2.3.0--hdcf5f25_3"
description: "shpc-registry automated BioContainers addition for mindthegap"
config: {"url": "https://biocontainers.pro/tools/mindthegap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mindthegap", "latest": {"2.3.0--hdcf5f25_3": "sha256:571eabf983ba9288549f87401b12275b056849fae941831f8a4da18023b7fbf0"}, "tags": {"2.3.0--hd03093a_1": "sha256:9a4c61eb00c2b9b64235adb72e93acb22483e447c80ca3b5f340cbf488af5179", "2.3.0--hd03093a_2": "sha256:825aa6d341f3e8153c63c6a9a9b2f15850cf8b1d258ab0fbbacd4fa6e8f3b6d4", "2.3.0--hdcf5f25_3": "sha256:571eabf983ba9288549f87401b12275b056849fae941831f8a4da18023b7fbf0"}, "docker": "quay.io/biocontainers/mindthegap", "aliases": {"MindTheGap": "/usr/local/bin/MindTheGap", "dbgh5": "/usr/local/bin/dbgh5", "dbginfo": "/usr/local/bin/dbginfo"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mindthegap.
shpc-registry automated BioContainers addition for mindthegap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mindthegap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mindthegap:2.3.0--hdcf5f25_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mindthegap/2.3.0--hdcf5f25_3
$ module help quay.io/biocontainers/mindthegap/2.3.0--hdcf5f25_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mindthegap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mindthegap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mindthegap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mindthegap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mindthegap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mindthegap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### MindTheGap

```bash
$ singularity exec <container> /usr/local/bin/MindTheGap
$ podman run --it --rm --entrypoint /usr/local/bin/MindTheGap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MindTheGap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbgh5

```bash
$ singularity exec <container> /usr/local/bin/dbgh5
$ podman run --it --rm --entrypoint /usr/local/bin/dbgh5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbgh5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbginfo

```bash
$ singularity exec <container> /usr/local/bin/dbginfo
$ podman run --it --rm --entrypoint /usr/local/bin/dbginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
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
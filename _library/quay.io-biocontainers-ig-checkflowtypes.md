---
layout: container
name:  "quay.io/biocontainers/ig-checkflowtypes"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ig-checkflowtypes/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ig-checkflowtypes/container.yaml"
updated_at: "2023-10-28 03:02:47.185895"
latest: "1.0.0--r36h4333106_3"
container_url: "https://biocontainers.pro/tools/ig-checkflowtypes"
aliases:
 - "checkFCS.R"
 - "checkFlowSOM.R"
 - "checkFlowSet.R"
 - "checkFlowframe.R"
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.0.0--r36h4333106_3"
description: "shpc-registry automated BioContainers addition for ig-checkflowtypes"
config: {"url": "https://biocontainers.pro/tools/ig-checkflowtypes", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ig-checkflowtypes", "latest": {"1.0.0--r36h4333106_3": "sha256:0dbe60b2b38b3e4186727714cd61b28065cbd1c74f568197fc6fe361ae327c16"}, "tags": {"1.0.0--r36h4333106_3": "sha256:0dbe60b2b38b3e4186727714cd61b28065cbd1c74f568197fc6fe361ae327c16"}, "docker": "quay.io/biocontainers/ig-checkflowtypes", "aliases": {"checkFCS.R": "/usr/local/bin/checkFCS.R", "checkFlowSOM.R": "/usr/local/bin/checkFlowSOM.R", "checkFlowSet.R": "/usr/local/bin/checkFlowSet.R", "checkFlowframe.R": "/usr/local/bin/checkFlowframe.R", "gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ig-checkflowtypes.
shpc-registry automated BioContainers addition for ig-checkflowtypes
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ig-checkflowtypes
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ig-checkflowtypes:1.0.0--r36h4333106_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ig-checkflowtypes/1.0.0--r36h4333106_3
$ module help quay.io/biocontainers/ig-checkflowtypes/1.0.0--r36h4333106_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ig-checkflowtypes-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ig-checkflowtypes-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ig-checkflowtypes-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ig-checkflowtypes-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ig-checkflowtypes-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ig-checkflowtypes-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### checkFCS.R

```bash
$ singularity exec <container> /usr/local/bin/checkFCS.R
$ podman run --it --rm --entrypoint /usr/local/bin/checkFCS.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checkFCS.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checkFlowSOM.R

```bash
$ singularity exec <container> /usr/local/bin/checkFlowSOM.R
$ podman run --it --rm --entrypoint /usr/local/bin/checkFlowSOM.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checkFlowSOM.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checkFlowSet.R

```bash
$ singularity exec <container> /usr/local/bin/checkFlowSet.R
$ podman run --it --rm --entrypoint /usr/local/bin/checkFlowSet.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checkFlowSet.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checkFlowframe.R

```bash
$ singularity exec <container> /usr/local/bin/checkFlowframe.R
$ podman run --it --rm --entrypoint /usr/local/bin/checkFlowframe.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checkFlowframe.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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
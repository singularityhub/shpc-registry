---
layout: container
name:  "quay.io/biocontainers/cwltool"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cwltool/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/cwltool/container.yaml"
updated_at: "2022-10-27 00:41:01.060540"
latest: "1.0.20180225105849--py_1"
container_url: "https://biocontainers.pro/tools/cwltool"
aliases:
 - "cwltest"
versions:
 - "1.0.20180225105849--py_1"
description: "shpc-registry automated BioContainers addition for cwltool"
config: {"url": "https://biocontainers.pro/tools/cwltool", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cwltool", "latest": {"1.0.20180225105849--py_1": "sha256:36261cc468c88fad8167fa02207c79b0d57d3736969d012bbcf8773c5a2ba8ba"}, "tags": {"1.0.20180225105849--py_1": "sha256:36261cc468c88fad8167fa02207c79b0d57d3736969d012bbcf8773c5a2ba8ba"}, "docker": "quay.io/biocontainers/cwltool", "aliases": {"cwltest": "/usr/local/bin/cwltest"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cwltool.
shpc-registry automated BioContainers addition for cwltool
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cwltool
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cwltool:1.0.20180225105849--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cwltool/1.0.20180225105849--py_1
$ module help quay.io/biocontainers/cwltool/1.0.20180225105849--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cwltool-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cwltool-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cwltool-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cwltool-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cwltool-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cwltool-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cwltest

```bash
$ singularity exec <container> /usr/local/bin/cwltest
$ podman run --it --rm --entrypoint /usr/local/bin/cwltest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwltest   -v ${PWD} -w ${PWD} <container> -c " $@"
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
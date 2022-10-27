---
layout: container
name:  "quay.io/biocontainers/spotyping3"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/spotyping3/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/spotyping3/container.yaml"
updated_at: "2022-10-27 00:30:13.167682"
latest: "3.0--py_0"
container_url: "https://biocontainers.pro/tools/spotyping3"
aliases:
 - "SpoTyping.py"
 - "SpoTyping_plot.r"
versions:
 - "3.0--py_0"
description: "shpc-registry automated BioContainers addition for spotyping3"
config: {"url": "https://biocontainers.pro/tools/spotyping3", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for spotyping3", "latest": {"3.0--py_0": "sha256:7180a61d05e07338b2e2726e460c5e419b8687b6db8c9871fd578fc02690ff3e"}, "tags": {"3.0--py_0": "sha256:7180a61d05e07338b2e2726e460c5e419b8687b6db8c9871fd578fc02690ff3e"}, "docker": "quay.io/biocontainers/spotyping3", "aliases": {"SpoTyping.py": "/usr/local/bin/SpoTyping.py", "SpoTyping_plot.r": "/usr/local/bin/SpoTyping_plot.r"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/spotyping3.
shpc-registry automated BioContainers addition for spotyping3
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/spotyping3
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/spotyping3:3.0--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/spotyping3/3.0--py_0
$ module help quay.io/biocontainers/spotyping3/3.0--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### spotyping3-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### spotyping3-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### spotyping3-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### spotyping3-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### spotyping3-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### spotyping3-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SpoTyping.py

```bash
$ singularity exec <container> /usr/local/bin/SpoTyping.py
$ podman run --it --rm --entrypoint /usr/local/bin/SpoTyping.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SpoTyping.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SpoTyping_plot.r

```bash
$ singularity exec <container> /usr/local/bin/SpoTyping_plot.r
$ podman run --it --rm --entrypoint /usr/local/bin/SpoTyping_plot.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SpoTyping_plot.r   -v ${PWD} -w ${PWD} <container> -c " $@"
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
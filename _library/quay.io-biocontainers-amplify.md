---
layout: container
name:  "quay.io/biocontainers/amplify"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/amplify/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/amplify/container.yaml"
updated_at: "2022-10-29 05:50:27.007889"
latest: "1.1.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/amplify"
aliases:
 - "AMPlify"
 - "train_amplify"
 - "2to3-3.6"
 - "f2py3.6"
 - "freeze_graph"
 - "gif2h5"
 - "h52gif"
 - "h5c++"
 - "h5cc"
 - "h5clear"
 - "h5copy"
 - "h5debug"
versions:
 - "1.1.0--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for amplify"
config: {"url": "https://biocontainers.pro/tools/amplify", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for amplify", "latest": {"1.1.0--hdfd78af_0": "sha256:787ca694b922f8ee6313d2df2b429ad62940444f8ebc60edc1f9b5e283a24928"}, "tags": {"1.1.0--hdfd78af_0": "sha256:787ca694b922f8ee6313d2df2b429ad62940444f8ebc60edc1f9b5e283a24928"}, "docker": "quay.io/biocontainers/amplify", "aliases": {"AMPlify": "/usr/local/bin/AMPlify", "train_amplify": "/usr/local/bin/train_amplify", "2to3-3.6": "/usr/local/bin/2to3-3.6", "f2py3.6": "/usr/local/bin/f2py3.6", "freeze_graph": "/usr/local/bin/freeze_graph", "gif2h5": "/usr/local/bin/gif2h5", "h52gif": "/usr/local/bin/h52gif", "h5c++": "/usr/local/bin/h5c++", "h5cc": "/usr/local/bin/h5cc", "h5clear": "/usr/local/bin/h5clear", "h5copy": "/usr/local/bin/h5copy", "h5debug": "/usr/local/bin/h5debug"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/amplify.
shpc-registry automated BioContainers addition for amplify
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/amplify
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/amplify:1.1.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/amplify/1.1.0--hdfd78af_0
$ module help quay.io/biocontainers/amplify/1.1.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### amplify-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### amplify-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### amplify-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### amplify-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### amplify-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### amplify-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### AMPlify

```bash
$ singularity exec <container> /usr/local/bin/AMPlify
$ podman run --it --rm --entrypoint /usr/local/bin/AMPlify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AMPlify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### train_amplify

```bash
$ singularity exec <container> /usr/local/bin/train_amplify
$ podman run --it --rm --entrypoint /usr/local/bin/train_amplify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/train_amplify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.6

```bash
$ singularity exec <container> /usr/local/bin/f2py3.6
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### freeze_graph

```bash
$ singularity exec <container> /usr/local/bin/freeze_graph
$ podman run --it --rm --entrypoint /usr/local/bin/freeze_graph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/freeze_graph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2h5

```bash
$ singularity exec <container> /usr/local/bin/gif2h5
$ podman run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h52gif

```bash
$ singularity exec <container> /usr/local/bin/h52gif
$ podman run --it --rm --entrypoint /usr/local/bin/h52gif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h52gif   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5c++

```bash
$ singularity exec <container> /usr/local/bin/h5c++
$ podman run --it --rm --entrypoint /usr/local/bin/h5c++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5c++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5cc

```bash
$ singularity exec <container> /usr/local/bin/h5cc
$ podman run --it --rm --entrypoint /usr/local/bin/h5cc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5cc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5clear

```bash
$ singularity exec <container> /usr/local/bin/h5clear
$ podman run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5copy

```bash
$ singularity exec <container> /usr/local/bin/h5copy
$ podman run --it --rm --entrypoint /usr/local/bin/h5copy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5copy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5debug

```bash
$ singularity exec <container> /usr/local/bin/h5debug
$ podman run --it --rm --entrypoint /usr/local/bin/h5debug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5debug   -v ${PWD} -w ${PWD} <container> -c " $@"
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
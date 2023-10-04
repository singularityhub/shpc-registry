---
layout: container
name:  "quay.io/biocontainers/deepbgc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/deepbgc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/deepbgc/container.yaml"
updated_at: "2023-10-04 05:19:51.508854"
latest: "0.1.30--pyhca03a8a_2"
container_url: "https://biocontainers.pro/tools/deepbgc"
aliases:
 - "deepbgc"
 - "g-ir-doc-tool"
 - "theano-cache"
 - "theano-nose"
 - "freeze_graph"
 - "mako-render"
 - "g-ir-annotation-tool"
 - "g-ir-compiler"
 - "g-ir-generate"
 - "g-ir-inspect"
 - "g-ir-scanner"
versions:
 - "0.1.9--py_0"
 - "0.1.30--pyhca03a8a_2"
description: "shpc-registry automated BioContainers addition for deepbgc"
config: {"url": "https://biocontainers.pro/tools/deepbgc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for deepbgc", "latest": {"0.1.30--pyhca03a8a_2": "sha256:3309f4fbb6ca00ef6bde62af358c78ac76da4e3600bb868bed34f13207f438ad"}, "tags": {"0.1.9--py_0": "sha256:5ef5c60c9039dee19ea53f5aba46fec1beea5fe69a40a8d901757ae26fbeddf9", "0.1.30--pyhca03a8a_2": "sha256:3309f4fbb6ca00ef6bde62af358c78ac76da4e3600bb868bed34f13207f438ad"}, "docker": "quay.io/biocontainers/deepbgc", "aliases": {"deepbgc": "/usr/local/bin/deepbgc", "g-ir-doc-tool": "/usr/local/bin/g-ir-doc-tool", "theano-cache": "/usr/local/bin/theano-cache", "theano-nose": "/usr/local/bin/theano-nose", "freeze_graph": "/usr/local/bin/freeze_graph", "mako-render": "/usr/local/bin/mako-render", "g-ir-annotation-tool": "/usr/local/bin/g-ir-annotation-tool", "g-ir-compiler": "/usr/local/bin/g-ir-compiler", "g-ir-generate": "/usr/local/bin/g-ir-generate", "g-ir-inspect": "/usr/local/bin/g-ir-inspect", "g-ir-scanner": "/usr/local/bin/g-ir-scanner"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/deepbgc.
shpc-registry automated BioContainers addition for deepbgc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/deepbgc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/deepbgc:0.1.30--pyhca03a8a_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/deepbgc/0.1.30--pyhca03a8a_2
$ module help quay.io/biocontainers/deepbgc/0.1.30--pyhca03a8a_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### deepbgc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### deepbgc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### deepbgc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### deepbgc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### deepbgc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### deepbgc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### deepbgc

```bash
$ singularity exec <container> /usr/local/bin/deepbgc
$ podman run --it --rm --entrypoint /usr/local/bin/deepbgc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deepbgc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-doc-tool

```bash
$ singularity exec <container> /usr/local/bin/g-ir-doc-tool
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-doc-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-doc-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### theano-cache

```bash
$ singularity exec <container> /usr/local/bin/theano-cache
$ podman run --it --rm --entrypoint /usr/local/bin/theano-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/theano-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### theano-nose

```bash
$ singularity exec <container> /usr/local/bin/theano-nose
$ podman run --it --rm --entrypoint /usr/local/bin/theano-nose   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/theano-nose   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### freeze_graph

```bash
$ singularity exec <container> /usr/local/bin/freeze_graph
$ podman run --it --rm --entrypoint /usr/local/bin/freeze_graph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/freeze_graph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mako-render

```bash
$ singularity exec <container> /usr/local/bin/mako-render
$ podman run --it --rm --entrypoint /usr/local/bin/mako-render   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mako-render   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-annotation-tool

```bash
$ singularity exec <container> /usr/local/bin/g-ir-annotation-tool
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-annotation-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-annotation-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-compiler

```bash
$ singularity exec <container> /usr/local/bin/g-ir-compiler
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-compiler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-compiler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-generate

```bash
$ singularity exec <container> /usr/local/bin/g-ir-generate
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-generate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-generate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-inspect

```bash
$ singularity exec <container> /usr/local/bin/g-ir-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-scanner

```bash
$ singularity exec <container> /usr/local/bin/g-ir-scanner
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-scanner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-scanner   -v ${PWD} -w ${PWD} <container> -c " $@"
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
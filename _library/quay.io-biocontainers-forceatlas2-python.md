---
layout: container
name:  "quay.io/biocontainers/forceatlas2-python"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/forceatlas2-python/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/forceatlas2-python/container.yaml"
updated_at: "2024-07-10 02:54:03.080740"
latest: "1.1--py_1"
container_url: "https://biocontainers.pro/tools/forceatlas2-python"
aliases:
 - "appletviewer"
 - "idlj"
 - "orbd"
 - "schemagen"
 - "servertool"
 - "tnameserv"
 - "wsgen"
 - "wsimport"
 - "xjc"
 - "jaotc"
versions:
 - "1.1--py_1"
description: "shpc-registry automated BioContainers addition for forceatlas2-python"
config: {"url": "https://biocontainers.pro/tools/forceatlas2-python", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for forceatlas2-python", "latest": {"1.1--py_1": "sha256:f37e1832ac2e3e3bb99d12f1e9090c1253a2359294e69b25940107ed9c4e7e3e"}, "tags": {"1.1--py_1": "sha256:f37e1832ac2e3e3bb99d12f1e9090c1253a2359294e69b25940107ed9c4e7e3e"}, "docker": "quay.io/biocontainers/forceatlas2-python", "aliases": {"appletviewer": "/usr/local/bin/appletviewer", "idlj": "/usr/local/bin/idlj", "orbd": "/usr/local/bin/orbd", "schemagen": "/usr/local/bin/schemagen", "servertool": "/usr/local/bin/servertool", "tnameserv": "/usr/local/bin/tnameserv", "wsgen": "/usr/local/bin/wsgen", "wsimport": "/usr/local/bin/wsimport", "xjc": "/usr/local/bin/xjc", "jaotc": "/usr/local/bin/jaotc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/forceatlas2-python.
shpc-registry automated BioContainers addition for forceatlas2-python
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/forceatlas2-python
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/forceatlas2-python:1.1--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/forceatlas2-python/1.1--py_1
$ module help quay.io/biocontainers/forceatlas2-python/1.1--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### forceatlas2-python-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### forceatlas2-python-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### forceatlas2-python-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### forceatlas2-python-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### forceatlas2-python-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### forceatlas2-python-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### appletviewer

```bash
$ singularity exec <container> /usr/local/bin/appletviewer
$ podman run --it --rm --entrypoint /usr/local/bin/appletviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/appletviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idlj

```bash
$ singularity exec <container> /usr/local/bin/idlj
$ podman run --it --rm --entrypoint /usr/local/bin/idlj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idlj   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orbd

```bash
$ singularity exec <container> /usr/local/bin/orbd
$ podman run --it --rm --entrypoint /usr/local/bin/orbd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orbd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### schemagen

```bash
$ singularity exec <container> /usr/local/bin/schemagen
$ podman run --it --rm --entrypoint /usr/local/bin/schemagen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/schemagen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### servertool

```bash
$ singularity exec <container> /usr/local/bin/servertool
$ podman run --it --rm --entrypoint /usr/local/bin/servertool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/servertool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tnameserv

```bash
$ singularity exec <container> /usr/local/bin/tnameserv
$ podman run --it --rm --entrypoint /usr/local/bin/tnameserv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tnameserv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wsgen

```bash
$ singularity exec <container> /usr/local/bin/wsgen
$ podman run --it --rm --entrypoint /usr/local/bin/wsgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wsgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wsimport

```bash
$ singularity exec <container> /usr/local/bin/wsimport
$ podman run --it --rm --entrypoint /usr/local/bin/wsimport   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wsimport   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xjc

```bash
$ singularity exec <container> /usr/local/bin/xjc
$ podman run --it --rm --entrypoint /usr/local/bin/xjc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xjc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jaotc

```bash
$ singularity exec <container> /usr/local/bin/jaotc
$ podman run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
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
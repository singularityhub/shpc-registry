---
layout: container
name:  "quay.io/biocontainers/demultiplexer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/demultiplexer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/demultiplexer/container.yaml"
updated_at: "2023-05-26 02:39:55.190675"
latest: "1.1.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/demultiplexer"
aliases:
 - "demultiplexer"
 - "psghelp"
 - "psgissue"
 - "psgmain"
 - "psgsettings"
 - "psgupgrade"
 - "psgver"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
 - "python3.1"
versions:
 - "1.1.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for demultiplexer"
config: {"url": "https://biocontainers.pro/tools/demultiplexer", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for demultiplexer", "latest": {"1.1.0--pyhdfd78af_0": "sha256:7c351b5bcd0d34db4ddd07b322d816d7a8f1cd898d690da7f0c37cb14e036797"}, "tags": {"1.1.0--pyhdfd78af_0": "sha256:7c351b5bcd0d34db4ddd07b322d816d7a8f1cd898d690da7f0c37cb14e036797"}, "docker": "quay.io/biocontainers/demultiplexer", "aliases": {"demultiplexer": "/usr/local/bin/demultiplexer", "psghelp": "/usr/local/bin/psghelp", "psgissue": "/usr/local/bin/psgissue", "psgmain": "/usr/local/bin/psgmain", "psgsettings": "/usr/local/bin/psgsettings", "psgupgrade": "/usr/local/bin/psgupgrade", "psgver": "/usr/local/bin/psgver", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/demultiplexer.
singularity registry hpc automated addition for demultiplexer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/demultiplexer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/demultiplexer:1.1.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/demultiplexer/1.1.0--pyhdfd78af_0
$ module help quay.io/biocontainers/demultiplexer/1.1.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### demultiplexer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### demultiplexer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### demultiplexer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### demultiplexer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### demultiplexer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### demultiplexer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### demultiplexer

```bash
$ singularity exec <container> /usr/local/bin/demultiplexer
$ podman run --it --rm --entrypoint /usr/local/bin/demultiplexer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/demultiplexer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psghelp

```bash
$ singularity exec <container> /usr/local/bin/psghelp
$ podman run --it --rm --entrypoint /usr/local/bin/psghelp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psghelp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psgissue

```bash
$ singularity exec <container> /usr/local/bin/psgissue
$ podman run --it --rm --entrypoint /usr/local/bin/psgissue   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psgissue   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psgmain

```bash
$ singularity exec <container> /usr/local/bin/psgmain
$ podman run --it --rm --entrypoint /usr/local/bin/psgmain   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psgmain   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psgsettings

```bash
$ singularity exec <container> /usr/local/bin/psgsettings
$ podman run --it --rm --entrypoint /usr/local/bin/psgsettings   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psgsettings   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psgupgrade

```bash
$ singularity exec <container> /usr/local/bin/psgupgrade
$ podman run --it --rm --entrypoint /usr/local/bin/psgupgrade   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psgupgrade   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psgver

```bash
$ singularity exec <container> /usr/local/bin/psgver
$ podman run --it --rm --entrypoint /usr/local/bin/psgver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psgver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
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
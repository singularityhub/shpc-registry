---
layout: container
name:  "quay.io/biocontainers/phu"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/phu/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/phu/container.yaml"
updated_at: "2025-10-03 03:22:33.301904"
latest: "0.2.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/phu"
aliases:
 - "dmypy"
 - "mypy"
 - "mypyc"
 - "phu"
 - "ruff"
 - "stubgen"
 - "stubtest"
 - "vclust"
 - "typer"
 - "seqkit"
 - "markdown-it"
 - "py.test"
 - "pytest"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "pygmentize"
versions:
 - "0.2.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for phu"
config: {"url": "https://biocontainers.pro/tools/phu", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for phu", "latest": {"0.2.1--pyhdfd78af_0": "sha256:f8e0139d507e2b5968b093b3b2d5ed93095bd84f294eb19c43f95929e21c0aa1"}, "tags": {"0.2.1--pyhdfd78af_0": "sha256:f8e0139d507e2b5968b093b3b2d5ed93095bd84f294eb19c43f95929e21c0aa1"}, "docker": "quay.io/biocontainers/phu", "aliases": {"dmypy": "/usr/local/bin/dmypy", "mypy": "/usr/local/bin/mypy", "mypyc": "/usr/local/bin/mypyc", "phu": "/usr/local/bin/phu", "ruff": "/usr/local/bin/ruff", "stubgen": "/usr/local/bin/stubgen", "stubtest": "/usr/local/bin/stubtest", "vclust": "/usr/local/bin/vclust", "typer": "/usr/local/bin/typer", "seqkit": "/usr/local/bin/seqkit", "markdown-it": "/usr/local/bin/markdown-it", "py.test": "/usr/local/bin/py.test", "pytest": "/usr/local/bin/pytest", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "pygmentize": "/usr/local/bin/pygmentize"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/phu.
singularity registry hpc automated addition for phu
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/phu
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/phu:0.2.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/phu/0.2.1--pyhdfd78af_0
$ module help quay.io/biocontainers/phu/0.2.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### phu-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### phu-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### phu-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### phu-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### phu-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### phu-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dmypy

```bash
$ singularity exec <container> /usr/local/bin/dmypy
$ podman run --it --rm --entrypoint /usr/local/bin/dmypy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dmypy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mypy

```bash
$ singularity exec <container> /usr/local/bin/mypy
$ podman run --it --rm --entrypoint /usr/local/bin/mypy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mypy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mypyc

```bash
$ singularity exec <container> /usr/local/bin/mypyc
$ podman run --it --rm --entrypoint /usr/local/bin/mypyc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mypyc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phu

```bash
$ singularity exec <container> /usr/local/bin/phu
$ podman run --it --rm --entrypoint /usr/local/bin/phu   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phu   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ruff

```bash
$ singularity exec <container> /usr/local/bin/ruff
$ podman run --it --rm --entrypoint /usr/local/bin/ruff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ruff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stubgen

```bash
$ singularity exec <container> /usr/local/bin/stubgen
$ podman run --it --rm --entrypoint /usr/local/bin/stubgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stubgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stubtest

```bash
$ singularity exec <container> /usr/local/bin/stubtest
$ podman run --it --rm --entrypoint /usr/local/bin/stubtest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stubtest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vclust

```bash
$ singularity exec <container> /usr/local/bin/vclust
$ podman run --it --rm --entrypoint /usr/local/bin/vclust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vclust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### typer

```bash
$ singularity exec <container> /usr/local/bin/typer
$ podman run --it --rm --entrypoint /usr/local/bin/typer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/typer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqkit

```bash
$ singularity exec <container> /usr/local/bin/seqkit
$ podman run --it --rm --entrypoint /usr/local/bin/seqkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqkit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### markdown-it

```bash
$ singularity exec <container> /usr/local/bin/markdown-it
$ podman run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### py.test

```bash
$ singularity exec <container> /usr/local/bin/py.test
$ podman run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pytest

```bash
$ singularity exec <container> /usr/local/bin/pytest
$ podman run --it --rm --entrypoint /usr/local/bin/pytest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pytest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.13

```bash
$ singularity exec <container> /usr/local/bin/idle3.13
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.13

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.13
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13

```bash
$ singularity exec <container> /usr/local/bin/python3.13
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13-config

```bash
$ singularity exec <container> /usr/local/bin/python3.13-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pygmentize

```bash
$ singularity exec <container> /usr/local/bin/pygmentize
$ podman run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
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
---
layout: container
name:  "quay.io/biocontainers/centrifuger"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/centrifuger/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/centrifuger/container.yaml"
updated_at: "2024-07-16 03:14:48.849372"
latest: "1.0.4--hdcf5f25_1"
container_url: "https://biocontainers.pro/tools/centrifuger"
aliases:
 - "centrifuger"
 - "centrifuger-build"
 - "centrifuger-download"
 - "centrifuger-inspect"
 - "centrifuger-kreport"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
 - "tar"
 - "idn2"
 - "wget"
versions:
 - "1.0.0--hdcf5f25_0"
 - "1.0.1--hdcf5f25_0"
 - "1.0.2--hdcf5f25_0"
 - "1.0.3--hdcf5f25_0"
 - "1.0.4--hdcf5f25_1"
description: "singularity registry hpc automated addition for centrifuger"
config: {"url": "https://biocontainers.pro/tools/centrifuger", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for centrifuger", "latest": {"1.0.4--hdcf5f25_1": "sha256:b45b0202c39df2e01dafe5a31cdf2e07c3f24fa2b68936e985c1efab195e2e1d"}, "tags": {"1.0.0--hdcf5f25_0": "sha256:127aff480ab97feb9b884907e158a8ebe6bb720e56aa1964ff45d4024166aeaf", "1.0.1--hdcf5f25_0": "sha256:2df1788e95f6b6283ee918a296fdf8c369241327be6a66c4243f9ca11065f9ec", "1.0.2--hdcf5f25_0": "sha256:95f9534ea3c58d3f6dbecde73f5799d43784bbea5888e2738d22ce05d86d76bd", "1.0.3--hdcf5f25_0": "sha256:bb03bfb39a1da0e985d7f2f5bdb7f48c988c0e03ab3bbe394a10bff2e6c70fad", "1.0.4--hdcf5f25_1": "sha256:b45b0202c39df2e01dafe5a31cdf2e07c3f24fa2b68936e985c1efab195e2e1d"}, "docker": "quay.io/biocontainers/centrifuger", "aliases": {"centrifuger": "/usr/local/bin/centrifuger", "centrifuger-build": "/usr/local/bin/centrifuger-build", "centrifuger-download": "/usr/local/bin/centrifuger-download", "centrifuger-inspect": "/usr/local/bin/centrifuger-inspect", "centrifuger-kreport": "/usr/local/bin/centrifuger-kreport", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config", "tar": "/usr/local/bin/tar", "idn2": "/usr/local/bin/idn2", "wget": "/usr/local/bin/wget"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/centrifuger.
singularity registry hpc automated addition for centrifuger
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/centrifuger
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/centrifuger:1.0.4--hdcf5f25_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/centrifuger/1.0.4--hdcf5f25_1
$ module help quay.io/biocontainers/centrifuger/1.0.4--hdcf5f25_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### centrifuger-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### centrifuger-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### centrifuger-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### centrifuger-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### centrifuger-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### centrifuger-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### centrifuger

```bash
$ singularity exec <container> /usr/local/bin/centrifuger
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuger   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuger   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuger-build

```bash
$ singularity exec <container> /usr/local/bin/centrifuger-build
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuger-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuger-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuger-download

```bash
$ singularity exec <container> /usr/local/bin/centrifuger-download
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuger-download   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuger-download   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuger-inspect

```bash
$ singularity exec <container> /usr/local/bin/centrifuger-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuger-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuger-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuger-kreport

```bash
$ singularity exec <container> /usr/local/bin/centrifuger-kreport
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuger-kreport   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuger-kreport   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.12

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.12
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.12

```bash
$ singularity exec <container> /usr/local/bin/idle3.12
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.12

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.12
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12

```bash
$ singularity exec <container> /usr/local/bin/python3.12
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12-config

```bash
$ singularity exec <container> /usr/local/bin/python3.12-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tar

```bash
$ singularity exec <container> /usr/local/bin/tar
$ podman run --it --rm --entrypoint /usr/local/bin/tar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idn2

```bash
$ singularity exec <container> /usr/local/bin/idn2
$ podman run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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
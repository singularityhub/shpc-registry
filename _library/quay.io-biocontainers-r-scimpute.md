---
layout: container
name:  "quay.io/biocontainers/r-scimpute"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-scimpute/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-scimpute/container.yaml"
updated_at: "2025-01-09 13:25:43.870366"
latest: "0.0.8--r43hdfd78af_5"
container_url: "https://biocontainers.pro/tools/r-scimpute"
aliases:
 - "parsort"
 - "env_parallel"
 - "env_parallel.ash"
 - "env_parallel.bash"
 - "env_parallel.csh"
 - "env_parallel.dash"
 - "env_parallel.fish"
 - "env_parallel.ksh"
 - "env_parallel.mksh"
 - "env_parallel.pdksh"
versions:
 - "0.0.8--r41hdfd78af_3"
 - "0.0.8--r42hdfd78af_4"
 - "0.0.8--r43hdfd78af_5"
description: "shpc-registry automated BioContainers addition for r-scimpute"
config: {"url": "https://biocontainers.pro/tools/r-scimpute", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-scimpute", "latest": {"0.0.8--r43hdfd78af_5": "sha256:c85972882b56f5302d498a751c51fbb4d3e7a51ae1f82796d787503cc6f61fa3"}, "tags": {"0.0.8--r41hdfd78af_3": "sha256:37e4dce33aeec428dbffd1f8528c37e4329f49de7075c549f828847025b06569", "0.0.8--r42hdfd78af_4": "sha256:cf4ded2db2bcae2794ec951aa260fc38ae1d56b216e8d6f496ebd6d29f4048d0", "0.0.8--r43hdfd78af_5": "sha256:c85972882b56f5302d498a751c51fbb4d3e7a51ae1f82796d787503cc6f61fa3"}, "docker": "quay.io/biocontainers/r-scimpute", "aliases": {"parsort": "/usr/local/bin/parsort", "env_parallel": "/usr/local/bin/env_parallel", "env_parallel.ash": "/usr/local/bin/env_parallel.ash", "env_parallel.bash": "/usr/local/bin/env_parallel.bash", "env_parallel.csh": "/usr/local/bin/env_parallel.csh", "env_parallel.dash": "/usr/local/bin/env_parallel.dash", "env_parallel.fish": "/usr/local/bin/env_parallel.fish", "env_parallel.ksh": "/usr/local/bin/env_parallel.ksh", "env_parallel.mksh": "/usr/local/bin/env_parallel.mksh", "env_parallel.pdksh": "/usr/local/bin/env_parallel.pdksh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-scimpute.
shpc-registry automated BioContainers addition for r-scimpute
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-scimpute
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-scimpute:0.0.8--r43hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-scimpute/0.0.8--r43hdfd78af_5
$ module help quay.io/biocontainers/r-scimpute/0.0.8--r43hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-scimpute-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-scimpute-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-scimpute-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-scimpute-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-scimpute-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-scimpute-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### parsort

```bash
$ singularity exec <container> /usr/local/bin/parsort
$ podman run --it --rm --entrypoint /usr/local/bin/parsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel

```bash
$ singularity exec <container> /usr/local/bin/env_parallel
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.ash

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.ash
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.ash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.ash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.bash

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.bash
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.csh

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.csh
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.csh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.csh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.dash

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.dash
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.dash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.dash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.fish

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.fish
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.fish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.fish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.ksh

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.ksh
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.ksh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.ksh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.mksh

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.mksh
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.mksh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.mksh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.pdksh

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.pdksh
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.pdksh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.pdksh   -v ${PWD} -w ${PWD} <container> -c " $@"
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
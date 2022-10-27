---
layout: container
name:  "quay.io/biocontainers/moff"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/moff/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/moff/container.yaml"
updated_at: "2022-10-27 01:13:51.976975"
latest: "2.0.3--hdfd78af_5"
container_url: "https://biocontainers.pro/tools/moff"
aliases:
 - "aprofutil"
 - "moff_all.py"
 - "mono-hang-watchdog"
versions:
 - "2.0.3--hdfd78af_5"
description: "shpc-registry automated BioContainers addition for moff"
config: {"url": "https://biocontainers.pro/tools/moff", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for moff", "latest": {"2.0.3--hdfd78af_5": "sha256:39d5c82e3f32c6fb9519b012301787f30382e2701b1ae9c900dad01f2c96fee6"}, "tags": {"2.0.3--hdfd78af_5": "sha256:39d5c82e3f32c6fb9519b012301787f30382e2701b1ae9c900dad01f2c96fee6"}, "docker": "quay.io/biocontainers/moff", "aliases": {"aprofutil": "/usr/local/bin/aprofutil", "moff_all.py": "/usr/local/bin/moff_all.py", "mono-hang-watchdog": "/usr/local/bin/mono-hang-watchdog"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/moff.
shpc-registry automated BioContainers addition for moff
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/moff
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/moff:2.0.3--hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/moff/2.0.3--hdfd78af_5
$ module help quay.io/biocontainers/moff/2.0.3--hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### moff-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### moff-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### moff-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### moff-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### moff-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### moff-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### aprofutil

```bash
$ singularity exec <container> /usr/local/bin/aprofutil
$ podman run --it --rm --entrypoint /usr/local/bin/aprofutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aprofutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### moff_all.py

```bash
$ singularity exec <container> /usr/local/bin/moff_all.py
$ podman run --it --rm --entrypoint /usr/local/bin/moff_all.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/moff_all.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mono-hang-watchdog

```bash
$ singularity exec <container> /usr/local/bin/mono-hang-watchdog
$ podman run --it --rm --entrypoint /usr/local/bin/mono-hang-watchdog   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mono-hang-watchdog   -v ${PWD} -w ${PWD} <container> -c " $@"
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
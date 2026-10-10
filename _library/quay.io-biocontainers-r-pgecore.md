---
layout: container
name:  "quay.io/biocontainers/r-pgecore"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-pgecore/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-pgecore/container.yaml"
updated_at: "2026-10-10 19:13:17.109222"
latest: "0.1.0--r45hab16a5f_0"
container_url: "https://biocontainers.pro/tools/r-pgecore"
aliases:
 - "fc-genconf"
 - "x86_64-conda-linux-gnu.cfg"
versions:
 - "0.1.0--r45hab16a5f_0"
description: "singularity registry hpc automated addition for r-pgecore"
config: {"url": "https://biocontainers.pro/tools/r-pgecore", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for r-pgecore", "latest": {"0.1.0--r45hab16a5f_0": "sha256:30c1842bd29909d8d192515ff906579798cae0ccb907867c20bdf5f72b825129"}, "tags": {"0.1.0--r45hab16a5f_0": "sha256:30c1842bd29909d8d192515ff906579798cae0ccb907867c20bdf5f72b825129"}, "docker": "quay.io/biocontainers/r-pgecore", "aliases": {"fc-genconf": "/usr/local/bin/fc-genconf", "x86_64-conda-linux-gnu.cfg": "/usr/local/bin/x86_64-conda-linux-gnu.cfg"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-pgecore.
singularity registry hpc automated addition for r-pgecore
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-pgecore
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-pgecore:0.1.0--r45hab16a5f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-pgecore/0.1.0--r45hab16a5f_0
$ module help quay.io/biocontainers/r-pgecore/0.1.0--r45hab16a5f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-pgecore-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-pgecore-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-pgecore-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-pgecore-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-pgecore-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-pgecore-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fc-genconf

```bash
$ singularity exec <container> /usr/local/bin/fc-genconf
$ podman run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu.cfg

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu.cfg
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
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
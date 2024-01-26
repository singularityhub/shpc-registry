---
layout: container
name:  "quay.io/biocontainers/r-grbase"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-grbase/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-grbase/container.yaml"
updated_at: "2024-01-26 02:47:56.374402"
latest: "2.0.1--r43hba8c641_0"
container_url: "https://biocontainers.pro/tools/r-grbase"

versions:
 - "1.8_6.7--r41h930fe3c_2"
 - "1.8.9--r42h25def4e_1"
 - "1.8.9--r42hba8c641_2"
 - "1.8.9--r43hba8c641_3"
 - "1.9.0--r43hba8c641_0"
 - "2.0.0--r43hba8c641_0"
 - "2.0.1--r43hba8c641_0"
description: "shpc-registry automated BioContainers addition for r-grbase"
config: {"url": "https://biocontainers.pro/tools/r-grbase", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-grbase", "latest": {"2.0.1--r43hba8c641_0": "sha256:2d6ece859cc5eb18586d32dc4703be237f9e02080d21dbd6308ab52f763da1ae"}, "tags": {"1.8_6.7--r41h930fe3c_2": "sha256:51bc8563430fac095fc0474d55215cb4fd74746f06eb80d9dae7685caf799531", "1.8.9--r42h25def4e_1": "sha256:763efd94c13300ce9eadff8c4dbe5ca6822fbf6c8c8518ee0eedc2263f62e3e5", "1.8.9--r42hba8c641_2": "sha256:68ae829df7a1982b3a92c04cf89c164a6ff369ec7a067c924d031e7493aebfc6", "1.8.9--r43hba8c641_3": "sha256:c1cd3e90904ab25d350c7be2c0841c902d748e39805305a3f166cfd4e0a5b6b2", "1.9.0--r43hba8c641_0": "sha256:8689ad3741677d1811029dc380ce834bc8ef4a751679e7ef3452ab43ceac9dc5", "2.0.0--r43hba8c641_0": "sha256:511a3edb1c5a0a915d6abadce1744a32280d7dedcf145618f3995d533c15da7e", "2.0.1--r43hba8c641_0": "sha256:2d6ece859cc5eb18586d32dc4703be237f9e02080d21dbd6308ab52f763da1ae"}, "docker": "quay.io/biocontainers/r-grbase"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-grbase.
shpc-registry automated BioContainers addition for r-grbase
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-grbase
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-grbase:2.0.1--r43hba8c641_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-grbase/2.0.1--r43hba8c641_0
$ module help quay.io/biocontainers/r-grbase/2.0.1--r43hba8c641_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-grbase-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-grbase-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-grbase-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-grbase-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-grbase-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-grbase-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-grbase

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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
---
layout: container
name:  "quay.io/biocontainers/myloasm-kmc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/myloasm-kmc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/myloasm-kmc/container.yaml"
updated_at: "2026-10-10 19:31:02.904684"
latest: "0.1.0--hdcadc20_0"
container_url: "https://biocontainers.pro/tools/myloasm-kmc"
aliases:
 - "myloasm-kmc-v1"
versions:
 - "0.1.0--hdcadc20_0"
description: "singularity registry hpc automated addition for myloasm-kmc"
config: {"url": "https://biocontainers.pro/tools/myloasm-kmc", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for myloasm-kmc", "latest": {"0.1.0--hdcadc20_0": "sha256:58427d88dac05f5b26f9d1deb3a2d44c301d359d80d727def58d5ef76ca40985"}, "tags": {"0.1.0--hdcadc20_0": "sha256:58427d88dac05f5b26f9d1deb3a2d44c301d359d80d727def58d5ef76ca40985"}, "docker": "quay.io/biocontainers/myloasm-kmc", "aliases": {"myloasm-kmc-v1": "/usr/local/bin/myloasm-kmc-v1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/myloasm-kmc.
singularity registry hpc automated addition for myloasm-kmc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/myloasm-kmc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/myloasm-kmc:0.1.0--hdcadc20_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/myloasm-kmc/0.1.0--hdcadc20_0
$ module help quay.io/biocontainers/myloasm-kmc/0.1.0--hdcadc20_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### myloasm-kmc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### myloasm-kmc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### myloasm-kmc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### myloasm-kmc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### myloasm-kmc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### myloasm-kmc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### myloasm-kmc-v1

```bash
$ singularity exec <container> /usr/local/bin/myloasm-kmc-v1
$ podman run --it --rm --entrypoint /usr/local/bin/myloasm-kmc-v1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/myloasm-kmc-v1   -v ${PWD} -w ${PWD} <container> -c " $@"
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
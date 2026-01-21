---
layout: container
name:  "quay.io/biocontainers/kamino"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kamino/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kamino/container.yaml"
updated_at: "2026-01-21 04:11:16.612088"
latest: "0.2.1--h4349ce8_0"
container_url: "https://biocontainers.pro/tools/kamino"
aliases:
 - "kamino"
versions:
 - "0.1.0--h4349ce8_0"
 - "0.2.1--h4349ce8_0"
description: "singularity registry hpc automated addition for kamino"
config: {"url": "https://biocontainers.pro/tools/kamino", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for kamino", "latest": {"0.2.1--h4349ce8_0": "sha256:5ab413d58487d018a805b4273320a341ac2f43503fe03055b7f036fe066fe704"}, "tags": {"0.1.0--h4349ce8_0": "sha256:025c7be0e57601396ba7b63358aacf41d86801db099e46a854e6824090fae136", "0.2.1--h4349ce8_0": "sha256:5ab413d58487d018a805b4273320a341ac2f43503fe03055b7f036fe066fe704"}, "docker": "quay.io/biocontainers/kamino", "aliases": {"kamino": "/usr/local/bin/kamino"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kamino.
singularity registry hpc automated addition for kamino
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kamino
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kamino:0.2.1--h4349ce8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kamino/0.2.1--h4349ce8_0
$ module help quay.io/biocontainers/kamino/0.2.1--h4349ce8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kamino-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kamino-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kamino-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kamino-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kamino-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kamino-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### kamino

```bash
$ singularity exec <container> /usr/local/bin/kamino
$ podman run --it --rm --entrypoint /usr/local/bin/kamino   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kamino   -v ${PWD} -w ${PWD} <container> -c " $@"
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
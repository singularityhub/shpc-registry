---
layout: container
name:  "quay.io/biocontainers/primalbedtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/primalbedtools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/primalbedtools/container.yaml"
updated_at: "2025-12-03 03:50:11.890385"
latest: "1.0.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/primalbedtools"
aliases:
 - "primalbedtools"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
versions:
 - "0.6.2--pyhdfd78af_0"
 - "0.8.1--pyhdfd78af_0"
 - "0.9--pyhdfd78af_0"
 - "0.10.1--pyhdfd78af_0"
 - "1.0.0--pyhdfd78af_0"
 - "0.11.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for primalbedtools"
config: {"url": "https://biocontainers.pro/tools/primalbedtools", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for primalbedtools", "latest": {"1.0.0--pyhdfd78af_0": "sha256:196c095a742c8ce37657d40083379a3be8a1dabd2fdc145c941ffe2858954dee"}, "tags": {"0.6.2--pyhdfd78af_0": "sha256:47428c46e378db2f66cd4f229df511abdbb8cb2fb5c7309fee42db3bf616a730", "0.8.1--pyhdfd78af_0": "sha256:053852e0433587543c5044c10804e5bbfbba1dfd2c9709837571561b5ce8bc22", "0.9--pyhdfd78af_0": "sha256:d94d7ba278f2783f9b4f3d14de5199235c39ab92b8a310394b2448b87390a13c", "0.10.1--pyhdfd78af_0": "sha256:d919228e7e4f21b7726ee2e78625b454f2b11ef2f89bdc0d9bba4c4486eafd86", "1.0.0--pyhdfd78af_0": "sha256:196c095a742c8ce37657d40083379a3be8a1dabd2fdc145c941ffe2858954dee", "0.11.1--pyhdfd78af_0": "sha256:6765bfc28d2777f10322b55f982e0cbdaf2117f36c55246de6add01fcae46295"}, "docker": "quay.io/biocontainers/primalbedtools", "aliases": {"primalbedtools": "/usr/local/bin/primalbedtools", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/primalbedtools.
singularity registry hpc automated addition for primalbedtools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/primalbedtools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/primalbedtools:1.0.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/primalbedtools/1.0.0--pyhdfd78af_0
$ module help quay.io/biocontainers/primalbedtools/1.0.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### primalbedtools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### primalbedtools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### primalbedtools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### primalbedtools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### primalbedtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### primalbedtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### primalbedtools

```bash
$ singularity exec <container> /usr/local/bin/primalbedtools
$ podman run --it --rm --entrypoint /usr/local/bin/primalbedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/primalbedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
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
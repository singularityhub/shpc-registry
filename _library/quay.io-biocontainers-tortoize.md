---
layout: container
name:  "quay.io/biocontainers/tortoize"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tortoize/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tortoize/container.yaml"
updated_at: "2025-12-15 04:41:21.841734"
latest: "2.0.15--haf24da9_1"
container_url: "https://biocontainers.pro/tools/tortoize"
aliases:
 - "mkdssp"
 - "tortoize"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "numpy-config"
versions:
 - "2.0.15--haf24da9_0"
 - "2.0.15--haf24da9_1"
description: "singularity registry hpc automated addition for tortoize"
config: {"url": "https://biocontainers.pro/tools/tortoize", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for tortoize", "latest": {"2.0.15--haf24da9_1": "sha256:cf56b3410bbbbe3199cd11345b86e86b610a3631933887a7e167a57a3c5fe94c"}, "tags": {"2.0.15--haf24da9_0": "sha256:db076092de8cd90efaf881ea506e97dd2ca2b4b3aaf15651a236fab649088ca6", "2.0.15--haf24da9_1": "sha256:cf56b3410bbbbe3199cd11345b86e86b610a3631933887a7e167a57a3c5fe94c"}, "docker": "quay.io/biocontainers/tortoize", "aliases": {"mkdssp": "/usr/local/bin/mkdssp", "tortoize": "/usr/local/bin/tortoize", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "numpy-config": "/usr/local/bin/numpy-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tortoize.
singularity registry hpc automated addition for tortoize
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tortoize
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tortoize:2.0.15--haf24da9_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tortoize/2.0.15--haf24da9_1
$ module help quay.io/biocontainers/tortoize/2.0.15--haf24da9_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tortoize-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tortoize-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tortoize-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tortoize-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tortoize-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tortoize-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mkdssp

```bash
$ singularity exec <container> /usr/local/bin/mkdssp
$ podman run --it --rm --entrypoint /usr/local/bin/mkdssp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mkdssp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tortoize

```bash
$ singularity exec <container> /usr/local/bin/tortoize
$ podman run --it --rm --entrypoint /usr/local/bin/tortoize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tortoize   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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
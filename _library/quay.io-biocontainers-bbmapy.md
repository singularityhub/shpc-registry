---
layout: container
name:  "quay.io/biocontainers/bbmapy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bbmapy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bbmapy/container.yaml"
updated_at: "2026-01-19 05:37:04.581479"
latest: "0.0.51--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/bbmapy"
aliases:
 - "bbmapy-ensure-java"
 - "bbmapy-test"
 - "generate-bbmapy-commands"
 - "markdown-it"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "pygmentize"
versions:
 - "0.0.46--pyhdfd78af_0"
 - "0.0.51--pyhdfd78af_0"
description: "singularity registry hpc automated addition for bbmapy"
config: {"url": "https://biocontainers.pro/tools/bbmapy", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bbmapy", "latest": {"0.0.51--pyhdfd78af_0": "sha256:313cde3f69353d143624871c6a9de2aa81778128fdb3c043185fecd600de87a9"}, "tags": {"0.0.46--pyhdfd78af_0": "sha256:24b7a8948a600fd44dcaaf5c6e77be65786b32108d6d8b36094a3821fe0f4183", "0.0.51--pyhdfd78af_0": "sha256:313cde3f69353d143624871c6a9de2aa81778128fdb3c043185fecd600de87a9"}, "docker": "quay.io/biocontainers/bbmapy", "aliases": {"bbmapy-ensure-java": "/usr/local/bin/bbmapy-ensure-java", "bbmapy-test": "/usr/local/bin/bbmapy-test", "generate-bbmapy-commands": "/usr/local/bin/generate-bbmapy-commands", "markdown-it": "/usr/local/bin/markdown-it", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "pygmentize": "/usr/local/bin/pygmentize"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bbmapy.
singularity registry hpc automated addition for bbmapy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bbmapy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bbmapy:0.0.51--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bbmapy/0.0.51--pyhdfd78af_0
$ module help quay.io/biocontainers/bbmapy/0.0.51--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bbmapy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bbmapy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bbmapy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bbmapy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bbmapy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bbmapy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bbmapy-ensure-java

```bash
$ singularity exec <container> /usr/local/bin/bbmapy-ensure-java
$ podman run --it --rm --entrypoint /usr/local/bin/bbmapy-ensure-java   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bbmapy-ensure-java   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bbmapy-test

```bash
$ singularity exec <container> /usr/local/bin/bbmapy-test
$ podman run --it --rm --entrypoint /usr/local/bin/bbmapy-test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bbmapy-test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate-bbmapy-commands

```bash
$ singularity exec <container> /usr/local/bin/generate-bbmapy-commands
$ podman run --it --rm --entrypoint /usr/local/bin/generate-bbmapy-commands   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate-bbmapy-commands   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### markdown-it

```bash
$ singularity exec <container> /usr/local/bin/markdown-it
$ podman run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
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
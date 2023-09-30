---
layout: container
name:  "quay.io/biocontainers/lua"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lua/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/lua/container.yaml"
updated_at: "2023-09-30 02:53:00.811169"
latest: "5.3.4"
container_url: "https://biocontainers.pro/tools/lua"
aliases:
 - "lua"
 - "luac"
versions:
 - "5.3.4"
description: "shpc-registry automated BioContainers addition for lua"
config: {"url": "https://biocontainers.pro/tools/lua", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for lua", "latest": {"5.3.4": "sha256:f567742f48e7da8324dfa60535516347ced782edfac5312f385e9e619a553fc0"}, "tags": {"5.3.4": "sha256:f567742f48e7da8324dfa60535516347ced782edfac5312f385e9e619a553fc0"}, "docker": "quay.io/biocontainers/lua", "aliases": {"lua": "/usr/local/bin/lua", "luac": "/usr/local/bin/luac"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/lua.
shpc-registry automated BioContainers addition for lua
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lua
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lua:5.3.4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lua/5.3.4
$ module help quay.io/biocontainers/lua/5.3.4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lua-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lua-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lua-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lua-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lua-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lua-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### lua

```bash
$ singularity exec <container> /usr/local/bin/lua
$ podman run --it --rm --entrypoint /usr/local/bin/lua   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lua   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### luac

```bash
$ singularity exec <container> /usr/local/bin/luac
$ podman run --it --rm --entrypoint /usr/local/bin/luac   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/luac   -v ${PWD} -w ${PWD} <container> -c " $@"
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
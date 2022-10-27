---
layout: container
name:  "quay.io/biocontainers/pasty"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pasty/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/pasty/container.yaml"
updated_at: "2022-10-27 01:02:17.265548"
latest: "1.0.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/pasty"
aliases:
 - "executor"
 - "pasty"
 - "rich-click"
versions:
 - "1.0.0--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for pasty"
config: {"url": "https://biocontainers.pro/tools/pasty", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pasty", "latest": {"1.0.0--hdfd78af_0": "sha256:8bfb41cd6285c342bc63462a7395af3f8426cf919dd13fa76e27bdddfd876926"}, "tags": {"1.0.0--hdfd78af_0": "sha256:8bfb41cd6285c342bc63462a7395af3f8426cf919dd13fa76e27bdddfd876926"}, "docker": "quay.io/biocontainers/pasty", "aliases": {"executor": "/usr/local/bin/executor", "pasty": "/usr/local/bin/pasty", "rich-click": "/usr/local/bin/rich-click"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pasty.
shpc-registry automated BioContainers addition for pasty
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pasty
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pasty:1.0.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pasty/1.0.0--hdfd78af_0
$ module help quay.io/biocontainers/pasty/1.0.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pasty-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pasty-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pasty-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pasty-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pasty-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pasty-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### executor

```bash
$ singularity exec <container> /usr/local/bin/executor
$ podman run --it --rm --entrypoint /usr/local/bin/executor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/executor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pasty

```bash
$ singularity exec <container> /usr/local/bin/pasty
$ podman run --it --rm --entrypoint /usr/local/bin/pasty   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pasty   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rich-click

```bash
$ singularity exec <container> /usr/local/bin/rich-click
$ podman run --it --rm --entrypoint /usr/local/bin/rich-click   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rich-click   -v ${PWD} -w ${PWD} <container> -c " $@"
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
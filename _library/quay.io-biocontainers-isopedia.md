---
layout: container
name:  "quay.io/biocontainers/isopedia"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/isopedia/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/isopedia/container.yaml"
updated_at: "2026-03-15 05:24:24.462362"
latest: "1.6.5--hf679fb9_0"
container_url: "https://biocontainers.pro/tools/isopedia"
aliases:
 - "isopedia"
 - "isopedia-splice-viz.py"
 - "isopedia-tools"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
versions:
 - "1.6.5--hf679fb9_0"
description: "singularity registry hpc automated addition for isopedia"
config: {"url": "https://biocontainers.pro/tools/isopedia", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for isopedia", "latest": {"1.6.5--hf679fb9_0": "sha256:a92e7a29dfe3b13fcde16181d123ec6b03199d528875be8bcdb053e3ff151077"}, "tags": {"1.6.5--hf679fb9_0": "sha256:a92e7a29dfe3b13fcde16181d123ec6b03199d528875be8bcdb053e3ff151077"}, "docker": "quay.io/biocontainers/isopedia", "aliases": {"isopedia": "/usr/local/bin/isopedia", "isopedia-splice-viz.py": "/usr/local/bin/isopedia-splice-viz.py", "isopedia-tools": "/usr/local/bin/isopedia-tools", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/isopedia.
singularity registry hpc automated addition for isopedia
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/isopedia
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/isopedia:1.6.5--hf679fb9_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/isopedia/1.6.5--hf679fb9_0
$ module help quay.io/biocontainers/isopedia/1.6.5--hf679fb9_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### isopedia-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### isopedia-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### isopedia-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### isopedia-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### isopedia-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### isopedia-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### isopedia

```bash
$ singularity exec <container> /usr/local/bin/isopedia
$ podman run --it --rm --entrypoint /usr/local/bin/isopedia   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isopedia   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isopedia-splice-viz.py

```bash
$ singularity exec <container> /usr/local/bin/isopedia-splice-viz.py
$ podman run --it --rm --entrypoint /usr/local/bin/isopedia-splice-viz.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isopedia-splice-viz.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isopedia-tools

```bash
$ singularity exec <container> /usr/local/bin/isopedia-tools
$ podman run --it --rm --entrypoint /usr/local/bin/isopedia-tools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isopedia-tools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.14

```bash
$ singularity exec <container> /usr/local/bin/idle3.14
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.14

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.14
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14

```bash
$ singularity exec <container> /usr/local/bin/python3.14
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14-config

```bash
$ singularity exec <container> /usr/local/bin/python3.14-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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
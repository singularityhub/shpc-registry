---
layout: container
name:  "quay.io/biocontainers/jupyterngsplugin"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/jupyterngsplugin/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/jupyterngsplugin/container.yaml"
updated_at: "2022-10-27 00:35:46.641027"
latest: "0.0.13a3--py_0"
container_url: "https://biocontainers.pro/tools/jupyterngsplugin"
aliases:
 - "x86_64-conda_cos6-linux-gnu-pkg-config"
versions:
 - "0.0.13a3--py_0"
description: "shpc-registry automated BioContainers addition for jupyterngsplugin"
config: {"url": "https://biocontainers.pro/tools/jupyterngsplugin", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for jupyterngsplugin", "latest": {"0.0.13a3--py_0": "sha256:a8fb3b77776d865b245d231c91c69e59f5a833c0a8bb874adc6e9504666ef51f"}, "tags": {"0.0.13a3--py_0": "sha256:a8fb3b77776d865b245d231c91c69e59f5a833c0a8bb874adc6e9504666ef51f"}, "docker": "quay.io/biocontainers/jupyterngsplugin", "aliases": {"x86_64-conda_cos6-linux-gnu-pkg-config": "/usr/local/bin/x86_64-conda_cos6-linux-gnu-pkg-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/jupyterngsplugin.
shpc-registry automated BioContainers addition for jupyterngsplugin
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/jupyterngsplugin
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/jupyterngsplugin:0.0.13a3--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/jupyterngsplugin/0.0.13a3--py_0
$ module help quay.io/biocontainers/jupyterngsplugin/0.0.13a3--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### jupyterngsplugin-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### jupyterngsplugin-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### jupyterngsplugin-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### jupyterngsplugin-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### jupyterngsplugin-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### jupyterngsplugin-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda_cos6-linux-gnu-pkg-config

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda_cos6-linux-gnu-pkg-config
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda_cos6-linux-gnu-pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda_cos6-linux-gnu-pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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
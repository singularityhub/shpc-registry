---
layout: container
name:  "quay.io/biocontainers/snakemake-interface-scheduler-plugins"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/snakemake-interface-scheduler-plugins/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/snakemake-interface-scheduler-plugins/container.yaml"
updated_at: "2025-10-01 03:26:16.235408"
latest: "2.0.1--pyhd4c3c12_0"
container_url: "https://biocontainers.pro/tools/snakemake-interface-scheduler-plugins"
aliases:
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
versions:
 - "2.0.0--pyhdfd78af_0"
 - "2.0.1--pyhd4c3c12_0"
description: "singularity registry hpc automated addition for snakemake-interface-scheduler-plugins"
config: {"url": "https://biocontainers.pro/tools/snakemake-interface-scheduler-plugins", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for snakemake-interface-scheduler-plugins", "latest": {"2.0.1--pyhd4c3c12_0": "sha256:78b0e30ac38469bacb3d4b8ed5d7c97ddb8bbefe5fa11239eb19a35cca4e8b0b"}, "tags": {"2.0.0--pyhdfd78af_0": "sha256:09b445f19336039f188084d2d390ae11815ef4f7e77388e1fdf41f281cfe24e9", "2.0.1--pyhd4c3c12_0": "sha256:78b0e30ac38469bacb3d4b8ed5d7c97ddb8bbefe5fa11239eb19a35cca4e8b0b"}, "docker": "quay.io/biocontainers/snakemake-interface-scheduler-plugins", "aliases": {"idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/snakemake-interface-scheduler-plugins.
singularity registry hpc automated addition for snakemake-interface-scheduler-plugins
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/snakemake-interface-scheduler-plugins
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/snakemake-interface-scheduler-plugins:2.0.1--pyhd4c3c12_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/snakemake-interface-scheduler-plugins/2.0.1--pyhd4c3c12_0
$ module help quay.io/biocontainers/snakemake-interface-scheduler-plugins/2.0.1--pyhd4c3c12_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### snakemake-interface-scheduler-plugins-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### snakemake-interface-scheduler-plugins-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### snakemake-interface-scheduler-plugins-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### snakemake-interface-scheduler-plugins-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### snakemake-interface-scheduler-plugins-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### snakemake-interface-scheduler-plugins-inspect-deffile:

```bash
$ singularity inspect -d <container>
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
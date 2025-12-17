---
layout: container
name:  "quay.io/biocontainers/snakemake-scheduler-plugin-firstfit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/snakemake-scheduler-plugin-firstfit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/snakemake-scheduler-plugin-firstfit/container.yaml"
updated_at: "2025-12-17 16:10:18.109218"
latest: "0.1.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/snakemake-scheduler-plugin-firstfit"
aliases:
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
versions:
 - "0.1.2--pyhdfd78af_0"
description: "singularity registry hpc automated addition for snakemake-scheduler-plugin-firstfit"
config: {"url": "https://biocontainers.pro/tools/snakemake-scheduler-plugin-firstfit", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for snakemake-scheduler-plugin-firstfit", "latest": {"0.1.2--pyhdfd78af_0": "sha256:ea078d918ca405c279941721fa53e61e6b0b56beb49508c07cd19336a91fc32a"}, "tags": {"0.1.2--pyhdfd78af_0": "sha256:ea078d918ca405c279941721fa53e61e6b0b56beb49508c07cd19336a91fc32a"}, "docker": "quay.io/biocontainers/snakemake-scheduler-plugin-firstfit", "aliases": {"idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/snakemake-scheduler-plugin-firstfit.
singularity registry hpc automated addition for snakemake-scheduler-plugin-firstfit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/snakemake-scheduler-plugin-firstfit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/snakemake-scheduler-plugin-firstfit:0.1.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/snakemake-scheduler-plugin-firstfit/0.1.2--pyhdfd78af_0
$ module help quay.io/biocontainers/snakemake-scheduler-plugin-firstfit/0.1.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### snakemake-scheduler-plugin-firstfit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### snakemake-scheduler-plugin-firstfit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### snakemake-scheduler-plugin-firstfit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### snakemake-scheduler-plugin-firstfit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### snakemake-scheduler-plugin-firstfit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### snakemake-scheduler-plugin-firstfit-inspect-deffile:

```bash
$ singularity inspect -d <container>
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
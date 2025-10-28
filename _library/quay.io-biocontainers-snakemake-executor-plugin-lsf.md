---
layout: container
name:  "quay.io/biocontainers/snakemake-executor-plugin-lsf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/snakemake-executor-plugin-lsf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/snakemake-executor-plugin-lsf/container.yaml"
updated_at: "2025-10-28 03:41:48.298021"
latest: "0.2.6--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/snakemake-executor-plugin-lsf"
aliases:
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
versions:
 - "0.2.2--pyhdfd78af_0"
 - "0.2.3--pyhdfd78af_0"
 - "0.2.4--pyhdfd78af_0"
 - "0.2.6--pyhdfd78af_0"
description: "singularity registry hpc automated addition for snakemake-executor-plugin-lsf"
config: {"url": "https://biocontainers.pro/tools/snakemake-executor-plugin-lsf", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for snakemake-executor-plugin-lsf", "latest": {"0.2.6--pyhdfd78af_0": "sha256:f5457e764d23b4aa312a350f1200207370aa6a48a92cf64c15ffcb29e50512d3"}, "tags": {"0.2.2--pyhdfd78af_0": "sha256:62c97160a1dea52fddae540cd151fc72fb4841082e30fdac2a77a54cc97571e5", "0.2.3--pyhdfd78af_0": "sha256:20feb3f699b45ff704af221cf1281bf1b3accccf5ee00adaee1e2f6f0f00523e", "0.2.4--pyhdfd78af_0": "sha256:13ba5a5d709060c7c9bdff3f646b775d7bcd2bcd95a4a42dfe6206a947ec00a9", "0.2.6--pyhdfd78af_0": "sha256:f5457e764d23b4aa312a350f1200207370aa6a48a92cf64c15ffcb29e50512d3"}, "docker": "quay.io/biocontainers/snakemake-executor-plugin-lsf", "aliases": {"2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/snakemake-executor-plugin-lsf.
singularity registry hpc automated addition for snakemake-executor-plugin-lsf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/snakemake-executor-plugin-lsf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/snakemake-executor-plugin-lsf:0.2.6--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/snakemake-executor-plugin-lsf/0.2.6--pyhdfd78af_0
$ module help quay.io/biocontainers/snakemake-executor-plugin-lsf/0.2.6--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### snakemake-executor-plugin-lsf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### snakemake-executor-plugin-lsf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### snakemake-executor-plugin-lsf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### snakemake-executor-plugin-lsf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### snakemake-executor-plugin-lsf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### snakemake-executor-plugin-lsf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.12

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.12
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.12

```bash
$ singularity exec <container> /usr/local/bin/idle3.12
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.12

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.12
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12

```bash
$ singularity exec <container> /usr/local/bin/python3.12
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12-config

```bash
$ singularity exec <container> /usr/local/bin/python3.12-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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
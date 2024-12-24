---
layout: container
name:  "quay.io/biocontainers/snakemake-storage-plugin-http"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/snakemake-storage-plugin-http/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/snakemake-storage-plugin-http/container.yaml"
updated_at: "2024-12-24 02:54:19.959478"
latest: "0.2.3--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/snakemake-storage-plugin-http"
aliases:
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
 - "normalizer"
versions:
 - "0.2.3--pyhdfd78af_1"
description: "singularity registry hpc automated addition for snakemake-storage-plugin-http"
config: {"url": "https://biocontainers.pro/tools/snakemake-storage-plugin-http", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for snakemake-storage-plugin-http", "latest": {"0.2.3--pyhdfd78af_1": "sha256:27894a2b08da24791ef84d82634d0dd713dcfa30da094bf92e54f48b6bbd2bb8"}, "tags": {"0.2.3--pyhdfd78af_1": "sha256:27894a2b08da24791ef84d82634d0dd713dcfa30da094bf92e54f48b6bbd2bb8"}, "docker": "quay.io/biocontainers/snakemake-storage-plugin-http", "aliases": {"2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config", "normalizer": "/usr/local/bin/normalizer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/snakemake-storage-plugin-http.
singularity registry hpc automated addition for snakemake-storage-plugin-http
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/snakemake-storage-plugin-http
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/snakemake-storage-plugin-http:0.2.3--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/snakemake-storage-plugin-http/0.2.3--pyhdfd78af_1
$ module help quay.io/biocontainers/snakemake-storage-plugin-http/0.2.3--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### snakemake-storage-plugin-http-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### snakemake-storage-plugin-http-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### snakemake-storage-plugin-http-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### snakemake-storage-plugin-http-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### snakemake-storage-plugin-http-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### snakemake-storage-plugin-http-inspect-deffile:

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


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
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
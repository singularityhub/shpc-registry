---
layout: container
name:  "quay.io/biocontainers/factorforge-cds"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/factorforge-cds/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/factorforge-cds/container.yaml"
updated_at: "2026-11-06 09:16:57.104067"
latest: "3.5.11--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/factorforge-cds"
aliases:
 - "factorforge"
 - "factorforge-validate"
 - "idle3.15"
 - "pydoc3.15"
 - "python3.15"
 - "python3.15-config"
 - "idna"
 - "numpy-config"
 - "normalizer"
versions:
 - "3.5.11--pyhdfd78af_0"
description: "singularity registry hpc automated addition for factorforge-cds"
config: {"url": "https://biocontainers.pro/tools/factorforge-cds", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for factorforge-cds", "latest": {"3.5.11--pyhdfd78af_0": "sha256:0a2c78277146aa42edc1bcf6c6b143d259dbdcb5b5db6e73478c50864c1e3cea"}, "tags": {"3.5.11--pyhdfd78af_0": "sha256:0a2c78277146aa42edc1bcf6c6b143d259dbdcb5b5db6e73478c50864c1e3cea"}, "docker": "quay.io/biocontainers/factorforge-cds", "aliases": {"factorforge": "/usr/local/bin/factorforge", "factorforge-validate": "/usr/local/bin/factorforge-validate", "idle3.15": "/usr/local/bin/idle3.15", "pydoc3.15": "/usr/local/bin/pydoc3.15", "python3.15": "/usr/local/bin/python3.15", "python3.15-config": "/usr/local/bin/python3.15-config", "idna": "/usr/local/bin/idna", "numpy-config": "/usr/local/bin/numpy-config", "normalizer": "/usr/local/bin/normalizer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/factorforge-cds.
singularity registry hpc automated addition for factorforge-cds
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/factorforge-cds
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/factorforge-cds:3.5.11--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/factorforge-cds/3.5.11--pyhdfd78af_0
$ module help quay.io/biocontainers/factorforge-cds/3.5.11--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### factorforge-cds-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### factorforge-cds-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### factorforge-cds-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### factorforge-cds-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### factorforge-cds-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### factorforge-cds-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### factorforge

```bash
$ singularity exec <container> /usr/local/bin/factorforge
$ podman run --it --rm --entrypoint /usr/local/bin/factorforge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/factorforge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### factorforge-validate

```bash
$ singularity exec <container> /usr/local/bin/factorforge-validate
$ podman run --it --rm --entrypoint /usr/local/bin/factorforge-validate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/factorforge-validate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.15

```bash
$ singularity exec <container> /usr/local/bin/idle3.15
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.15

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.15
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.15

```bash
$ singularity exec <container> /usr/local/bin/python3.15
$ podman run --it --rm --entrypoint /usr/local/bin/python3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.15-config

```bash
$ singularity exec <container> /usr/local/bin/python3.15-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.15-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.15-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idna

```bash
$ singularity exec <container> /usr/local/bin/idna
$ podman run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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
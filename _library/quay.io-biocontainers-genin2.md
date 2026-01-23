---
layout: container
name:  "quay.io/biocontainers/genin2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/genin2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/genin2/container.yaml"
updated_at: "2026-01-23 03:56:16.795473"
latest: "2.1.5--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/genin2"
aliases:
 - "genin2"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "numpy-config"
 - "normalizer"
versions:
 - "2.1.2--pyhdfd78af_0"
 - "2.1.3--pyhdfd78af_0"
 - "2.1.5--pyhdfd78af_0"
description: "singularity registry hpc automated addition for genin2"
config: {"url": "https://biocontainers.pro/tools/genin2", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for genin2", "latest": {"2.1.5--pyhdfd78af_0": "sha256:abda48eaff17ef82ba16f07d3732644c6f178baf794ae6afbc0ae2e24f5a20f8"}, "tags": {"2.1.2--pyhdfd78af_0": "sha256:6e7a89b10fda980cd8e73c411b3210101205fb02e304dd18cbca2d7466ac95fb", "2.1.3--pyhdfd78af_0": "sha256:3c1323da02de46feb9591548bd71f819bc4929754ec17eebde3a95b2477e6e3f", "2.1.5--pyhdfd78af_0": "sha256:abda48eaff17ef82ba16f07d3732644c6f178baf794ae6afbc0ae2e24f5a20f8"}, "docker": "quay.io/biocontainers/genin2", "aliases": {"genin2": "/usr/local/bin/genin2", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "numpy-config": "/usr/local/bin/numpy-config", "normalizer": "/usr/local/bin/normalizer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/genin2.
singularity registry hpc automated addition for genin2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/genin2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/genin2:2.1.5--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/genin2/2.1.5--pyhdfd78af_0
$ module help quay.io/biocontainers/genin2/2.1.5--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### genin2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### genin2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### genin2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### genin2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### genin2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### genin2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### genin2

```bash
$ singularity exec <container> /usr/local/bin/genin2
$ podman run --it --rm --entrypoint /usr/local/bin/genin2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genin2   -v ${PWD} -w ${PWD} <container> -c " $@"
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
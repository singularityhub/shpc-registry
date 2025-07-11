---
layout: container
name:  "quay.io/biocontainers/alignlib-lite"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/alignlib-lite/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/alignlib-lite/container.yaml"
updated_at: "2025-07-11 04:27:44.017321"
latest: "0.3--py312h9c9b0c2_9"
container_url: "https://biocontainers.pro/tools/alignlib-lite"
aliases:
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "0.3--py39he1fd14c_5"
 - "0.3--py310h99d9a7c_6"
 - "0.3--py38h529b8a6_6"
 - "0.3--py39h0dd7abe_8"
 - "0.3--py312h9c9b0c2_9"
description: "shpc-registry automated BioContainers addition for alignlib-lite"
config: {"url": "https://biocontainers.pro/tools/alignlib-lite", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for alignlib-lite", "latest": {"0.3--py312h9c9b0c2_9": "sha256:1dcf9c33260f7c93876ce019a4419c72489d74ec8d6c23a73e3bca0eb7130d28"}, "tags": {"0.3--py39he1fd14c_5": "sha256:9060e90edfb1e18d4b4febdb1c24b19ce5b4083c7f4f0fd3371a92c46bd56a0b", "0.3--py310h99d9a7c_6": "sha256:80358d722d5bcc0a9ae854444632f95d26df7bf3db36eb6b5354f01500fac39d", "0.3--py38h529b8a6_6": "sha256:e287f550305d259bc97245321bf157047909093c3dc86ab9274254d87ff6be24", "0.3--py39h0dd7abe_8": "sha256:39a1e3ebb407950e9b0035364be558fe7cee783458e281e8582f570c4d2ad290", "0.3--py312h9c9b0c2_9": "sha256:1dcf9c33260f7c93876ce019a4419c72489d74ec8d6c23a73e3bca0eb7130d28"}, "docker": "quay.io/biocontainers/alignlib-lite", "aliases": {"2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/alignlib-lite.
shpc-registry automated BioContainers addition for alignlib-lite
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/alignlib-lite
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/alignlib-lite:0.3--py312h9c9b0c2_9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/alignlib-lite/0.3--py312h9c9b0c2_9
$ module help quay.io/biocontainers/alignlib-lite/0.3--py312h9c9b0c2_9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### alignlib-lite-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### alignlib-lite-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### alignlib-lite-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### alignlib-lite-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### alignlib-lite-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### alignlib-lite-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9

```bash
$ singularity exec <container> /usr/local/bin/python3.9
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9-config

```bash
$ singularity exec <container> /usr/local/bin/python3.9-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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
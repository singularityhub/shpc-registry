---
layout: container
name:  "quay.io/biocontainers/enzywizard-mut-clean"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/enzywizard-mut-clean/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/enzywizard-mut-clean/container.yaml"
updated_at: "2026-06-23 16:34:52.713471"
latest: "1.0.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/enzywizard-mut-clean"
aliases:
 - "enzywizard-mut-clean"
 - "pdbfixer"
 - "rdhc"
 - "cllayerinfo"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
 - "numpy-config"
versions:
 - "1.0.2--pyhdfd78af_0"
description: "singularity registry hpc automated addition for enzywizard-mut-clean"
config: {"url": "https://biocontainers.pro/tools/enzywizard-mut-clean", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for enzywizard-mut-clean", "latest": {"1.0.2--pyhdfd78af_0": "sha256:abd3506d1f21cd6dac9073b4955d0cedf0d9eb93cad7e0d83d00d8d11ced1232"}, "tags": {"1.0.2--pyhdfd78af_0": "sha256:abd3506d1f21cd6dac9073b4955d0cedf0d9eb93cad7e0d83d00d8d11ced1232"}, "docker": "quay.io/biocontainers/enzywizard-mut-clean", "aliases": {"enzywizard-mut-clean": "/usr/local/bin/enzywizard-mut-clean", "pdbfixer": "/usr/local/bin/pdbfixer", "rdhc": "/usr/local/bin/rdhc", "cllayerinfo": "/usr/local/bin/cllayerinfo", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config", "numpy-config": "/usr/local/bin/numpy-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/enzywizard-mut-clean.
singularity registry hpc automated addition for enzywizard-mut-clean
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/enzywizard-mut-clean
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/enzywizard-mut-clean:1.0.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/enzywizard-mut-clean/1.0.2--pyhdfd78af_0
$ module help quay.io/biocontainers/enzywizard-mut-clean/1.0.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### enzywizard-mut-clean-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### enzywizard-mut-clean-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### enzywizard-mut-clean-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### enzywizard-mut-clean-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### enzywizard-mut-clean-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### enzywizard-mut-clean-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### enzywizard-mut-clean

```bash
$ singularity exec <container> /usr/local/bin/enzywizard-mut-clean
$ podman run --it --rm --entrypoint /usr/local/bin/enzywizard-mut-clean   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/enzywizard-mut-clean   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdbfixer

```bash
$ singularity exec <container> /usr/local/bin/pdbfixer
$ podman run --it --rm --entrypoint /usr/local/bin/pdbfixer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdbfixer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rdhc

```bash
$ singularity exec <container> /usr/local/bin/rdhc
$ podman run --it --rm --entrypoint /usr/local/bin/rdhc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rdhc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cllayerinfo

```bash
$ singularity exec <container> /usr/local/bin/cllayerinfo
$ podman run --it --rm --entrypoint /usr/local/bin/cllayerinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cllayerinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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
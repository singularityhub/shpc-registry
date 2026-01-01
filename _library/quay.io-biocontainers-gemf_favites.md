---
layout: container
name:  "quay.io/biocontainers/gemf_favites"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gemf_favites/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gemf_favites/container.yaml"
updated_at: "2026-01-01 04:16:13.652353"
latest: "1.0.3--h7b50bb2_1"
container_url: "https://biocontainers.pro/tools/gemf_favites"
aliases:
 - "GEMF"
 - "GEMF_FAVITES.py"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
versions:
 - "1.0.3--h031d066_0"
 - "1.0.3--h7b50bb2_1"
description: "singularity registry hpc automated addition for gemf_favites"
config: {"url": "https://biocontainers.pro/tools/gemf_favites", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for gemf_favites", "latest": {"1.0.3--h7b50bb2_1": "sha256:c2d2781378dc425632b92565a0a5e2dce944d446108de3f2b7017ec96b9cff2b"}, "tags": {"1.0.3--h031d066_0": "sha256:9da81451fad523e4d00c9bb30f61949aab542626490397e98c5b5bd34eea0e1c", "1.0.3--h7b50bb2_1": "sha256:c2d2781378dc425632b92565a0a5e2dce944d446108de3f2b7017ec96b9cff2b"}, "docker": "quay.io/biocontainers/gemf_favites", "aliases": {"GEMF": "/usr/local/bin/GEMF", "GEMF_FAVITES.py": "/usr/local/bin/GEMF_FAVITES.py", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gemf_favites.
singularity registry hpc automated addition for gemf_favites
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gemf_favites
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gemf_favites:1.0.3--h7b50bb2_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gemf_favites/1.0.3--h7b50bb2_1
$ module help quay.io/biocontainers/gemf_favites/1.0.3--h7b50bb2_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gemf_favites-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gemf_favites-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gemf_favites-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gemf_favites-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gemf_favites-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gemf_favites-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GEMF

```bash
$ singularity exec <container> /usr/local/bin/GEMF
$ podman run --it --rm --entrypoint /usr/local/bin/GEMF   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GEMF   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GEMF_FAVITES.py

```bash
$ singularity exec <container> /usr/local/bin/GEMF_FAVITES.py
$ podman run --it --rm --entrypoint /usr/local/bin/GEMF_FAVITES.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GEMF_FAVITES.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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
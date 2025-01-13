---
layout: container
name:  "quay.io/biocontainers/skyline2isocor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/skyline2isocor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/skyline2isocor/container.yaml"
updated_at: "2025-01-13 03:30:43.928218"
latest: "1.0.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/skyline2isocor"
aliases:
 - "skyline2isocor"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
versions:
 - "0.1.2--pyhdfd78af_0"
 - "0.2.0--pyhdfd78af_0"
 - "0.3.0--pyhdfd78af_0"
 - "1.0.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for skyline2isocor"
config: {"url": "https://biocontainers.pro/tools/skyline2isocor", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for skyline2isocor", "latest": {"1.0.0--pyhdfd78af_0": "sha256:f44becb50d88989c85fba61ffdfe8b5847f4b4a159ffbd6a3e57dd375d7f6e95"}, "tags": {"0.1.2--pyhdfd78af_0": "sha256:a5be5e9e02d9c30921e811a3b27e1e58fd24d7f35228a7f8ca48607e8c032b11", "0.2.0--pyhdfd78af_0": "sha256:1291248f4c2e9be73b4d02ddde18cdbedc1d7b42d9f1c2fd1237fa26afa818f9", "0.3.0--pyhdfd78af_0": "sha256:e1e77eb970d8cecca7f73b55ea43cb747a64b2752df52868961567731fd3edd7", "1.0.0--pyhdfd78af_0": "sha256:f44becb50d88989c85fba61ffdfe8b5847f4b4a159ffbd6a3e57dd375d7f6e95"}, "docker": "quay.io/biocontainers/skyline2isocor", "aliases": {"skyline2isocor": "/usr/local/bin/skyline2isocor", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/skyline2isocor.
singularity registry hpc automated addition for skyline2isocor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/skyline2isocor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/skyline2isocor:1.0.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/skyline2isocor/1.0.0--pyhdfd78af_0
$ module help quay.io/biocontainers/skyline2isocor/1.0.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### skyline2isocor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### skyline2isocor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### skyline2isocor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### skyline2isocor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### skyline2isocor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### skyline2isocor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### skyline2isocor

```bash
$ singularity exec <container> /usr/local/bin/skyline2isocor
$ podman run --it --rm --entrypoint /usr/local/bin/skyline2isocor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/skyline2isocor   -v ${PWD} -w ${PWD} <container> -c " $@"
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
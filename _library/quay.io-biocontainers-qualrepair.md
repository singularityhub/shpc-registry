---
layout: container
name:  "quay.io/biocontainers/qualrepair"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/qualrepair/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/qualrepair/container.yaml"
updated_at: "2025-12-17 16:20:46.612329"
latest: "1.0.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/qualrepair"
aliases:
 - "qualrepair"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
versions:
 - "1.0.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for qualrepair"
config: {"url": "https://biocontainers.pro/tools/qualrepair", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for qualrepair", "latest": {"1.0.0--pyhdfd78af_0": "sha256:c260a3821a2ea14f1703ce7cee55a0bbe56550656e2be6188f9352ff5fa072e2"}, "tags": {"1.0.0--pyhdfd78af_0": "sha256:c260a3821a2ea14f1703ce7cee55a0bbe56550656e2be6188f9352ff5fa072e2"}, "docker": "quay.io/biocontainers/qualrepair", "aliases": {"qualrepair": "/usr/local/bin/qualrepair", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/qualrepair.
singularity registry hpc automated addition for qualrepair
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/qualrepair
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/qualrepair:1.0.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/qualrepair/1.0.0--pyhdfd78af_0
$ module help quay.io/biocontainers/qualrepair/1.0.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### qualrepair-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### qualrepair-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### qualrepair-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### qualrepair-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### qualrepair-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### qualrepair-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### qualrepair

```bash
$ singularity exec <container> /usr/local/bin/qualrepair
$ podman run --it --rm --entrypoint /usr/local/bin/qualrepair   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qualrepair   -v ${PWD} -w ${PWD} <container> -c " $@"
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
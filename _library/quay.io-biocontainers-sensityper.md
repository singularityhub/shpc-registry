---
layout: container
name:  "quay.io/biocontainers/sensityper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sensityper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sensityper/container.yaml"
updated_at: "2026-10-28 08:23:24.053263"
latest: "1.0.4--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/sensityper"
aliases:
 - "idle3.15"
 - "pydoc3.15"
 - "python3.15"
 - "python3.15-config"
 - "sensityper"
 - "sensityping-metrics"
 - "plotly_get_chrome"
 - "numpy-config"
versions:
 - "1.0.4--pyhdfd78af_0"
description: "singularity registry hpc automated addition for sensityper"
config: {"url": "https://biocontainers.pro/tools/sensityper", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for sensityper", "latest": {"1.0.4--pyhdfd78af_0": "sha256:71fac72193e03bcd82dd0e719c114daa5bfc0e0e14ca808a389e02022e696a9b"}, "tags": {"1.0.4--pyhdfd78af_0": "sha256:71fac72193e03bcd82dd0e719c114daa5bfc0e0e14ca808a389e02022e696a9b"}, "docker": "quay.io/biocontainers/sensityper", "aliases": {"idle3.15": "/usr/local/bin/idle3.15", "pydoc3.15": "/usr/local/bin/pydoc3.15", "python3.15": "/usr/local/bin/python3.15", "python3.15-config": "/usr/local/bin/python3.15-config", "sensityper": "/usr/local/bin/sensityper", "sensityping-metrics": "/usr/local/bin/sensityping-metrics", "plotly_get_chrome": "/usr/local/bin/plotly_get_chrome", "numpy-config": "/usr/local/bin/numpy-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sensityper.
singularity registry hpc automated addition for sensityper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sensityper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sensityper:1.0.4--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sensityper/1.0.4--pyhdfd78af_0
$ module help quay.io/biocontainers/sensityper/1.0.4--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sensityper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sensityper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sensityper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sensityper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sensityper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sensityper-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### sensityper

```bash
$ singularity exec <container> /usr/local/bin/sensityper
$ podman run --it --rm --entrypoint /usr/local/bin/sensityper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sensityper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sensityping-metrics

```bash
$ singularity exec <container> /usr/local/bin/sensityping-metrics
$ podman run --it --rm --entrypoint /usr/local/bin/sensityping-metrics   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sensityping-metrics   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotly_get_chrome

```bash
$ singularity exec <container> /usr/local/bin/plotly_get_chrome
$ podman run --it --rm --entrypoint /usr/local/bin/plotly_get_chrome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotly_get_chrome   -v ${PWD} -w ${PWD} <container> -c " $@"
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
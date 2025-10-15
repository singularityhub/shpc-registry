---
layout: container
name:  "quay.io/biocontainers/influx-si-data-manager"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/influx-si-data-manager/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/influx-si-data-manager/container.yaml"
updated_at: "2025-10-15 03:51:05.832229"
latest: "1.1.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/influx-si-data-manager"
aliases:
 - "influx_si_data_manager"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
versions:
 - "0.1.4--pyhdfd78af_0"
 - "1.0.0--pyhdfd78af_0"
 - "1.0.2--pyhdfd78af_0"
 - "1.0.3--pyhdfd78af_0"
 - "1.1.0--pyhdfd78af_0"
 - "1.1.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for influx-si-data-manager"
config: {"url": "https://biocontainers.pro/tools/influx-si-data-manager", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for influx-si-data-manager", "latest": {"1.1.1--pyhdfd78af_0": "sha256:9b141e9a50e716ee11bd4bdfff6a9e73346ee51c30d802309a714446ae0dac4f"}, "tags": {"0.1.4--pyhdfd78af_0": "sha256:9095dd141c29b87b08fb004d600c50d3c480d126a6815adf4cb67bf419cc51b3", "1.0.0--pyhdfd78af_0": "sha256:9fc7dff24f6a41a7be93eb882abcb3ef7e41dcff19a9f5f34fd939ce493e133c", "1.0.2--pyhdfd78af_0": "sha256:a298fbddb5f328f986ef2ce801db60867518a9ad3d761b8144ef6a1e8e71ff15", "1.0.3--pyhdfd78af_0": "sha256:98df8b7e7e0a29823beedc41d3242c30a99da178a215731eafdc2e9e88dcfe35", "1.1.0--pyhdfd78af_0": "sha256:559a505eafc6510e676abe8e3c4fe33233d290e1fd75e44aece2f507db4a5b2a", "1.1.1--pyhdfd78af_0": "sha256:9b141e9a50e716ee11bd4bdfff6a9e73346ee51c30d802309a714446ae0dac4f"}, "docker": "quay.io/biocontainers/influx-si-data-manager", "aliases": {"influx_si_data_manager": "/usr/local/bin/influx_si_data_manager", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/influx-si-data-manager.
singularity registry hpc automated addition for influx-si-data-manager
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/influx-si-data-manager
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/influx-si-data-manager:1.1.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/influx-si-data-manager/1.1.1--pyhdfd78af_0
$ module help quay.io/biocontainers/influx-si-data-manager/1.1.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### influx-si-data-manager-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### influx-si-data-manager-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### influx-si-data-manager-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### influx-si-data-manager-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### influx-si-data-manager-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### influx-si-data-manager-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### influx_si_data_manager

```bash
$ singularity exec <container> /usr/local/bin/influx_si_data_manager
$ podman run --it --rm --entrypoint /usr/local/bin/influx_si_data_manager   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/influx_si_data_manager   -v ${PWD} -w ${PWD} <container> -c " $@"
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
---
layout: container
name:  "quay.io/biocontainers/telomerehunter2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/telomerehunter2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/telomerehunter2/container.yaml"
updated_at: "2026-09-01 07:37:09.462011"
latest: "1.0.11--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/telomerehunter2"
aliases:
 - "choreo_diagnose"
 - "choreo_get_chrome"
 - "kaleido_get_chrome"
 - "kaleido_mocker"
 - "telomerehunter2"
 - "telomerehunter2-sc"
 - "plotly_get_chrome"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "numpy-config"
versions:
 - "1.0.11--pyhdfd78af_0"
description: "singularity registry hpc automated addition for telomerehunter2"
config: {"url": "https://biocontainers.pro/tools/telomerehunter2", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for telomerehunter2", "latest": {"1.0.11--pyhdfd78af_0": "sha256:78dfc0b7ad07779637e84854ffbafb0c38ec621dc7c6a9684d1aee9e99fe1595"}, "tags": {"1.0.11--pyhdfd78af_0": "sha256:78dfc0b7ad07779637e84854ffbafb0c38ec621dc7c6a9684d1aee9e99fe1595"}, "docker": "quay.io/biocontainers/telomerehunter2", "aliases": {"choreo_diagnose": "/usr/local/bin/choreo_diagnose", "choreo_get_chrome": "/usr/local/bin/choreo_get_chrome", "kaleido_get_chrome": "/usr/local/bin/kaleido_get_chrome", "kaleido_mocker": "/usr/local/bin/kaleido_mocker", "telomerehunter2": "/usr/local/bin/telomerehunter2", "telomerehunter2-sc": "/usr/local/bin/telomerehunter2-sc", "plotly_get_chrome": "/usr/local/bin/plotly_get_chrome", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "numpy-config": "/usr/local/bin/numpy-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/telomerehunter2.
singularity registry hpc automated addition for telomerehunter2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/telomerehunter2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/telomerehunter2:1.0.11--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/telomerehunter2/1.0.11--pyhdfd78af_0
$ module help quay.io/biocontainers/telomerehunter2/1.0.11--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### telomerehunter2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### telomerehunter2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### telomerehunter2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### telomerehunter2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### telomerehunter2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### telomerehunter2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### choreo_diagnose

```bash
$ singularity exec <container> /usr/local/bin/choreo_diagnose
$ podman run --it --rm --entrypoint /usr/local/bin/choreo_diagnose   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/choreo_diagnose   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### choreo_get_chrome

```bash
$ singularity exec <container> /usr/local/bin/choreo_get_chrome
$ podman run --it --rm --entrypoint /usr/local/bin/choreo_get_chrome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/choreo_get_chrome   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kaleido_get_chrome

```bash
$ singularity exec <container> /usr/local/bin/kaleido_get_chrome
$ podman run --it --rm --entrypoint /usr/local/bin/kaleido_get_chrome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kaleido_get_chrome   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kaleido_mocker

```bash
$ singularity exec <container> /usr/local/bin/kaleido_mocker
$ podman run --it --rm --entrypoint /usr/local/bin/kaleido_mocker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kaleido_mocker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### telomerehunter2

```bash
$ singularity exec <container> /usr/local/bin/telomerehunter2
$ podman run --it --rm --entrypoint /usr/local/bin/telomerehunter2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/telomerehunter2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### telomerehunter2-sc

```bash
$ singularity exec <container> /usr/local/bin/telomerehunter2-sc
$ podman run --it --rm --entrypoint /usr/local/bin/telomerehunter2-sc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/telomerehunter2-sc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotly_get_chrome

```bash
$ singularity exec <container> /usr/local/bin/plotly_get_chrome
$ podman run --it --rm --entrypoint /usr/local/bin/plotly_get_chrome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotly_get_chrome   -v ${PWD} -w ${PWD} <container> -c " $@"
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
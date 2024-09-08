---
layout: container
name:  "quay.io/biocontainers/sequana_pipetools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sequana_pipetools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sequana_pipetools/container.yaml"
updated_at: "2024-09-08 03:25:32.560742"
latest: "0.9.4--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/sequana_pipetools"
aliases:
 - "pykwalify"
 - "sequana_completion"
 - "sequana_slurm_status"
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "browse"
 - "normalizer"
 - "tqdm"
 - "python3.1"
versions:
 - "0.9.4--pyh7cba7a3_0"
description: "singularity registry hpc automated addition for sequana_pipetools"
config: {"url": "https://biocontainers.pro/tools/sequana_pipetools", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for sequana_pipetools", "latest": {"0.9.4--pyh7cba7a3_0": "sha256:9bd37c8704648a8ecfee50de9f8552d2bd2f1f038e9c9c7d4655c66ab50db4a5"}, "tags": {"0.9.4--pyh7cba7a3_0": "sha256:9bd37c8704648a8ecfee50de9f8552d2bd2f1f038e9c9c7d4655c66ab50db4a5"}, "docker": "quay.io/biocontainers/sequana_pipetools", "aliases": {"pykwalify": "/usr/local/bin/pykwalify", "sequana_completion": "/usr/local/bin/sequana_completion", "sequana_slurm_status": "/usr/local/bin/sequana_slurm_status", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "browse": "/usr/local/bin/browse", "normalizer": "/usr/local/bin/normalizer", "tqdm": "/usr/local/bin/tqdm", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sequana_pipetools.
singularity registry hpc automated addition for sequana_pipetools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sequana_pipetools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sequana_pipetools:0.9.4--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sequana_pipetools/0.9.4--pyh7cba7a3_0
$ module help quay.io/biocontainers/sequana_pipetools/0.9.4--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sequana_pipetools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sequana_pipetools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sequana_pipetools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sequana_pipetools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sequana_pipetools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sequana_pipetools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pykwalify

```bash
$ singularity exec <container> /usr/local/bin/pykwalify
$ podman run --it --rm --entrypoint /usr/local/bin/pykwalify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pykwalify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sequana_completion

```bash
$ singularity exec <container> /usr/local/bin/sequana_completion
$ podman run --it --rm --entrypoint /usr/local/bin/sequana_completion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sequana_completion   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sequana_slurm_status

```bash
$ singularity exec <container> /usr/local/bin/sequana_slurm_status
$ podman run --it --rm --entrypoint /usr/local/bin/sequana_slurm_status   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sequana_slurm_status   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.11

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.11
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.11

```bash
$ singularity exec <container> /usr/local/bin/idle3.11
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.11

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.11
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11

```bash
$ singularity exec <container> /usr/local/bin/python3.11
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11-config

```bash
$ singularity exec <container> /usr/local/bin/python3.11-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### browse

```bash
$ singularity exec <container> /usr/local/bin/browse
$ podman run --it --rm --entrypoint /usr/local/bin/browse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/browse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tqdm

```bash
$ singularity exec <container> /usr/local/bin/tqdm
$ podman run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
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
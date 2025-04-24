---
layout: container
name:  "quay.io/biocontainers/pyhmmsearch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pyhmmsearch/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pyhmmsearch/container.yaml"
updated_at: "2025-04-24 03:41:23.297956"
latest: "2024.10.20--pyh7e72e81_0"
container_url: "https://biocontainers.pro/tools/pyhmmsearch"
aliases:
 - "pyhmmsearch"
 - "reformat_pyhmmsearch"
 - "serialize_hmm_models"
 - "numpy-config"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
 - "tqdm"
versions:
 - "2024.10.20--pyh7e72e81_0"
description: "singularity registry hpc automated addition for pyhmmsearch"
config: {"url": "https://biocontainers.pro/tools/pyhmmsearch", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pyhmmsearch", "latest": {"2024.10.20--pyh7e72e81_0": "sha256:94883c85ae516ea270416d3265cc89dbb33a617016263538ae6fb55662df636a"}, "tags": {"2024.10.20--pyh7e72e81_0": "sha256:94883c85ae516ea270416d3265cc89dbb33a617016263538ae6fb55662df636a"}, "docker": "quay.io/biocontainers/pyhmmsearch", "aliases": {"pyhmmsearch": "/usr/local/bin/pyhmmsearch", "reformat_pyhmmsearch": "/usr/local/bin/reformat_pyhmmsearch", "serialize_hmm_models": "/usr/local/bin/serialize_hmm_models", "numpy-config": "/usr/local/bin/numpy-config", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config", "tqdm": "/usr/local/bin/tqdm"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pyhmmsearch.
singularity registry hpc automated addition for pyhmmsearch
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pyhmmsearch
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pyhmmsearch:2024.10.20--pyh7e72e81_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pyhmmsearch/2024.10.20--pyh7e72e81_0
$ module help quay.io/biocontainers/pyhmmsearch/2024.10.20--pyh7e72e81_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pyhmmsearch-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pyhmmsearch-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pyhmmsearch-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pyhmmsearch-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pyhmmsearch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pyhmmsearch-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pyhmmsearch

```bash
$ singularity exec <container> /usr/local/bin/pyhmmsearch
$ podman run --it --rm --entrypoint /usr/local/bin/pyhmmsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyhmmsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reformat_pyhmmsearch

```bash
$ singularity exec <container> /usr/local/bin/reformat_pyhmmsearch
$ podman run --it --rm --entrypoint /usr/local/bin/reformat_pyhmmsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reformat_pyhmmsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### serialize_hmm_models

```bash
$ singularity exec <container> /usr/local/bin/serialize_hmm_models
$ podman run --it --rm --entrypoint /usr/local/bin/serialize_hmm_models   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/serialize_hmm_models   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### tqdm

```bash
$ singularity exec <container> /usr/local/bin/tqdm
$ podman run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
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
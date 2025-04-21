---
layout: container
name:  "quay.io/biocontainers/pykofamsearch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pykofamsearch/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pykofamsearch/container.yaml"
updated_at: "2025-04-21 03:12:53.344911"
latest: "2024.10.20--pyh7e72e81_0"
container_url: "https://biocontainers.pro/tools/pykofamsearch"
aliases:
 - "pykofamsearch"
 - "reformat_enzymes"
 - "reformat_pykofamsearch"
 - "serialize_kofam_models"
 - "subset_serialized_models"
 - "numpy-config"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
 - "tqdm"
versions:
 - "2024.10.20--pyh7e72e81_0"
description: "singularity registry hpc automated addition for pykofamsearch"
config: {"url": "https://biocontainers.pro/tools/pykofamsearch", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pykofamsearch", "latest": {"2024.10.20--pyh7e72e81_0": "sha256:841ac00797ee078ad80f146cd8e243d66358ce985dcef388abb04056047247a5"}, "tags": {"2024.10.20--pyh7e72e81_0": "sha256:841ac00797ee078ad80f146cd8e243d66358ce985dcef388abb04056047247a5"}, "docker": "quay.io/biocontainers/pykofamsearch", "aliases": {"pykofamsearch": "/usr/local/bin/pykofamsearch", "reformat_enzymes": "/usr/local/bin/reformat_enzymes", "reformat_pykofamsearch": "/usr/local/bin/reformat_pykofamsearch", "serialize_kofam_models": "/usr/local/bin/serialize_kofam_models", "subset_serialized_models": "/usr/local/bin/subset_serialized_models", "numpy-config": "/usr/local/bin/numpy-config", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config", "tqdm": "/usr/local/bin/tqdm"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pykofamsearch.
singularity registry hpc automated addition for pykofamsearch
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pykofamsearch
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pykofamsearch:2024.10.20--pyh7e72e81_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pykofamsearch/2024.10.20--pyh7e72e81_0
$ module help quay.io/biocontainers/pykofamsearch/2024.10.20--pyh7e72e81_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pykofamsearch-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pykofamsearch-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pykofamsearch-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pykofamsearch-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pykofamsearch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pykofamsearch-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pykofamsearch

```bash
$ singularity exec <container> /usr/local/bin/pykofamsearch
$ podman run --it --rm --entrypoint /usr/local/bin/pykofamsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pykofamsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reformat_enzymes

```bash
$ singularity exec <container> /usr/local/bin/reformat_enzymes
$ podman run --it --rm --entrypoint /usr/local/bin/reformat_enzymes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reformat_enzymes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reformat_pykofamsearch

```bash
$ singularity exec <container> /usr/local/bin/reformat_pykofamsearch
$ podman run --it --rm --entrypoint /usr/local/bin/reformat_pykofamsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reformat_pykofamsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### serialize_kofam_models

```bash
$ singularity exec <container> /usr/local/bin/serialize_kofam_models
$ podman run --it --rm --entrypoint /usr/local/bin/serialize_kofam_models   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/serialize_kofam_models   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### subset_serialized_models

```bash
$ singularity exec <container> /usr/local/bin/subset_serialized_models
$ podman run --it --rm --entrypoint /usr/local/bin/subset_serialized_models   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/subset_serialized_models   -v ${PWD} -w ${PWD} <container> -c " $@"
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
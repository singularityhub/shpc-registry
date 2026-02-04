---
layout: container
name:  "quay.io/biocontainers/mimi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mimi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mimi/container.yaml"
updated_at: "2026-02-04 04:49:09.257530"
latest: "1.0.4--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/mimi"
aliases:
 - "mimi_cache_create"
 - "mimi_cache_dump"
 - "mimi_hmdb_extract"
 - "mimi_kegg_extract"
 - "mimi_mass_analysis"
 - "pyjson5"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "numpy-config"
 - "tqdm"
versions:
 - "1.0.1--pyhdfd78af_0"
 - "1.0.2--pyhdfd78af_0"
 - "1.0.4--pyhdfd78af_0"
description: "singularity registry hpc automated addition for mimi"
config: {"url": "https://biocontainers.pro/tools/mimi", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mimi", "latest": {"1.0.4--pyhdfd78af_0": "sha256:38446eb83d51ab212bae792d8439dae0cfaca8b8b3076ff1eecf112890f011d6"}, "tags": {"1.0.1--pyhdfd78af_0": "sha256:9a5940ef0375972dae3c12565c84362ece0fd0009a0816b7e131967bb44c1132", "1.0.2--pyhdfd78af_0": "sha256:8c19ef7db5e28f3463823dd63249bf83db991bb42346303be5f97de47ef9945b", "1.0.4--pyhdfd78af_0": "sha256:38446eb83d51ab212bae792d8439dae0cfaca8b8b3076ff1eecf112890f011d6"}, "docker": "quay.io/biocontainers/mimi", "aliases": {"mimi_cache_create": "/usr/local/bin/mimi_cache_create", "mimi_cache_dump": "/usr/local/bin/mimi_cache_dump", "mimi_hmdb_extract": "/usr/local/bin/mimi_hmdb_extract", "mimi_kegg_extract": "/usr/local/bin/mimi_kegg_extract", "mimi_mass_analysis": "/usr/local/bin/mimi_mass_analysis", "pyjson5": "/usr/local/bin/pyjson5", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "numpy-config": "/usr/local/bin/numpy-config", "tqdm": "/usr/local/bin/tqdm"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mimi.
singularity registry hpc automated addition for mimi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mimi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mimi:1.0.4--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mimi/1.0.4--pyhdfd78af_0
$ module help quay.io/biocontainers/mimi/1.0.4--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mimi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mimi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mimi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mimi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mimi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mimi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mimi_cache_create

```bash
$ singularity exec <container> /usr/local/bin/mimi_cache_create
$ podman run --it --rm --entrypoint /usr/local/bin/mimi_cache_create   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mimi_cache_create   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mimi_cache_dump

```bash
$ singularity exec <container> /usr/local/bin/mimi_cache_dump
$ podman run --it --rm --entrypoint /usr/local/bin/mimi_cache_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mimi_cache_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mimi_hmdb_extract

```bash
$ singularity exec <container> /usr/local/bin/mimi_hmdb_extract
$ podman run --it --rm --entrypoint /usr/local/bin/mimi_hmdb_extract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mimi_hmdb_extract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mimi_kegg_extract

```bash
$ singularity exec <container> /usr/local/bin/mimi_kegg_extract
$ podman run --it --rm --entrypoint /usr/local/bin/mimi_kegg_extract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mimi_kegg_extract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mimi_mass_analysis

```bash
$ singularity exec <container> /usr/local/bin/mimi_mass_analysis
$ podman run --it --rm --entrypoint /usr/local/bin/mimi_mass_analysis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mimi_mass_analysis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyjson5

```bash
$ singularity exec <container> /usr/local/bin/pyjson5
$ podman run --it --rm --entrypoint /usr/local/bin/pyjson5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyjson5   -v ${PWD} -w ${PWD} <container> -c " $@"
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
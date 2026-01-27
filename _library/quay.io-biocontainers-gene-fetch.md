---
layout: container
name:  "quay.io/biocontainers/gene-fetch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gene-fetch/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gene-fetch/container.yaml"
updated_at: "2026-01-27 04:36:41.288975"
latest: "1.0.21--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/gene-fetch"
aliases:
 - "gene-fetch"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "numpy-config"
versions:
 - "1.0.11--pyh7e72e81_0"
 - "1.0.13--pyh7e72e81_0"
 - "1.0.15--pyh7e72e81_0"
 - "1.0.17--pyhdfd78af_0"
 - "1.0.18--pyhdfd78af_0"
 - "1.0.21--pyhdfd78af_0"
description: "singularity registry hpc automated addition for gene-fetch"
config: {"url": "https://biocontainers.pro/tools/gene-fetch", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for gene-fetch", "latest": {"1.0.21--pyhdfd78af_0": "sha256:1a99ae44650757c5ba99a8b8c2d8029446f54df360bddf2205a6371b7d726f8c"}, "tags": {"1.0.11--pyh7e72e81_0": "sha256:af4403a41ff513ce177292f0845abf0371948dec425bbdde42f12227cbb8dc84", "1.0.13--pyh7e72e81_0": "sha256:68e954d1f463ca8f18b732beb11c911f980f6374add25b30013f64e3bf36c03f", "1.0.15--pyh7e72e81_0": "sha256:ded99c7bdbb9cfebb621bd8942747927caeffe100feb3e43fe32500212b06c7e", "1.0.17--pyhdfd78af_0": "sha256:f49c302ca33c9382931a4ad605814257d08f7a25cb507fb38e426fa0e16eba3c", "1.0.18--pyhdfd78af_0": "sha256:29fa2aab733bbcc7288a72b180dcadacb8199081701fc8cb43ceddd5a7dd40ad", "1.0.21--pyhdfd78af_0": "sha256:1a99ae44650757c5ba99a8b8c2d8029446f54df360bddf2205a6371b7d726f8c"}, "docker": "quay.io/biocontainers/gene-fetch", "aliases": {"gene-fetch": "/usr/local/bin/gene-fetch", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "numpy-config": "/usr/local/bin/numpy-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gene-fetch.
singularity registry hpc automated addition for gene-fetch
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gene-fetch
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gene-fetch:1.0.21--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gene-fetch/1.0.21--pyhdfd78af_0
$ module help quay.io/biocontainers/gene-fetch/1.0.21--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gene-fetch-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gene-fetch-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gene-fetch-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gene-fetch-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gene-fetch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gene-fetch-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gene-fetch

```bash
$ singularity exec <container> /usr/local/bin/gene-fetch
$ podman run --it --rm --entrypoint /usr/local/bin/gene-fetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gene-fetch   -v ${PWD} -w ${PWD} <container> -c " $@"
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
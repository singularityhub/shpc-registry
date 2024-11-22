---
layout: container
name:  "quay.io/biocontainers/versionix"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/versionix/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/versionix/container.yaml"
updated_at: "2024-11-22 03:14:12.581965"
latest: "0.99.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/versionix"
aliases:
 - "versionix"
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "python3.1"
versions:
 - "0.2.0--pyhdfd78af_0"
 - "0.2.1--pyhdfd78af_0"
 - "0.2.2--pyhdfd78af_0"
 - "0.2.3--pyhdfd78af_0"
 - "0.2.4--pyhdfd78af_0"
 - "0.99.1--pyhdfd78af_0"
 - "0.3.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for versionix"
config: {"url": "https://biocontainers.pro/tools/versionix", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for versionix", "latest": {"0.99.1--pyhdfd78af_0": "sha256:1a48155d9c54bcfcc0ceb06f6f3fcb8f0cdfdbe3e48de70dae825972c2ce0613"}, "tags": {"0.2.0--pyhdfd78af_0": "sha256:66d17854284bbe6dd78fb5aa5941017983400bdb63dc880e65950c857fb22dcb", "0.2.1--pyhdfd78af_0": "sha256:db7b8a89fd8a46f2128ca6e3cf9375ebb9d844021e9d182686fd9e3141e9cfd1", "0.2.2--pyhdfd78af_0": "sha256:4995d3bc1fe8464495e19128a2ea748df8b9f50914f1c43832bc412d6328bcad", "0.2.3--pyhdfd78af_0": "sha256:6d36702aeb6ad25737b2c3f114625c58b972b3ca0e9416df123d18a959ae3304", "0.2.4--pyhdfd78af_0": "sha256:621ca79e5580150daa71ed82a217be59f08fa77e8b655bbe367d5ba68943de0a", "0.99.1--pyhdfd78af_0": "sha256:1a48155d9c54bcfcc0ceb06f6f3fcb8f0cdfdbe3e48de70dae825972c2ce0613", "0.3.0--pyhdfd78af_0": "sha256:00a73c69552533cd28dc470cfa2621ab96242378634755b66f98a4127f9da44f"}, "docker": "quay.io/biocontainers/versionix", "aliases": {"versionix": "/usr/local/bin/versionix", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/versionix.
singularity registry hpc automated addition for versionix
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/versionix
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/versionix:0.99.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/versionix/0.99.1--pyhdfd78af_0
$ module help quay.io/biocontainers/versionix/0.99.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### versionix-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### versionix-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### versionix-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### versionix-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### versionix-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### versionix-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### versionix

```bash
$ singularity exec <container> /usr/local/bin/versionix
$ podman run --it --rm --entrypoint /usr/local/bin/versionix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/versionix   -v ${PWD} -w ${PWD} <container> -c " $@"
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
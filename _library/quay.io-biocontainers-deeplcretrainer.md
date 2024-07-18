---
layout: container
name:  "quay.io/biocontainers/deeplcretrainer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/deeplcretrainer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/deeplcretrainer/container.yaml"
updated_at: "2024-07-18 02:41:18.120358"
latest: "0.2.12--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/deeplcretrainer"
aliases:
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "python3.1"
versions:
 - "0.1.17--pyh7cba7a3_0"
 - "0.1.19--pyh7cba7a3_0"
 - "0.1.21--pyh7cba7a3_0"
 - "0.1.22--pyh7cba7a3_0"
 - "0.2.1--pyh7cba7a3_0"
 - "0.2.8--pyh7cba7a3_0"
 - "0.2.11--pyh7cba7a3_0"
 - "0.2.12--pyh7cba7a3_0"
description: "singularity registry hpc automated addition for deeplcretrainer"
config: {"url": "https://biocontainers.pro/tools/deeplcretrainer", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for deeplcretrainer", "latest": {"0.2.12--pyh7cba7a3_0": "sha256:5f40e1c5e8728f419e9736c9e98f31cd32c70e74c2ac97565fc1d7c627bd4c02"}, "tags": {"0.1.17--pyh7cba7a3_0": "sha256:207c0ff610fdc8d2ef7c8158afdf435889daf40531467b1c92225970c7c492ab", "0.1.19--pyh7cba7a3_0": "sha256:4131c801a8be3e8b058e0aab9b0be431e19f48d071dd08e7091ed7aa4fb601af", "0.1.21--pyh7cba7a3_0": "sha256:3c2e04a6c8d37e4e3f86db8c8bde8b6baf84d06bc5a935d4f15e870abc4ec141", "0.1.22--pyh7cba7a3_0": "sha256:3de86fc729527b7d9a5fc5c90fe68e99a22f40cec9656e988b8d018628983f76", "0.2.1--pyh7cba7a3_0": "sha256:6f0622dba3dab51c78556e1054890b99a15162c6c53b08c819eade6a57cf52f9", "0.2.8--pyh7cba7a3_0": "sha256:d4a754b85715f322ec5d0c2bc9b8165f406e1a99206f4f4f5187cbe2cb468c91", "0.2.11--pyh7cba7a3_0": "sha256:d2b002afa881aa21655664c7b10488547a333b88df182acbd540a0f2cf5e8462", "0.2.12--pyh7cba7a3_0": "sha256:5f40e1c5e8728f419e9736c9e98f31cd32c70e74c2ac97565fc1d7c627bd4c02"}, "docker": "quay.io/biocontainers/deeplcretrainer", "aliases": {"2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/deeplcretrainer.
singularity registry hpc automated addition for deeplcretrainer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/deeplcretrainer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/deeplcretrainer:0.2.12--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/deeplcretrainer/0.2.12--pyh7cba7a3_0
$ module help quay.io/biocontainers/deeplcretrainer/0.2.12--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### deeplcretrainer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### deeplcretrainer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### deeplcretrainer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### deeplcretrainer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### deeplcretrainer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### deeplcretrainer-inspect-deffile:

```bash
$ singularity inspect -d <container>
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
---
layout: container
name:  "quay.io/biocontainers/cstag"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cstag/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cstag/container.yaml"
updated_at: "2023-11-20 03:01:03.327474"
latest: "1.0.5--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/cstag"
aliases:
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
 - "python3.1"
versions:
 - "0.3.1--pyhdfd78af_0"
 - "1.0.5--pyhdfd78af_0"
 - "0.6.2--pyhdfd78af_0"
 - "0.5.1--pyhdfd78af_0"
 - "0.4.3--pyh7cba7a3_0"
description: "singularity registry hpc automated addition for cstag"
config: {"url": "https://biocontainers.pro/tools/cstag", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for cstag", "latest": {"1.0.5--pyhdfd78af_0": "sha256:3c0dce1d395cc740c6412f2ddf44a8214b6710c2f0240036b8a119f5cc04aa1c"}, "tags": {"0.3.1--pyhdfd78af_0": "sha256:0abb07b2d5031df525423a1f41e4154bbdd254773ab8cdfc2a810fd6b422672f", "1.0.5--pyhdfd78af_0": "sha256:3c0dce1d395cc740c6412f2ddf44a8214b6710c2f0240036b8a119f5cc04aa1c", "0.6.2--pyhdfd78af_0": "sha256:0bbc6b804e63d7e653df692bfec7417ca97f14eedae81cf2efab89d8fab61bea", "0.5.1--pyhdfd78af_0": "sha256:6b7f8cf85b00e236e99309c57fa084e26353b4937b2be0ca2865c4ad889a5625", "0.4.3--pyh7cba7a3_0": "sha256:9b2f907357d33d8348cb97557dec3b0c39ffee7d7a416a0bc59e5ad062aa134d"}, "docker": "quay.io/biocontainers/cstag", "aliases": {"2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cstag.
singularity registry hpc automated addition for cstag
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cstag
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cstag:1.0.5--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cstag/1.0.5--pyhdfd78af_0
$ module help quay.io/biocontainers/cstag/1.0.5--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cstag-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cstag-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cstag-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cstag-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cstag-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cstag-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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
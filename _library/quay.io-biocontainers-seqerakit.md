---
layout: container
name:  "quay.io/biocontainers/seqerakit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/seqerakit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/seqerakit/container.yaml"
updated_at: "2024-11-07 03:25:58.803284"
latest: "0.4.9--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/seqerakit"
aliases:
 - "seqerakit"
 - "tw"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
versions:
 - "0.4.2--pyhdfd78af_0"
 - "0.4.4--pyhdfd78af_0"
 - "0.4.5--pyhdfd78af_0"
 - "0.4.6--pyhdfd78af_0"
 - "0.4.8--pyhdfd78af_0"
 - "0.4.9--pyhdfd78af_0"
description: "singularity registry hpc automated addition for seqerakit"
config: {"url": "https://biocontainers.pro/tools/seqerakit", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for seqerakit", "latest": {"0.4.9--pyhdfd78af_0": "sha256:916bffcbd18d59d359cee28717a1b17b8ad7c086d8fcda733f64b6b8990f87a4"}, "tags": {"0.4.2--pyhdfd78af_0": "sha256:8162bcdf3e991c9dcaac249c8332943103271169b61b0ad8498aa3e0aa5f78b0", "0.4.4--pyhdfd78af_0": "sha256:7fb524504772fbe2746f29371df54ecba9cfb5187b688b705e492a50b479da5b", "0.4.5--pyhdfd78af_0": "sha256:ebccdbd2ccd6a0351c88fd7f74d0541435ae8e2950920077136a393ba791a4d8", "0.4.6--pyhdfd78af_0": "sha256:b062f0c4ae4374c6197e4c0f2e190ba3fb960843a971d7a797b779ad38d4f7ab", "0.4.8--pyhdfd78af_0": "sha256:40ee12a32fc4612cbff4a2b8c67345573ebd3b09db8d33748d4e32b7523c616e", "0.4.9--pyhdfd78af_0": "sha256:916bffcbd18d59d359cee28717a1b17b8ad7c086d8fcda733f64b6b8990f87a4"}, "docker": "quay.io/biocontainers/seqerakit", "aliases": {"seqerakit": "/usr/local/bin/seqerakit", "tw": "/usr/local/bin/tw", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/seqerakit.
singularity registry hpc automated addition for seqerakit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/seqerakit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/seqerakit:0.4.9--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/seqerakit/0.4.9--pyhdfd78af_0
$ module help quay.io/biocontainers/seqerakit/0.4.9--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### seqerakit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### seqerakit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### seqerakit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### seqerakit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### seqerakit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### seqerakit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### seqerakit

```bash
$ singularity exec <container> /usr/local/bin/seqerakit
$ podman run --it --rm --entrypoint /usr/local/bin/seqerakit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqerakit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tw

```bash
$ singularity exec <container> /usr/local/bin/tw
$ podman run --it --rm --entrypoint /usr/local/bin/tw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tw   -v ${PWD} -w ${PWD} <container> -c " $@"
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
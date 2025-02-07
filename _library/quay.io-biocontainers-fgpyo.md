---
layout: container
name:  "quay.io/biocontainers/fgpyo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fgpyo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fgpyo/container.yaml"
updated_at: "2025-02-07 03:06:30.074995"
latest: "0.8.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/fgpyo"
aliases:
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
 - "python3.1"
versions:
 - "0.0.5--pyhdfd78af_0"
 - "0.0.6--pyhdfd78af_0"
 - "0.0.7--pyhdfd78af_0"
 - "0.0.8--pyhdfd78af_0"
 - "0.1.0--pyhdfd78af_0"
 - "0.1.2--pyhdfd78af_0"
 - "0.1.3--pyhdfd78af_0"
 - "0.2.0--pyhdfd78af_0"
 - "0.3.0--pyhdfd78af_0"
 - "0.4.0--pyhdfd78af_0"
 - "0.7.1--pyhdfd78af_0"
 - "0.6.0--pyhdfd78af_0"
 - "0.5.0--pyhdfd78af_0"
 - "0.8.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for fgpyo"
config: {"url": "https://biocontainers.pro/tools/fgpyo", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for fgpyo", "latest": {"0.8.0--pyhdfd78af_0": "sha256:e05e6f254712f840afd86352912526ea0f8049114599163008c9a4ceed45338f"}, "tags": {"0.0.5--pyhdfd78af_0": "sha256:84a3d6c8bb8b341403007ed54edf11d218aabadc777a27b7eccb1741d29b05cb", "0.0.6--pyhdfd78af_0": "sha256:1e4d36c00d27f78bfea912b4e05dd808da3a4be0b8f45018884d0551eeadb4a6", "0.0.7--pyhdfd78af_0": "sha256:28b830ca50a804ffbbcec4f6044aee7aa1bd7dd463538dc662548efb9a7b5938", "0.0.8--pyhdfd78af_0": "sha256:dc6626ee0cd133440c0cbfc005258e479008c71320e6f0142c9f390fc8f488cc", "0.1.0--pyhdfd78af_0": "sha256:44a6ede8d1aab2d130e40cb605588bf2c9046297f125d05757c66d9e5a51b8da", "0.1.2--pyhdfd78af_0": "sha256:d0eac5044dafe692f381420a4caf62d2a540e806bcaa08800ec281094d4f1743", "0.1.3--pyhdfd78af_0": "sha256:75d579cdaab75ecdda1221b8eb7a0ec179700ede9ce601e4331af3110af7358d", "0.2.0--pyhdfd78af_0": "sha256:95df4844ed3b62cd2ebf1c3afe2373d91bd738dcca7a224a46eb75a9a4eedd25", "0.3.0--pyhdfd78af_0": "sha256:2d4555f752543186f49251963c09517c17550cd6cf12138eb63494c2ef5a420b", "0.4.0--pyhdfd78af_0": "sha256:e61fa349924a29597dfee46f4b9235a6ef0f75cdf55ee6b19564d88f34a99b91", "0.7.1--pyhdfd78af_0": "sha256:502a87af5e81d322e3465980539da7d08a7390cad1b17f43c8043b56a2809086", "0.6.0--pyhdfd78af_0": "sha256:1e336b72cf0b843117471c8a6a03a074e1ddc18400280c98495777139268f0da", "0.5.0--pyhdfd78af_0": "sha256:1c35e0316904fc6d62886e7ed06b44d68ab58dfdd50cf8efa955b885b3f4aaeb", "0.8.0--pyhdfd78af_0": "sha256:e05e6f254712f840afd86352912526ea0f8049114599163008c9a4ceed45338f"}, "docker": "quay.io/biocontainers/fgpyo", "aliases": {"2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fgpyo.
singularity registry hpc automated addition for fgpyo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fgpyo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fgpyo:0.8.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fgpyo/0.8.0--pyhdfd78af_0
$ module help quay.io/biocontainers/fgpyo/0.8.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fgpyo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fgpyo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fgpyo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fgpyo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fgpyo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fgpyo-inspect-deffile:

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
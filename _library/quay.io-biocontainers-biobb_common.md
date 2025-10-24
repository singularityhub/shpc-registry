---
layout: container
name:  "quay.io/biocontainers/biobb_common"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/biobb_common/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/biobb_common/container.yaml"
updated_at: "2025-10-24 03:35:38.416437"
latest: "5.1.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/biobb_common"
aliases:
 - "normalizer"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
versions:
 - "3.8.1--pyhdfd78af_0"
 - "3.9.0--pyhdfd78af_0"
 - "4.0.0--pyhdfd78af_0"
 - "4.1.0--pyhdfd78af_1"
 - "4.2.0--pyhdfd78af_0"
 - "5.0.0--pyhdfd78af_0"
 - "5.0.1--pyhdfd78af_0"
 - "5.1.0--pyhdfd78af_0"
 - "5.1.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for biobb_common"
config: {"url": "https://biocontainers.pro/tools/biobb_common", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for biobb_common", "latest": {"5.1.1--pyhdfd78af_0": "sha256:77eaf46691fd09d40602236034aab3a1192b84e1960981fb6ae1050d1da44ac4"}, "tags": {"3.8.1--pyhdfd78af_0": "sha256:85e5f6e5e5027591ec3651c77886149686dfbd7ca34b2dc397f491f3a9e9d16e", "3.9.0--pyhdfd78af_0": "sha256:a6c918c45fc0a7062dbfb5db0c6399947adffff7ae126ec2d978743d0c05c5bb", "4.0.0--pyhdfd78af_0": "sha256:8eb8e1285f21f02577144f697ce057b28d7c595fbab0644e5849f52bff1e2444", "4.1.0--pyhdfd78af_1": "sha256:047babc11bdb2b4805e9d1a4c201b15b652d21b29430c3541bbbc1d9da989895", "4.2.0--pyhdfd78af_0": "sha256:8bf6dc9a6ff561ad9d0e661ed2fa9f02344409365ed4adb180294fe997de46b9", "5.0.0--pyhdfd78af_0": "sha256:5a2d5090748d23bf64e9ded8f0ef50f93efba9fa89f52964607686a04cca0ccb", "5.0.1--pyhdfd78af_0": "sha256:cd9991145e7aef041c7747b4bf216e4b93a35b14d3ae3bc7d1b96c06f896b101", "5.1.0--pyhdfd78af_0": "sha256:8b5fb5cc79c8c8dc41d2b7aa64d036cfa2df045e8f434efd64bd9c1f97302039", "5.1.1--pyhdfd78af_0": "sha256:77eaf46691fd09d40602236034aab3a1192b84e1960981fb6ae1050d1da44ac4"}, "docker": "quay.io/biocontainers/biobb_common", "aliases": {"normalizer": "/usr/local/bin/normalizer", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/biobb_common.
shpc-registry automated BioContainers addition for biobb_common
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/biobb_common
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/biobb_common:5.1.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/biobb_common/5.1.1--pyhdfd78af_0
$ module help quay.io/biocontainers/biobb_common/5.1.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### biobb_common-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### biobb_common-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### biobb_common-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### biobb_common-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### biobb_common-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biobb_common-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
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
---
layout: container
name:  "quay.io/biocontainers/samsum"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/samsum/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/samsum/container.yaml"
updated_at: "2024-12-31 02:52:34.918806"
latest: "0.1.4--py312h8f4af18_6"
container_url: "https://biocontainers.pro/tools/samsum"
aliases:
 - "pyfastx"
 - "samsum"
 - "py.test"
 - "pytest"
 - "f2py3.6"
 - "2to3-3.6"
 - "idle3.6"
 - "pydoc3.6"
 - "python3.6"
 - "python3.6-config"
 - "python3.6m"
 - "python3.6m-config"
versions:
 - "0.1.4--py36hffcf100_2"
 - "0.1.4--py39hf662ef1_3"
 - "0.1.4--py310hc2b1e32_3"
 - "0.1.4--py39hf662ef1_4"
 - "0.1.4--py39h1ebeb1a_5"
 - "0.1.4--py312h8f4af18_6"
description: "shpc-registry automated BioContainers addition for samsum"
config: {"url": "https://biocontainers.pro/tools/samsum", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for samsum", "latest": {"0.1.4--py312h8f4af18_6": "sha256:4cddccee492f0314bb01e01ddb446755d43bf04bb6baf3f82ee5081dcd629e15"}, "tags": {"0.1.4--py36hffcf100_2": "sha256:8d94f17326d703d462d1281076b78eacdcd1883de203ebc508eabbc3551b42ec", "0.1.4--py39hf662ef1_3": "sha256:46e847336dd07a9cb31590c3c7f1b3c0bcf115ae5215e64386ccec56b145726f", "0.1.4--py310hc2b1e32_3": "sha256:7964df8891b17d24de5477261b01ed918fc357470834922f6e8351b33c08bffe", "0.1.4--py39hf662ef1_4": "sha256:c473f472ebc551d2f0826fbf1d40953ce8daff2ba1239fc1cd932b31d8a0dc1d", "0.1.4--py39h1ebeb1a_5": "sha256:c8d3beaf961a1abbd49b1efc9db32c9535ce38a90ad5cbe3648373d1edd887ca", "0.1.4--py312h8f4af18_6": "sha256:4cddccee492f0314bb01e01ddb446755d43bf04bb6baf3f82ee5081dcd629e15"}, "docker": "quay.io/biocontainers/samsum", "aliases": {"pyfastx": "/usr/local/bin/pyfastx", "samsum": "/usr/local/bin/samsum", "py.test": "/usr/local/bin/py.test", "pytest": "/usr/local/bin/pytest", "f2py3.6": "/usr/local/bin/f2py3.6", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6", "pydoc3.6": "/usr/local/bin/pydoc3.6", "python3.6": "/usr/local/bin/python3.6", "python3.6-config": "/usr/local/bin/python3.6-config", "python3.6m": "/usr/local/bin/python3.6m", "python3.6m-config": "/usr/local/bin/python3.6m-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/samsum.
shpc-registry automated BioContainers addition for samsum
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/samsum
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/samsum:0.1.4--py312h8f4af18_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/samsum/0.1.4--py312h8f4af18_6
$ module help quay.io/biocontainers/samsum/0.1.4--py312h8f4af18_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### samsum-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### samsum-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### samsum-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### samsum-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### samsum-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### samsum-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pyfastx

```bash
$ singularity exec <container> /usr/local/bin/pyfastx
$ podman run --it --rm --entrypoint /usr/local/bin/pyfastx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyfastx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### samsum

```bash
$ singularity exec <container> /usr/local/bin/samsum
$ podman run --it --rm --entrypoint /usr/local/bin/samsum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/samsum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### py.test

```bash
$ singularity exec <container> /usr/local/bin/py.test
$ podman run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pytest

```bash
$ singularity exec <container> /usr/local/bin/pytest
$ podman run --it --rm --entrypoint /usr/local/bin/pytest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pytest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.6

```bash
$ singularity exec <container> /usr/local/bin/f2py3.6
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.6

```bash
$ singularity exec <container> /usr/local/bin/idle3.6
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.6

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6

```bash
$ singularity exec <container> /usr/local/bin/python3.6
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m

```bash
$ singularity exec <container> /usr/local/bin/python3.6m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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
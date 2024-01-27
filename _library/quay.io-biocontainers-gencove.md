---
layout: container
name:  "quay.io/biocontainers/gencove"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gencove/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gencove/container.yaml"
updated_at: "2024-01-27 02:43:02.079797"
latest: "2.8.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/gencove"
aliases:
 - "gencove"
 - "jp.py"
 - "py.test"
 - "pytest"
 - "normalizer"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
 - "python3.1"
versions:
 - "2.4.5--pyhdfd78af_0"
 - "2.4.6--pyhdfd78af_0"
 - "2.5.0--pyhdfd78af_0"
 - "2.4.7--pyhdfd78af_0"
 - "2.5.2--pyhdfd78af_0"
 - "2.6.0--pyhdfd78af_0"
 - "2.7.2--pyhdfd78af_0"
 - "2.8.0--pyhdfd78af_0"
 - "2.7.3--pyhdfd78af_0"
 - "2.8.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for gencove"
config: {"url": "https://biocontainers.pro/tools/gencove", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for gencove", "latest": {"2.8.1--pyhdfd78af_0": "sha256:815d8e766e1329a745c301dfbaddb340d9eec7dff563dba70c9e609636e0842d"}, "tags": {"2.4.5--pyhdfd78af_0": "sha256:f7d346dff471cc0543fc1f90d4ab6c6af85462c762c955812973caa5e25676a3", "2.4.6--pyhdfd78af_0": "sha256:592e024e7be8bb234bc695737f160012b804c7cbc4b5b841dba2c9e2d7b6fe68", "2.5.0--pyhdfd78af_0": "sha256:79a0b324cff26cad6c701b9e3501a1079913ecb826de12676a7cc6cf8819d442", "2.4.7--pyhdfd78af_0": "sha256:a964119c48b0df040d7aba1dc4c3b29942b846bb5b4db14a1cf8d57339b68962", "2.5.2--pyhdfd78af_0": "sha256:322f8f894e53d5664827adc8869854eb5051267a34af0781d112976b5500530c", "2.6.0--pyhdfd78af_0": "sha256:27f59ae81af2d0eb492437454fe45fb503548c0225cc5df633cf40f59140be03", "2.7.2--pyhdfd78af_0": "sha256:dbd7aa7839be9c86f6fc952eaf64cb2304a8e748dec510ec4da7a4fb48b485da", "2.8.0--pyhdfd78af_0": "sha256:0a5d010b54d844c7b4b9807f4cd3ed4a643d756f17a52f286b999cc9b3fc496c", "2.7.3--pyhdfd78af_0": "sha256:e6b89e85114cc1d67af43955e12474ae83f7ac689a02f7785ea7b54511937ca2", "2.8.1--pyhdfd78af_0": "sha256:815d8e766e1329a745c301dfbaddb340d9eec7dff563dba70c9e609636e0842d"}, "docker": "quay.io/biocontainers/gencove", "aliases": {"gencove": "/usr/local/bin/gencove", "jp.py": "/usr/local/bin/jp.py", "py.test": "/usr/local/bin/py.test", "pytest": "/usr/local/bin/pytest", "normalizer": "/usr/local/bin/normalizer", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gencove.
singularity registry hpc automated addition for gencove
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gencove
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gencove:2.8.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gencove/2.8.1--pyhdfd78af_0
$ module help quay.io/biocontainers/gencove/2.8.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gencove-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gencove-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gencove-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gencove-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gencove-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gencove-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gencove

```bash
$ singularity exec <container> /usr/local/bin/gencove
$ podman run --it --rm --entrypoint /usr/local/bin/gencove   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gencove   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jp.py

```bash
$ singularity exec <container> /usr/local/bin/jp.py
$ podman run --it --rm --entrypoint /usr/local/bin/jp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
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
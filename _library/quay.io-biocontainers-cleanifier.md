---
layout: container
name:  "quay.io/biocontainers/cleanifier"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cleanifier/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cleanifier/container.yaml"
updated_at: "2026-01-24 04:26:54.977517"
latest: "1.2.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/cleanifier"
aliases:
 - "cleanifier"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "numpy-config"
 - "py.test"
 - "pytest"
 - "numba"
 - "jsonschema"
 - "activate-global-python-argcomplete"
 - "python-argcomplete-check-easy-install-script"
 - "register-python-argcomplete"
 - "normalizer"
versions:
 - "0.1.3--pyhdfd78af_0"
 - "1.0.0--pyhdfd78af_0"
 - "0.2.1--pyhdfd78af_0"
 - "1.1.0--pyhdfd78af_0"
 - "1.0.1--pyhdfd78af_0"
 - "1.1.2--pyhdfd78af_0"
 - "1.1.3--pyhdfd78af_0"
 - "1.1.4--pyhdfd78af_0"
 - "1.2.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for cleanifier"
config: {"url": "https://biocontainers.pro/tools/cleanifier", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for cleanifier", "latest": {"1.2.0--pyhdfd78af_0": "sha256:4b7f1e10b760736fe483c7093b9793fc16b04b742eaeec8ababa0f84bc47ad5d"}, "tags": {"0.1.3--pyhdfd78af_0": "sha256:b19e6e1042ab803192c38ab2a6d0b729ece5a129c3656b3068264e647fde3b00", "1.0.0--pyhdfd78af_0": "sha256:06e9b6a7c845d193e8691474abedd20f9b7c4fbf1f6400627394bc2bd6c30441", "0.2.1--pyhdfd78af_0": "sha256:b912c2c2e283a7250e2de9915cfa0bab34b85885870305b321d75a033c427251", "1.1.0--pyhdfd78af_0": "sha256:22f5d969f8d997d14bf71f674d32a4580d46e69407ce7e4443e8921f874eed2b", "1.0.1--pyhdfd78af_0": "sha256:051291c632f34594fb21ca9d808158f95c0dd031721220a98e15956f9f7cabe1", "1.1.2--pyhdfd78af_0": "sha256:850d21d5042678aa185117bc666af1f790e1ff730c77f2dc3b126edd4a468663", "1.1.3--pyhdfd78af_0": "sha256:7bf69c50c0797928db5686acb91f3b4b2bee2f53dca7bd21015ac4f3a2f01d1f", "1.1.4--pyhdfd78af_0": "sha256:15b37a8ad5e49d9cae3dd198da8f00b8a0e79b140db58ff75800804b730ff7a2", "1.2.0--pyhdfd78af_0": "sha256:4b7f1e10b760736fe483c7093b9793fc16b04b742eaeec8ababa0f84bc47ad5d"}, "docker": "quay.io/biocontainers/cleanifier", "aliases": {"cleanifier": "/usr/local/bin/cleanifier", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "numpy-config": "/usr/local/bin/numpy-config", "py.test": "/usr/local/bin/py.test", "pytest": "/usr/local/bin/pytest", "numba": "/usr/local/bin/numba", "jsonschema": "/usr/local/bin/jsonschema", "activate-global-python-argcomplete": "/usr/local/bin/activate-global-python-argcomplete", "python-argcomplete-check-easy-install-script": "/usr/local/bin/python-argcomplete-check-easy-install-script", "register-python-argcomplete": "/usr/local/bin/register-python-argcomplete", "normalizer": "/usr/local/bin/normalizer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cleanifier.
singularity registry hpc automated addition for cleanifier
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cleanifier
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cleanifier:1.2.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cleanifier/1.2.0--pyhdfd78af_0
$ module help quay.io/biocontainers/cleanifier/1.2.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cleanifier-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cleanifier-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cleanifier-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cleanifier-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cleanifier-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cleanifier-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cleanifier

```bash
$ singularity exec <container> /usr/local/bin/cleanifier
$ podman run --it --rm --entrypoint /usr/local/bin/cleanifier   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cleanifier   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### numba

```bash
$ singularity exec <container> /usr/local/bin/numba
$ podman run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsonschema

```bash
$ singularity exec <container> /usr/local/bin/jsonschema
$ podman run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### activate-global-python-argcomplete

```bash
$ singularity exec <container> /usr/local/bin/activate-global-python-argcomplete
$ podman run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-argcomplete-check-easy-install-script

```bash
$ singularity exec <container> /usr/local/bin/python-argcomplete-check-easy-install-script
$ podman run --it --rm --entrypoint /usr/local/bin/python-argcomplete-check-easy-install-script   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-argcomplete-check-easy-install-script   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### register-python-argcomplete

```bash
$ singularity exec <container> /usr/local/bin/register-python-argcomplete
$ podman run --it --rm --entrypoint /usr/local/bin/register-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/register-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
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
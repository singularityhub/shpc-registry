---
layout: container
name:  "quay.io/biocontainers/pybwa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pybwa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pybwa/container.yaml"
updated_at: "2026-01-11 04:14:11.816637"
latest: "2.2.0--py311hb456a96_0"
container_url: "https://biocontainers.pro/tools/pybwa"
aliases:
 - "py.test"
 - "pytest"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
versions:
 - "1.4.3--py310h397c9d8_0"
 - "1.4.6--py312h4711d71_0"
 - "1.4.7--py39h0699b22_0"
 - "2.0.0--py312h47d5410_0"
 - "1.6.0--py311hb456a96_0"
 - "1.5.2--py310h64e62c9_0"
 - "1.4.8--py311h384fd50_0"
 - "2.1.0--py311hb456a96_0"
 - "2.0.1--py312h47d5410_0"
 - "2.2.0--py311hb456a96_0"
description: "singularity registry hpc automated addition for pybwa"
config: {"url": "https://biocontainers.pro/tools/pybwa", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pybwa", "latest": {"2.2.0--py311hb456a96_0": "sha256:531fa8e8bb92adba83ea007d2acceea1e76547bcbba9d13eb6b061ed76295c8f"}, "tags": {"1.4.3--py310h397c9d8_0": "sha256:4b5e9430a809f0a2e0859a9669853be192a0b63f2288122a9b456b554baf5173", "1.4.6--py312h4711d71_0": "sha256:ddb510356dec4cea4801d66c1bc61c13e1637c6437ccc4768c38c6708cb5b862", "1.4.7--py39h0699b22_0": "sha256:bdfe598f35528578f11a908cf83873254cdf0256df6ab0ad2364b9f3a548d285", "2.0.0--py312h47d5410_0": "sha256:5f07c1ad677c3b5f8ad48918ad43f8e5307af9986451bf5a6510914696b898ba", "1.6.0--py311hb456a96_0": "sha256:596932c73c4d680291e8a61014a36780d83e9ccfd6182c4d1904d490692672ce", "1.5.2--py310h64e62c9_0": "sha256:a821545fb96a2124b99cbe01dcf78d9eefe18fb3dd4c6ed181bbec6ff7eaac2c", "1.4.8--py311h384fd50_0": "sha256:a2ff5483291ddff677b22f704d72f3e8039d362e4429be70ba08dd8614f9f93f", "2.1.0--py311hb456a96_0": "sha256:84dacb1f795150db2c0f997e2f18a96633c1a36b16a4b13e5c2b12c427116eb2", "2.0.1--py312h47d5410_0": "sha256:0b0e4dde1afb9a1f02b72e8694d9ed6d8da8d61171b23cf3cc24adc3feadecd7", "2.2.0--py311hb456a96_0": "sha256:531fa8e8bb92adba83ea007d2acceea1e76547bcbba9d13eb6b061ed76295c8f"}, "docker": "quay.io/biocontainers/pybwa", "aliases": {"py.test": "/usr/local/bin/py.test", "pytest": "/usr/local/bin/pytest", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pybwa.
singularity registry hpc automated addition for pybwa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pybwa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pybwa:2.2.0--py311hb456a96_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pybwa/2.2.0--py311hb456a96_0
$ module help quay.io/biocontainers/pybwa/2.2.0--py311hb456a96_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pybwa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pybwa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pybwa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pybwa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pybwa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pybwa-inspect-deffile:

```bash
$ singularity inspect -d <container>
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
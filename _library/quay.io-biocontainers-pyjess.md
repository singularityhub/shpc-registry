---
layout: container
name:  "quay.io/biocontainers/pyjess"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pyjess/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pyjess/container.yaml"
updated_at: "2026-02-07 05:01:01.290671"
latest: "0.9.1--py310h1fe012e_0"
container_url: "https://biocontainers.pro/tools/pyjess"
aliases:
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
versions:
 - "0.3.3--py310h7c593f9_0"
 - "0.3.3--py38h0020b31_0"
 - "0.4.1--py310h1fe012e_1"
 - "0.5.0--py39hbcbf7aa_0"
 - "0.7.0--py311haab0aaa_0"
 - "0.6.0--py311haab0aaa_0"
 - "0.5.2--py312h0fa9677_0"
 - "0.8.0--py312h0fa9677_0"
 - "0.9.0--py310h1fe012e_0"
 - "0.9.1--py310h1fe012e_0"
description: "singularity registry hpc automated addition for pyjess"
config: {"url": "https://biocontainers.pro/tools/pyjess", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pyjess", "latest": {"0.9.1--py310h1fe012e_0": "sha256:2b8a10bb631f45194259ed0a74d2bb075401bbf40204de7a228ff6ae87839103"}, "tags": {"0.3.3--py310h7c593f9_0": "sha256:b26497d8f602038b90bb66a07137110953ecd733058059ee33f8957532284aa0", "0.3.3--py38h0020b31_0": "sha256:e40a1c8e68ab0a5c92a382aa0abeb69b881e337eba6f3a3a878ac5842b6d5d9d", "0.4.1--py310h1fe012e_1": "sha256:54cffc78a64f4d4803b2219d6bb7220c48f9707134f1e3ac464457fd0bfbe70c", "0.5.0--py39hbcbf7aa_0": "sha256:f0a77b55084dd444d8485896ec656e6a1858d5f67637d535fdd1e796aef880ee", "0.7.0--py311haab0aaa_0": "sha256:9d87b71520af0ed8fc561a2f34a498cb54cdbbc38fb4a9c8057d39f038953955", "0.6.0--py311haab0aaa_0": "sha256:4d3b20ce9fcad839a24289ad1c9c03b0e6bbe4b8aa881640c9480b325d739487", "0.5.2--py312h0fa9677_0": "sha256:29c2e5818211bdc2228885ad5c215bbf30744241bc84acb254002eb9965d24e3", "0.8.0--py312h0fa9677_0": "sha256:483aa788d4fac59d06c04d7ae962d8de444eb7339bd135c321095c4e6ad5b5e5", "0.9.0--py310h1fe012e_0": "sha256:8b34316294fc963dd2de77fe432d529f85eb3a73c77fac92a9e3548de21fbf72", "0.9.1--py310h1fe012e_0": "sha256:2b8a10bb631f45194259ed0a74d2bb075401bbf40204de7a228ff6ae87839103"}, "docker": "quay.io/biocontainers/pyjess", "aliases": {"2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pyjess.
singularity registry hpc automated addition for pyjess
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pyjess
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pyjess:0.9.1--py310h1fe012e_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pyjess/0.9.1--py310h1fe012e_0
$ module help quay.io/biocontainers/pyjess/0.9.1--py310h1fe012e_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pyjess-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pyjess-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pyjess-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pyjess-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pyjess-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pyjess-inspect-deffile:

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
---
layout: container
name:  "quay.io/biocontainers/chromatiblock"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/chromatiblock/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/chromatiblock/container.yaml"
updated_at: "2022-10-27 00:54:28.132823"
latest: "1.0.0--py_0"
container_url: "https://biocontainers.pro/tools/chromatiblock"
aliases:
 - "C-Sibelia.py"
 - "Sibelia"
 - "cairosvg"
 - "chromatiblock"
 - "snpEffAnnotate.py"
versions:
 - "1.0.0--py_0"
description: "shpc-registry automated BioContainers addition for chromatiblock"
config: {"url": "https://biocontainers.pro/tools/chromatiblock", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for chromatiblock", "latest": {"1.0.0--py_0": "sha256:fce5317ca2a8159debfe7f1aa57cf173602b7b58aa01897f5c746a07e5fb1f9d"}, "tags": {"1.0.0--py_0": "sha256:fce5317ca2a8159debfe7f1aa57cf173602b7b58aa01897f5c746a07e5fb1f9d"}, "docker": "quay.io/biocontainers/chromatiblock", "aliases": {"C-Sibelia.py": "/usr/local/bin/C-Sibelia.py", "Sibelia": "/usr/local/bin/Sibelia", "cairosvg": "/usr/local/bin/cairosvg", "chromatiblock": "/usr/local/bin/chromatiblock", "snpEffAnnotate.py": "/usr/local/bin/snpEffAnnotate.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/chromatiblock.
shpc-registry automated BioContainers addition for chromatiblock
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/chromatiblock
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/chromatiblock:1.0.0--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/chromatiblock/1.0.0--py_0
$ module help quay.io/biocontainers/chromatiblock/1.0.0--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### chromatiblock-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### chromatiblock-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### chromatiblock-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### chromatiblock-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### chromatiblock-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### chromatiblock-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### C-Sibelia.py

```bash
$ singularity exec <container> /usr/local/bin/C-Sibelia.py
$ podman run --it --rm --entrypoint /usr/local/bin/C-Sibelia.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/C-Sibelia.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Sibelia

```bash
$ singularity exec <container> /usr/local/bin/Sibelia
$ podman run --it --rm --entrypoint /usr/local/bin/Sibelia   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Sibelia   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cairosvg

```bash
$ singularity exec <container> /usr/local/bin/cairosvg
$ podman run --it --rm --entrypoint /usr/local/bin/cairosvg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cairosvg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chromatiblock

```bash
$ singularity exec <container> /usr/local/bin/chromatiblock
$ podman run --it --rm --entrypoint /usr/local/bin/chromatiblock   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chromatiblock   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snpEffAnnotate.py

```bash
$ singularity exec <container> /usr/local/bin/snpEffAnnotate.py
$ podman run --it --rm --entrypoint /usr/local/bin/snpEffAnnotate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snpEffAnnotate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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
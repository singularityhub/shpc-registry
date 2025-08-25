---
layout: container
name:  "quay.io/biocontainers/dnachisel"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dnachisel/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dnachisel/container.yaml"
updated_at: "2025-08-25 03:53:44.877071"
latest: "3.2.16--pyh7e72e81_0"
container_url: "https://biocontainers.pro/tools/dnachisel"
aliases:
 - "dnachisel"
 - "tqdm"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
versions:
 - "3.2.9--pyh5e36f6f_0"
 - "3.2.10--pyh7cba7a3_0"
 - "3.2.11--pyh7cba7a3_0"
 - "3.2.12--pyh7e72e81_0"
 - "3.2.13--pyh7e72e81_0"
 - "3.2.15--pyh7e72e81_0"
 - "3.2.16--pyh7e72e81_0"
description: "shpc-registry automated BioContainers addition for dnachisel"
config: {"url": "https://biocontainers.pro/tools/dnachisel", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dnachisel", "latest": {"3.2.16--pyh7e72e81_0": "sha256:44a4fc609820fe02e65438cbe74ae6b3134c5005219077a73144d419e1382c8a"}, "tags": {"3.2.9--pyh5e36f6f_0": "sha256:2e07e9392dd878f886499351dddfd8f62d7a8431dbcadba852ca88e22452b7b5", "3.2.10--pyh7cba7a3_0": "sha256:89f78a6f65464b17223c8bb3f4225ca1c654f60259a45ad4a10a788f1c746dcc", "3.2.11--pyh7cba7a3_0": "sha256:149c216473f1318d265b472d8862eec798913dd906337bf98f191ac54a443c84", "3.2.12--pyh7e72e81_0": "sha256:8a7fdb86ca676194486dd9caa0c16ba6ec46c6fcd3ca8336387e1dc5dbfebfce", "3.2.13--pyh7e72e81_0": "sha256:1fb7565ac94b37b861ce1aa5043bb266e92f4237c7b61c0209e3a40186aee96e", "3.2.15--pyh7e72e81_0": "sha256:16fd9c2ed6f09e3ef7ab7c90738f0480460b679f0513999850d72067f9e6a233", "3.2.16--pyh7e72e81_0": "sha256:44a4fc609820fe02e65438cbe74ae6b3134c5005219077a73144d419e1382c8a"}, "docker": "quay.io/biocontainers/dnachisel", "aliases": {"dnachisel": "/usr/local/bin/dnachisel", "tqdm": "/usr/local/bin/tqdm", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dnachisel.
shpc-registry automated BioContainers addition for dnachisel
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dnachisel
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dnachisel:3.2.16--pyh7e72e81_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dnachisel/3.2.16--pyh7e72e81_0
$ module help quay.io/biocontainers/dnachisel/3.2.16--pyh7e72e81_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dnachisel-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dnachisel-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dnachisel-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dnachisel-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dnachisel-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dnachisel-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dnachisel

```bash
$ singularity exec <container> /usr/local/bin/dnachisel
$ podman run --it --rm --entrypoint /usr/local/bin/dnachisel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnachisel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tqdm

```bash
$ singularity exec <container> /usr/local/bin/tqdm
$ podman run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
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
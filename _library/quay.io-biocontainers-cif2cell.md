---
layout: container
name:  "quay.io/biocontainers/cif2cell"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cif2cell/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cif2cell/container.yaml"
updated_at: "2025-09-25 03:44:48.527142"
latest: "2.0.0a3"
container_url: "https://biocontainers.pro/tools/cif2cell"
aliases:
 - "cif2cell"
 - "vasp2cif"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
versions:
 - "2.0.0a3"
description: "shpc-registry automated BioContainers addition for cif2cell"
config: {"url": "https://biocontainers.pro/tools/cif2cell", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cif2cell", "latest": {"2.0.0a3": "sha256:9a13a63ad7a2a467c8a4e29d1cb1d7494ab9cac9dbfa2db257fa6c3e806e2ee4"}, "tags": {"2.0.0a3": "sha256:9a13a63ad7a2a467c8a4e29d1cb1d7494ab9cac9dbfa2db257fa6c3e806e2ee4"}, "docker": "quay.io/biocontainers/cif2cell", "aliases": {"cif2cell": "/usr/local/bin/cif2cell", "vasp2cif": "/usr/local/bin/vasp2cif", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cif2cell.
shpc-registry automated BioContainers addition for cif2cell
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cif2cell
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cif2cell:2.0.0a3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cif2cell/2.0.0a3
$ module help quay.io/biocontainers/cif2cell/2.0.0a3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cif2cell-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cif2cell-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cif2cell-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cif2cell-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cif2cell-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cif2cell-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cif2cell

```bash
$ singularity exec <container> /usr/local/bin/cif2cell
$ podman run --it --rm --entrypoint /usr/local/bin/cif2cell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cif2cell   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vasp2cif

```bash
$ singularity exec <container> /usr/local/bin/vasp2cif
$ podman run --it --rm --entrypoint /usr/local/bin/vasp2cif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vasp2cif   -v ${PWD} -w ${PWD} <container> -c " $@"
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
---
layout: container
name:  "quay.io/pawsey/intel-hpc-python"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/pawsey/intel-hpc-python/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/pawsey/intel-hpc-python/container.yaml"
updated_at: "2023-10-06 02:22:54.699457"
latest: "2022.03"
container_url: "https://quay.io/repository/pawsey/intel-hpc-python"
aliases:
 - "python"
 - "python3"
versions:
 - "2021.09"
 - "2021.09-hdf5mpi"
 - "2022.03"
 - "2022.03-hdf5mpi"
description: "Base Python images with popular packages for HPC workflows, using Intel Python."
config: {"docker": "quay.io/pawsey/intel-hpc-python", "url": "https://quay.io/repository/pawsey/intel-hpc-python", "maintainer": "@marcodelapierre", "description": "Base Python images with popular packages for HPC workflows, using Intel Python.", "latest": {"2022.03": "sha256:d2a8ac146efbdff9b147f1d921295a710678d281a5af149c6f272da1cedf20a4"}, "tags": {"2021.09": "sha256:a22b12d7341cac98f41fa59cff964d61838e53e88ab8ec7f4148a8b5624e794e", "2021.09-hdf5mpi": "sha256:1fee6bca096915d6929cae10f75a0e8adc13859aeef2e140aa7ec4f9728f774d", "2022.03": "sha256:d2a8ac146efbdff9b147f1d921295a710678d281a5af149c6f272da1cedf20a4", "2022.03-hdf5mpi": "sha256:8cb0238d2ed84f284c50cf1cd8811b12043e687a2b5ff4c858eac70acec7a549"}, "aliases": {"python": "/opt/conda/bin/python", "python3": "/opt/conda/bin/python3"}, "env": {"PYTHONSTARTUP": "", "PYTHONUSERBASE": ""}, "features": {"home": true}}
---

This module is a singularity container wrapper for quay.io/pawsey/intel-hpc-python.
Base Python images with popular packages for HPC workflows, using Intel Python.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/pawsey/intel-hpc-python
```

Or a specific version:

```bash
$ shpc install quay.io/pawsey/intel-hpc-python:2022.03
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/pawsey/intel-hpc-python/2022.03
$ module help quay.io/pawsey/intel-hpc-python/2022.03
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### intel-hpc-python-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### intel-hpc-python-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### intel-hpc-python-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### intel-hpc-python-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### intel-hpc-python-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### intel-hpc-python-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### python

```bash
$ singularity exec <container> /opt/conda/bin/python
$ podman run --it --rm --entrypoint /opt/conda/bin/python   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/conda/bin/python   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3

```bash
$ singularity exec <container> /opt/conda/bin/python3
$ podman run --it --rm --entrypoint /opt/conda/bin/python3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/conda/bin/python3   -v ${PWD} -w ${PWD} <container> -c " $@"
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
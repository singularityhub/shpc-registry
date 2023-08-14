---
layout: container
name:  "quay.io/biocontainers/msms"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/msms/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/msms/container.yaml"
updated_at: "2023-08-14 02:28:45.766804"
latest: "2.6.1--h9ee0642_3"
container_url: "https://biocontainers.pro/tools/msms"
aliases:
 - "msms"
 - "pdb_to_xyzr"
 - "pdb_to_xyzrn"
versions:
 - "2.6.1--h9ee0642_3"
description: "shpc-registry automated BioContainers addition for msms"
config: {"url": "https://biocontainers.pro/tools/msms", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for msms", "latest": {"2.6.1--h9ee0642_3": "sha256:18f7e3d4e5515d2a2cb5ae53145b08df891e8e2661170dc403fb27cd62a4d3ac"}, "tags": {"2.6.1--h9ee0642_3": "sha256:18f7e3d4e5515d2a2cb5ae53145b08df891e8e2661170dc403fb27cd62a4d3ac"}, "docker": "quay.io/biocontainers/msms", "aliases": {"msms": "/usr/local/bin/msms", "pdb_to_xyzr": "/usr/local/bin/pdb_to_xyzr", "pdb_to_xyzrn": "/usr/local/bin/pdb_to_xyzrn"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/msms.
shpc-registry automated BioContainers addition for msms
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/msms
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/msms:2.6.1--h9ee0642_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/msms/2.6.1--h9ee0642_3
$ module help quay.io/biocontainers/msms/2.6.1--h9ee0642_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### msms-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### msms-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### msms-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### msms-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### msms-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### msms-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### msms

```bash
$ singularity exec <container> /usr/local/bin/msms
$ podman run --it --rm --entrypoint /usr/local/bin/msms   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/msms   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdb_to_xyzr

```bash
$ singularity exec <container> /usr/local/bin/pdb_to_xyzr
$ podman run --it --rm --entrypoint /usr/local/bin/pdb_to_xyzr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdb_to_xyzr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdb_to_xyzrn

```bash
$ singularity exec <container> /usr/local/bin/pdb_to_xyzrn
$ podman run --it --rm --entrypoint /usr/local/bin/pdb_to_xyzrn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdb_to_xyzrn   -v ${PWD} -w ${PWD} <container> -c " $@"
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
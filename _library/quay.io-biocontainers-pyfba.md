---
layout: container
name:  "quay.io/biocontainers/pyfba"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pyfba/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/pyfba/container.yaml"
updated_at: "2022-10-27 00:51:07.546082"
latest: "2.62--py39h8c4442e_2"
container_url: "https://biocontainers.pro/tools/pyfba"
aliases:
 - "black-primer"
 - "jupyter-dejavu"
 - "jupyter-execute"
 - "pyfba"
 - "send2trash"
versions:
 - "2.62--py39h8c4442e_2"
description: "shpc-registry automated BioContainers addition for pyfba"
config: {"url": "https://biocontainers.pro/tools/pyfba", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pyfba", "latest": {"2.62--py39h8c4442e_2": "sha256:4b3eaf5f92231aacb9cb5a9f2e6dc78f6836edc9bac0a014efb23482c7ab3a7f"}, "tags": {"2.62--py39h8c4442e_2": "sha256:4b3eaf5f92231aacb9cb5a9f2e6dc78f6836edc9bac0a014efb23482c7ab3a7f"}, "docker": "quay.io/biocontainers/pyfba", "aliases": {"black-primer": "/usr/local/bin/black-primer", "jupyter-dejavu": "/usr/local/bin/jupyter-dejavu", "jupyter-execute": "/usr/local/bin/jupyter-execute", "pyfba": "/usr/local/bin/pyfba", "send2trash": "/usr/local/bin/send2trash"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pyfba.
shpc-registry automated BioContainers addition for pyfba
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pyfba
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pyfba:2.62--py39h8c4442e_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pyfba/2.62--py39h8c4442e_2
$ module help quay.io/biocontainers/pyfba/2.62--py39h8c4442e_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pyfba-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pyfba-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pyfba-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pyfba-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pyfba-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pyfba-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### black-primer

```bash
$ singularity exec <container> /usr/local/bin/black-primer
$ podman run --it --rm --entrypoint /usr/local/bin/black-primer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/black-primer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-dejavu

```bash
$ singularity exec <container> /usr/local/bin/jupyter-dejavu
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-dejavu   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-dejavu   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-execute

```bash
$ singularity exec <container> /usr/local/bin/jupyter-execute
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-execute   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-execute   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyfba

```bash
$ singularity exec <container> /usr/local/bin/pyfba
$ podman run --it --rm --entrypoint /usr/local/bin/pyfba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyfba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### send2trash

```bash
$ singularity exec <container> /usr/local/bin/send2trash
$ podman run --it --rm --entrypoint /usr/local/bin/send2trash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/send2trash   -v ${PWD} -w ${PWD} <container> -c " $@"
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
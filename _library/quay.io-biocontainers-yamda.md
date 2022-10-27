---
layout: container
name:  "quay.io/biocontainers/yamda"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/yamda/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/yamda/container.yaml"
updated_at: "2022-10-27 01:10:58.367938"
latest: "0.1.00e9c9d--py_0"
container_url: "https://biocontainers.pro/tools/yamda"
aliases:
 - "erase_annoying_sequences.py"
 - "run_em.py"
versions:
 - "0.1.00e9c9d--py_0"
description: "shpc-registry automated BioContainers addition for yamda"
config: {"url": "https://biocontainers.pro/tools/yamda", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for yamda", "latest": {"0.1.00e9c9d--py_0": "sha256:42f192c9857983c333056af650fa916b119e6c59403e553f2491faa36dccf478"}, "tags": {"0.1.00e9c9d--py_0": "sha256:42f192c9857983c333056af650fa916b119e6c59403e553f2491faa36dccf478"}, "docker": "quay.io/biocontainers/yamda", "aliases": {"erase_annoying_sequences.py": "/usr/local/bin/erase_annoying_sequences.py", "run_em.py": "/usr/local/bin/run_em.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/yamda.
shpc-registry automated BioContainers addition for yamda
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/yamda
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/yamda:0.1.00e9c9d--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/yamda/0.1.00e9c9d--py_0
$ module help quay.io/biocontainers/yamda/0.1.00e9c9d--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### yamda-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### yamda-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### yamda-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### yamda-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### yamda-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### yamda-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### erase_annoying_sequences.py

```bash
$ singularity exec <container> /usr/local/bin/erase_annoying_sequences.py
$ podman run --it --rm --entrypoint /usr/local/bin/erase_annoying_sequences.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/erase_annoying_sequences.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_em.py

```bash
$ singularity exec <container> /usr/local/bin/run_em.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_em.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_em.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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
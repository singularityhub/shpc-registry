---
layout: container
name:  "quay.io/jupyter/pyspark-notebook"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/jupyter/pyspark-notebook/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/jupyter/pyspark-notebook/container.yaml"
updated_at: "2025-07-29 03:52:28.223092"
latest: "2025-07-14"
container_url: "https://quay.io/repository/jupyter/pyspark-notebook"
aliases:
 - "run-notebook"
versions:
 - "latest"
 - "2025-05-30"
 - "2025-06-16"
 - "2025-07-14"
 - "2025-06-30"
description: "Jupyter PySpark Notebook from https://github.com/jupyter/docker-stacks"
config: {"docker": "quay.io/jupyter/pyspark-notebook", "url": "https://quay.io/repository/jupyter/pyspark-notebook", "maintainer": "@HasseJohansen", "description": "Jupyter PySpark Notebook from https://github.com/jupyter/docker-stacks", "latest": {"2025-07-14": "sha256:b97366efa13188a11ba7b503dcb41c871121323c1d6588df4cdb219c8701b142"}, "tags": {"latest": "sha256:b97366efa13188a11ba7b503dcb41c871121323c1d6588df4cdb219c8701b142", "2025-05-30": "sha256:aae52902c4ef29831c33c3e04f671ff104cc625611a09666b6eb58378ee813d3", "2025-06-16": "sha256:ac028861a31baeba4ee8905235c526f94f2e8971627a71cb0ec7b363f800a333", "2025-07-14": "sha256:b97366efa13188a11ba7b503dcb41c871121323c1d6588df4cdb219c8701b142", "2025-06-30": "sha256:d81e3385397a8e7e7ca34d7be5aa55c5872138298c571176fbdac834ce8f8629"}, "aliases": [{"name": "run-notebook", "command": "jupyter notebook --no-browser --port=$(shuf -i 2000-65000 -n 1) --ip 0.0.0.0"}]}
---

This module is a singularity container wrapper for quay.io/jupyter/pyspark-notebook.
Jupyter PySpark Notebook from https://github.com/jupyter/docker-stacks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/jupyter/pyspark-notebook
```

Or a specific version:

```bash
$ shpc install quay.io/jupyter/pyspark-notebook:2025-07-14
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/jupyter/pyspark-notebook/2025-07-14
$ module help quay.io/jupyter/pyspark-notebook/2025-07-14
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pyspark-notebook-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pyspark-notebook-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pyspark-notebook-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pyspark-notebook-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pyspark-notebook-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pyspark-notebook-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### run-notebook

```bash
$ singularity exec <container> jupyter notebook --no-browser --port=$(shuf -i 2000-65000 -n 1) --ip 0.0.0.0
$ podman run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
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
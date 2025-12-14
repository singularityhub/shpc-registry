---
layout: container
name:  "quay.io/jupyter/pyspark-notebook"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/jupyter/pyspark-notebook/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/jupyter/pyspark-notebook/container.yaml"
updated_at: "2025-12-14 03:42:28.111453"
latest: "2025-11-10"
container_url: "https://quay.io/repository/jupyter/pyspark-notebook"
aliases:
 - "run-notebook"
versions:
 - "latest"
 - "2025-05-30"
 - "2025-06-16"
 - "2025-07-14"
 - "2025-06-30"
 - "2025-08-15"
 - "2025-09-16"
 - "2025-10-13"
 - "2025-08-18"
 - "2025-07-28"
 - "2025-11-10"
 - "2025-10-27"
 - "2025-09-30"
 - "2025-08-25"
description: "Jupyter PySpark Notebook from https://github.com/jupyter/docker-stacks"
config: {"docker": "quay.io/jupyter/pyspark-notebook", "url": "https://quay.io/repository/jupyter/pyspark-notebook", "maintainer": "@HasseJohansen", "description": "Jupyter PySpark Notebook from https://github.com/jupyter/docker-stacks", "latest": {"2025-11-10": "sha256:6287c0ba787930d8dec08f8c5c81866b1e86be14adbfb3efe2b18d4e5db877ff"}, "tags": {"latest": "sha256:6287c0ba787930d8dec08f8c5c81866b1e86be14adbfb3efe2b18d4e5db877ff", "2025-05-30": "sha256:aae52902c4ef29831c33c3e04f671ff104cc625611a09666b6eb58378ee813d3", "2025-06-16": "sha256:ac028861a31baeba4ee8905235c526f94f2e8971627a71cb0ec7b363f800a333", "2025-07-14": "sha256:b97366efa13188a11ba7b503dcb41c871121323c1d6588df4cdb219c8701b142", "2025-06-30": "sha256:d81e3385397a8e7e7ca34d7be5aa55c5872138298c571176fbdac834ce8f8629", "2025-08-15": "sha256:e77fedc10a70c7fd929b348282b2b2bd57b1cce571f746301db4f3de685f1c73", "2025-09-16": "sha256:9bf2ebb78e682b5798a7b55de4843f84a6947777e499f9011a356db5b201c1fe", "2025-10-13": "sha256:9d645d59f94f477c27c87e39bb9b281868572720231faed58a51afb31ef5e423", "2025-08-18": "sha256:90a71622798dbb92a3cd2b329a2a372afc0bda37d48b13d97541146ed2cdd8e7", "2025-07-28": "sha256:221b7c5331d0bb2d3e324eddd10d06d36064431888d034c428bddbf458bb6909", "2025-11-10": "sha256:6287c0ba787930d8dec08f8c5c81866b1e86be14adbfb3efe2b18d4e5db877ff", "2025-10-27": "sha256:1d3d4e48f7a0766b4f56eb01b2aac8103b2bc759a5eb5fd0623d28a16ef93602", "2025-09-30": "sha256:79a020d160670e5c33d75dbe1a40878579ce32e8d68faad9f752a5d3e219d2f4", "2025-08-25": "sha256:938fdd57901e764b4e6e0adbe7438725e703a782608dc79bd2a7c722a4f8a0bf"}, "aliases": [{"name": "run-notebook", "command": "jupyter notebook --no-browser --port=$(shuf -i 2000-65000 -n 1) --ip 0.0.0.0"}]}
---

This module is a singularity container wrapper for quay.io/jupyter/pyspark-notebook.
Jupyter PySpark Notebook from https://github.com/jupyter/docker-stacks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/jupyter/pyspark-notebook
```

Or a specific version:

```bash
$ shpc install quay.io/jupyter/pyspark-notebook:2025-11-10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/jupyter/pyspark-notebook/2025-11-10
$ module help quay.io/jupyter/pyspark-notebook/2025-11-10
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
---
layout: container
name:  "quay.io/jupyter/all-spark-notebook"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/jupyter/all-spark-notebook/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/jupyter/all-spark-notebook/container.yaml"
updated_at: "2026-01-12 03:53:22.457432"
latest: "2025-12-31"
container_url: "https://quay.io/repository/jupyter/all-spark-notebook"
aliases:
 - "run-notebook"
versions:
 - "latest"
 - "2025-06-02"
 - "2025-06-30"
 - "2025-07-28"
 - "2025-08-25"
 - "2025-09-30"
 - "2025-08-18"
 - "2025-11-03"
 - "2025-10-06"
 - "2025-12-03"
 - "2025-12-31"
description: "Jupyter All Spark Notebook from https://github.com/jupyter/docker-stacks"
config: {"docker": "quay.io/jupyter/all-spark-notebook", "url": "https://quay.io/repository/jupyter/all-spark-notebook", "maintainer": "@HasseJohansen", "description": "Jupyter All Spark Notebook from https://github.com/jupyter/docker-stacks", "latest": {"2025-12-31": "sha256:33d2294ced30655d2db7f9ee6f28c3d08e0193b279c1a6321223a7bf35e7bd69"}, "tags": {"latest": "sha256:33d2294ced30655d2db7f9ee6f28c3d08e0193b279c1a6321223a7bf35e7bd69", "2025-06-02": "sha256:949c3fd651200ef9b18c6bef38e827f6c00d3dce26965ea9168150e98d0f9a26", "2025-06-30": "sha256:1459be53cf4f51f0ead1dafafb440cff0d9251501fe7a9bdb6ccafe2148af34c", "2025-07-28": "sha256:03d5a184f3b6abe3c0709afcc78ece041a71f016e3088e76fe3aca57df4950eb", "2025-08-25": "sha256:6a374fe825b0391006dccbaf0529aaa462adaf461d41c47f2dcea044a61a21d9", "2025-09-30": "sha256:1472236b6fcd0e6dd8e3d40a61391f11e54552e989afb88f7f042f36046b07f7", "2025-08-18": "sha256:7973559eb50f7f8a57cafba4a100ef2e50f13a8312d800e385cb7f07f7b44ffa", "2025-11-03": "sha256:5379f8beb3bc98460c452a616172142ef85981c996718a90ef95a845f11796a5", "2025-10-06": "sha256:5917fe6ee4d0b9d48467f619059bb1f1b1c62dc8f7e97e2974f8754e0a9da3df", "2025-12-03": "sha256:1876713d83d850e9097c22ef68432cc04cc47bea1193d7726b94223b272202be", "2025-12-31": "sha256:33d2294ced30655d2db7f9ee6f28c3d08e0193b279c1a6321223a7bf35e7bd69"}, "aliases": [{"name": "run-notebook", "command": "jupyter notebook --no-browser --port=$(shuf -i 2000-65000 -n 1) --ip 0.0.0.0"}]}
---

This module is a singularity container wrapper for quay.io/jupyter/all-spark-notebook.
Jupyter All Spark Notebook from https://github.com/jupyter/docker-stacks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/jupyter/all-spark-notebook
```

Or a specific version:

```bash
$ shpc install quay.io/jupyter/all-spark-notebook:2025-12-31
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/jupyter/all-spark-notebook/2025-12-31
$ module help quay.io/jupyter/all-spark-notebook/2025-12-31
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### all-spark-notebook-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### all-spark-notebook-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### all-spark-notebook-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### all-spark-notebook-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### all-spark-notebook-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### all-spark-notebook-inspect-deffile:

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
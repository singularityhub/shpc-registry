---
layout: container
name:  "quay.io/jupyter/pytorch-notebook"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/jupyter/pytorch-notebook/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/jupyter/pytorch-notebook/container.yaml"
updated_at: "2025-07-27 03:50:29.420210"
latest: "2025-07-07"
container_url: "https://quay.io/repository/jupyter/pytorch-notebook"
aliases:
 - "run-notebook"
versions:
 - "latest"
 - "2025-06-02"
 - "cuda12-2025-06-02"
 - "cuda11-2025-06-02"
 - "2025-05-30"
 - "2025-03-24"
 - "2025-02-26"
 - "2025-01-28"
 - "2025-07-07"
 - "2025-06-30"
 - "2025-05-05"
 - "2025-04-30"
description: "Jupyter PyTorch Notebook from https://github.com/jupyter/docker-stacks"
config: {"docker": "quay.io/jupyter/pytorch-notebook", "url": "https://quay.io/repository/jupyter/pytorch-notebook", "maintainer": "@HasseJohansen", "description": "Jupyter PyTorch Notebook from https://github.com/jupyter/docker-stacks", "latest": {"2025-07-07": "sha256:9255af4c23c6a049d62e8ed8b4eb28f2439cd25e20880d94feaac451df95e940"}, "tags": {"latest": "sha256:9255af4c23c6a049d62e8ed8b4eb28f2439cd25e20880d94feaac451df95e940", "2025-06-02": "sha256:39c64d643a377cab73e03ff2d161879a6b8b360271247645de96aeb12fa86c31", "cuda12-2025-06-02": "sha256:7266ffb8e19e9a61bf05437bdcc854c7c02a7b1ce1fd0af94e5dd41f3335a3df", "cuda11-2025-06-02": "sha256:9a230d0c3334bf92f5000ec83ccff4b1df045ad54935364f5ce510c60316b7ad", "2025-05-30": "sha256:608f916f0b03014606c96e25bc375d3280bd5a90844cde0896568ed8e4f49f91", "2025-03-24": "sha256:de7914bae2df832c345457955d1da00582d6849e7807358cac5cea8b314544f6", "2025-02-26": "sha256:6014e504860c570e2d92bf0f7140273cb7f0a105f6b6fe425a6a276a1f6d11cf", "2025-01-28": "sha256:556496d6c30216b11ad3f55432e3247439b85f38a76cc63998b1694284ea8b75", "2025-07-07": "sha256:9255af4c23c6a049d62e8ed8b4eb28f2439cd25e20880d94feaac451df95e940", "2025-06-30": "sha256:f69034ce54b8d8f5edec2f3c857d38f2be45d2b8d66fb90842fccb6bc94a2741", "2025-05-05": "sha256:81385abbee70ba638b48ce4607f72b84d2207de31b1fb253f4237c5eee1958d4", "2025-04-30": "sha256:b8dc1fe5e636a5d3aa0933785af406b6fc2cd3d8b8e89ceeaa498d19b414a197"}, "aliases": [{"name": "run-notebook", "command": "jupyter notebook --no-browser --port=$(shuf -i 2000-65000 -n 1) --ip 0.0.0.0"}]}
---

This module is a singularity container wrapper for quay.io/jupyter/pytorch-notebook.
Jupyter PyTorch Notebook from https://github.com/jupyter/docker-stacks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/jupyter/pytorch-notebook
```

Or a specific version:

```bash
$ shpc install quay.io/jupyter/pytorch-notebook:2025-07-07
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/jupyter/pytorch-notebook/2025-07-07
$ module help quay.io/jupyter/pytorch-notebook/2025-07-07
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pytorch-notebook-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pytorch-notebook-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pytorch-notebook-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pytorch-notebook-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pytorch-notebook-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pytorch-notebook-inspect-deffile:

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
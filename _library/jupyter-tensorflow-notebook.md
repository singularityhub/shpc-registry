---
layout: container
name:  "jupyter/tensorflow-notebook"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/jupyter/tensorflow-notebook/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/jupyter/tensorflow-notebook/container.yaml"
updated_at: "2023-08-12 02:17:30.992898"
latest: "x86_64-ubuntu-22.04"
container_url: "https://hub.docker.com/r/jupyter/tensorflow-notebook"
aliases:
 - "run-notebook"
versions:
 - "latest"
 - "ubuntu-20.04"
 - "ubuntu-22.04"
 - "x86_64-ubuntu-22.04"
 - "aarch64-ubuntu-22.04"
description: "Jupyter Tensorflow Notebook from https://github.com/jupyter/docker-stacks"
config: {"docker": "jupyter/tensorflow-notebook", "url": "https://hub.docker.com/r/jupyter/tensorflow-notebook", "maintainer": "@vsoch", "description": "Jupyter Tensorflow Notebook from https://github.com/jupyter/docker-stacks", "latest": {"x86_64-ubuntu-22.04": "sha256:11b98e0a1a2a2b0091bd41cd5a706fcaae188eeb9c164b708c363862be11046b"}, "tags": {"latest": "sha256:7d0f3ccf1eeb0f25ffc4182f02846b05ebc3526076797207b3912e72df1251df", "ubuntu-20.04": "sha256:1bbb4dd5fd643f693567c84173e86ec7ed0c2e11ac70f2326e057539698f91f2", "ubuntu-22.04": "sha256:7d0f3ccf1eeb0f25ffc4182f02846b05ebc3526076797207b3912e72df1251df", "x86_64-ubuntu-22.04": "sha256:11b98e0a1a2a2b0091bd41cd5a706fcaae188eeb9c164b708c363862be11046b", "aarch64-ubuntu-22.04": "sha256:dc2438d97dea11a394c592140425af742ed231e4b7572c5690bdeb30a72016ec"}, "filter": ["ubuntu*"], "aliases": [{"name": "run-notebook", "command": "jupyter notebook --no-browser --port=$(shuf -i 2000-65000 -n 1) --ip 0.0.0.0"}]}
---

This module is a singularity container wrapper for jupyter/tensorflow-notebook.
Jupyter Tensorflow Notebook from https://github.com/jupyter/docker-stacks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install jupyter/tensorflow-notebook
```

Or a specific version:

```bash
$ shpc install jupyter/tensorflow-notebook:x86_64-ubuntu-22.04
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load jupyter/tensorflow-notebook/x86_64-ubuntu-22.04
$ module help jupyter/tensorflow-notebook/x86_64-ubuntu-22.04
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tensorflow-notebook-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tensorflow-notebook-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tensorflow-notebook-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tensorflow-notebook-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tensorflow-notebook-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tensorflow-notebook-inspect-deffile:

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
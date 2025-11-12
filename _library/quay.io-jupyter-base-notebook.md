---
layout: container
name:  "quay.io/jupyter/base-notebook"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/jupyter/base-notebook/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/jupyter/base-notebook/container.yaml"
updated_at: "2025-11-12 03:15:27.946998"
latest: "2025-10-21"
container_url: "https://quay.io/repository/jupyter/base-notebook"
aliases:
 - "run-notebook"
versions:
 - "latest"
 - "2025-05-30"
 - "2025-06-23"
 - "2025-08-18"
 - "2025-06-16"
 - "2025-09-23"
 - "2025-10-21"
 - "2025-09-15"
 - "2025-08-25"
 - "2025-07-28"
description: "Jupyter Base Notebook from https://github.com/jupyter/docker-stacks"
config: {"docker": "quay.io/jupyter/base-notebook", "url": "https://quay.io/repository/jupyter/base-notebook", "maintainer": "@HasseJohansen", "description": "Jupyter Base Notebook from https://github.com/jupyter/docker-stacks", "latest": {"2025-10-21": "sha256:1c565c1fb58fd67bbab1ac4a5250aa58fbdadf45206c1efdc242cce3402a03da"}, "tags": {"latest": "sha256:1c565c1fb58fd67bbab1ac4a5250aa58fbdadf45206c1efdc242cce3402a03da", "2025-05-30": "sha256:da04e895f1ccd395827f3033023603daafad818e9815c22c1fdc5cb6bd523a04", "2025-06-23": "sha256:50b5bcbea649bebb20c450c512f75750d20e98a04b2e0a948337a13d14528fe4", "2025-08-18": "sha256:f2e2b6d7a348938ad6d4aeabb4953babd28ed18fda3ab60bccb14780ab9555de", "2025-06-16": "sha256:cfba03d4beff02257ab6fc4bc855a767ef44009dbb6661e93b1c0f4bdffd00a8", "2025-09-23": "sha256:57f10d10087e75157d0d1304ae7dfeb3c0224a09ca6ff0d1302aee9d6c0e84be", "2025-10-21": "sha256:1c565c1fb58fd67bbab1ac4a5250aa58fbdadf45206c1efdc242cce3402a03da", "2025-09-15": "sha256:71bd13aaf92fe98f9f138bc0267e529ba40221be44d90967afd21372f4951542", "2025-08-25": "sha256:e9222d8476431543c605f1f203654ef8f89f573cb169c2065e6b1aff8bbfa5b9", "2025-07-28": "sha256:ae76b2693b46c268f83f81fe593bb1dc93564ace1e4662dd55aca20fc73a9cab"}, "aliases": [{"name": "run-notebook", "command": "jupyter notebook --no-browser --port=$(shuf -i 2000-65000 -n 1) --ip 0.0.0.0"}]}
---

This module is a singularity container wrapper for quay.io/jupyter/base-notebook.
Jupyter Base Notebook from https://github.com/jupyter/docker-stacks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/jupyter/base-notebook
```

Or a specific version:

```bash
$ shpc install quay.io/jupyter/base-notebook:2025-10-21
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/jupyter/base-notebook/2025-10-21
$ module help quay.io/jupyter/base-notebook/2025-10-21
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### base-notebook-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### base-notebook-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### base-notebook-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### base-notebook-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### base-notebook-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### base-notebook-inspect-deffile:

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
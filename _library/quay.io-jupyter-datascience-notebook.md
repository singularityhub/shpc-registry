---
layout: container
name:  "quay.io/jupyter/datascience-notebook"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/jupyter/datascience-notebook/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/jupyter/datascience-notebook/container.yaml"
updated_at: "2025-10-03 02:59:26.823951"
latest: "2025-09-08"
container_url: "https://quay.io/repository/jupyter/datascience-notebook"
aliases:
 - "run-notebook"
versions:
 - "latest"
 - "2025-05-26"
 - "2025-06-02"
 - "2025-07-14"
 - "2025-08-12"
 - "2025-07-28"
 - "2025-05-30"
 - "2025-09-08"
 - "2025-07-07"
 - "2025-06-30"
description: "Jupyter Datascience Notebook from https://github.com/jupyter/docker-stacks"
config: {"docker": "quay.io/jupyter/datascience-notebook", "url": "https://quay.io/repository/jupyter/datascience-notebook", "maintainer": "@HasseJohansen", "description": "Jupyter Datascience Notebook from https://github.com/jupyter/docker-stacks", "latest": {"2025-09-08": "sha256:7be8838ae1f0417dc78c1587c09ca6b3675d124990bebe2efb8ce7b6b3c704c3"}, "tags": {"latest": "sha256:7be8838ae1f0417dc78c1587c09ca6b3675d124990bebe2efb8ce7b6b3c704c3", "2025-05-26": "sha256:47a4ffb2783c68ffdb83ae0cf9d749aa70725987a69d26ce7109cbd0f77984a8", "2025-06-02": "sha256:2014f3b923d90d48dc45a9df5935efa97258ed557159a994921f4651d571b101", "2025-07-14": "sha256:20be99bdec2d0ae0c17845e1805a152e3d6629a38aee5a6bf1348bfcf2c12231", "2025-08-12": "sha256:3d88c2f752484071888d148dafedabfa2b13236243b82432b250de564d331d5f", "2025-07-28": "sha256:4b93f99fc05b7a4d2318bc1a25ca36083132bb9dfdf280c2e7edd7f6a3075a11", "2025-05-30": "sha256:c3157a080fab9ad7718a904a751cd5cbfa1190365f13f15f80f349b7f7dee4a1", "2025-09-08": "sha256:7be8838ae1f0417dc78c1587c09ca6b3675d124990bebe2efb8ce7b6b3c704c3", "2025-07-07": "sha256:0cc31bc531fc6a4500f31584d649c975530bde5febd3ec805eb85aea653527b3", "2025-06-30": "sha256:32dd384a6d6e31c12933cd19199ba630ec4abf8bff8b9d25c8cbd31bd1e3ea07"}, "aliases": [{"name": "run-notebook", "command": "jupyter notebook --no-browser --port=$(shuf -i 2000-65000 -n 1) --ip 0.0.0.0"}]}
---

This module is a singularity container wrapper for quay.io/jupyter/datascience-notebook.
Jupyter Datascience Notebook from https://github.com/jupyter/docker-stacks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/jupyter/datascience-notebook
```

Or a specific version:

```bash
$ shpc install quay.io/jupyter/datascience-notebook:2025-09-08
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/jupyter/datascience-notebook/2025-09-08
$ module help quay.io/jupyter/datascience-notebook/2025-09-08
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### datascience-notebook-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### datascience-notebook-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### datascience-notebook-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### datascience-notebook-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### datascience-notebook-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### datascience-notebook-inspect-deffile:

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
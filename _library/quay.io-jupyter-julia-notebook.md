---
layout: container
name:  "quay.io/jupyter/julia-notebook"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/jupyter/julia-notebook/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/jupyter/julia-notebook/container.yaml"
updated_at: "2026-01-21 03:47:44.929450"
latest: "2025-12-31"
container_url: "https://quay.io/repository/jupyter/julia-notebook"
aliases:
 - "run-notebook"
versions:
 - "latest"
 - "2025-05-30"
 - "2025-06-30"
 - "2025-07-28"
 - "2025-08-25"
 - "2025-09-30"
 - "2025-11-03"
 - "2025-12-03"
 - "2025-11-24"
 - "2025-09-22"
 - "2025-12-31"
 - "2025-11-29"
 - "2025-10-27"
description: "Jupyter Julia Notebook from https://github.com/jupyter/docker-stacks"
config: {"docker": "quay.io/jupyter/julia-notebook", "url": "https://quay.io/repository/jupyter/julia-notebook", "maintainer": "@HasseJohansen", "description": "Jupyter Julia Notebook from https://github.com/jupyter/docker-stacks", "latest": {"2025-12-31": "sha256:5ba5e8e9f618eaa7567c902c001f9ee656007b7d97161c4389a1e9209bef2132"}, "tags": {"latest": "sha256:5ba5e8e9f618eaa7567c902c001f9ee656007b7d97161c4389a1e9209bef2132", "2025-05-30": "sha256:9792324e1f10544aa7c56b79852129f131a09e86ce40cd64d7bcf63dc6e588ee", "2025-06-30": "sha256:85812ed3ee9b29a3937f95314abd427bdf904f1cd21e4de1d0696e48c5786caf", "2025-07-28": "sha256:5b7cd17b85b51e5153314840e30bd4240c1b1691ffb599a931ce94b0c75afaa7", "2025-08-25": "sha256:1f2f657acf9ad0c2d7e14a838dfb554992a1e5f3696014366fd9dacd2ab06e6a", "2025-09-30": "sha256:0617dcbcf9e2d9d27d67a0ca15d91e364cce40932ce311757acab4aa65328525", "2025-11-03": "sha256:ecd7b4a4d4af8ca53042573b87a8c6556cd036576a965b5c06cedc44b447ef3c", "2025-12-03": "sha256:59d98f166bd833f09be57a05b99fad58498b35bc76f52734617ce45f80f5fbfe", "2025-11-24": "sha256:b2852c53b56bfd73ee43bf4c30633a954e93f2baaf25a5c8bdec456b9a94e167", "2025-09-22": "sha256:cacaff91ce73c02e6319d81336285bf59642811529a69f054963571426618897", "2025-12-31": "sha256:5ba5e8e9f618eaa7567c902c001f9ee656007b7d97161c4389a1e9209bef2132", "2025-11-29": "sha256:50979fd069712a9a4dd42f46c35e5adc924bd68b8d5e6813ef5369cdecbf2177", "2025-10-27": "sha256:be55ce756bc101f16b5858962d988300d086ca69f645078f9c245bdc7af50857"}, "aliases": [{"name": "run-notebook", "command": "jupyter notebook --no-browser --port=$(shuf -i 2000-65000 -n 1) --ip 0.0.0.0"}]}
---

This module is a singularity container wrapper for quay.io/jupyter/julia-notebook.
Jupyter Julia Notebook from https://github.com/jupyter/docker-stacks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/jupyter/julia-notebook
```

Or a specific version:

```bash
$ shpc install quay.io/jupyter/julia-notebook:2025-12-31
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/jupyter/julia-notebook/2025-12-31
$ module help quay.io/jupyter/julia-notebook/2025-12-31
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### julia-notebook-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### julia-notebook-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### julia-notebook-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### julia-notebook-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### julia-notebook-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### julia-notebook-inspect-deffile:

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
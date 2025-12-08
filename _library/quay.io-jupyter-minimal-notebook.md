---
layout: container
name:  "quay.io/jupyter/minimal-notebook"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/jupyter/minimal-notebook/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/jupyter/minimal-notebook/container.yaml"
updated_at: "2025-12-08 04:46:52.717422"
latest: "2025-11-20"
container_url: "https://quay.io/repository/jupyter/minimal-notebook"
aliases:
 - "run-notebook"
versions:
 - "latest"
 - "2025-05-30"
 - "2025-06-23"
 - "2025-08-18"
 - "2025-09-23"
 - "2025-10-21"
 - "2025-09-15"
 - "2025-08-25"
 - "2025-07-28"
 - "2025-11-20"
 - "2025-10-27"
 - "2025-09-30"
description: "Jupyter Minimal Notebook from https://github.com/jupyter/docker-stacks"
config: {"docker": "quay.io/jupyter/minimal-notebook", "url": "https://quay.io/repository/jupyter/minimal-notebook", "maintainer": "@HasseJohansen", "description": "Jupyter Minimal Notebook from https://github.com/jupyter/docker-stacks", "latest": {"2025-11-20": "sha256:e87c3727bd85c6427b0ace27482acf42c873d90cc0381db3b68fabb684e0e5ba"}, "tags": {"latest": "sha256:e87c3727bd85c6427b0ace27482acf42c873d90cc0381db3b68fabb684e0e5ba", "2025-05-30": "sha256:b1e5df5d0147db361f004f898700feffc80a58d09bca567bb93395945a30a8a2", "2025-06-23": "sha256:5e4e24ca25cf1a76c322792fc7915d9839f216867da89f1a1e18e71c9279972a", "2025-08-18": "sha256:83b6d0b5da37638d0957f812a07707e4e25ce44227c64588395c124140f96831", "2025-09-23": "sha256:f5c19ac74a97d8ead52a494d3d1208aa35101f4ba02d2e03c80063e3b8dc129b", "2025-10-21": "sha256:5ce9db63d08e37ea4ff425e445d3a29e610bd2b031997d1a3cae0b835cfb5f03", "2025-09-15": "sha256:f4b1950fffd01fef0b46ed8b3a4cf790bb8d89a8a295d4b2ed2789199f69ef8a", "2025-08-25": "sha256:1de4c9a7e52c2268beb011fe4146a02dd78c42fd428f73147fa9cf13fd6dbc77", "2025-07-28": "sha256:8ba77869d9e10eb0d8544c8359416efbe4185e00e99489e40cb029ad79a6c11c", "2025-11-20": "sha256:e87c3727bd85c6427b0ace27482acf42c873d90cc0381db3b68fabb684e0e5ba", "2025-10-27": "sha256:291d59447816307a0d5deaa8bd6a322cce1194c4dbafe0521077c835be9ac7fc", "2025-09-30": "sha256:40d4175df5ccbf92e648d422d2a4fe511f373aa3e1b1c0404ac68f029463ea3b"}, "aliases": [{"name": "run-notebook", "command": "jupyter notebook --no-browser --port=$(shuf -i 2000-65000 -n 1) --ip 0.0.0.0"}]}
---

This module is a singularity container wrapper for quay.io/jupyter/minimal-notebook.
Jupyter Minimal Notebook from https://github.com/jupyter/docker-stacks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/jupyter/minimal-notebook
```

Or a specific version:

```bash
$ shpc install quay.io/jupyter/minimal-notebook:2025-11-20
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/jupyter/minimal-notebook/2025-11-20
$ module help quay.io/jupyter/minimal-notebook/2025-11-20
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### minimal-notebook-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### minimal-notebook-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### minimal-notebook-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### minimal-notebook-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### minimal-notebook-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### minimal-notebook-inspect-deffile:

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
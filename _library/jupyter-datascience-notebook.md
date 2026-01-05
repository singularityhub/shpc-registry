---
layout: container
name:  "jupyter/datascience-notebook"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/jupyter/datascience-notebook/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/jupyter/datascience-notebook/container.yaml"
updated_at: "2026-01-05 05:39:56.322589"
latest: "2023-10-20"
container_url: "https://hub.docker.com/r/jupyter/datascience-notebook"
aliases:
 - "run-notebook"
versions:
 - "latest"
 - "2023-01-15"
 - "2023-01-30"
 - "2023-02-13"
 - "2023-02-28"
 - "2023-03-13"
 - "2023-06-29"
 - "2023-07-31"
 - "2023-08-28"
 - "2023-09-25"
 - "2023-10-20"
description: "Jupyter Datascience Notebook from https://github.com/jupyter/docker-stacks (use quay.io/jupyter/datascience-notebook for recent versions)"
config: {"docker": "jupyter/datascience-notebook", "url": "https://hub.docker.com/r/jupyter/datascience-notebook", "maintainer": "@vsoch", "description": "Jupyter Datascience Notebook from https://github.com/jupyter/docker-stacks (use quay.io/jupyter/datascience-notebook for recent versions)", "latest": {"2023-10-20": "sha256:476c6e673e7d5d8b5059f8680b1c6a988942a79263da651bf302dc696ab311f2"}, "tags": {"latest": "sha256:476c6e673e7d5d8b5059f8680b1c6a988942a79263da651bf302dc696ab311f2", "2023-01-15": "sha256:f60e0309bf0dfa53efc6207c393ca6ffc0cfb1a5f94c01920fef98840384276d", "2023-01-30": "sha256:8488d97f786edee0c44bfc3e0b64dd7f6b743abbcd57b6bddbbcae0d68abc1e6", "2023-02-13": "sha256:ac852f6d705a1fc018d2aaf11549d898f436ec5a000a4a9296a65ee37790344e", "2023-02-28": "sha256:1ccab5f21fe947f3aa373f8c17287b3e9c5efc5e229bc77c28280e24d872ffb6", "2023-03-13": "sha256:d128d6577567375c17d0f90113f2f9ab1105268f14eabe6fcf782c9813eb61de", "2023-06-29": "sha256:4075458752a946c5721fa52b971f877fa348095a7c7c9acc874e89733b110493", "2023-07-31": "sha256:ca5b0ed14c07b0bae0a1a20e632abcff3fa7cf8c06df2e88fc0f28b4e3761b9d", "2023-08-28": "sha256:6926b9e2290b0e7db6ff3624ec79a992df2f6be4d208c2acdcc70019e6bf1626", "2023-09-25": "sha256:07c04aaed8e6aa1603887bc09dfd317580f38e219e9f660578a00f5acee45cff", "2023-10-20": "sha256:476c6e673e7d5d8b5059f8680b1c6a988942a79263da651bf302dc696ab311f2"}, "filter": ["2023-*"], "aliases": [{"name": "run-notebook", "command": "jupyter notebook --no-browser --port=$(shuf -i 2000-65000 -n 1) --ip 0.0.0.0"}]}
---

This module is a singularity container wrapper for jupyter/datascience-notebook.
Jupyter Datascience Notebook from https://github.com/jupyter/docker-stacks (use quay.io/jupyter/datascience-notebook for recent versions)
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install jupyter/datascience-notebook
```

Or a specific version:

```bash
$ shpc install jupyter/datascience-notebook:2023-10-20
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load jupyter/datascience-notebook/2023-10-20
$ module help jupyter/datascience-notebook/2023-10-20
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
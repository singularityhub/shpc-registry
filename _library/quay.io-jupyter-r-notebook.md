---
layout: container
name:  "quay.io/jupyter/r-notebook"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/jupyter/r-notebook/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/jupyter/r-notebook/container.yaml"
updated_at: "2025-12-22 05:04:48.173594"
latest: "2025-11-24"
container_url: "https://quay.io/repository/jupyter/r-notebook"
aliases:
 - "run-notebook"
versions:
 - "latest"
 - "2025-06-02"
 - "2025-06-23"
 - "2025-07-21"
 - "2025-06-30"
 - "2025-08-18"
 - "2025-07-07"
 - "2025-09-23"
 - "2025-10-21"
 - "2025-09-22"
 - "2025-08-25"
 - "2025-07-28"
 - "2025-11-24"
 - "2025-09-29"
description: "Jupyter R Notebook from https://github.com/jupyter/docker-stacks"
config: {"docker": "quay.io/jupyter/r-notebook", "url": "https://quay.io/repository/jupyter/r-notebook", "maintainer": "@HasseJohansen", "description": "Jupyter R Notebook from https://github.com/jupyter/docker-stacks", "latest": {"2025-11-24": "sha256:69560a6949e149bd1d4aeb5ccdc088e8dc1b4c74f0d31287e3747aa6776fc003"}, "tags": {"latest": "sha256:69560a6949e149bd1d4aeb5ccdc088e8dc1b4c74f0d31287e3747aa6776fc003", "2025-06-02": "sha256:1cfec8732d6b8eaf891e6b3ea1a6844e50a90a1bf3d012e7d463869efd713093", "2025-06-23": "sha256:0c2d79320666490af2f9da1b072d1a8ae54cb49fd314d32bdb15631140b01103", "2025-07-21": "sha256:1d1b8104db0d372fe5a069f9441919de28a481d7660dffb1522fa8ac704a025b", "2025-06-30": "sha256:6186d4db7cf4af13a473987bb59c0e0bbf9912b6b64b36b4ea25e7c3bc4a574a", "2025-08-18": "sha256:f486264bdbe74b906bcb7edb6ed19f6dfed50eb8a743720e59e8379e5f598e81", "2025-07-07": "sha256:9c054c26494cfbdd1e12db686d35e514fd760c2b81821a8794c8044fd301d77d", "2025-09-23": "sha256:e4ccb7dee3c6484216ee653a6ad407c9227a008289e5fe330b52c4c272013e3f", "2025-10-21": "sha256:121ed2f270eaeefe255138821fc6ff7fb4ea9be00e8b9789888c4cb042c2c654", "2025-09-22": "sha256:7ffa5c3fd9dd8454960035e6fbb68770ac5d8d6dac001dfddc5c3acf6fc34b86", "2025-08-25": "sha256:87cc45eba17dfd6a2ea43e79bee4a9e75f22bc37a6f098634bb4bdef45088306", "2025-07-28": "sha256:006007eb2f8613ad4c7b21f8f9ad3baba91e4ed28b879e1e40e2d027b2a0618c", "2025-11-24": "sha256:69560a6949e149bd1d4aeb5ccdc088e8dc1b4c74f0d31287e3747aa6776fc003", "2025-09-29": "sha256:d81e81da1975801c8a03e6c97469626a56d78188827f829b3ce68e729720c0fd"}, "aliases": [{"name": "run-notebook", "command": "jupyter notebook --no-browser --port=$(shuf -i 2000-65000 -n 1) --ip 0.0.0.0"}]}
---

This module is a singularity container wrapper for quay.io/jupyter/r-notebook.
Jupyter R Notebook from https://github.com/jupyter/docker-stacks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/jupyter/r-notebook
```

Or a specific version:

```bash
$ shpc install quay.io/jupyter/r-notebook:2025-11-24
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/jupyter/r-notebook/2025-11-24
$ module help quay.io/jupyter/r-notebook/2025-11-24
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-notebook-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-notebook-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-notebook-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-notebook-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-notebook-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-notebook-inspect-deffile:

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
---
layout: container
name:  "quay.io/biocontainers/bioconductor-g4snvhunter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-g4snvhunter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-g4snvhunter/container.yaml"
updated_at: "2026-03-23 04:43:22.524775"
latest: "1.2.0--r45ha27e39d_0"
container_url: "https://biocontainers.pro/tools/bioconductor-g4snvhunter"
aliases:
 - "x86_64-conda-linux-gnu.cfg"
 - "hb-info"
 - "tjbench"
versions:
 - "1.2.0--r45ha27e39d_0"
description: "singularity registry hpc automated addition for bioconductor-g4snvhunter"
config: {"url": "https://biocontainers.pro/tools/bioconductor-g4snvhunter", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-g4snvhunter", "latest": {"1.2.0--r45ha27e39d_0": "sha256:e1a79d6c79510dd475fa23803907c519794ca7367d2d12751836069bd0af7692"}, "tags": {"1.2.0--r45ha27e39d_0": "sha256:e1a79d6c79510dd475fa23803907c519794ca7367d2d12751836069bd0af7692"}, "docker": "quay.io/biocontainers/bioconductor-g4snvhunter", "aliases": {"x86_64-conda-linux-gnu.cfg": "/usr/local/bin/x86_64-conda-linux-gnu.cfg", "hb-info": "/usr/local/bin/hb-info", "tjbench": "/usr/local/bin/tjbench"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-g4snvhunter.
singularity registry hpc automated addition for bioconductor-g4snvhunter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-g4snvhunter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-g4snvhunter:1.2.0--r45ha27e39d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-g4snvhunter/1.2.0--r45ha27e39d_0
$ module help quay.io/biocontainers/bioconductor-g4snvhunter/1.2.0--r45ha27e39d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-g4snvhunter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-g4snvhunter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-g4snvhunter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-g4snvhunter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-g4snvhunter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-g4snvhunter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu.cfg

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu.cfg
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
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
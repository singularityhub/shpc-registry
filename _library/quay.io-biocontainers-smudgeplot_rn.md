---
layout: container
name:  "quay.io/biocontainers/smudgeplot_rn"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/smudgeplot_rn/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/smudgeplot_rn/container.yaml"
updated_at: "2025-09-08 03:34:22.192319"
latest: "0.2.5_RN--py313r44h7b50bb2_7"
container_url: "https://biocontainers.pro/tools/smudgeplot_rn"
aliases:
 - "smudgeplot.py"
 - "smudgeplot_plot.R"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
versions:
 - "0.2.5_RN--py310r41h779adbc_2"
 - "0.2.5_RN--py311r42hec16e2b_4"
 - "0.2.5_RN--py311r42h031d066_5"
 - "0.2.5_RN--py313r44h7b50bb2_7"
description: "shpc-registry automated BioContainers addition for smudgeplot_rn"
config: {"url": "https://biocontainers.pro/tools/smudgeplot_rn", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for smudgeplot_rn", "latest": {"0.2.5_RN--py313r44h7b50bb2_7": "sha256:5c9bf78beee27573d4c36d343c69499f41ee85e019a39c6c484b2d09d88a37d2"}, "tags": {"0.2.5_RN--py310r41h779adbc_2": "sha256:65153eb99b634041fe41c4ea1fe070367b2dc23ddae94d7fe260a95d28defefb", "0.2.5_RN--py311r42hec16e2b_4": "sha256:1a34e0b12d461a230a398c86c13b68520d8f8f42c32712ac7d58801212131b97", "0.2.5_RN--py311r42h031d066_5": "sha256:bf6bef3e8916d1e1427efee5f3aa6a3a047926bfab46b90487224e47bb3a4803", "0.2.5_RN--py313r44h7b50bb2_7": "sha256:5c9bf78beee27573d4c36d343c69499f41ee85e019a39c6c484b2d09d88a37d2"}, "docker": "quay.io/biocontainers/smudgeplot_rn", "aliases": {"smudgeplot.py": "/usr/local/bin/smudgeplot.py", "smudgeplot_plot.R": "/usr/local/bin/smudgeplot_plot.R", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/smudgeplot_rn.
shpc-registry automated BioContainers addition for smudgeplot_rn
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/smudgeplot_rn
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/smudgeplot_rn:0.2.5_RN--py313r44h7b50bb2_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/smudgeplot_rn/0.2.5_RN--py313r44h7b50bb2_7
$ module help quay.io/biocontainers/smudgeplot_rn/0.2.5_RN--py313r44h7b50bb2_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### smudgeplot_rn-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### smudgeplot_rn-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### smudgeplot_rn-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### smudgeplot_rn-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### smudgeplot_rn-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### smudgeplot_rn-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### smudgeplot.py

```bash
$ singularity exec <container> /usr/local/bin/smudgeplot.py
$ podman run --it --rm --entrypoint /usr/local/bin/smudgeplot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smudgeplot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smudgeplot_plot.R

```bash
$ singularity exec <container> /usr/local/bin/smudgeplot_plot.R
$ podman run --it --rm --entrypoint /usr/local/bin/smudgeplot_plot.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smudgeplot_plot.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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
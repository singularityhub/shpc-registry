---
layout: container
name:  "quay.io/biocontainers/pybigwig"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pybigwig/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pybigwig/container.yaml"
updated_at: "2025-05-08 05:30:35.744028"
latest: "0.3.24--py311hd8c7dd8_0"
container_url: "https://biocontainers.pro/tools/pybigwig"
aliases:
 - "2to3-3.5"
 - "idle3.5"
 - "pydoc3.5"
 - "python3.5"
 - "python3.5-config"
 - "python3.5m"
 - "python3.5m-config"
 - "pyvenv-3.5"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "0.3.9--np113py35_0"
 - "0.3.13--py37h92ddc84_1"
 - "0.3.22--py39h44c22c2_1"
 - "0.3.22--py38h5df1436_2"
 - "0.3.22--py312hfa7e9eb_3"
 - "0.3.23--py39h616c374_0"
 - "0.3.24--py311hd8c7dd8_0"
description: "shpc-registry automated BioContainers addition for pybigwig"
config: {"url": "https://biocontainers.pro/tools/pybigwig", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pybigwig", "latest": {"0.3.24--py311hd8c7dd8_0": "sha256:ca5ac92c2abe4983cd630f95dbeff8c359693e8ab7ba00e74ae0d5d7aa89acd9"}, "tags": {"0.3.9--np113py35_0": "sha256:0e824284363490ccb389b0d1eb417056508e806fea6d5c762494323e31e2ae2a", "0.3.13--py37h92ddc84_1": "sha256:e1e8966984ba022db918582e51c467e2665b651418c67a2dac411ad6e2756a43", "0.3.22--py39h44c22c2_1": "sha256:e0e1d048a89596448ae8e5978c2de3325cae4132be50bae8112bf1be34660203", "0.3.22--py38h5df1436_2": "sha256:9bf10b5c100a5a768a859d331826f5585d3b35ed1291693378d06cd2d3ec19d8", "0.3.22--py312hfa7e9eb_3": "sha256:c159ee717c118bc4cb8b8694e464bd364fad401bf2428a24e18129a23984b21e", "0.3.23--py39h616c374_0": "sha256:7440383ba51640b94ba6360e4c08b01cfb4aeb33c555807845fe352cec73e67e", "0.3.24--py311hd8c7dd8_0": "sha256:ca5ac92c2abe4983cd630f95dbeff8c359693e8ab7ba00e74ae0d5d7aa89acd9"}, "docker": "quay.io/biocontainers/pybigwig", "aliases": {"2to3-3.5": "/usr/local/bin/2to3-3.5", "idle3.5": "/usr/local/bin/idle3.5", "pydoc3.5": "/usr/local/bin/pydoc3.5", "python3.5": "/usr/local/bin/python3.5", "python3.5-config": "/usr/local/bin/python3.5-config", "python3.5m": "/usr/local/bin/python3.5m", "python3.5m-config": "/usr/local/bin/python3.5m-config", "pyvenv-3.5": "/usr/local/bin/pyvenv-3.5", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pybigwig.
shpc-registry automated BioContainers addition for pybigwig
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pybigwig
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pybigwig:0.3.24--py311hd8c7dd8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pybigwig/0.3.24--py311hd8c7dd8_0
$ module help quay.io/biocontainers/pybigwig/0.3.24--py311hd8c7dd8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pybigwig-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pybigwig-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pybigwig-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pybigwig-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pybigwig-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pybigwig-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.5

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.5
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.5

```bash
$ singularity exec <container> /usr/local/bin/idle3.5
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.5

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.5
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.5

```bash
$ singularity exec <container> /usr/local/bin/python3.5
$ podman run --it --rm --entrypoint /usr/local/bin/python3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.5-config

```bash
$ singularity exec <container> /usr/local/bin/python3.5-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.5m

```bash
$ singularity exec <container> /usr/local/bin/python3.5m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.5m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.5m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.5m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.5m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.5m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.5m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.5

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.5
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncurses5-config

```bash
$ singularity exec <container> /usr/local/bin/ncurses5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncursesw5-config

```bash
$ singularity exec <container> /usr/local/bin/ncursesw5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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
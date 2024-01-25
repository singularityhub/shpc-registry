---
layout: container
name:  "quay.io/biocontainers/smudgeplot"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/smudgeplot/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/smudgeplot/container.yaml"
updated_at: "2024-01-25 02:36:10.659961"
latest: "0.2.5--py38r42he5da3d1_3"
container_url: "https://biocontainers.pro/tools/smudgeplot"
aliases:
 - "smudgeplot.py"
 - "smudgeplot_plot.R"
 - "f2py3.8"
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
versions:
 - "0.2.5--py38r41hbff2b2d_0"
 - "0.2.5--py38r42hbff2b2d_1"
 - "0.2.5--py38r42he5da3d1_3"
description: "shpc-registry automated BioContainers addition for smudgeplot"
config: {"url": "https://biocontainers.pro/tools/smudgeplot", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for smudgeplot", "latest": {"0.2.5--py38r42he5da3d1_3": "sha256:3713fc0d0491334c6e65598dde03b78a1ed065bcda64bffdf8338f0b6c66ab27"}, "tags": {"0.2.5--py38r41hbff2b2d_0": "sha256:9e47c3550abc185291a5466bc5137d4f5f711bb258f3363fe6fe6129ba2c8b62", "0.2.5--py38r42hbff2b2d_1": "sha256:b7b1f193b1ed0ab39de60086f6e892cfa415253d233576fef27db493cdf639ba", "0.2.5--py38r42he5da3d1_3": "sha256:3713fc0d0491334c6e65598dde03b78a1ed065bcda64bffdf8338f0b6c66ab27"}, "docker": "quay.io/biocontainers/smudgeplot", "aliases": {"smudgeplot.py": "/usr/local/bin/smudgeplot.py", "smudgeplot_plot.R": "/usr/local/bin/smudgeplot_plot.R", "f2py3.8": "/usr/local/bin/f2py3.8", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/smudgeplot.
shpc-registry automated BioContainers addition for smudgeplot
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/smudgeplot
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/smudgeplot:0.2.5--py38r42he5da3d1_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/smudgeplot/0.2.5--py38r42he5da3d1_3
$ module help quay.io/biocontainers/smudgeplot/0.2.5--py38r42he5da3d1_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### smudgeplot-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### smudgeplot-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### smudgeplot-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### smudgeplot-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### smudgeplot-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### smudgeplot-inspect-deffile:

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


#### f2py3.8

```bash
$ singularity exec <container> /usr/local/bin/f2py3.8
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.8

```bash
$ singularity exec <container> /usr/local/bin/idle3.8
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.8

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.8
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8

```bash
$ singularity exec <container> /usr/local/bin/python3.8
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8-config

```bash
$ singularity exec <container> /usr/local/bin/python3.8-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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
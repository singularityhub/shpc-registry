---
layout: container
name:  "quay.io/biocontainers/treemix"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/treemix/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/treemix/container.yaml"
updated_at: "2024-03-07 02:50:17.609086"
latest: "1.13--hf961e7c_8"
container_url: "https://biocontainers.pro/tools/treemix"
aliases:
 - "f4ratio"
 - "fourpop"
 - "plotting_funcs.R"
 - "threepop"
 - "treemix"
 - "2to3-3.6"
 - "idle3.6"
 - "pydoc3.6"
 - "python3.6"
 - "python3.6-config"
 - "python3.6m"
 - "python3.6m-config"
 - "pyvenv-3.6"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.13--boost1.64_gsl2.2_0"
 - "1.13--hc564dbc_6"
 - "1.13--hf961e7c_8"
description: "shpc-registry automated BioContainers addition for treemix"
config: {"url": "https://biocontainers.pro/tools/treemix", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for treemix", "latest": {"1.13--hf961e7c_8": "sha256:eae67acfb6bd3099c6125b7d94296e796b3274a6b03432014cdccbc2ca70b059"}, "tags": {"1.13--boost1.64_gsl2.2_0": "sha256:49b7b2234549b331adf8c1af85707b99c4c902b521799052ef60c1c0e4e78779", "1.13--hc564dbc_6": "sha256:d8b1c1fa1b228e52ed4feb9e96b044d5ff3f776e9b0951affc1ae71fe8849129", "1.13--hf961e7c_8": "sha256:eae67acfb6bd3099c6125b7d94296e796b3274a6b03432014cdccbc2ca70b059"}, "docker": "quay.io/biocontainers/treemix", "aliases": {"f4ratio": "/usr/local/bin/f4ratio", "fourpop": "/usr/local/bin/fourpop", "plotting_funcs.R": "/usr/local/bin/plotting_funcs.R", "threepop": "/usr/local/bin/threepop", "treemix": "/usr/local/bin/treemix", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6", "pydoc3.6": "/usr/local/bin/pydoc3.6", "python3.6": "/usr/local/bin/python3.6", "python3.6-config": "/usr/local/bin/python3.6-config", "python3.6m": "/usr/local/bin/python3.6m", "python3.6m-config": "/usr/local/bin/python3.6m-config", "pyvenv-3.6": "/usr/local/bin/pyvenv-3.6", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/treemix.
shpc-registry automated BioContainers addition for treemix
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/treemix
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/treemix:1.13--hf961e7c_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/treemix/1.13--hf961e7c_8
$ module help quay.io/biocontainers/treemix/1.13--hf961e7c_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### treemix-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### treemix-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### treemix-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### treemix-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### treemix-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### treemix-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### f4ratio

```bash
$ singularity exec <container> /usr/local/bin/f4ratio
$ podman run --it --rm --entrypoint /usr/local/bin/f4ratio   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f4ratio   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fourpop

```bash
$ singularity exec <container> /usr/local/bin/fourpop
$ podman run --it --rm --entrypoint /usr/local/bin/fourpop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fourpop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotting_funcs.R

```bash
$ singularity exec <container> /usr/local/bin/plotting_funcs.R
$ podman run --it --rm --entrypoint /usr/local/bin/plotting_funcs.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotting_funcs.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### threepop

```bash
$ singularity exec <container> /usr/local/bin/threepop
$ podman run --it --rm --entrypoint /usr/local/bin/threepop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/threepop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### treemix

```bash
$ singularity exec <container> /usr/local/bin/treemix
$ podman run --it --rm --entrypoint /usr/local/bin/treemix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/treemix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.6

```bash
$ singularity exec <container> /usr/local/bin/idle3.6
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.6

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6

```bash
$ singularity exec <container> /usr/local/bin/python3.6
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m

```bash
$ singularity exec <container> /usr/local/bin/python3.6m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.6

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
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
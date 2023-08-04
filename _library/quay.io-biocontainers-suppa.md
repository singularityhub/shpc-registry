---
layout: container
name:  "quay.io/biocontainers/suppa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/suppa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/suppa/container.yaml"
updated_at: "2023-08-04 02:45:16.848057"
latest: "2.3--py_2"
container_url: "https://biocontainers.pro/tools/suppa"
aliases:
 - "eventClusterer.py"
 - "eventGenerator.py"
 - "fileMerger.py"
 - "multipleFieldSelection.py"
 - "psiCalculator.py"
 - "psiPerGene.py"
 - "significanceCalculator.py"
 - "suppa.py"
 - "f2py3.7"
 - "2to3-3.7"
 - "idle3.7"
 - "pydoc3.7"
 - "python3.7"
 - "python3.7-config"
 - "python3.7m"
 - "python3.7m-config"
 - "pyvenv-3.7"
 - "pyvenv"
versions:
 - "2.3--py_2"
description: "shpc-registry automated BioContainers addition for suppa"
config: {"url": "https://biocontainers.pro/tools/suppa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for suppa", "latest": {"2.3--py_2": "sha256:3dadbfa11b5ca40d1980c31ccc56139be261fc614b83954ae4086a7cb70454a0"}, "tags": {"2.3--py_2": "sha256:3dadbfa11b5ca40d1980c31ccc56139be261fc614b83954ae4086a7cb70454a0"}, "docker": "quay.io/biocontainers/suppa", "aliases": {"eventClusterer.py": "/usr/local/bin/eventClusterer.py", "eventGenerator.py": "/usr/local/bin/eventGenerator.py", "fileMerger.py": "/usr/local/bin/fileMerger.py", "multipleFieldSelection.py": "/usr/local/bin/multipleFieldSelection.py", "psiCalculator.py": "/usr/local/bin/psiCalculator.py", "psiPerGene.py": "/usr/local/bin/psiPerGene.py", "significanceCalculator.py": "/usr/local/bin/significanceCalculator.py", "suppa.py": "/usr/local/bin/suppa.py", "f2py3.7": "/usr/local/bin/f2py3.7", "2to3-3.7": "/usr/local/bin/2to3-3.7", "idle3.7": "/usr/local/bin/idle3.7", "pydoc3.7": "/usr/local/bin/pydoc3.7", "python3.7": "/usr/local/bin/python3.7", "python3.7-config": "/usr/local/bin/python3.7-config", "python3.7m": "/usr/local/bin/python3.7m", "python3.7m-config": "/usr/local/bin/python3.7m-config", "pyvenv-3.7": "/usr/local/bin/pyvenv-3.7", "pyvenv": "/usr/local/bin/pyvenv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/suppa.
shpc-registry automated BioContainers addition for suppa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/suppa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/suppa:2.3--py_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/suppa/2.3--py_2
$ module help quay.io/biocontainers/suppa/2.3--py_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### suppa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### suppa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### suppa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### suppa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### suppa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### suppa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### eventClusterer.py

```bash
$ singularity exec <container> /usr/local/bin/eventClusterer.py
$ podman run --it --rm --entrypoint /usr/local/bin/eventClusterer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eventClusterer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eventGenerator.py

```bash
$ singularity exec <container> /usr/local/bin/eventGenerator.py
$ podman run --it --rm --entrypoint /usr/local/bin/eventGenerator.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eventGenerator.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fileMerger.py

```bash
$ singularity exec <container> /usr/local/bin/fileMerger.py
$ podman run --it --rm --entrypoint /usr/local/bin/fileMerger.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fileMerger.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multipleFieldSelection.py

```bash
$ singularity exec <container> /usr/local/bin/multipleFieldSelection.py
$ podman run --it --rm --entrypoint /usr/local/bin/multipleFieldSelection.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multipleFieldSelection.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psiCalculator.py

```bash
$ singularity exec <container> /usr/local/bin/psiCalculator.py
$ podman run --it --rm --entrypoint /usr/local/bin/psiCalculator.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psiCalculator.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psiPerGene.py

```bash
$ singularity exec <container> /usr/local/bin/psiPerGene.py
$ podman run --it --rm --entrypoint /usr/local/bin/psiPerGene.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psiPerGene.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### significanceCalculator.py

```bash
$ singularity exec <container> /usr/local/bin/significanceCalculator.py
$ podman run --it --rm --entrypoint /usr/local/bin/significanceCalculator.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/significanceCalculator.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### suppa.py

```bash
$ singularity exec <container> /usr/local/bin/suppa.py
$ podman run --it --rm --entrypoint /usr/local/bin/suppa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/suppa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.7

```bash
$ singularity exec <container> /usr/local/bin/f2py3.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.7

```bash
$ singularity exec <container> /usr/local/bin/idle3.7
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.7

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.7
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7

```bash
$ singularity exec <container> /usr/local/bin/python3.7
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7-config

```bash
$ singularity exec <container> /usr/local/bin/python3.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7m

```bash
$ singularity exec <container> /usr/local/bin/python3.7m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.7m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.7

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv

```bash
$ singularity exec <container> /usr/local/bin/pyvenv
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
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
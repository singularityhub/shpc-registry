---
layout: container
name:  "quay.io/biocontainers/spades"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/spades/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/spades/container.yaml"
updated_at: "2022-10-29 05:38:27.412782"
latest: "3.9.1--h9ee0642_1"
container_url: "https://biocontainers.pro/tools/spades"
aliases:
 - "bwa-spades"
 - "corrector"
 - "dipspades"
 - "dipspades.py"
 - "hammer"
 - "ionhammer"
 - "scaffold_correction"
 - "spades"
 - "2to3-3.5"
 - "idle3.5"
 - "metaspades.py"
 - "plasmidspades.py"
 - "pydoc3.5"
 - "python3.5"
 - "python3.5-config"
 - "python3.5m"
 - "python3.5m-config"
 - "pyvenv-3.5"
versions:
 - "3.15.0--h633aebb_0"
 - "3.15.2--h95f258a_1"
 - "3.15.3--h95f258a_0"
 - "3.15.4--h95f258a_0"
 - "3.9.1--h9ee0642_1"
description: "shpc-registry automated BioContainers addition for spades"
config: {"docker": "quay.io/biocontainers/spades", "url": "https://biocontainers.pro/tools/spades", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for spades", "latest": {"3.9.1--h9ee0642_1": "sha256:fd23ddfae841eb045747193287761e61c8874e970c621803f22e9be936c2c2ab"}, "tags": {"3.15.0--h633aebb_0": "sha256:4cc7e41f53d3effb25b59afedc3fbd2d3e08fff449a507ecfa6731ff6d81ff79", "3.15.2--h95f258a_1": "sha256:250657af71d37fafdff81af644e92bf84485d4d9b6894f58ff84efdc1a6ec9eb", "3.15.3--h95f258a_0": "sha256:a5cb2eb2740fdba4902e541c50307c7958b3b0824be2904323319eb275b256c7", "3.15.4--h95f258a_0": "sha256:7dfda44ae2535ba1ccc7c60c2ec265f8672cfd45885f458a964daf1b839a7ec1", "3.9.1--h9ee0642_1": "sha256:fd23ddfae841eb045747193287761e61c8874e970c621803f22e9be936c2c2ab"}, "aliases": {"bwa-spades": "/usr/local/bin/bwa-spades", "corrector": "/usr/local/bin/corrector", "dipspades": "/usr/local/bin/dipspades", "dipspades.py": "/usr/local/bin/dipspades.py", "hammer": "/usr/local/bin/hammer", "ionhammer": "/usr/local/bin/ionhammer", "scaffold_correction": "/usr/local/bin/scaffold_correction", "spades": "/usr/local/bin/spades", "2to3-3.5": "/usr/local/bin/2to3-3.5", "idle3.5": "/usr/local/bin/idle3.5", "metaspades.py": "/usr/local/bin/metaspades.py", "plasmidspades.py": "/usr/local/bin/plasmidspades.py", "pydoc3.5": "/usr/local/bin/pydoc3.5", "python3.5": "/usr/local/bin/python3.5", "python3.5-config": "/usr/local/bin/python3.5-config", "python3.5m": "/usr/local/bin/python3.5m", "python3.5m-config": "/usr/local/bin/python3.5m-config", "pyvenv-3.5": "/usr/local/bin/pyvenv-3.5"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/spades.
shpc-registry automated BioContainers addition for spades
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/spades
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/spades:3.15.0--h633aebb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/spades/3.15.0--h633aebb_0
$ module help quay.io/biocontainers/spades/3.15.0--h633aebb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### spades-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### spades-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### spades-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### spades-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### spades-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### spades-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bwa-spades

```bash
$ singularity exec <container> /usr/local/bin/bwa-spades
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-spades   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-spades   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### corrector

```bash
$ singularity exec <container> /usr/local/bin/corrector
$ podman run --it --rm --entrypoint /usr/local/bin/corrector   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/corrector   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dipspades

```bash
$ singularity exec <container> /usr/local/bin/dipspades
$ podman run --it --rm --entrypoint /usr/local/bin/dipspades   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dipspades   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dipspades.py

```bash
$ singularity exec <container> /usr/local/bin/dipspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/dipspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dipspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hammer

```bash
$ singularity exec <container> /usr/local/bin/hammer
$ podman run --it --rm --entrypoint /usr/local/bin/hammer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hammer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ionhammer

```bash
$ singularity exec <container> /usr/local/bin/ionhammer
$ podman run --it --rm --entrypoint /usr/local/bin/ionhammer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ionhammer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scaffold_correction

```bash
$ singularity exec <container> /usr/local/bin/scaffold_correction
$ podman run --it --rm --entrypoint /usr/local/bin/scaffold_correction   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scaffold_correction   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades

```bash
$ singularity exec <container> /usr/local/bin/spades
$ podman run --it --rm --entrypoint /usr/local/bin/spades   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### metaspades.py

```bash
$ singularity exec <container> /usr/local/bin/metaspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plasmidspades.py

```bash
$ singularity exec <container> /usr/local/bin/plasmidspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/plasmidspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plasmidspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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
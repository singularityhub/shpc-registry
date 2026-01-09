---
layout: container
name:  "quay.io/biocontainers/pastrami"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pastrami/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pastrami/container.yaml"
updated_at: "2026-01-09 04:28:00.315122"
latest: "1.0.1--pyh67a8953_0"
container_url: "https://biocontainers.pro/tools/pastrami"
aliases:
 - "pastrami.py"
 - "pathos_connect"
 - "plink2"
 - "portpicker"
 - "pox"
 - "ppserver"
 - "get_objgraph"
 - "undill"
 - "f2py3.11"
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "normalizer"
 - "python3.1"
versions:
 - "0.9.6--pyhdfd78af_0"
 - "1.0.0--pyh67a8953_0"
 - "1.0.1--pyh67a8953_0"
description: "singularity registry hpc automated addition for pastrami"
config: {"url": "https://biocontainers.pro/tools/pastrami", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pastrami", "latest": {"1.0.1--pyh67a8953_0": "sha256:11f07eec7b21c97795656686d05553f5a27e557b41df7360fe0bfe3786dcbdd9"}, "tags": {"0.9.6--pyhdfd78af_0": "sha256:1d84add1a8456f1d981435406ee06b64b42fd85ee3dee037fc5e7b0981805bd2", "1.0.0--pyh67a8953_0": "sha256:56034fc83d62abbe07f1efe458e1c52837eee99f21d8753ca0ed73845f5a5243", "1.0.1--pyh67a8953_0": "sha256:11f07eec7b21c97795656686d05553f5a27e557b41df7360fe0bfe3786dcbdd9"}, "docker": "quay.io/biocontainers/pastrami", "aliases": {"pastrami.py": "/usr/local/bin/pastrami.py", "pathos_connect": "/usr/local/bin/pathos_connect", "plink2": "/usr/local/bin/plink2", "portpicker": "/usr/local/bin/portpicker", "pox": "/usr/local/bin/pox", "ppserver": "/usr/local/bin/ppserver", "get_objgraph": "/usr/local/bin/get_objgraph", "undill": "/usr/local/bin/undill", "f2py3.11": "/usr/local/bin/f2py3.11", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "normalizer": "/usr/local/bin/normalizer", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pastrami.
singularity registry hpc automated addition for pastrami
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pastrami
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pastrami:1.0.1--pyh67a8953_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pastrami/1.0.1--pyh67a8953_0
$ module help quay.io/biocontainers/pastrami/1.0.1--pyh67a8953_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pastrami-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pastrami-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pastrami-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pastrami-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pastrami-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pastrami-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pastrami.py

```bash
$ singularity exec <container> /usr/local/bin/pastrami.py
$ podman run --it --rm --entrypoint /usr/local/bin/pastrami.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pastrami.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pathos_connect

```bash
$ singularity exec <container> /usr/local/bin/pathos_connect
$ podman run --it --rm --entrypoint /usr/local/bin/pathos_connect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pathos_connect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plink2

```bash
$ singularity exec <container> /usr/local/bin/plink2
$ podman run --it --rm --entrypoint /usr/local/bin/plink2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plink2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### portpicker

```bash
$ singularity exec <container> /usr/local/bin/portpicker
$ podman run --it --rm --entrypoint /usr/local/bin/portpicker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/portpicker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pox

```bash
$ singularity exec <container> /usr/local/bin/pox
$ podman run --it --rm --entrypoint /usr/local/bin/pox   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pox   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ppserver

```bash
$ singularity exec <container> /usr/local/bin/ppserver
$ podman run --it --rm --entrypoint /usr/local/bin/ppserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ppserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_objgraph

```bash
$ singularity exec <container> /usr/local/bin/get_objgraph
$ podman run --it --rm --entrypoint /usr/local/bin/get_objgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_objgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### undill

```bash
$ singularity exec <container> /usr/local/bin/undill
$ podman run --it --rm --entrypoint /usr/local/bin/undill   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/undill   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.11

```bash
$ singularity exec <container> /usr/local/bin/f2py3.11
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.11

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.11
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.11

```bash
$ singularity exec <container> /usr/local/bin/idle3.11
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.11

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.11
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11

```bash
$ singularity exec <container> /usr/local/bin/python3.11
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11-config

```bash
$ singularity exec <container> /usr/local/bin/python3.11-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
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
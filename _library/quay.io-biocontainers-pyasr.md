---
layout: container
name:  "quay.io/biocontainers/pyasr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pyasr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pyasr/container.yaml"
updated_at: "2024-07-07 03:16:51.842805"
latest: "0.6.1--py_0"
container_url: "https://biocontainers.pro/tools/pyasr"
aliases:
 - "sumlabels.py"
 - "sumtrees.py"
 - "2to3-3.6"
 - "idle3.6"
 - "pydoc3.6"
 - "python3.6"
 - "python3.6-config"
 - "python3.6m"
 - "python3.6m-config"
 - "pyvenv-3.6"
versions:
 - "0.6.1--py_0"
description: "shpc-registry automated BioContainers addition for pyasr"
config: {"url": "https://biocontainers.pro/tools/pyasr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pyasr", "latest": {"0.6.1--py_0": "sha256:2feb7cf6cea3df644af72a9a46c1b68e4847aab070262f25bef25700956c6199"}, "tags": {"0.6.1--py_0": "sha256:2feb7cf6cea3df644af72a9a46c1b68e4847aab070262f25bef25700956c6199"}, "docker": "quay.io/biocontainers/pyasr", "aliases": {"sumlabels.py": "/usr/local/bin/sumlabels.py", "sumtrees.py": "/usr/local/bin/sumtrees.py", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6", "pydoc3.6": "/usr/local/bin/pydoc3.6", "python3.6": "/usr/local/bin/python3.6", "python3.6-config": "/usr/local/bin/python3.6-config", "python3.6m": "/usr/local/bin/python3.6m", "python3.6m-config": "/usr/local/bin/python3.6m-config", "pyvenv-3.6": "/usr/local/bin/pyvenv-3.6"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pyasr.
shpc-registry automated BioContainers addition for pyasr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pyasr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pyasr:0.6.1--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pyasr/0.6.1--py_0
$ module help quay.io/biocontainers/pyasr/0.6.1--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pyasr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pyasr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pyasr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pyasr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pyasr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pyasr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sumlabels.py

```bash
$ singularity exec <container> /usr/local/bin/sumlabels.py
$ podman run --it --rm --entrypoint /usr/local/bin/sumlabels.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sumlabels.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sumtrees.py

```bash
$ singularity exec <container> /usr/local/bin/sumtrees.py
$ podman run --it --rm --entrypoint /usr/local/bin/sumtrees.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sumtrees.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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
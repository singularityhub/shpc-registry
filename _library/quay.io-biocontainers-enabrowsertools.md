---
layout: container
name:  "quay.io/biocontainers/enabrowsertools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/enabrowsertools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/enabrowsertools/container.yaml"
updated_at: "2025-05-15 04:24:21.144179"
latest: "1.5.4--0"
container_url: "https://biocontainers.pro/tools/enabrowsertools"
aliases:
 - "assemblyGet.py"
 - "enaDataGet"
 - "enaDataGet.py"
 - "enaGroupGet"
 - "enaGroupGet.py"
 - "readGet.py"
 - "sequenceGet.py"
 - "utils.py"
 - "utils_py2.py"
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
 - "1.5.4--0"
description: "shpc-registry automated BioContainers addition for enabrowsertools"
config: {"url": "https://biocontainers.pro/tools/enabrowsertools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for enabrowsertools", "latest": {"1.5.4--0": "sha256:794a909aec3167fd4d143f6a3c05d8e465a45d635501856b2d3a1919b923ee1c"}, "tags": {"1.5.4--0": "sha256:794a909aec3167fd4d143f6a3c05d8e465a45d635501856b2d3a1919b923ee1c"}, "docker": "quay.io/biocontainers/enabrowsertools", "aliases": {"assemblyGet.py": "/usr/local/bin/assemblyGet.py", "enaDataGet": "/usr/local/bin/enaDataGet", "enaDataGet.py": "/usr/local/bin/enaDataGet.py", "enaGroupGet": "/usr/local/bin/enaGroupGet", "enaGroupGet.py": "/usr/local/bin/enaGroupGet.py", "readGet.py": "/usr/local/bin/readGet.py", "sequenceGet.py": "/usr/local/bin/sequenceGet.py", "utils.py": "/usr/local/bin/utils.py", "utils_py2.py": "/usr/local/bin/utils_py2.py", "2to3-3.7": "/usr/local/bin/2to3-3.7", "idle3.7": "/usr/local/bin/idle3.7", "pydoc3.7": "/usr/local/bin/pydoc3.7", "python3.7": "/usr/local/bin/python3.7", "python3.7-config": "/usr/local/bin/python3.7-config", "python3.7m": "/usr/local/bin/python3.7m", "python3.7m-config": "/usr/local/bin/python3.7m-config", "pyvenv-3.7": "/usr/local/bin/pyvenv-3.7", "pyvenv": "/usr/local/bin/pyvenv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/enabrowsertools.
shpc-registry automated BioContainers addition for enabrowsertools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/enabrowsertools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/enabrowsertools:1.5.4--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/enabrowsertools/1.5.4--0
$ module help quay.io/biocontainers/enabrowsertools/1.5.4--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### enabrowsertools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### enabrowsertools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### enabrowsertools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### enabrowsertools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### enabrowsertools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### enabrowsertools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### assemblyGet.py

```bash
$ singularity exec <container> /usr/local/bin/assemblyGet.py
$ podman run --it --rm --entrypoint /usr/local/bin/assemblyGet.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/assemblyGet.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### enaDataGet

```bash
$ singularity exec <container> /usr/local/bin/enaDataGet
$ podman run --it --rm --entrypoint /usr/local/bin/enaDataGet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/enaDataGet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### enaDataGet.py

```bash
$ singularity exec <container> /usr/local/bin/enaDataGet.py
$ podman run --it --rm --entrypoint /usr/local/bin/enaDataGet.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/enaDataGet.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### enaGroupGet

```bash
$ singularity exec <container> /usr/local/bin/enaGroupGet
$ podman run --it --rm --entrypoint /usr/local/bin/enaGroupGet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/enaGroupGet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### enaGroupGet.py

```bash
$ singularity exec <container> /usr/local/bin/enaGroupGet.py
$ podman run --it --rm --entrypoint /usr/local/bin/enaGroupGet.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/enaGroupGet.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### readGet.py

```bash
$ singularity exec <container> /usr/local/bin/readGet.py
$ podman run --it --rm --entrypoint /usr/local/bin/readGet.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/readGet.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sequenceGet.py

```bash
$ singularity exec <container> /usr/local/bin/sequenceGet.py
$ podman run --it --rm --entrypoint /usr/local/bin/sequenceGet.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sequenceGet.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### utils.py

```bash
$ singularity exec <container> /usr/local/bin/utils.py
$ podman run --it --rm --entrypoint /usr/local/bin/utils.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/utils.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### utils_py2.py

```bash
$ singularity exec <container> /usr/local/bin/utils_py2.py
$ podman run --it --rm --entrypoint /usr/local/bin/utils_py2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/utils_py2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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
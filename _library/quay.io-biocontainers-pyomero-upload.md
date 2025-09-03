---
layout: container
name:  "quay.io/biocontainers/pyomero-upload"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pyomero-upload/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pyomero-upload/container.yaml"
updated_at: "2025-09-03 03:07:46.025870"
latest: "5.6.2_2.2.0--py_0"
container_url: "https://biocontainers.pro/tools/pyomero-upload"
aliases:
 - "omero"
 - "omero.bat"
 - "setpythonpath.bat"
 - "slice2py"
 - "winconfig.bat"
 - "futurize"
 - "pasteurize"
 - "f2py3.7"
 - "chardetect"
 - "2to3-3.7"
 - "idle3.7"
 - "pydoc3.7"
 - "python3.7"
 - "python3.7-config"
 - "python3.7m"
versions:
 - "5.6.2_2.2.0--py_0"
description: "shpc-registry automated BioContainers addition for pyomero-upload"
config: {"url": "https://biocontainers.pro/tools/pyomero-upload", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pyomero-upload", "latest": {"5.6.2_2.2.0--py_0": "sha256:a93203020efcf69d4f457cab7023e7b6ebb0f37c036d9d9299770afaa8bea246"}, "tags": {"5.6.2_2.2.0--py_0": "sha256:a93203020efcf69d4f457cab7023e7b6ebb0f37c036d9d9299770afaa8bea246"}, "docker": "quay.io/biocontainers/pyomero-upload", "aliases": {"omero": "/usr/local/bin/omero", "omero.bat": "/usr/local/bin/omero.bat", "setpythonpath.bat": "/usr/local/bin/setpythonpath.bat", "slice2py": "/usr/local/bin/slice2py", "winconfig.bat": "/usr/local/bin/winconfig.bat", "futurize": "/usr/local/bin/futurize", "pasteurize": "/usr/local/bin/pasteurize", "f2py3.7": "/usr/local/bin/f2py3.7", "chardetect": "/usr/local/bin/chardetect", "2to3-3.7": "/usr/local/bin/2to3-3.7", "idle3.7": "/usr/local/bin/idle3.7", "pydoc3.7": "/usr/local/bin/pydoc3.7", "python3.7": "/usr/local/bin/python3.7", "python3.7-config": "/usr/local/bin/python3.7-config", "python3.7m": "/usr/local/bin/python3.7m"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pyomero-upload.
shpc-registry automated BioContainers addition for pyomero-upload
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pyomero-upload
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pyomero-upload:5.6.2_2.2.0--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pyomero-upload/5.6.2_2.2.0--py_0
$ module help quay.io/biocontainers/pyomero-upload/5.6.2_2.2.0--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pyomero-upload-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pyomero-upload-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pyomero-upload-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pyomero-upload-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pyomero-upload-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pyomero-upload-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### omero

```bash
$ singularity exec <container> /usr/local/bin/omero
$ podman run --it --rm --entrypoint /usr/local/bin/omero   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/omero   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### omero.bat

```bash
$ singularity exec <container> /usr/local/bin/omero.bat
$ podman run --it --rm --entrypoint /usr/local/bin/omero.bat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/omero.bat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setpythonpath.bat

```bash
$ singularity exec <container> /usr/local/bin/setpythonpath.bat
$ podman run --it --rm --entrypoint /usr/local/bin/setpythonpath.bat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setpythonpath.bat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### slice2py

```bash
$ singularity exec <container> /usr/local/bin/slice2py
$ podman run --it --rm --entrypoint /usr/local/bin/slice2py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slice2py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### winconfig.bat

```bash
$ singularity exec <container> /usr/local/bin/winconfig.bat
$ podman run --it --rm --entrypoint /usr/local/bin/winconfig.bat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/winconfig.bat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### futurize

```bash
$ singularity exec <container> /usr/local/bin/futurize
$ podman run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pasteurize

```bash
$ singularity exec <container> /usr/local/bin/pasteurize
$ podman run --it --rm --entrypoint /usr/local/bin/pasteurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pasteurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.7

```bash
$ singularity exec <container> /usr/local/bin/f2py3.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
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
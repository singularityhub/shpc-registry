---
layout: container
name:  "quay.io/biocontainers/idr-py"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/idr-py/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/idr-py/container.yaml"
updated_at: "2022-10-27 00:21:22.178682"
latest: "0.4.2--py_0"
container_url: "https://biocontainers.pro/tools/idr-py"
aliases:
 - "omero"
 - "omero.bat"
 - "setpythonpath.bat"
 - "slice2py"
 - "winconfig.bat"
versions:
 - "0.4.2--py_0"
description: "shpc-registry automated BioContainers addition for idr-py"
config: {"url": "https://biocontainers.pro/tools/idr-py", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for idr-py", "latest": {"0.4.2--py_0": "sha256:d1b3cd1be9d9b716de992e402caa561ac98df95d4b65831a93470d448fbe7c80"}, "tags": {"0.4.2--py_0": "sha256:d1b3cd1be9d9b716de992e402caa561ac98df95d4b65831a93470d448fbe7c80"}, "docker": "quay.io/biocontainers/idr-py", "aliases": {"omero": "/usr/local/bin/omero", "omero.bat": "/usr/local/bin/omero.bat", "setpythonpath.bat": "/usr/local/bin/setpythonpath.bat", "slice2py": "/usr/local/bin/slice2py", "winconfig.bat": "/usr/local/bin/winconfig.bat"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/idr-py.
shpc-registry automated BioContainers addition for idr-py
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/idr-py
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/idr-py:0.4.2--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/idr-py/0.4.2--py_0
$ module help quay.io/biocontainers/idr-py/0.4.2--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### idr-py-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### idr-py-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### idr-py-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### idr-py-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### idr-py-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### idr-py-inspect-deffile:

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
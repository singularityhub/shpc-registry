---
layout: container
name:  "quay.io/biocontainers/fwdpy11"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fwdpy11/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fwdpy11/container.yaml"
updated_at: "2023-06-26 03:23:12.085934"
latest: "0.6.3--py36h7d13203_0"
container_url: "https://biocontainers.pro/tools/fwdpy11"
aliases:
 - "tskit"
 - "numba"
 - "pycc"
 - "f2py3.6"
 - "jsonschema"
 - "2to3-3.6"
 - "idle3.6"
 - "pydoc3.6"
 - "python3.6"
 - "python3.6-config"
 - "python3.6m"
versions:
 - "0.6.3--py36h7d13203_0"
description: "shpc-registry automated BioContainers addition for fwdpy11"
config: {"url": "https://biocontainers.pro/tools/fwdpy11", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fwdpy11", "latest": {"0.6.3--py36h7d13203_0": "sha256:cbffbbec5c22c11bb9895a922aa215b028abe9b76140c68f2e308ec87c289a2e"}, "tags": {"0.6.3--py36h7d13203_0": "sha256:cbffbbec5c22c11bb9895a922aa215b028abe9b76140c68f2e308ec87c289a2e"}, "docker": "quay.io/biocontainers/fwdpy11", "aliases": {"tskit": "/usr/local/bin/tskit", "numba": "/usr/local/bin/numba", "pycc": "/usr/local/bin/pycc", "f2py3.6": "/usr/local/bin/f2py3.6", "jsonschema": "/usr/local/bin/jsonschema", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6", "pydoc3.6": "/usr/local/bin/pydoc3.6", "python3.6": "/usr/local/bin/python3.6", "python3.6-config": "/usr/local/bin/python3.6-config", "python3.6m": "/usr/local/bin/python3.6m"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fwdpy11.
shpc-registry automated BioContainers addition for fwdpy11
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fwdpy11
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fwdpy11:0.6.3--py36h7d13203_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fwdpy11/0.6.3--py36h7d13203_0
$ module help quay.io/biocontainers/fwdpy11/0.6.3--py36h7d13203_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fwdpy11-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fwdpy11-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fwdpy11-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fwdpy11-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fwdpy11-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fwdpy11-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tskit

```bash
$ singularity exec <container> /usr/local/bin/tskit
$ podman run --it --rm --entrypoint /usr/local/bin/tskit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tskit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numba

```bash
$ singularity exec <container> /usr/local/bin/numba
$ podman run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pycc

```bash
$ singularity exec <container> /usr/local/bin/pycc
$ podman run --it --rm --entrypoint /usr/local/bin/pycc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pycc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.6

```bash
$ singularity exec <container> /usr/local/bin/f2py3.6
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsonschema

```bash
$ singularity exec <container> /usr/local/bin/jsonschema
$ podman run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
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
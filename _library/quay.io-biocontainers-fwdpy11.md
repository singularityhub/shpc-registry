---
layout: container
name:  "quay.io/biocontainers/fwdpy11"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fwdpy11/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fwdpy11/container.yaml"
updated_at: "2024-04-22 02:50:33.315199"
latest: "0.22.2--py39h58a975e_0"
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
 - "0.22.2--py39h58a975e_0"
 - "0.21.0--py38h15ccf8d_0"
 - "0.20.1--py310h7677ecb_0"
 - "0.19.10--py39h8c02b11_0"
 - "0.18.3--py39h8c02b11_0"
description: "shpc-registry automated BioContainers addition for fwdpy11"
config: {"url": "https://biocontainers.pro/tools/fwdpy11", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fwdpy11", "latest": {"0.22.2--py39h58a975e_0": "sha256:729c1c0fb0b038749d79124e0362119137f306d4ebeab07fa0a3c5a7bd83f1aa"}, "tags": {"0.6.3--py36h7d13203_0": "sha256:cbffbbec5c22c11bb9895a922aa215b028abe9b76140c68f2e308ec87c289a2e", "0.22.2--py39h58a975e_0": "sha256:729c1c0fb0b038749d79124e0362119137f306d4ebeab07fa0a3c5a7bd83f1aa", "0.21.0--py38h15ccf8d_0": "sha256:d85472e85fde7ccb479fcfd4a385d77e580ddaae3ac98da7850ed4c4984b62a1", "0.20.1--py310h7677ecb_0": "sha256:e5cae637e4871e1bc396656faef6230c5b14be93c7a2aabcdc5b3adf49539d85", "0.19.10--py39h8c02b11_0": "sha256:6d597672b1eac4d399a88a85a8740ccf64caefe2c975b4b8cda2c40e56ad09d1", "0.18.3--py39h8c02b11_0": "sha256:307bcc550cfb6c6b3447d76b33041b2fef62661edc0899ba3cd8d8d2a29368bd"}, "docker": "quay.io/biocontainers/fwdpy11", "aliases": {"tskit": "/usr/local/bin/tskit", "numba": "/usr/local/bin/numba", "pycc": "/usr/local/bin/pycc", "f2py3.6": "/usr/local/bin/f2py3.6", "jsonschema": "/usr/local/bin/jsonschema", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6", "pydoc3.6": "/usr/local/bin/pydoc3.6", "python3.6": "/usr/local/bin/python3.6", "python3.6-config": "/usr/local/bin/python3.6-config", "python3.6m": "/usr/local/bin/python3.6m"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fwdpy11.
shpc-registry automated BioContainers addition for fwdpy11
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fwdpy11
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fwdpy11:0.22.2--py39h58a975e_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fwdpy11/0.22.2--py39h58a975e_0
$ module help quay.io/biocontainers/fwdpy11/0.22.2--py39h58a975e_0
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
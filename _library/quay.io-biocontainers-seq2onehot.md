---
layout: container
name:  "quay.io/biocontainers/seq2onehot"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/seq2onehot/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/seq2onehot/container.yaml"
updated_at: "2025-12-13 03:44:25.892920"
latest: "0.0.1--pyhfa5458b_0"
container_url: "https://biocontainers.pro/tools/seq2onehot"
aliases:
 - "seq2onehot"
 - "f2py3.9"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "0.0.1--pyhfa5458b_0"
description: "shpc-registry automated BioContainers addition for seq2onehot"
config: {"url": "https://biocontainers.pro/tools/seq2onehot", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for seq2onehot", "latest": {"0.0.1--pyhfa5458b_0": "sha256:6d116b0b2ea78644926072e1dbc2b0891e7810e526a4b5069c3a6122022bc31f"}, "tags": {"0.0.1--pyhfa5458b_0": "sha256:6d116b0b2ea78644926072e1dbc2b0891e7810e526a4b5069c3a6122022bc31f"}, "docker": "quay.io/biocontainers/seq2onehot", "aliases": {"seq2onehot": "/usr/local/bin/seq2onehot", "f2py3.9": "/usr/local/bin/f2py3.9", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/seq2onehot.
shpc-registry automated BioContainers addition for seq2onehot
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/seq2onehot
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/seq2onehot:0.0.1--pyhfa5458b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/seq2onehot/0.0.1--pyhfa5458b_0
$ module help quay.io/biocontainers/seq2onehot/0.0.1--pyhfa5458b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### seq2onehot-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### seq2onehot-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### seq2onehot-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### seq2onehot-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### seq2onehot-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### seq2onehot-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### seq2onehot

```bash
$ singularity exec <container> /usr/local/bin/seq2onehot
$ podman run --it --rm --entrypoint /usr/local/bin/seq2onehot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seq2onehot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9

```bash
$ singularity exec <container> /usr/local/bin/python3.9
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9-config

```bash
$ singularity exec <container> /usr/local/bin/python3.9-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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
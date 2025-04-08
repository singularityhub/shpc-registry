---
layout: container
name:  "quay.io/biocontainers/ffindex-dbkit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ffindex-dbkit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ffindex-dbkit/container.yaml"
updated_at: "2025-04-08 03:14:00.327753"
latest: "0.2--pyh5e36f6f_2"
container_url: "https://biocontainers.pro/tools/ffindex-dbkit"
aliases:
 - "dbkit_create.py"
 - "dbkit_extract.py"
 - "dbkit_merge.py"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "0.2--pyh5e36f6f_2"
description: "shpc-registry automated BioContainers addition for ffindex-dbkit"
config: {"url": "https://biocontainers.pro/tools/ffindex-dbkit", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ffindex-dbkit", "latest": {"0.2--pyh5e36f6f_2": "sha256:54836d70e734369d00861024200762246a65ca788d97b90043c4b244b94e7729"}, "tags": {"0.2--pyh5e36f6f_2": "sha256:54836d70e734369d00861024200762246a65ca788d97b90043c4b244b94e7729"}, "docker": "quay.io/biocontainers/ffindex-dbkit", "aliases": {"dbkit_create.py": "/usr/local/bin/dbkit_create.py", "dbkit_extract.py": "/usr/local/bin/dbkit_extract.py", "dbkit_merge.py": "/usr/local/bin/dbkit_merge.py", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ffindex-dbkit.
shpc-registry automated BioContainers addition for ffindex-dbkit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ffindex-dbkit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ffindex-dbkit:0.2--pyh5e36f6f_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ffindex-dbkit/0.2--pyh5e36f6f_2
$ module help quay.io/biocontainers/ffindex-dbkit/0.2--pyh5e36f6f_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ffindex-dbkit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ffindex-dbkit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ffindex-dbkit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ffindex-dbkit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ffindex-dbkit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ffindex-dbkit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dbkit_create.py

```bash
$ singularity exec <container> /usr/local/bin/dbkit_create.py
$ podman run --it --rm --entrypoint /usr/local/bin/dbkit_create.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbkit_create.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbkit_extract.py

```bash
$ singularity exec <container> /usr/local/bin/dbkit_extract.py
$ podman run --it --rm --entrypoint /usr/local/bin/dbkit_extract.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbkit_extract.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbkit_merge.py

```bash
$ singularity exec <container> /usr/local/bin/dbkit_merge.py
$ podman run --it --rm --entrypoint /usr/local/bin/dbkit_merge.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbkit_merge.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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
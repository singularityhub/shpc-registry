---
layout: container
name:  "quay.io/biocontainers/cobra"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cobra/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cobra/container.yaml"
updated_at: "2023-12-26 02:33:13.919914"
latest: "0.21.0--pyh5e36f6f_1"
container_url: "https://biocontainers.pro/tools/cobra"
aliases:
 - "glpsol"
 - "2to3-3.5"
 - "idle3.5"
 - "pydoc3.5"
 - "python3.5"
 - "python3.5-config"
 - "python3.5m"
 - "python3.5m-config"
 - "pyvenv-3.5"
 - "xslt-config"
versions:
 - "0.4.0b6--py35_0"
 - "0.21.0--pyh5e36f6f_1"
 - "0.20.0--pyh3252c3a_0"
 - "0.19.0--pyh864c0ab_0"
 - "0.18.1--pyh864c0ab_1"
 - "0.17.1--py_0"
description: "shpc-registry automated BioContainers addition for cobra"
config: {"url": "https://biocontainers.pro/tools/cobra", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cobra", "latest": {"0.21.0--pyh5e36f6f_1": "sha256:86b3e2f5de186eae27c29ef803b61aea121b77d4396e3be1f9520e149218cfcf"}, "tags": {"0.4.0b6--py35_0": "sha256:5f16c88186911111b9674164f82267860b5b80ac67a466c48d7f14141be5bf7c", "0.21.0--pyh5e36f6f_1": "sha256:86b3e2f5de186eae27c29ef803b61aea121b77d4396e3be1f9520e149218cfcf", "0.20.0--pyh3252c3a_0": "sha256:146ee1835b11dc76bc34df6163a82336f0f6edfae90e12dc56e2af709ea544be", "0.19.0--pyh864c0ab_0": "sha256:965d05da0beb8943616dbceec50ff337f8d0e50eda1856e305f750b27caab84a", "0.18.1--pyh864c0ab_1": "sha256:9d0aac96014ca4d7fb9f6532d6d87fb493059b18c816713e8f3b13cb4822dd2f", "0.17.1--py_0": "sha256:20568094f1a546bf5a8cea091d477ed66a5c5524baadc2dcc1ff89a5c71f8e78"}, "docker": "quay.io/biocontainers/cobra", "aliases": {"glpsol": "/usr/local/bin/glpsol", "2to3-3.5": "/usr/local/bin/2to3-3.5", "idle3.5": "/usr/local/bin/idle3.5", "pydoc3.5": "/usr/local/bin/pydoc3.5", "python3.5": "/usr/local/bin/python3.5", "python3.5-config": "/usr/local/bin/python3.5-config", "python3.5m": "/usr/local/bin/python3.5m", "python3.5m-config": "/usr/local/bin/python3.5m-config", "pyvenv-3.5": "/usr/local/bin/pyvenv-3.5", "xslt-config": "/usr/local/bin/xslt-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cobra.
shpc-registry automated BioContainers addition for cobra
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cobra
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cobra:0.21.0--pyh5e36f6f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cobra/0.21.0--pyh5e36f6f_1
$ module help quay.io/biocontainers/cobra/0.21.0--pyh5e36f6f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cobra-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cobra-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cobra-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cobra-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cobra-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cobra-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### xslt-config

```bash
$ singularity exec <container> /usr/local/bin/xslt-config
$ podman run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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
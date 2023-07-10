---
layout: container
name:  "quay.io/biocontainers/pizzly"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pizzly/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pizzly/container.yaml"
updated_at: "2023-07-10 03:08:56.514261"
latest: "0.37.3--h470a237_3"
container_url: "https://biocontainers.pro/tools/pizzly"
aliases:
 - "pizzly"
 - "pizzly_flatten_json.py"
 - "pizzly_flatten_json.py.bak"
 - "pizzly_get_fragment_length.py"
 - "pizzly_get_fragment_length.py.bak"
 - "2to3-3.6"
 - "idle3.6"
 - "pydoc3.6"
 - "python3.6"
 - "python3.6-config"
 - "python3.6m"
 - "python3.6m-config"
 - "pyvenv-3.6"
 - "h5clear"
 - "h5format_convert"
versions:
 - "0.37.3--h470a237_3"
description: "shpc-registry automated BioContainers addition for pizzly"
config: {"url": "https://biocontainers.pro/tools/pizzly", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pizzly", "latest": {"0.37.3--h470a237_3": "sha256:ead1dc712bec8e196aeeea9f1312603de07579b33814fa301a6cdc56e3619631"}, "tags": {"0.37.3--h470a237_3": "sha256:ead1dc712bec8e196aeeea9f1312603de07579b33814fa301a6cdc56e3619631"}, "docker": "quay.io/biocontainers/pizzly", "aliases": {"pizzly": "/usr/local/bin/pizzly", "pizzly_flatten_json.py": "/usr/local/bin/pizzly_flatten_json.py", "pizzly_flatten_json.py.bak": "/usr/local/bin/pizzly_flatten_json.py.bak", "pizzly_get_fragment_length.py": "/usr/local/bin/pizzly_get_fragment_length.py", "pizzly_get_fragment_length.py.bak": "/usr/local/bin/pizzly_get_fragment_length.py.bak", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6", "pydoc3.6": "/usr/local/bin/pydoc3.6", "python3.6": "/usr/local/bin/python3.6", "python3.6-config": "/usr/local/bin/python3.6-config", "python3.6m": "/usr/local/bin/python3.6m", "python3.6m-config": "/usr/local/bin/python3.6m-config", "pyvenv-3.6": "/usr/local/bin/pyvenv-3.6", "h5clear": "/usr/local/bin/h5clear", "h5format_convert": "/usr/local/bin/h5format_convert"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pizzly.
shpc-registry automated BioContainers addition for pizzly
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pizzly
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pizzly:0.37.3--h470a237_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pizzly/0.37.3--h470a237_3
$ module help quay.io/biocontainers/pizzly/0.37.3--h470a237_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pizzly-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pizzly-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pizzly-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pizzly-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pizzly-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pizzly-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pizzly

```bash
$ singularity exec <container> /usr/local/bin/pizzly
$ podman run --it --rm --entrypoint /usr/local/bin/pizzly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pizzly   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pizzly_flatten_json.py

```bash
$ singularity exec <container> /usr/local/bin/pizzly_flatten_json.py
$ podman run --it --rm --entrypoint /usr/local/bin/pizzly_flatten_json.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pizzly_flatten_json.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pizzly_flatten_json.py.bak

```bash
$ singularity exec <container> /usr/local/bin/pizzly_flatten_json.py.bak
$ podman run --it --rm --entrypoint /usr/local/bin/pizzly_flatten_json.py.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pizzly_flatten_json.py.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pizzly_get_fragment_length.py

```bash
$ singularity exec <container> /usr/local/bin/pizzly_get_fragment_length.py
$ podman run --it --rm --entrypoint /usr/local/bin/pizzly_get_fragment_length.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pizzly_get_fragment_length.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pizzly_get_fragment_length.py.bak

```bash
$ singularity exec <container> /usr/local/bin/pizzly_get_fragment_length.py.bak
$ podman run --it --rm --entrypoint /usr/local/bin/pizzly_get_fragment_length.py.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pizzly_get_fragment_length.py.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### h5clear

```bash
$ singularity exec <container> /usr/local/bin/h5clear
$ podman run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5format_convert

```bash
$ singularity exec <container> /usr/local/bin/h5format_convert
$ podman run --it --rm --entrypoint /usr/local/bin/h5format_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5format_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
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
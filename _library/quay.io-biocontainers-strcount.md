---
layout: container
name:  "quay.io/biocontainers/strcount"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/strcount/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/strcount/container.yaml"
updated_at: "2025-05-19 03:38:30.379563"
latest: "0.1.1--py312h7e72e81_2"
container_url: "https://biocontainers.pro/tools/strcount"
aliases:
 - "STRcount"
 - "STRcount.py"
 - "genome_str_graph_generator.py"
 - "parse_gaf.py"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
 - "python3.1"
versions:
 - "0.1.1--py310h7cba7a3_1"
 - "0.1.1--py312h7e72e81_2"
description: "singularity registry hpc automated addition for strcount"
config: {"url": "https://biocontainers.pro/tools/strcount", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for strcount", "latest": {"0.1.1--py312h7e72e81_2": "sha256:e0cb84f2b7de7583e3e0b8fa558ef993e9d26e199cef004062b4e25f3bbd40dd"}, "tags": {"0.1.1--py310h7cba7a3_1": "sha256:82cd8d8d9ce1f49bfe58bee2eead716e442f62156ddf29ceff66f442feb26840", "0.1.1--py312h7e72e81_2": "sha256:e0cb84f2b7de7583e3e0b8fa558ef993e9d26e199cef004062b4e25f3bbd40dd"}, "docker": "quay.io/biocontainers/strcount", "aliases": {"STRcount": "/usr/local/bin/STRcount", "STRcount.py": "/usr/local/bin/STRcount.py", "genome_str_graph_generator.py": "/usr/local/bin/genome_str_graph_generator.py", "parse_gaf.py": "/usr/local/bin/parse_gaf.py", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/strcount.
singularity registry hpc automated addition for strcount
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/strcount
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/strcount:0.1.1--py312h7e72e81_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/strcount/0.1.1--py312h7e72e81_2
$ module help quay.io/biocontainers/strcount/0.1.1--py312h7e72e81_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### strcount-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### strcount-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### strcount-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### strcount-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### strcount-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### strcount-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### STRcount

```bash
$ singularity exec <container> /usr/local/bin/STRcount
$ podman run --it --rm --entrypoint /usr/local/bin/STRcount   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STRcount   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STRcount.py

```bash
$ singularity exec <container> /usr/local/bin/STRcount.py
$ podman run --it --rm --entrypoint /usr/local/bin/STRcount.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STRcount.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genome_str_graph_generator.py

```bash
$ singularity exec <container> /usr/local/bin/genome_str_graph_generator.py
$ podman run --it --rm --entrypoint /usr/local/bin/genome_str_graph_generator.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genome_str_graph_generator.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parse_gaf.py

```bash
$ singularity exec <container> /usr/local/bin/parse_gaf.py
$ podman run --it --rm --entrypoint /usr/local/bin/parse_gaf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parse_gaf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
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
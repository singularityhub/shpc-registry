---
layout: container
name:  "quay.io/biocontainers/moods"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/moods/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/moods/container.yaml"
updated_at: "2025-12-22 03:48:47.014057"
latest: "1.9.4.2--py39h2de1943_3"
container_url: "https://biocontainers.pro/tools/moods"
aliases:
 - "ccache-swig"
 - "moods-dna.py"
 - "swig"
 - "2to3-3.6"
 - "idle3.6"
 - "pydoc3.6"
 - "python3.6"
 - "python3.6-config"
 - "python3.6m"
 - "python3.6m-config"
 - "pyvenv-3.6"
 - "pyvenv"
versions:
 - "1.9.4.1--py36hf484d3e_0"
 - "1.9.4.1--py37h675a0cb_2"
 - "1.9.4.1--py39he10ea66_4"
 - "1.9.4.2--py310h0dbaff4_0"
 - "1.9.4.2--py38h2494328_0"
 - "1.9.4.2--py310h84f13bb_1"
 - "1.9.4.2--py312h28adbb1_2"
 - "1.9.4.2--py39h2de1943_3"
description: "shpc-registry automated BioContainers addition for moods"
config: {"url": "https://biocontainers.pro/tools/moods", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for moods", "latest": {"1.9.4.2--py39h2de1943_3": "sha256:9fb41facce9af7dcee19f97dec1dd65d05c3a8e45bed0e599df7e3e87c80b3ca"}, "tags": {"1.9.4.1--py36hf484d3e_0": "sha256:ef8a6f81654088a43ff1b3f8e57906c0be9382dded8edf832bd63d2e8613f301", "1.9.4.1--py37h675a0cb_2": "sha256:fd7385b3661197aeee37395efcf79cd853774ddfc2f46e12832a2af8ecfe7de2", "1.9.4.1--py39he10ea66_4": "sha256:21d2f9db79869927c43312b68686a9d13ea28403b42d6d56e8473c5476e48e72", "1.9.4.2--py310h0dbaff4_0": "sha256:e1e6edb654eb35f735d79a293b1f0486f0581787436f803b175ac1fd8c872fa2", "1.9.4.2--py38h2494328_0": "sha256:ee8591de074ee17e2dc303c5de26c586eb315090bbe222a445991d7460daadbd", "1.9.4.2--py310h84f13bb_1": "sha256:21ec22aa5a4d1ac65908d6ea97c4a3bb489ebfc8da36e1ce9189b10dfcad6c94", "1.9.4.2--py312h28adbb1_2": "sha256:e6a819fbc300630e292e9645973972ce5612c917f37de861fef0ab4b3b25f2cc", "1.9.4.2--py39h2de1943_3": "sha256:9fb41facce9af7dcee19f97dec1dd65d05c3a8e45bed0e599df7e3e87c80b3ca"}, "docker": "quay.io/biocontainers/moods", "aliases": {"ccache-swig": "/usr/local/bin/ccache-swig", "moods-dna.py": "/usr/local/bin/moods-dna.py", "swig": "/usr/local/bin/swig", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6", "pydoc3.6": "/usr/local/bin/pydoc3.6", "python3.6": "/usr/local/bin/python3.6", "python3.6-config": "/usr/local/bin/python3.6-config", "python3.6m": "/usr/local/bin/python3.6m", "python3.6m-config": "/usr/local/bin/python3.6m-config", "pyvenv-3.6": "/usr/local/bin/pyvenv-3.6", "pyvenv": "/usr/local/bin/pyvenv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/moods.
shpc-registry automated BioContainers addition for moods
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/moods
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/moods:1.9.4.2--py39h2de1943_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/moods/1.9.4.2--py39h2de1943_3
$ module help quay.io/biocontainers/moods/1.9.4.2--py39h2de1943_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### moods-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### moods-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### moods-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### moods-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### moods-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### moods-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ccache-swig

```bash
$ singularity exec <container> /usr/local/bin/ccache-swig
$ podman run --it --rm --entrypoint /usr/local/bin/ccache-swig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccache-swig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### moods-dna.py

```bash
$ singularity exec <container> /usr/local/bin/moods-dna.py
$ podman run --it --rm --entrypoint /usr/local/bin/moods-dna.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/moods-dna.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### swig

```bash
$ singularity exec <container> /usr/local/bin/swig
$ podman run --it --rm --entrypoint /usr/local/bin/swig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/swig   -v ${PWD} -w ${PWD} <container> -c " $@"
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
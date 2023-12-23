---
layout: container
name:  "quay.io/biocontainers/pgr-tk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pgr-tk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pgr-tk/container.yaml"
updated_at: "2023-12-23 02:42:53.551814"
latest: "0.5.1--py38h8fa8eaa_0"
container_url: "https://biocontainers.pro/tools/pgr-tk"
aliases:
 - "pgr-mdb"
 - "f2py3.9"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "0.3.6--py39h67e14b5_0"
 - "0.3.6--py39he10ea66_2"
 - "0.5.1--py38h8fa8eaa_0"
description: "singularity registry hpc automated addition for pgr-tk"
config: {"url": "https://biocontainers.pro/tools/pgr-tk", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pgr-tk", "latest": {"0.5.1--py38h8fa8eaa_0": "sha256:e439d7a6f5b714503b46ef2c716acb1ec315390017e41ff471e0bd23072e57cd"}, "tags": {"0.3.6--py39h67e14b5_0": "sha256:9b8403494fdf04181be9a8b0b76b4e36946d4e1f519ca42b24eb3a52ab4fa29f", "0.3.6--py39he10ea66_2": "sha256:4d7bb485e8fd69bc1c7d1045307065c0d580c7ae166fc037647f9c7e555cc30f", "0.5.1--py38h8fa8eaa_0": "sha256:e439d7a6f5b714503b46ef2c716acb1ec315390017e41ff471e0bd23072e57cd"}, "docker": "quay.io/biocontainers/pgr-tk", "aliases": {"pgr-mdb": "/usr/local/bin/pgr-mdb", "f2py3.9": "/usr/local/bin/f2py3.9", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pgr-tk.
singularity registry hpc automated addition for pgr-tk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pgr-tk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pgr-tk:0.5.1--py38h8fa8eaa_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pgr-tk/0.5.1--py38h8fa8eaa_0
$ module help quay.io/biocontainers/pgr-tk/0.5.1--py38h8fa8eaa_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pgr-tk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pgr-tk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pgr-tk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pgr-tk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pgr-tk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pgr-tk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pgr-mdb

```bash
$ singularity exec <container> /usr/local/bin/pgr-mdb
$ podman run --it --rm --entrypoint /usr/local/bin/pgr-mdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pgr-mdb   -v ${PWD} -w ${PWD} <container> -c " $@"
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
---
layout: container
name:  "quay.io/biocontainers/geofetch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/geofetch/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/geofetch/container.yaml"
updated_at: "2023-06-30 03:26:52.067006"
latest: "0.12.2--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/geofetch"
aliases:
 - "f2py3.11"
 - "geofetch"
 - "markdown-it"
 - "sraconvert"
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "coloredlogs"
 - "humanfriendly"
 - "py.test"
 - "pytest"
 - "jsonschema"
 - "pygmentize"
 - "normalizer"
 - "python3.1"
versions:
 - "0.12.0--pyh7cba7a3_0"
 - "0.12.1--pyh7cba7a3_0"
 - "0.12.2--pyh7cba7a3_0"
description: "singularity registry hpc automated addition for geofetch"
config: {"url": "https://biocontainers.pro/tools/geofetch", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for geofetch", "latest": {"0.12.2--pyh7cba7a3_0": "sha256:3ad10795812fcb36434b6fea3a6ceb9bca3a8f12ea4e1951427c8e3a49965dde"}, "tags": {"0.12.0--pyh7cba7a3_0": "sha256:9518cba6862d92fc62ebb645b7dd21d4a155606348b92857289c72c4a11139d3", "0.12.1--pyh7cba7a3_0": "sha256:b279b8bbd2e86aa2d4f9ae6988967174586d6f4072723050276e8433a60c66c5", "0.12.2--pyh7cba7a3_0": "sha256:3ad10795812fcb36434b6fea3a6ceb9bca3a8f12ea4e1951427c8e3a49965dde"}, "docker": "quay.io/biocontainers/geofetch", "aliases": {"f2py3.11": "/usr/local/bin/f2py3.11", "geofetch": "/usr/local/bin/geofetch", "markdown-it": "/usr/local/bin/markdown-it", "sraconvert": "/usr/local/bin/sraconvert", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "coloredlogs": "/usr/local/bin/coloredlogs", "humanfriendly": "/usr/local/bin/humanfriendly", "py.test": "/usr/local/bin/py.test", "pytest": "/usr/local/bin/pytest", "jsonschema": "/usr/local/bin/jsonschema", "pygmentize": "/usr/local/bin/pygmentize", "normalizer": "/usr/local/bin/normalizer", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/geofetch.
singularity registry hpc automated addition for geofetch
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/geofetch
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/geofetch:0.12.2--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/geofetch/0.12.2--pyh7cba7a3_0
$ module help quay.io/biocontainers/geofetch/0.12.2--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### geofetch-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### geofetch-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### geofetch-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### geofetch-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### geofetch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### geofetch-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### f2py3.11

```bash
$ singularity exec <container> /usr/local/bin/f2py3.11
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geofetch

```bash
$ singularity exec <container> /usr/local/bin/geofetch
$ podman run --it --rm --entrypoint /usr/local/bin/geofetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geofetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### markdown-it

```bash
$ singularity exec <container> /usr/local/bin/markdown-it
$ podman run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sraconvert

```bash
$ singularity exec <container> /usr/local/bin/sraconvert
$ podman run --it --rm --entrypoint /usr/local/bin/sraconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sraconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.11

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.11
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.11

```bash
$ singularity exec <container> /usr/local/bin/idle3.11
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.11

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.11
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11

```bash
$ singularity exec <container> /usr/local/bin/python3.11
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11-config

```bash
$ singularity exec <container> /usr/local/bin/python3.11-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coloredlogs

```bash
$ singularity exec <container> /usr/local/bin/coloredlogs
$ podman run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### humanfriendly

```bash
$ singularity exec <container> /usr/local/bin/humanfriendly
$ podman run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### py.test

```bash
$ singularity exec <container> /usr/local/bin/py.test
$ podman run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pytest

```bash
$ singularity exec <container> /usr/local/bin/pytest
$ podman run --it --rm --entrypoint /usr/local/bin/pytest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pytest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsonschema

```bash
$ singularity exec <container> /usr/local/bin/jsonschema
$ podman run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pygmentize

```bash
$ singularity exec <container> /usr/local/bin/pygmentize
$ podman run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
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
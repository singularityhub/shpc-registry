---
layout: container
name:  "quay.io/biocontainers/refgenieserver"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/refgenieserver/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/refgenieserver/container.yaml"
updated_at: "2025-03-06 03:51:58.779192"
latest: "0.7.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/refgenieserver"
aliases:
 - "dotenv"
 - "refgenieserver"
 - "uvicorn"
 - "watchgod"
 - "cmark"
 - "py.test"
 - "pytest"
 - "jsonschema"
 - "pygmentize"
 - "futurize"
 - "pasteurize"
 - "chardetect"
 - "2to3-3.9"
 - "idle3.9"
versions:
 - "0.6.0--py_0"
 - "0.7.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for refgenieserver"
config: {"url": "https://biocontainers.pro/tools/refgenieserver", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for refgenieserver", "latest": {"0.7.0--pyhdfd78af_0": "sha256:da17b8021581514cf9e74dadf54064391662d82fa04a68e26dd248fbc62c1982"}, "tags": {"0.6.0--py_0": "sha256:8de5845748fbf02c28ee49f5f8e4aa85335a9b504162637e9f4a97cdb133aaaa", "0.7.0--pyhdfd78af_0": "sha256:da17b8021581514cf9e74dadf54064391662d82fa04a68e26dd248fbc62c1982"}, "docker": "quay.io/biocontainers/refgenieserver", "aliases": {"dotenv": "/usr/local/bin/dotenv", "refgenieserver": "/usr/local/bin/refgenieserver", "uvicorn": "/usr/local/bin/uvicorn", "watchgod": "/usr/local/bin/watchgod", "cmark": "/usr/local/bin/cmark", "py.test": "/usr/local/bin/py.test", "pytest": "/usr/local/bin/pytest", "jsonschema": "/usr/local/bin/jsonschema", "pygmentize": "/usr/local/bin/pygmentize", "futurize": "/usr/local/bin/futurize", "pasteurize": "/usr/local/bin/pasteurize", "chardetect": "/usr/local/bin/chardetect", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/refgenieserver.
shpc-registry automated BioContainers addition for refgenieserver
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/refgenieserver
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/refgenieserver:0.7.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/refgenieserver/0.7.0--pyhdfd78af_0
$ module help quay.io/biocontainers/refgenieserver/0.7.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### refgenieserver-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### refgenieserver-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### refgenieserver-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### refgenieserver-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### refgenieserver-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### refgenieserver-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dotenv

```bash
$ singularity exec <container> /usr/local/bin/dotenv
$ podman run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### refgenieserver

```bash
$ singularity exec <container> /usr/local/bin/refgenieserver
$ podman run --it --rm --entrypoint /usr/local/bin/refgenieserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/refgenieserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uvicorn

```bash
$ singularity exec <container> /usr/local/bin/uvicorn
$ podman run --it --rm --entrypoint /usr/local/bin/uvicorn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uvicorn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### watchgod

```bash
$ singularity exec <container> /usr/local/bin/watchgod
$ podman run --it --rm --entrypoint /usr/local/bin/watchgod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/watchgod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmark

```bash
$ singularity exec <container> /usr/local/bin/cmark
$ podman run --it --rm --entrypoint /usr/local/bin/cmark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmark   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### futurize

```bash
$ singularity exec <container> /usr/local/bin/futurize
$ podman run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pasteurize

```bash
$ singularity exec <container> /usr/local/bin/pasteurize
$ podman run --it --rm --entrypoint /usr/local/bin/pasteurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pasteurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
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
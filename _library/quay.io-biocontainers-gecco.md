---
layout: container
name:  "quay.io/biocontainers/gecco"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gecco/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/gecco/container.yaml"
updated_at: "2022-10-29 05:40:25.648901"
latest: "0.9.5--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/gecco"
aliases:
 - "gecco"
 - "pyrodigal"
 - "2to3-3.10"
 - "cmark"
 - "f2py3.10"
 - "futurize"
 - "idle3.10"
 - "pasteurize"
 - "pydoc3.10"
 - "pygmentize"
 - "python3.1"
 - "python3.10"
versions:
 - "0.9.5--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for gecco"
config: {"url": "https://biocontainers.pro/tools/gecco", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gecco", "latest": {"0.9.5--pyhdfd78af_0": "sha256:9f1bdcf94165e8596a452d1adae6098311a398121fc1beaa36ebb17d65e3a58c"}, "tags": {"0.9.5--pyhdfd78af_0": "sha256:9f1bdcf94165e8596a452d1adae6098311a398121fc1beaa36ebb17d65e3a58c"}, "docker": "quay.io/biocontainers/gecco", "aliases": {"gecco": "/usr/local/bin/gecco", "pyrodigal": "/usr/local/bin/pyrodigal", "2to3-3.10": "/usr/local/bin/2to3-3.10", "cmark": "/usr/local/bin/cmark", "f2py3.10": "/usr/local/bin/f2py3.10", "futurize": "/usr/local/bin/futurize", "idle3.10": "/usr/local/bin/idle3.10", "pasteurize": "/usr/local/bin/pasteurize", "pydoc3.10": "/usr/local/bin/pydoc3.10", "pygmentize": "/usr/local/bin/pygmentize", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gecco.
shpc-registry automated BioContainers addition for gecco
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gecco
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gecco:0.9.5--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gecco/0.9.5--pyhdfd78af_0
$ module help quay.io/biocontainers/gecco/0.9.5--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gecco-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gecco-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gecco-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gecco-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gecco-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gecco-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gecco

```bash
$ singularity exec <container> /usr/local/bin/gecco
$ podman run --it --rm --entrypoint /usr/local/bin/gecco   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gecco   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrodigal

```bash
$ singularity exec <container> /usr/local/bin/pyrodigal
$ podman run --it --rm --entrypoint /usr/local/bin/pyrodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmark

```bash
$ singularity exec <container> /usr/local/bin/cmark
$ podman run --it --rm --entrypoint /usr/local/bin/cmark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmark   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### futurize

```bash
$ singularity exec <container> /usr/local/bin/futurize
$ podman run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pasteurize

```bash
$ singularity exec <container> /usr/local/bin/pasteurize
$ podman run --it --rm --entrypoint /usr/local/bin/pasteurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pasteurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pygmentize

```bash
$ singularity exec <container> /usr/local/bin/pygmentize
$ podman run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
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
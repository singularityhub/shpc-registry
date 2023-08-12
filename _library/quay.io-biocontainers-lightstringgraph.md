---
layout: container
name:  "quay.io/biocontainers/lightstringgraph"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lightstringgraph/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/lightstringgraph/container.yaml"
updated_at: "2023-08-12 02:37:47.046665"
latest: "0.4.0--hfce7173_5"
container_url: "https://biocontainers.pro/tools/lightstringgraph"
aliases:
 - "graph2asqg"
 - "lsg"
 - "redbuild"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
versions:
 - "0.4.0--ha04c180_3"
 - "0.4.0--hfce7173_5"
description: "shpc-registry automated BioContainers addition for lightstringgraph"
config: {"url": "https://biocontainers.pro/tools/lightstringgraph", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for lightstringgraph", "latest": {"0.4.0--hfce7173_5": "sha256:8e72b6b91597b324b471a79c8cb05f45d89a64695ef50ba0a2d4e0449dc8bb68"}, "tags": {"0.4.0--ha04c180_3": "sha256:9ebb171ec036d2921aaa7059e4eb74356472eb5d32fdb9571e142626716a8e9a", "0.4.0--hfce7173_5": "sha256:8e72b6b91597b324b471a79c8cb05f45d89a64695ef50ba0a2d4e0449dc8bb68"}, "docker": "quay.io/biocontainers/lightstringgraph", "aliases": {"graph2asqg": "/usr/local/bin/graph2asqg", "lsg": "/usr/local/bin/lsg", "redbuild": "/usr/local/bin/redbuild", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/lightstringgraph.
shpc-registry automated BioContainers addition for lightstringgraph
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lightstringgraph
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lightstringgraph:0.4.0--hfce7173_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lightstringgraph/0.4.0--hfce7173_5
$ module help quay.io/biocontainers/lightstringgraph/0.4.0--hfce7173_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lightstringgraph-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lightstringgraph-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lightstringgraph-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lightstringgraph-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lightstringgraph-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lightstringgraph-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### graph2asqg

```bash
$ singularity exec <container> /usr/local/bin/graph2asqg
$ podman run --it --rm --entrypoint /usr/local/bin/graph2asqg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/graph2asqg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lsg

```bash
$ singularity exec <container> /usr/local/bin/lsg
$ podman run --it --rm --entrypoint /usr/local/bin/lsg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lsg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### redbuild

```bash
$ singularity exec <container> /usr/local/bin/redbuild
$ podman run --it --rm --entrypoint /usr/local/bin/redbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/redbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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
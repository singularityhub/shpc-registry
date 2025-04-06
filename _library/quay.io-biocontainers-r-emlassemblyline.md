---
layout: container
name:  "quay.io/biocontainers/r-emlassemblyline"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-emlassemblyline/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-emlassemblyline/container.yaml"
updated_at: "2025-04-06 03:52:50.286305"
latest: "3.5.5"
container_url: "https://biocontainers.pro/tools/r-emlassemblyline"
aliases:
 - "hb-info"
 - "tjbench"
 - "glpsol"
 - "jq"
 - "onig-config"
 - "pandoc"
versions:
 - "3.5.5"
description: "singularity registry hpc automated addition for r-emlassemblyline"
config: {"url": "https://biocontainers.pro/tools/r-emlassemblyline", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for r-emlassemblyline", "latest": {"3.5.5": "sha256:ae89ede403af3f7151ac75ad3d9d1227d708572af38c85769d8dd468d04f4762"}, "tags": {"3.5.5": "sha256:ae89ede403af3f7151ac75ad3d9d1227d708572af38c85769d8dd468d04f4762"}, "docker": "quay.io/biocontainers/r-emlassemblyline", "aliases": {"hb-info": "/usr/local/bin/hb-info", "tjbench": "/usr/local/bin/tjbench", "glpsol": "/usr/local/bin/glpsol", "jq": "/usr/local/bin/jq", "onig-config": "/usr/local/bin/onig-config", "pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-emlassemblyline.
singularity registry hpc automated addition for r-emlassemblyline
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-emlassemblyline
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-emlassemblyline:3.5.5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-emlassemblyline/3.5.5
$ module help quay.io/biocontainers/r-emlassemblyline/3.5.5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-emlassemblyline-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-emlassemblyline-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-emlassemblyline-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-emlassemblyline-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-emlassemblyline-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-emlassemblyline-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jq

```bash
$ singularity exec <container> /usr/local/bin/jq
$ podman run --it --rm --entrypoint /usr/local/bin/jq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### onig-config

```bash
$ singularity exec <container> /usr/local/bin/onig-config
$ podman run --it --rm --entrypoint /usr/local/bin/onig-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/onig-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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
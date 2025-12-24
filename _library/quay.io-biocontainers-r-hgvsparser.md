---
layout: container
name:  "quay.io/biocontainers/r-hgvsparser"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-hgvsparser/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-hgvsparser/container.yaml"
updated_at: "2025-12-24 04:10:00.242841"
latest: "0.1.0--r44hdfd78af_1"
container_url: "https://biocontainers.pro/tools/r-hgvsparser"
aliases:
 - "pandoc-lua"
 - "git2"
 - "pandoc-server"
 - "hb-info"
 - "pandoc"
 - "tjbench"
versions:
 - "0.1.0--r43hdfd78af_0"
 - "0.1.0--r44hdfd78af_1"
description: "singularity registry hpc automated addition for r-hgvsparser"
config: {"url": "https://biocontainers.pro/tools/r-hgvsparser", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for r-hgvsparser", "latest": {"0.1.0--r44hdfd78af_1": "sha256:c85afcca958633e3836386f313c9b589034db47cfff7d56cadfca64c92b4f2b9"}, "tags": {"0.1.0--r43hdfd78af_0": "sha256:7a661cccf3035b5718700061e6768f4c31fee7ba50ff9b30a23400f22e353259", "0.1.0--r44hdfd78af_1": "sha256:c85afcca958633e3836386f313c9b589034db47cfff7d56cadfca64c92b4f2b9"}, "docker": "quay.io/biocontainers/r-hgvsparser", "aliases": {"pandoc-lua": "/usr/local/bin/pandoc-lua", "git2": "/usr/local/bin/git2", "pandoc-server": "/usr/local/bin/pandoc-server", "hb-info": "/usr/local/bin/hb-info", "pandoc": "/usr/local/bin/pandoc", "tjbench": "/usr/local/bin/tjbench"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-hgvsparser.
singularity registry hpc automated addition for r-hgvsparser
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-hgvsparser
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-hgvsparser:0.1.0--r44hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-hgvsparser/0.1.0--r44hdfd78af_1
$ module help quay.io/biocontainers/r-hgvsparser/0.1.0--r44hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-hgvsparser-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-hgvsparser-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-hgvsparser-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-hgvsparser-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-hgvsparser-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-hgvsparser-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc-lua

```bash
$ singularity exec <container> /usr/local/bin/pandoc-lua
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-lua   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-lua   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git2

```bash
$ singularity exec <container> /usr/local/bin/git2
$ podman run --it --rm --entrypoint /usr/local/bin/git2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc-server

```bash
$ singularity exec <container> /usr/local/bin/pandoc-server
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
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
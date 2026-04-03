---
layout: container
name:  "quay.io/biocontainers/bioconductor-xaitest"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-xaitest/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-xaitest/container.yaml"
updated_at: "2026-04-03 05:21:14.998847"
latest: "1.2.0--r45hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-xaitest"
aliases:
 - "pandoc-lua"
 - "pandoc-server"
 - "x86_64-conda-linux-gnu.cfg"
 - "pandoc"
 - "hb-info"
versions:
 - "1.2.0--r45hdfd78af_0"
description: "singularity registry hpc automated addition for bioconductor-xaitest"
config: {"url": "https://biocontainers.pro/tools/bioconductor-xaitest", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-xaitest", "latest": {"1.2.0--r45hdfd78af_0": "sha256:4c6215ef773dd46f97b0720fd9fb14e0d9faa40436365f154555205f81995fb1"}, "tags": {"1.2.0--r45hdfd78af_0": "sha256:4c6215ef773dd46f97b0720fd9fb14e0d9faa40436365f154555205f81995fb1"}, "docker": "quay.io/biocontainers/bioconductor-xaitest", "aliases": {"pandoc-lua": "/usr/local/bin/pandoc-lua", "pandoc-server": "/usr/local/bin/pandoc-server", "x86_64-conda-linux-gnu.cfg": "/usr/local/bin/x86_64-conda-linux-gnu.cfg", "pandoc": "/usr/local/bin/pandoc", "hb-info": "/usr/local/bin/hb-info"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-xaitest.
singularity registry hpc automated addition for bioconductor-xaitest
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-xaitest
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-xaitest:1.2.0--r45hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-xaitest/1.2.0--r45hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-xaitest/1.2.0--r45hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-xaitest-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-xaitest-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-xaitest-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-xaitest-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-xaitest-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-xaitest-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc-lua

```bash
$ singularity exec <container> /usr/local/bin/pandoc-lua
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-lua   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-lua   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc-server

```bash
$ singularity exec <container> /usr/local/bin/pandoc-server
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu.cfg

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu.cfg
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
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
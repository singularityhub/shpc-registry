---
layout: container
name:  "quay.io/biocontainers/bioconductor-cytopipelinegui"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cytopipelinegui/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cytopipelinegui/container.yaml"
updated_at: "2024-07-28 02:53:23.825305"
latest: "1.0.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cytopipelinegui"
aliases:
 - "pcre2posix_test"
 - "hb-info"
 - "tjbench"
 - "pandoc"
versions:
 - "1.0.0--r43hdfd78af_0"
description: "singularity registry hpc automated addition for bioconductor-cytopipelinegui"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cytopipelinegui", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-cytopipelinegui", "latest": {"1.0.0--r43hdfd78af_0": "sha256:2d11b8e6d1423c3bf8bb141b8ad996efed2785b80cc9dac3b9b81a22969f7e53"}, "tags": {"1.0.0--r43hdfd78af_0": "sha256:2d11b8e6d1423c3bf8bb141b8ad996efed2785b80cc9dac3b9b81a22969f7e53"}, "docker": "quay.io/biocontainers/bioconductor-cytopipelinegui", "aliases": {"pcre2posix_test": "/usr/local/bin/pcre2posix_test", "hb-info": "/usr/local/bin/hb-info", "tjbench": "/usr/local/bin/tjbench", "pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cytopipelinegui.
singularity registry hpc automated addition for bioconductor-cytopipelinegui
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cytopipelinegui
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cytopipelinegui:1.0.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cytopipelinegui/1.0.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cytopipelinegui/1.0.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cytopipelinegui-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cytopipelinegui-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cytopipelinegui-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cytopipelinegui-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cytopipelinegui-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cytopipelinegui-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pcre2posix_test

```bash
$ singularity exec <container> /usr/local/bin/pcre2posix_test
$ podman run --it --rm --entrypoint /usr/local/bin/pcre2posix_test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pcre2posix_test   -v ${PWD} -w ${PWD} <container> -c " $@"
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
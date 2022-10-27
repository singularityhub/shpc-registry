---
layout: container
name:  "quay.io/biocontainers/jasminesv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/jasminesv/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/jasminesv/container.yaml"
updated_at: "2022-10-27 00:29:58.597075"
latest: "1.1.5--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/jasminesv"
aliases:
 - "igv_jasmine"
 - "iris"
 - "iris.jar"
 - "jasmine"
 - "jasmine.jar"
 - "jasmine_igv.jar"
 - "jasmine_iris.jar"
versions:
 - "1.1.5--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for jasminesv"
config: {"url": "https://biocontainers.pro/tools/jasminesv", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for jasminesv", "latest": {"1.1.5--hdfd78af_0": "sha256:a1523c661ee6e4c5d7d1a33559446454e7cd9cae70b011ce46cc00acbab4dd71"}, "tags": {"1.1.5--hdfd78af_0": "sha256:a1523c661ee6e4c5d7d1a33559446454e7cd9cae70b011ce46cc00acbab4dd71"}, "docker": "quay.io/biocontainers/jasminesv", "aliases": {"igv_jasmine": "/usr/local/bin/igv_jasmine", "iris": "/usr/local/bin/iris", "iris.jar": "/usr/local/bin/iris.jar", "jasmine": "/usr/local/bin/jasmine", "jasmine.jar": "/usr/local/bin/jasmine.jar", "jasmine_igv.jar": "/usr/local/bin/jasmine_igv.jar", "jasmine_iris.jar": "/usr/local/bin/jasmine_iris.jar"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/jasminesv.
shpc-registry automated BioContainers addition for jasminesv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/jasminesv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/jasminesv:1.1.5--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/jasminesv/1.1.5--hdfd78af_0
$ module help quay.io/biocontainers/jasminesv/1.1.5--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### jasminesv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### jasminesv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### jasminesv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### jasminesv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### jasminesv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### jasminesv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### igv_jasmine

```bash
$ singularity exec <container> /usr/local/bin/igv_jasmine
$ podman run --it --rm --entrypoint /usr/local/bin/igv_jasmine   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igv_jasmine   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iris

```bash
$ singularity exec <container> /usr/local/bin/iris
$ podman run --it --rm --entrypoint /usr/local/bin/iris   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iris   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iris.jar

```bash
$ singularity exec <container> /usr/local/bin/iris.jar
$ podman run --it --rm --entrypoint /usr/local/bin/iris.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iris.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jasmine

```bash
$ singularity exec <container> /usr/local/bin/jasmine
$ podman run --it --rm --entrypoint /usr/local/bin/jasmine   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jasmine   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jasmine.jar

```bash
$ singularity exec <container> /usr/local/bin/jasmine.jar
$ podman run --it --rm --entrypoint /usr/local/bin/jasmine.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jasmine.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jasmine_igv.jar

```bash
$ singularity exec <container> /usr/local/bin/jasmine_igv.jar
$ podman run --it --rm --entrypoint /usr/local/bin/jasmine_igv.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jasmine_igv.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jasmine_iris.jar

```bash
$ singularity exec <container> /usr/local/bin/jasmine_iris.jar
$ podman run --it --rm --entrypoint /usr/local/bin/jasmine_iris.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jasmine_iris.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
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
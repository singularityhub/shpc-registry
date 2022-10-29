---
layout: container
name:  "quay.io/biocontainers/cromshell"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cromshell/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/cromshell/container.yaml"
updated_at: "2022-10-29 05:34:44.239809"
latest: "0.5.2--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/cromshell"
aliases:
 - "cromshell"
 - "jq"
 - "onig-config"
 - "womtool"
 - "2to3-3.9"
 - "appletviewer"
 - "clhsdb"
 - "extcheck"
 - "hsdb"
 - "idle3.9"
 - "idlj"
 - "jar"
 - "jarsigner"
 - "java"
versions:
 - "0.5.2--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for cromshell"
config: {"url": "https://biocontainers.pro/tools/cromshell", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cromshell", "latest": {"0.5.2--hdfd78af_0": "sha256:c399ad57321b0564b48fb06beed6e2dc7736032d50d623baefe1e83f8ee14300"}, "tags": {"0.5.2--hdfd78af_0": "sha256:c399ad57321b0564b48fb06beed6e2dc7736032d50d623baefe1e83f8ee14300"}, "docker": "quay.io/biocontainers/cromshell", "aliases": {"cromshell": "/usr/local/bin/cromshell", "jq": "/usr/local/bin/jq", "onig-config": "/usr/local/bin/onig-config", "womtool": "/usr/local/bin/womtool", "2to3-3.9": "/usr/local/bin/2to3-3.9", "appletviewer": "/usr/local/bin/appletviewer", "clhsdb": "/usr/local/bin/clhsdb", "extcheck": "/usr/local/bin/extcheck", "hsdb": "/usr/local/bin/hsdb", "idle3.9": "/usr/local/bin/idle3.9", "idlj": "/usr/local/bin/idlj", "jar": "/usr/local/bin/jar", "jarsigner": "/usr/local/bin/jarsigner", "java": "/usr/local/bin/java"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cromshell.
shpc-registry automated BioContainers addition for cromshell
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cromshell
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cromshell:0.5.2--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cromshell/0.5.2--hdfd78af_0
$ module help quay.io/biocontainers/cromshell/0.5.2--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cromshell-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cromshell-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cromshell-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cromshell-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cromshell-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cromshell-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cromshell

```bash
$ singularity exec <container> /usr/local/bin/cromshell
$ podman run --it --rm --entrypoint /usr/local/bin/cromshell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cromshell   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### womtool

```bash
$ singularity exec <container> /usr/local/bin/womtool
$ podman run --it --rm --entrypoint /usr/local/bin/womtool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/womtool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### appletviewer

```bash
$ singularity exec <container> /usr/local/bin/appletviewer
$ podman run --it --rm --entrypoint /usr/local/bin/appletviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/appletviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clhsdb

```bash
$ singularity exec <container> /usr/local/bin/clhsdb
$ podman run --it --rm --entrypoint /usr/local/bin/clhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extcheck

```bash
$ singularity exec <container> /usr/local/bin/extcheck
$ podman run --it --rm --entrypoint /usr/local/bin/extcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hsdb

```bash
$ singularity exec <container> /usr/local/bin/hsdb
$ podman run --it --rm --entrypoint /usr/local/bin/hsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idlj

```bash
$ singularity exec <container> /usr/local/bin/idlj
$ podman run --it --rm --entrypoint /usr/local/bin/idlj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idlj   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jar

```bash
$ singularity exec <container> /usr/local/bin/jar
$ podman run --it --rm --entrypoint /usr/local/bin/jar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jarsigner

```bash
$ singularity exec <container> /usr/local/bin/jarsigner
$ podman run --it --rm --entrypoint /usr/local/bin/jarsigner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jarsigner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### java

```bash
$ singularity exec <container> /usr/local/bin/java
$ podman run --it --rm --entrypoint /usr/local/bin/java   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/java   -v ${PWD} -w ${PWD} <container> -c " $@"
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
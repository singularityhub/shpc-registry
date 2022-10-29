---
layout: container
name:  "quay.io/biocontainers/effectivet3"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/effectivet3/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/effectivet3/container.yaml"
updated_at: "2022-10-29 05:31:51.460051"
latest: "1.0.1--py35_0"
container_url: "https://biocontainers.pro/tools/effectivet3"
aliases:
 - "effectivet3"
 - "2to3-3.5"
 - "appletviewer"
 - "easy_install-3.5"
 - "extcheck"
 - "idle3.5"
 - "idlj"
 - "jar"
 - "jarsigner"
 - "java"
 - "java-rmi.cgi"
versions:
 - "1.0.1--py35_0"
description: "shpc-registry automated BioContainers addition for effectivet3"
config: {"url": "https://biocontainers.pro/tools/effectivet3", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for effectivet3", "latest": {"1.0.1--py35_0": "sha256:b516f07ffee3469afa4e67f0f7576e31ed3bff326ca7758f9d94e6e152aeb2db"}, "tags": {"1.0.1--py35_0": "sha256:b516f07ffee3469afa4e67f0f7576e31ed3bff326ca7758f9d94e6e152aeb2db"}, "docker": "quay.io/biocontainers/effectivet3", "aliases": {"effectivet3": "/usr/local/bin/effectivet3", "2to3-3.5": "/usr/local/bin/2to3-3.5", "appletviewer": "/usr/local/bin/appletviewer", "easy_install-3.5": "/usr/local/bin/easy_install-3.5", "extcheck": "/usr/local/bin/extcheck", "idle3.5": "/usr/local/bin/idle3.5", "idlj": "/usr/local/bin/idlj", "jar": "/usr/local/bin/jar", "jarsigner": "/usr/local/bin/jarsigner", "java": "/usr/local/bin/java", "java-rmi.cgi": "/usr/local/bin/java-rmi.cgi"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/effectivet3.
shpc-registry automated BioContainers addition for effectivet3
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/effectivet3
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/effectivet3:1.0.1--py35_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/effectivet3/1.0.1--py35_0
$ module help quay.io/biocontainers/effectivet3/1.0.1--py35_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### effectivet3-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### effectivet3-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### effectivet3-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### effectivet3-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### effectivet3-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### effectivet3-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### effectivet3

```bash
$ singularity exec <container> /usr/local/bin/effectivet3
$ podman run --it --rm --entrypoint /usr/local/bin/effectivet3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/effectivet3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.5

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.5
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### appletviewer

```bash
$ singularity exec <container> /usr/local/bin/appletviewer
$ podman run --it --rm --entrypoint /usr/local/bin/appletviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/appletviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### easy_install-3.5

```bash
$ singularity exec <container> /usr/local/bin/easy_install-3.5
$ podman run --it --rm --entrypoint /usr/local/bin/easy_install-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easy_install-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extcheck

```bash
$ singularity exec <container> /usr/local/bin/extcheck
$ podman run --it --rm --entrypoint /usr/local/bin/extcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.5

```bash
$ singularity exec <container> /usr/local/bin/idle3.5
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### java-rmi.cgi

```bash
$ singularity exec <container> /usr/local/bin/java-rmi.cgi
$ podman run --it --rm --entrypoint /usr/local/bin/java-rmi.cgi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/java-rmi.cgi   -v ${PWD} -w ${PWD} <container> -c " $@"
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
---
layout: container
name:  "quay.io/biocontainers/strudel"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/strudel/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/strudel/container.yaml"
updated_at: "2022-10-29 05:58:55.001515"
latest: "1.15.08.25--1"
container_url: "https://biocontainers.pro/tools/strudel"
aliases:
 - "strudel"
 - "appletviewer"
 - "extcheck"
 - "idlj"
 - "jar"
 - "jarsigner"
 - "java"
 - "java-rmi.cgi"
 - "javac"
 - "javadoc"
 - "javah"
versions:
 - "1.15.08.25--1"
description: "shpc-registry automated BioContainers addition for strudel"
config: {"url": "https://biocontainers.pro/tools/strudel", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for strudel", "latest": {"1.15.08.25--1": "sha256:2779a69ceecd13a9a430d6f791c1f9fad4eabfba31c66ffd553b4dcf66f16d0b"}, "tags": {"1.15.08.25--1": "sha256:2779a69ceecd13a9a430d6f791c1f9fad4eabfba31c66ffd553b4dcf66f16d0b"}, "docker": "quay.io/biocontainers/strudel", "aliases": {"strudel": "/usr/local/bin/strudel", "appletviewer": "/usr/local/bin/appletviewer", "extcheck": "/usr/local/bin/extcheck", "idlj": "/usr/local/bin/idlj", "jar": "/usr/local/bin/jar", "jarsigner": "/usr/local/bin/jarsigner", "java": "/usr/local/bin/java", "java-rmi.cgi": "/usr/local/bin/java-rmi.cgi", "javac": "/usr/local/bin/javac", "javadoc": "/usr/local/bin/javadoc", "javah": "/usr/local/bin/javah"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/strudel.
shpc-registry automated BioContainers addition for strudel
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/strudel
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/strudel:1.15.08.25--1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/strudel/1.15.08.25--1
$ module help quay.io/biocontainers/strudel/1.15.08.25--1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### strudel-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### strudel-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### strudel-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### strudel-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### strudel-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### strudel-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### strudel

```bash
$ singularity exec <container> /usr/local/bin/strudel
$ podman run --it --rm --entrypoint /usr/local/bin/strudel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/strudel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### appletviewer

```bash
$ singularity exec <container> /usr/local/bin/appletviewer
$ podman run --it --rm --entrypoint /usr/local/bin/appletviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/appletviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extcheck

```bash
$ singularity exec <container> /usr/local/bin/extcheck
$ podman run --it --rm --entrypoint /usr/local/bin/extcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### javac

```bash
$ singularity exec <container> /usr/local/bin/javac
$ podman run --it --rm --entrypoint /usr/local/bin/javac   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/javac   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### javadoc

```bash
$ singularity exec <container> /usr/local/bin/javadoc
$ podman run --it --rm --entrypoint /usr/local/bin/javadoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/javadoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### javah

```bash
$ singularity exec <container> /usr/local/bin/javah
$ podman run --it --rm --entrypoint /usr/local/bin/javah   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/javah   -v ${PWD} -w ${PWD} <container> -c " $@"
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
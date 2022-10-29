---
layout: container
name:  "quay.io/biocontainers/beast2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/beast2/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/beast2/container.yaml"
updated_at: "2022-10-29 05:36:38.649174"
latest: "2.6.3--hf1b8bbb_0"
container_url: "https://biocontainers.pro/tools/beast2"
aliases:
 - "applauncher"
 - "beast"
 - "beauti"
 - "densitree"
 - "loganalyser"
 - "logcombiner"
 - "packagemanager"
 - "treeannotator"
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
 - "2.6.3--hf1b8bbb_0"
description: "shpc-registry automated BioContainers addition for beast2"
config: {"docker": "quay.io/biocontainers/beast2", "url": "https://biocontainers.pro/tools/beast2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for beast2", "latest": {"2.6.3--hf1b8bbb_0": "sha256:e1445642dc3d56960309cfe8a6d7720650606f5577485eb16038fb9abb015d1d"}, "tags": {"2.6.3--hf1b8bbb_0": "sha256:e1445642dc3d56960309cfe8a6d7720650606f5577485eb16038fb9abb015d1d"}, "aliases": {"applauncher": "/usr/local/bin/applauncher", "beast": "/usr/local/bin/beast", "beauti": "/usr/local/bin/beauti", "densitree": "/usr/local/bin/densitree", "loganalyser": "/usr/local/bin/loganalyser", "logcombiner": "/usr/local/bin/logcombiner", "packagemanager": "/usr/local/bin/packagemanager", "treeannotator": "/usr/local/bin/treeannotator", "appletviewer": "/usr/local/bin/appletviewer", "extcheck": "/usr/local/bin/extcheck", "idlj": "/usr/local/bin/idlj", "jar": "/usr/local/bin/jar", "jarsigner": "/usr/local/bin/jarsigner", "java": "/usr/local/bin/java", "java-rmi.cgi": "/usr/local/bin/java-rmi.cgi", "javac": "/usr/local/bin/javac", "javadoc": "/usr/local/bin/javadoc", "javah": "/usr/local/bin/javah"}, "env": {"DISPLAY": ""}, "features": {"home": true}}
---

This module is a singularity container wrapper for quay.io/biocontainers/beast2.
shpc-registry automated BioContainers addition for beast2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/beast2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/beast2:2.6.3--hf1b8bbb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/beast2/2.6.3--hf1b8bbb_0
$ module help quay.io/biocontainers/beast2/2.6.3--hf1b8bbb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### beast2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### beast2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### beast2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### beast2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### beast2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### beast2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### applauncher

```bash
$ singularity exec <container> /usr/local/bin/applauncher
$ podman run --it --rm --entrypoint /usr/local/bin/applauncher   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/applauncher   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### beast

```bash
$ singularity exec <container> /usr/local/bin/beast
$ podman run --it --rm --entrypoint /usr/local/bin/beast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/beast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### beauti

```bash
$ singularity exec <container> /usr/local/bin/beauti
$ podman run --it --rm --entrypoint /usr/local/bin/beauti   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/beauti   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### densitree

```bash
$ singularity exec <container> /usr/local/bin/densitree
$ podman run --it --rm --entrypoint /usr/local/bin/densitree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/densitree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### loganalyser

```bash
$ singularity exec <container> /usr/local/bin/loganalyser
$ podman run --it --rm --entrypoint /usr/local/bin/loganalyser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/loganalyser   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### logcombiner

```bash
$ singularity exec <container> /usr/local/bin/logcombiner
$ podman run --it --rm --entrypoint /usr/local/bin/logcombiner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/logcombiner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### packagemanager

```bash
$ singularity exec <container> /usr/local/bin/packagemanager
$ podman run --it --rm --entrypoint /usr/local/bin/packagemanager   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/packagemanager   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### treeannotator

```bash
$ singularity exec <container> /usr/local/bin/treeannotator
$ podman run --it --rm --entrypoint /usr/local/bin/treeannotator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/treeannotator   -v ${PWD} -w ${PWD} <container> -c " $@"
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
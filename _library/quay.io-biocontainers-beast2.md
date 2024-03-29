---
layout: container
name:  "quay.io/biocontainers/beast2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/beast2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/beast2/container.yaml"
updated_at: "2024-03-29 02:31:04.170595"
latest: "2.6.3--he65b2d3_2"
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
 - "extcheck"
 - "java-rmi.cgi"
 - "javah"
 - "jhat"
 - "jsadebugd"
 - "native2ascii"
 - "policytool"
 - "appletviewer"
 - "idlj"
 - "orbd"
versions:
 - "2.6.3--hf1b8bbb_0"
 - "2.6.3--hadc2ddb_1"
 - "2.6.3--he65b2d3_2"
description: "shpc-registry automated BioContainers addition for beast2"
config: {"url": "https://biocontainers.pro/tools/beast2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for beast2", "latest": {"2.6.3--he65b2d3_2": "sha256:d34d0211431e84d6f27dfb7a13954d51fb1a2597ffbebe2f99bebd2c1a292989"}, "tags": {"2.6.3--hf1b8bbb_0": "sha256:e1445642dc3d56960309cfe8a6d7720650606f5577485eb16038fb9abb015d1d", "2.6.3--hadc2ddb_1": "sha256:25798ed4d280574b7f6aa6cb6d32d2abe23d7a70f1dbb589140270358aef887d", "2.6.3--he65b2d3_2": "sha256:d34d0211431e84d6f27dfb7a13954d51fb1a2597ffbebe2f99bebd2c1a292989"}, "docker": "quay.io/biocontainers/beast2", "aliases": {"applauncher": "/usr/local/bin/applauncher", "beast": "/usr/local/bin/beast", "beauti": "/usr/local/bin/beauti", "densitree": "/usr/local/bin/densitree", "loganalyser": "/usr/local/bin/loganalyser", "logcombiner": "/usr/local/bin/logcombiner", "packagemanager": "/usr/local/bin/packagemanager", "treeannotator": "/usr/local/bin/treeannotator", "extcheck": "/usr/local/bin/extcheck", "java-rmi.cgi": "/usr/local/bin/java-rmi.cgi", "javah": "/usr/local/bin/javah", "jhat": "/usr/local/bin/jhat", "jsadebugd": "/usr/local/bin/jsadebugd", "native2ascii": "/usr/local/bin/native2ascii", "policytool": "/usr/local/bin/policytool", "appletviewer": "/usr/local/bin/appletviewer", "idlj": "/usr/local/bin/idlj", "orbd": "/usr/local/bin/orbd"}, "env": {"DISPLAY": "", "JAVA_HOME": "", "JAVA_ROOT": "", "JAVA_BINDIR": ""}, "features": {"home": true}}
---

This module is a singularity container wrapper for quay.io/biocontainers/beast2.
shpc-registry automated BioContainers addition for beast2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/beast2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/beast2:2.6.3--he65b2d3_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/beast2/2.6.3--he65b2d3_2
$ module help quay.io/biocontainers/beast2/2.6.3--he65b2d3_2
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


#### extcheck

```bash
$ singularity exec <container> /usr/local/bin/extcheck
$ podman run --it --rm --entrypoint /usr/local/bin/extcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### java-rmi.cgi

```bash
$ singularity exec <container> /usr/local/bin/java-rmi.cgi
$ podman run --it --rm --entrypoint /usr/local/bin/java-rmi.cgi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/java-rmi.cgi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### javah

```bash
$ singularity exec <container> /usr/local/bin/javah
$ podman run --it --rm --entrypoint /usr/local/bin/javah   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/javah   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jhat

```bash
$ singularity exec <container> /usr/local/bin/jhat
$ podman run --it --rm --entrypoint /usr/local/bin/jhat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jhat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsadebugd

```bash
$ singularity exec <container> /usr/local/bin/jsadebugd
$ podman run --it --rm --entrypoint /usr/local/bin/jsadebugd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsadebugd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### native2ascii

```bash
$ singularity exec <container> /usr/local/bin/native2ascii
$ podman run --it --rm --entrypoint /usr/local/bin/native2ascii   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/native2ascii   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### policytool

```bash
$ singularity exec <container> /usr/local/bin/policytool
$ podman run --it --rm --entrypoint /usr/local/bin/policytool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/policytool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### appletviewer

```bash
$ singularity exec <container> /usr/local/bin/appletviewer
$ podman run --it --rm --entrypoint /usr/local/bin/appletviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/appletviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idlj

```bash
$ singularity exec <container> /usr/local/bin/idlj
$ podman run --it --rm --entrypoint /usr/local/bin/idlj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idlj   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orbd

```bash
$ singularity exec <container> /usr/local/bin/orbd
$ podman run --it --rm --entrypoint /usr/local/bin/orbd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orbd   -v ${PWD} -w ${PWD} <container> -c " $@"
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
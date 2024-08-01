---
layout: container
name:  "quay.io/biocontainers/astral-tree"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/astral-tree/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/astral-tree/container.yaml"
updated_at: "2024-08-01 03:16:51.348052"
latest: "5.7.8--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/astral-tree"
aliases:
 - "astral"
 - "jfr"
 - "jaotc"
 - "aserver"
 - "jdeprscan"
 - "jhsdb"
 - "jimage"
 - "jlink"
 - "jmod"
 - "jshell"
 - "jjs"
 - "pack200"
 - "rmic"
 - "rmid"
 - "unpack200"
 - "jdeps"
 - "jar"
 - "jarsigner"
 - "java"
 - "javac"
 - "javadoc"
 - "javap"
 - "jcmd"
 - "jconsole"
 - "jdb"
 - "jinfo"
versions:
 - "5.7.8--hdfd78af_0"
 - "5.7.8--hdfd78af_1"
description: "singularity registry hpc automated addition for astral-tree"
config: {"url": "https://biocontainers.pro/tools/astral-tree", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for astral-tree", "latest": {"5.7.8--hdfd78af_1": "sha256:7a80d997d6aa3efeea158016912addb858a5e6e435f79a4e3c45d8deb6af2d78"}, "tags": {"5.7.8--hdfd78af_0": "sha256:79a44e8ce8fb2d25bf7cad5cd6622e184e57a456d21462159914c11eb03713a4", "5.7.8--hdfd78af_1": "sha256:7a80d997d6aa3efeea158016912addb858a5e6e435f79a4e3c45d8deb6af2d78"}, "docker": "quay.io/biocontainers/astral-tree", "aliases": {"astral": "/usr/local/bin/astral", "jfr": "/usr/local/bin/jfr", "jaotc": "/usr/local/bin/jaotc", "aserver": "/usr/local/bin/aserver", "jdeprscan": "/usr/local/bin/jdeprscan", "jhsdb": "/usr/local/bin/jhsdb", "jimage": "/usr/local/bin/jimage", "jlink": "/usr/local/bin/jlink", "jmod": "/usr/local/bin/jmod", "jshell": "/usr/local/bin/jshell", "jjs": "/usr/local/bin/jjs", "pack200": "/usr/local/bin/pack200", "rmic": "/usr/local/bin/rmic", "rmid": "/usr/local/bin/rmid", "unpack200": "/usr/local/bin/unpack200", "jdeps": "/usr/local/bin/jdeps", "jar": "/usr/local/bin/jar", "jarsigner": "/usr/local/bin/jarsigner", "java": "/usr/local/bin/java", "javac": "/usr/local/bin/javac", "javadoc": "/usr/local/bin/javadoc", "javap": "/usr/local/bin/javap", "jcmd": "/usr/local/bin/jcmd", "jconsole": "/usr/local/bin/jconsole", "jdb": "/usr/local/bin/jdb", "jinfo": "/usr/local/bin/jinfo"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/astral-tree.
singularity registry hpc automated addition for astral-tree
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/astral-tree
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/astral-tree:5.7.8--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/astral-tree/5.7.8--hdfd78af_1
$ module help quay.io/biocontainers/astral-tree/5.7.8--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### astral-tree-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### astral-tree-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### astral-tree-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### astral-tree-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### astral-tree-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### astral-tree-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### astral

```bash
$ singularity exec <container> /usr/local/bin/astral
$ podman run --it --rm --entrypoint /usr/local/bin/astral   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/astral   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jfr

```bash
$ singularity exec <container> /usr/local/bin/jfr
$ podman run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jaotc

```bash
$ singularity exec <container> /usr/local/bin/jaotc
$ podman run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jdeprscan

```bash
$ singularity exec <container> /usr/local/bin/jdeprscan
$ podman run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jhsdb

```bash
$ singularity exec <container> /usr/local/bin/jhsdb
$ podman run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jimage

```bash
$ singularity exec <container> /usr/local/bin/jimage
$ podman run --it --rm --entrypoint /usr/local/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jlink

```bash
$ singularity exec <container> /usr/local/bin/jlink
$ podman run --it --rm --entrypoint /usr/local/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jmod

```bash
$ singularity exec <container> /usr/local/bin/jmod
$ podman run --it --rm --entrypoint /usr/local/bin/jmod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jmod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jshell

```bash
$ singularity exec <container> /usr/local/bin/jshell
$ podman run --it --rm --entrypoint /usr/local/bin/jshell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jshell   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jjs

```bash
$ singularity exec <container> /usr/local/bin/jjs
$ podman run --it --rm --entrypoint /usr/local/bin/jjs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jjs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pack200

```bash
$ singularity exec <container> /usr/local/bin/pack200
$ podman run --it --rm --entrypoint /usr/local/bin/pack200   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pack200   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rmic

```bash
$ singularity exec <container> /usr/local/bin/rmic
$ podman run --it --rm --entrypoint /usr/local/bin/rmic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rmic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rmid

```bash
$ singularity exec <container> /usr/local/bin/rmid
$ podman run --it --rm --entrypoint /usr/local/bin/rmid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rmid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unpack200

```bash
$ singularity exec <container> /usr/local/bin/unpack200
$ podman run --it --rm --entrypoint /usr/local/bin/unpack200   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unpack200   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jdeps

```bash
$ singularity exec <container> /usr/local/bin/jdeps
$ podman run --it --rm --entrypoint /usr/local/bin/jdeps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jdeps   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### javap

```bash
$ singularity exec <container> /usr/local/bin/javap
$ podman run --it --rm --entrypoint /usr/local/bin/javap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/javap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jcmd

```bash
$ singularity exec <container> /usr/local/bin/jcmd
$ podman run --it --rm --entrypoint /usr/local/bin/jcmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jcmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jconsole

```bash
$ singularity exec <container> /usr/local/bin/jconsole
$ podman run --it --rm --entrypoint /usr/local/bin/jconsole   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jconsole   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jdb

```bash
$ singularity exec <container> /usr/local/bin/jdb
$ podman run --it --rm --entrypoint /usr/local/bin/jdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jinfo

```bash
$ singularity exec <container> /usr/local/bin/jinfo
$ podman run --it --rm --entrypoint /usr/local/bin/jinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
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
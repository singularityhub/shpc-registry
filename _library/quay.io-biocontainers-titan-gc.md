---
layout: container
name:  "quay.io/biocontainers/titan-gc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/titan-gc/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/titan-gc/container.yaml"
updated_at: "2022-10-29 05:31:41.663222"
latest: "1.5.3--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/titan-gc"
aliases:
 - "cromwell"
 - "find"
 - "locate"
 - "titan-gc"
 - "titan-gc-organize.py"
 - "titan-gc-prepare.py"
 - "updatedb"
 - "womtool"
 - "xargs"
 - "aserver"
 - "jaotc"
 - "jar"
 - "jarsigner"
 - "java"
 - "javac"
 - "javadoc"
 - "javap"
 - "jcmd"
 - "jconsole"
versions:
 - "1.5.3--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for titan-gc"
config: {"url": "https://biocontainers.pro/tools/titan-gc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for titan-gc", "latest": {"1.5.3--hdfd78af_1": "sha256:4d24c7175705d1c147c903308fbc5f79a1f3af965abb5bd6a29947b4b1c0a6b3"}, "tags": {"1.5.3--hdfd78af_1": "sha256:4d24c7175705d1c147c903308fbc5f79a1f3af965abb5bd6a29947b4b1c0a6b3"}, "docker": "quay.io/biocontainers/titan-gc", "aliases": {"cromwell": "/usr/local/bin/cromwell", "find": "/usr/local/bin/find", "locate": "/usr/local/bin/locate", "titan-gc": "/usr/local/bin/titan-gc", "titan-gc-organize.py": "/usr/local/bin/titan-gc-organize.py", "titan-gc-prepare.py": "/usr/local/bin/titan-gc-prepare.py", "updatedb": "/usr/local/bin/updatedb", "womtool": "/usr/local/bin/womtool", "xargs": "/usr/local/bin/xargs", "aserver": "/usr/local/bin/aserver", "jaotc": "/usr/local/bin/jaotc", "jar": "/usr/local/bin/jar", "jarsigner": "/usr/local/bin/jarsigner", "java": "/usr/local/bin/java", "javac": "/usr/local/bin/javac", "javadoc": "/usr/local/bin/javadoc", "javap": "/usr/local/bin/javap", "jcmd": "/usr/local/bin/jcmd", "jconsole": "/usr/local/bin/jconsole"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/titan-gc.
shpc-registry automated BioContainers addition for titan-gc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/titan-gc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/titan-gc:1.5.3--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/titan-gc/1.5.3--hdfd78af_1
$ module help quay.io/biocontainers/titan-gc/1.5.3--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### titan-gc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### titan-gc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### titan-gc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### titan-gc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### titan-gc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### titan-gc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cromwell

```bash
$ singularity exec <container> /usr/local/bin/cromwell
$ podman run --it --rm --entrypoint /usr/local/bin/cromwell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cromwell   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find

```bash
$ singularity exec <container> /usr/local/bin/find
$ podman run --it --rm --entrypoint /usr/local/bin/find   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### locate

```bash
$ singularity exec <container> /usr/local/bin/locate
$ podman run --it --rm --entrypoint /usr/local/bin/locate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/locate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### titan-gc

```bash
$ singularity exec <container> /usr/local/bin/titan-gc
$ podman run --it --rm --entrypoint /usr/local/bin/titan-gc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/titan-gc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### titan-gc-organize.py

```bash
$ singularity exec <container> /usr/local/bin/titan-gc-organize.py
$ podman run --it --rm --entrypoint /usr/local/bin/titan-gc-organize.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/titan-gc-organize.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### titan-gc-prepare.py

```bash
$ singularity exec <container> /usr/local/bin/titan-gc-prepare.py
$ podman run --it --rm --entrypoint /usr/local/bin/titan-gc-prepare.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/titan-gc-prepare.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### updatedb

```bash
$ singularity exec <container> /usr/local/bin/updatedb
$ podman run --it --rm --entrypoint /usr/local/bin/updatedb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/updatedb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### womtool

```bash
$ singularity exec <container> /usr/local/bin/womtool
$ podman run --it --rm --entrypoint /usr/local/bin/womtool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/womtool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xargs

```bash
$ singularity exec <container> /usr/local/bin/xargs
$ podman run --it --rm --entrypoint /usr/local/bin/xargs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xargs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jaotc

```bash
$ singularity exec <container> /usr/local/bin/jaotc
$ podman run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
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
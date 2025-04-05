---
layout: container
name:  "ghcr.io/autamus/openjdk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/openjdk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/openjdk/container.yaml"
updated_at: "2025-04-05 03:47:06.411892"
latest: "latest"
container_url: "https://github.com/orgs/autamus/packages/container/package/openjdk"
aliases:
 - "jaotc"
 - "jar"
 - "jarsigner"
 - "java"
 - "javac"
 - "javadoc"
 - "javap"
 - "jcmd"
 - "jconsole"
 - "jdb"
 - "jdeps"
 - "jfr"
 - "jhsdb"
 - "jimage"
 - "jinfo"
 - "jjs"
 - "jlink"
 - "jmap"
 - "jmod"
 - "jps"
 - "jrunscript"
 - "jshell"
 - "jstack"
 - "jstat"
 - "jstatd"
versions:
 - "latest"
description: "Open Java Development Kit"
config: {"docker": "ghcr.io/autamus/openjdk", "url": "https://github.com/orgs/autamus/packages/container/package/openjdk", "maintainer": "@vsoch", "description": "Open Java Development Kit", "latest": {"latest": "sha256:697b10d24f6dc12c41f4a7ebcce4ae72b2b6b1bb09d1f3e636b1ca57ec63cd0f"}, "tags": {"latest": "sha256:697b10d24f6dc12c41f4a7ebcce4ae72b2b6b1bb09d1f3e636b1ca57ec63cd0f"}, "aliases": {"jaotc": "/opt/view/bin/jaotc", "jar": "/opt/view/bin/jar", "jarsigner": "/opt/view/bin/jarsigner", "java": "/opt/view/bin/java", "javac": "/opt/view/bin/javac", "javadoc": "/opt/view/bin/javadoc", "javap": "/opt/view/bin/javap", "jcmd": "/opt/view/bin/jcmd", "jconsole": "/opt/view/bin/jconsole", "jdb": "/opt/view/bin/jdb", "jdeps": "/opt/view/bin/jdeps", "jfr": "/opt/view/bin/jfr", "jhsdb": "/opt/view/bin/jhsdb", "jimage": "/opt/view/bin/jimage", "jinfo": "/opt/view/bin/jinfo", "jjs": "/opt/view/bin/jjs", "jlink": "/opt/view/bin/jlink", "jmap": "/opt/view/bin/jmap", "jmod": "/opt/view/bin/jmod", "jps": "/opt/view/bin/jps", "jrunscript": "/opt/view/bin/jrunscript", "jshell": "/opt/view/bin/jshell", "jstack": "/opt/view/bin/jstack", "jstat": "/opt/view/bin/jstat", "jstatd": "/opt/view/bin/jstatd"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/openjdk.
Open Java Development Kit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/openjdk
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/openjdk:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/openjdk/latest
$ module help ghcr.io/autamus/openjdk/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### openjdk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### openjdk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### openjdk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### openjdk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### openjdk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### openjdk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### jaotc

```bash
$ singularity exec <container> /opt/view/bin/jaotc
$ podman run --it --rm --entrypoint /opt/view/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jar

```bash
$ singularity exec <container> /opt/view/bin/jar
$ podman run --it --rm --entrypoint /opt/view/bin/jar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/jar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jarsigner

```bash
$ singularity exec <container> /opt/view/bin/jarsigner
$ podman run --it --rm --entrypoint /opt/view/bin/jarsigner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/jarsigner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### java

```bash
$ singularity exec <container> /opt/view/bin/java
$ podman run --it --rm --entrypoint /opt/view/bin/java   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/java   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### javac

```bash
$ singularity exec <container> /opt/view/bin/javac
$ podman run --it --rm --entrypoint /opt/view/bin/javac   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/javac   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### javadoc

```bash
$ singularity exec <container> /opt/view/bin/javadoc
$ podman run --it --rm --entrypoint /opt/view/bin/javadoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/javadoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### javap

```bash
$ singularity exec <container> /opt/view/bin/javap
$ podman run --it --rm --entrypoint /opt/view/bin/javap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/javap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jcmd

```bash
$ singularity exec <container> /opt/view/bin/jcmd
$ podman run --it --rm --entrypoint /opt/view/bin/jcmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/jcmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jconsole

```bash
$ singularity exec <container> /opt/view/bin/jconsole
$ podman run --it --rm --entrypoint /opt/view/bin/jconsole   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/jconsole   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jdb

```bash
$ singularity exec <container> /opt/view/bin/jdb
$ podman run --it --rm --entrypoint /opt/view/bin/jdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/jdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jdeps

```bash
$ singularity exec <container> /opt/view/bin/jdeps
$ podman run --it --rm --entrypoint /opt/view/bin/jdeps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/jdeps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jfr

```bash
$ singularity exec <container> /opt/view/bin/jfr
$ podman run --it --rm --entrypoint /opt/view/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jhsdb

```bash
$ singularity exec <container> /opt/view/bin/jhsdb
$ podman run --it --rm --entrypoint /opt/view/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jimage

```bash
$ singularity exec <container> /opt/view/bin/jimage
$ podman run --it --rm --entrypoint /opt/view/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jinfo

```bash
$ singularity exec <container> /opt/view/bin/jinfo
$ podman run --it --rm --entrypoint /opt/view/bin/jinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/jinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jjs

```bash
$ singularity exec <container> /opt/view/bin/jjs
$ podman run --it --rm --entrypoint /opt/view/bin/jjs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/jjs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jlink

```bash
$ singularity exec <container> /opt/view/bin/jlink
$ podman run --it --rm --entrypoint /opt/view/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jmap

```bash
$ singularity exec <container> /opt/view/bin/jmap
$ podman run --it --rm --entrypoint /opt/view/bin/jmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/jmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jmod

```bash
$ singularity exec <container> /opt/view/bin/jmod
$ podman run --it --rm --entrypoint /opt/view/bin/jmod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/jmod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jps

```bash
$ singularity exec <container> /opt/view/bin/jps
$ podman run --it --rm --entrypoint /opt/view/bin/jps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/jps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jrunscript

```bash
$ singularity exec <container> /opt/view/bin/jrunscript
$ podman run --it --rm --entrypoint /opt/view/bin/jrunscript   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/jrunscript   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jshell

```bash
$ singularity exec <container> /opt/view/bin/jshell
$ podman run --it --rm --entrypoint /opt/view/bin/jshell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/jshell   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jstack

```bash
$ singularity exec <container> /opt/view/bin/jstack
$ podman run --it --rm --entrypoint /opt/view/bin/jstack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/jstack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jstat

```bash
$ singularity exec <container> /opt/view/bin/jstat
$ podman run --it --rm --entrypoint /opt/view/bin/jstat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/jstat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jstatd

```bash
$ singularity exec <container> /opt/view/bin/jstatd
$ podman run --it --rm --entrypoint /opt/view/bin/jstatd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/jstatd   -v ${PWD} -w ${PWD} <container> -c " $@"
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
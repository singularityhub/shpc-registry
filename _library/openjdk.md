---
layout: container
name:  "openjdk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/openjdk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/openjdk/container.yaml"
updated_at: "2024-12-18 03:47:14.419507"
latest: "25"
container_url: "https://hub.docker.com/_/openjdk"
aliases:
 - "jar"
 - "jarsigner"
 - "java"
 - "javac"
 - "javadoc"
 - "javap"
 - "jcmd"
 - "jconsole"
 - "jdb"
 - "jdeprscan"
 - "jdeps"
 - "jfr"
 - "jhsdb"
 - "jimage"
 - "jinfo"
 - "jlink"
 - "jmap"
 - "jmod"
 - "jobs"
 - "join"
 - "jpackage"
 - "jps"
 - "jrunscript"
 - "jshell"
 - "jstack"
 - "jstat"
 - "jstatd"
versions:
 - "16.0.1-buster"
 - "16.0.2"
 - "17.0.1"
 - "17.0.2"
 - "latest"
 - "19"
 - "19-alpine3.15"
 - "18"
 - "18-alpine3.15"
 - "17"
 - "18.0"
 - "19-alpine3.16"
 - "20"
 - "21"
 - "22"
 - "24"
 - "23"
 - "25"
description: "OpenJDK is an open-source implementation of the Java Platform, Standard Edition."
config: {"docker": "openjdk", "url": "https://hub.docker.com/_/openjdk", "maintainer": "@vsoch", "description": "OpenJDK is an open-source implementation of the Java Platform, Standard Edition.", "filter": ["^(?!.*ea).*$", "^(?!.*windows).*$", "^(?!.*nanoserver).*$", "^(?!.*oracle).*$"], "latest": {"25": "sha256:a1524532942ef87969c70e22150a3605ea1599082377522bd048750cac39a3d3"}, "tags": {"16.0.1-buster": "sha256:61f3786a28ed911028f8e7e3b65a57a8a9ed04067d137317d369c9b3bc11b289", "16.0.2": "sha256:bb68f084c2000c8532b1675ca7034f3922f4aa10e9c7126d29551c0ffd6dee8f", "17.0.1": "sha256:0da39ed69dec14f9603e2b916592691cc39341510abdf4255abb1c90b00eb3f4", "17.0.2": "sha256:528707081fdb9562eb819128a9f85ae7fe000e2fbaeaf9f87662e7b3f38cb7d8", "latest": "sha256:9b448de897d211c9e0ec635a485650aed6e28d4eca1efbc34940560a480b3f1f", "19": "sha256:4123be55fd6853980020c59e7530d017ea08996abbe71741a51c62f7b7586bee", "19-alpine3.15": "sha256:00b9080d669d1997313721aa3ed907ab1cac2df3019e5781a4682c9511d08bbb", "18": "sha256:9b448de897d211c9e0ec635a485650aed6e28d4eca1efbc34940560a480b3f1f", "18-alpine3.15": "sha256:e5c5b35b831a4f655074a25604130ce53e33567b82c8a7204f0e5641b66d477e", "17": "sha256:528707081fdb9562eb819128a9f85ae7fe000e2fbaeaf9f87662e7b3f38cb7d8", "18.0": "sha256:9b448de897d211c9e0ec635a485650aed6e28d4eca1efbc34940560a480b3f1f", "19-alpine3.16": "sha256:1686909f4ca66f3e13463e2b00a1c53808aa155f81ae9a8aad8f4b89420d91ef", "20": "sha256:cbf26a2c1a9c347a907a5ceb2edad13dc0e9cc22464cef5861ac6d278e730322", "21": "sha256:af9de795d1f8d3b6172f6c55ca9ba1c5768baa11bb2dc8af7045c7db9d4c33ac", "22": "sha256:b7d44427f4622d3f6b9a60583e5218ecfa8b4e44f3e01dfd0d9b7d7abba31c9a", "24": "sha256:893b4dbab5c52e784c6eb5635575944f6524d5d31a97f096631c6a7d8608eb20", "23": "sha256:fd0f3721ad4abbfe393ac1a2672abf4b7f53b5ecd9803a4e2444aa3acd7d398e", "25": "sha256:a1524532942ef87969c70e22150a3605ea1599082377522bd048750cac39a3d3"}, "aliases": {"jar": "/usr/bin/jar", "jarsigner": "/usr/bin/jarsigner", "java": "/usr/bin/java", "javac": "/usr/bin/javac", "javadoc": "/usr/bin/javadoc", "javap": "/usr/bin/javap", "jcmd": "/usr/bin/jcmd", "jconsole": "/usr/bin/jconsole", "jdb": "/usr/bin/jdb", "jdeprscan": "/usr/bin/jdeprscan", "jdeps": "/usr/bin/jdeps", "jfr": "/usr/bin/jfr", "jhsdb": "/usr/bin/jhsdb", "jimage": "/usr/bin/jimage", "jinfo": "/usr/bin/jinfo", "jlink": "/usr/bin/jlink", "jmap": "/usr/bin/jmap", "jmod": "/usr/bin/jmod", "jobs": "/usr/bin/jobs", "join": "/usr/bin/join", "jpackage": "/usr/bin/jpackage", "jps": "/usr/bin/jps", "jrunscript": "/usr/bin/jrunscript", "jshell": "/usr/bin/jshell", "jstack": "/usr/bin/jstack", "jstat": "/usr/bin/jstat", "jstatd": "/usr/bin/jstatd"}}
---

This module is a singularity container wrapper for openjdk.
OpenJDK is an open-source implementation of the Java Platform, Standard Edition.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install openjdk
```

Or a specific version:

```bash
$ shpc install openjdk:25
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load openjdk/25
$ module help openjdk/25
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


#### jar

```bash
$ singularity exec <container> /usr/bin/jar
$ podman run --it --rm --entrypoint /usr/bin/jar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jarsigner

```bash
$ singularity exec <container> /usr/bin/jarsigner
$ podman run --it --rm --entrypoint /usr/bin/jarsigner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jarsigner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### java

```bash
$ singularity exec <container> /usr/bin/java
$ podman run --it --rm --entrypoint /usr/bin/java   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/java   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### javac

```bash
$ singularity exec <container> /usr/bin/javac
$ podman run --it --rm --entrypoint /usr/bin/javac   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/javac   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### javadoc

```bash
$ singularity exec <container> /usr/bin/javadoc
$ podman run --it --rm --entrypoint /usr/bin/javadoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/javadoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### javap

```bash
$ singularity exec <container> /usr/bin/javap
$ podman run --it --rm --entrypoint /usr/bin/javap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/javap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jcmd

```bash
$ singularity exec <container> /usr/bin/jcmd
$ podman run --it --rm --entrypoint /usr/bin/jcmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jcmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jconsole

```bash
$ singularity exec <container> /usr/bin/jconsole
$ podman run --it --rm --entrypoint /usr/bin/jconsole   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jconsole   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jdb

```bash
$ singularity exec <container> /usr/bin/jdb
$ podman run --it --rm --entrypoint /usr/bin/jdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jdeprscan

```bash
$ singularity exec <container> /usr/bin/jdeprscan
$ podman run --it --rm --entrypoint /usr/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jdeps

```bash
$ singularity exec <container> /usr/bin/jdeps
$ podman run --it --rm --entrypoint /usr/bin/jdeps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jdeps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jfr

```bash
$ singularity exec <container> /usr/bin/jfr
$ podman run --it --rm --entrypoint /usr/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jhsdb

```bash
$ singularity exec <container> /usr/bin/jhsdb
$ podman run --it --rm --entrypoint /usr/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jimage

```bash
$ singularity exec <container> /usr/bin/jimage
$ podman run --it --rm --entrypoint /usr/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jinfo

```bash
$ singularity exec <container> /usr/bin/jinfo
$ podman run --it --rm --entrypoint /usr/bin/jinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jlink

```bash
$ singularity exec <container> /usr/bin/jlink
$ podman run --it --rm --entrypoint /usr/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jmap

```bash
$ singularity exec <container> /usr/bin/jmap
$ podman run --it --rm --entrypoint /usr/bin/jmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jmod

```bash
$ singularity exec <container> /usr/bin/jmod
$ podman run --it --rm --entrypoint /usr/bin/jmod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jmod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jobs

```bash
$ singularity exec <container> /usr/bin/jobs
$ podman run --it --rm --entrypoint /usr/bin/jobs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jobs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### join

```bash
$ singularity exec <container> /usr/bin/join
$ podman run --it --rm --entrypoint /usr/bin/join   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/join   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jpackage

```bash
$ singularity exec <container> /usr/bin/jpackage
$ podman run --it --rm --entrypoint /usr/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jps

```bash
$ singularity exec <container> /usr/bin/jps
$ podman run --it --rm --entrypoint /usr/bin/jps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jrunscript

```bash
$ singularity exec <container> /usr/bin/jrunscript
$ podman run --it --rm --entrypoint /usr/bin/jrunscript   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jrunscript   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jshell

```bash
$ singularity exec <container> /usr/bin/jshell
$ podman run --it --rm --entrypoint /usr/bin/jshell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jshell   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jstack

```bash
$ singularity exec <container> /usr/bin/jstack
$ podman run --it --rm --entrypoint /usr/bin/jstack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jstack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jstat

```bash
$ singularity exec <container> /usr/bin/jstat
$ podman run --it --rm --entrypoint /usr/bin/jstat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jstat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jstatd

```bash
$ singularity exec <container> /usr/bin/jstatd
$ podman run --it --rm --entrypoint /usr/bin/jstatd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jstatd   -v ${PWD} -w ${PWD} <container> -c " $@"
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
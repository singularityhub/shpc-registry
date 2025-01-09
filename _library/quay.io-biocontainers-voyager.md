---
layout: container
name:  "quay.io/biocontainers/voyager"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/voyager/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/voyager/container.yaml"
updated_at: "2025-01-09 13:30:14.453151"
latest: "0.1.4--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/voyager"
aliases:
 - "voyager-build-cli"
 - "voyager-cli"
 - "voyager-combine-cli"
 - "voyager-debug-index"
 - "voyager-monitor"
 - "jwebserver"
 - "jpackage"
 - "cups-config"
 - "ippeveprinter"
 - "ipptool"
 - "hb-info"
 - "jfr"
 - "tjbench"
 - "jdeprscan"
 - "jhsdb"
 - "jimage"
 - "jlink"
 - "jmod"
 - "jshell"
 - "aserver"
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
versions:
 - "0.1.0--hdfd78af_0"
 - "0.1.1--hdfd78af_0"
 - "0.1.2--hdfd78af_0"
 - "0.1.3--hdfd78af_0"
 - "0.1.4--hdfd78af_0"
description: "singularity registry hpc automated addition for voyager"
config: {"url": "https://biocontainers.pro/tools/voyager", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for voyager", "latest": {"0.1.4--hdfd78af_0": "sha256:1031781f347737f1a6bb7f9e33f975bccf46d3a49829f801babc696e8da18a0e"}, "tags": {"0.1.0--hdfd78af_0": "sha256:95818ef8131dd39512ca206fe4a50e8ad459f10bb51ae77875bdcc6a918543cc", "0.1.1--hdfd78af_0": "sha256:291ff5e9c7d96a359c1a743620af77c5c1bf7f2530de3db2cb1b841598f230b5", "0.1.2--hdfd78af_0": "sha256:d54f7753cde91ef74a215a53b3932de17f94dcebc5ebc628bfa64339de3f324a", "0.1.3--hdfd78af_0": "sha256:02649a00cc0e01660949eaec54c7e4788cea9506a4800aaaf6b0965dd6d87dd5", "0.1.4--hdfd78af_0": "sha256:1031781f347737f1a6bb7f9e33f975bccf46d3a49829f801babc696e8da18a0e"}, "docker": "quay.io/biocontainers/voyager", "aliases": {"voyager-build-cli": "/usr/local/bin/voyager-build-cli", "voyager-cli": "/usr/local/bin/voyager-cli", "voyager-combine-cli": "/usr/local/bin/voyager-combine-cli", "voyager-debug-index": "/usr/local/bin/voyager-debug-index", "voyager-monitor": "/usr/local/bin/voyager-monitor", "jwebserver": "/usr/local/bin/jwebserver", "jpackage": "/usr/local/bin/jpackage", "cups-config": "/usr/local/bin/cups-config", "ippeveprinter": "/usr/local/bin/ippeveprinter", "ipptool": "/usr/local/bin/ipptool", "hb-info": "/usr/local/bin/hb-info", "jfr": "/usr/local/bin/jfr", "tjbench": "/usr/local/bin/tjbench", "jdeprscan": "/usr/local/bin/jdeprscan", "jhsdb": "/usr/local/bin/jhsdb", "jimage": "/usr/local/bin/jimage", "jlink": "/usr/local/bin/jlink", "jmod": "/usr/local/bin/jmod", "jshell": "/usr/local/bin/jshell", "aserver": "/usr/local/bin/aserver", "jdeps": "/usr/local/bin/jdeps", "jar": "/usr/local/bin/jar", "jarsigner": "/usr/local/bin/jarsigner", "java": "/usr/local/bin/java", "javac": "/usr/local/bin/javac", "javadoc": "/usr/local/bin/javadoc", "javap": "/usr/local/bin/javap", "jcmd": "/usr/local/bin/jcmd", "jconsole": "/usr/local/bin/jconsole", "jdb": "/usr/local/bin/jdb"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/voyager.
singularity registry hpc automated addition for voyager
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/voyager
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/voyager:0.1.4--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/voyager/0.1.4--hdfd78af_0
$ module help quay.io/biocontainers/voyager/0.1.4--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### voyager-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### voyager-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### voyager-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### voyager-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### voyager-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### voyager-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### voyager-build-cli

```bash
$ singularity exec <container> /usr/local/bin/voyager-build-cli
$ podman run --it --rm --entrypoint /usr/local/bin/voyager-build-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/voyager-build-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### voyager-cli

```bash
$ singularity exec <container> /usr/local/bin/voyager-cli
$ podman run --it --rm --entrypoint /usr/local/bin/voyager-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/voyager-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### voyager-combine-cli

```bash
$ singularity exec <container> /usr/local/bin/voyager-combine-cli
$ podman run --it --rm --entrypoint /usr/local/bin/voyager-combine-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/voyager-combine-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### voyager-debug-index

```bash
$ singularity exec <container> /usr/local/bin/voyager-debug-index
$ podman run --it --rm --entrypoint /usr/local/bin/voyager-debug-index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/voyager-debug-index   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### voyager-monitor

```bash
$ singularity exec <container> /usr/local/bin/voyager-monitor
$ podman run --it --rm --entrypoint /usr/local/bin/voyager-monitor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/voyager-monitor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jwebserver

```bash
$ singularity exec <container> /usr/local/bin/jwebserver
$ podman run --it --rm --entrypoint /usr/local/bin/jwebserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jwebserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jpackage

```bash
$ singularity exec <container> /usr/local/bin/jpackage
$ podman run --it --rm --entrypoint /usr/local/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cups-config

```bash
$ singularity exec <container> /usr/local/bin/cups-config
$ podman run --it --rm --entrypoint /usr/local/bin/cups-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cups-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ippeveprinter

```bash
$ singularity exec <container> /usr/local/bin/ippeveprinter
$ podman run --it --rm --entrypoint /usr/local/bin/ippeveprinter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ippeveprinter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipptool

```bash
$ singularity exec <container> /usr/local/bin/ipptool
$ podman run --it --rm --entrypoint /usr/local/bin/ipptool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipptool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jfr

```bash
$ singularity exec <container> /usr/local/bin/jfr
$ podman run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
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
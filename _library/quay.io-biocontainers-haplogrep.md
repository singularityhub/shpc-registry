---
layout: container
name:  "quay.io/biocontainers/haplogrep"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/haplogrep/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/haplogrep/container.yaml"
updated_at: "2022-10-29 05:53:18.184077"
latest: "2.4.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/haplogrep"
aliases:
 - "haplogrep"
 - "haplogrep.jar"
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
 - "2.4.0--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for haplogrep"
config: {"url": "https://biocontainers.pro/tools/haplogrep", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for haplogrep", "latest": {"2.4.0--hdfd78af_0": "sha256:007b643e393117f5de59e5650893591a0f19e9d1fec3da9dabbd6693ba680d7f"}, "tags": {"2.4.0--hdfd78af_0": "sha256:007b643e393117f5de59e5650893591a0f19e9d1fec3da9dabbd6693ba680d7f"}, "docker": "quay.io/biocontainers/haplogrep", "aliases": {"haplogrep": "/usr/local/bin/haplogrep", "haplogrep.jar": "/usr/local/bin/haplogrep.jar", "aserver": "/usr/local/bin/aserver", "jaotc": "/usr/local/bin/jaotc", "jar": "/usr/local/bin/jar", "jarsigner": "/usr/local/bin/jarsigner", "java": "/usr/local/bin/java", "javac": "/usr/local/bin/javac", "javadoc": "/usr/local/bin/javadoc", "javap": "/usr/local/bin/javap", "jcmd": "/usr/local/bin/jcmd", "jconsole": "/usr/local/bin/jconsole"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/haplogrep.
shpc-registry automated BioContainers addition for haplogrep
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/haplogrep
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/haplogrep:2.4.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/haplogrep/2.4.0--hdfd78af_0
$ module help quay.io/biocontainers/haplogrep/2.4.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### haplogrep-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### haplogrep-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### haplogrep-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### haplogrep-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### haplogrep-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### haplogrep-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### haplogrep

```bash
$ singularity exec <container> /usr/local/bin/haplogrep
$ podman run --it --rm --entrypoint /usr/local/bin/haplogrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/haplogrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### haplogrep.jar

```bash
$ singularity exec <container> /usr/local/bin/haplogrep.jar
$ podman run --it --rm --entrypoint /usr/local/bin/haplogrep.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/haplogrep.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
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
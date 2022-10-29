---
layout: container
name:  "quay.io/biocontainers/hmftools-amber"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hmftools-amber/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/hmftools-amber/container.yaml"
updated_at: "2022-10-29 05:53:26.340092"
latest: "3.9--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/hmftools-amber"
aliases:
 - "AMBER"
 - "aserver"
 - "cups-config"
 - "ippeveprinter"
 - "ipptool"
 - "jar"
 - "jarsigner"
 - "java"
 - "javac"
 - "javadoc"
 - "javap"
versions:
 - "3.9--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for hmftools-amber"
config: {"url": "https://biocontainers.pro/tools/hmftools-amber", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hmftools-amber", "latest": {"3.9--hdfd78af_1": "sha256:2735782fa475aed6f552b466dcd7ca4f03e7431e4555f1369d67d088b04d0247"}, "tags": {"3.9--hdfd78af_1": "sha256:2735782fa475aed6f552b466dcd7ca4f03e7431e4555f1369d67d088b04d0247"}, "docker": "quay.io/biocontainers/hmftools-amber", "aliases": {"AMBER": "/usr/local/bin/AMBER", "aserver": "/usr/local/bin/aserver", "cups-config": "/usr/local/bin/cups-config", "ippeveprinter": "/usr/local/bin/ippeveprinter", "ipptool": "/usr/local/bin/ipptool", "jar": "/usr/local/bin/jar", "jarsigner": "/usr/local/bin/jarsigner", "java": "/usr/local/bin/java", "javac": "/usr/local/bin/javac", "javadoc": "/usr/local/bin/javadoc", "javap": "/usr/local/bin/javap"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hmftools-amber.
shpc-registry automated BioContainers addition for hmftools-amber
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hmftools-amber
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hmftools-amber:3.9--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hmftools-amber/3.9--hdfd78af_1
$ module help quay.io/biocontainers/hmftools-amber/3.9--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hmftools-amber-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hmftools-amber-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hmftools-amber-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hmftools-amber-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hmftools-amber-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hmftools-amber-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### AMBER

```bash
$ singularity exec <container> /usr/local/bin/AMBER
$ podman run --it --rm --entrypoint /usr/local/bin/AMBER   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AMBER   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
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
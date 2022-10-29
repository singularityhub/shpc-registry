---
layout: container
name:  "quay.io/biocontainers/hmftools-gripss"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hmftools-gripss/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/hmftools-gripss/container.yaml"
updated_at: "2022-10-29 05:31:09.523189"
latest: "2.2--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/hmftools-gripss"
aliases:
 - "gripss"
 - "aserver"
 - "cups-config"
 - "ippeveprinter"
 - "ipptool"
 - "jaotc"
 - "jar"
 - "jarsigner"
 - "java"
 - "javac"
 - "javadoc"
versions:
 - "2.2--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for hmftools-gripss"
config: {"url": "https://biocontainers.pro/tools/hmftools-gripss", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hmftools-gripss", "latest": {"2.2--hdfd78af_0": "sha256:fe16bb19af8b567a95e3f5f06f0c86fa255fb80a3d0dd7268b75c1bea19e4d01"}, "tags": {"2.2--hdfd78af_0": "sha256:fe16bb19af8b567a95e3f5f06f0c86fa255fb80a3d0dd7268b75c1bea19e4d01"}, "docker": "quay.io/biocontainers/hmftools-gripss", "aliases": {"gripss": "/usr/local/bin/gripss", "aserver": "/usr/local/bin/aserver", "cups-config": "/usr/local/bin/cups-config", "ippeveprinter": "/usr/local/bin/ippeveprinter", "ipptool": "/usr/local/bin/ipptool", "jaotc": "/usr/local/bin/jaotc", "jar": "/usr/local/bin/jar", "jarsigner": "/usr/local/bin/jarsigner", "java": "/usr/local/bin/java", "javac": "/usr/local/bin/javac", "javadoc": "/usr/local/bin/javadoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hmftools-gripss.
shpc-registry automated BioContainers addition for hmftools-gripss
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hmftools-gripss
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hmftools-gripss:2.2--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hmftools-gripss/2.2--hdfd78af_0
$ module help quay.io/biocontainers/hmftools-gripss/2.2--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hmftools-gripss-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hmftools-gripss-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hmftools-gripss-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hmftools-gripss-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hmftools-gripss-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hmftools-gripss-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gripss

```bash
$ singularity exec <container> /usr/local/bin/gripss
$ podman run --it --rm --entrypoint /usr/local/bin/gripss   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gripss   -v ${PWD} -w ${PWD} <container> -c " $@"
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
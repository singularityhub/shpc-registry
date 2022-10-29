---
layout: container
name:  "quay.io/biocontainers/haplocheck"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/haplocheck/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/haplocheck/container.yaml"
updated_at: "2022-10-29 05:56:59.232237"
latest: "1.3.3--h4a94de4_0"
container_url: "https://biocontainers.pro/tools/haplocheck"
aliases:
 - "cloudgene.yaml"
 - "haplocheck"
 - "haplocheck.jar"
 - "mutserve.jar"
 - "rCRS.fasta"
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
 - "1.3.3--h4a94de4_0"
description: "shpc-registry automated BioContainers addition for haplocheck"
config: {"url": "https://biocontainers.pro/tools/haplocheck", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for haplocheck", "latest": {"1.3.3--h4a94de4_0": "sha256:a2d2bace16d9c2cec327aa984d48a6b456b0ce228120975072f8e2ac4a798afc"}, "tags": {"1.3.3--h4a94de4_0": "sha256:a2d2bace16d9c2cec327aa984d48a6b456b0ce228120975072f8e2ac4a798afc"}, "docker": "quay.io/biocontainers/haplocheck", "aliases": {"cloudgene.yaml": "/usr/local/bin/cloudgene.yaml", "haplocheck": "/usr/local/bin/haplocheck", "haplocheck.jar": "/usr/local/bin/haplocheck.jar", "mutserve.jar": "/usr/local/bin/mutserve.jar", "rCRS.fasta": "/usr/local/bin/rCRS.fasta", "aserver": "/usr/local/bin/aserver", "jaotc": "/usr/local/bin/jaotc", "jar": "/usr/local/bin/jar", "jarsigner": "/usr/local/bin/jarsigner", "java": "/usr/local/bin/java", "javac": "/usr/local/bin/javac", "javadoc": "/usr/local/bin/javadoc", "javap": "/usr/local/bin/javap", "jcmd": "/usr/local/bin/jcmd", "jconsole": "/usr/local/bin/jconsole"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/haplocheck.
shpc-registry automated BioContainers addition for haplocheck
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/haplocheck
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/haplocheck:1.3.3--h4a94de4_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/haplocheck/1.3.3--h4a94de4_0
$ module help quay.io/biocontainers/haplocheck/1.3.3--h4a94de4_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### haplocheck-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### haplocheck-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### haplocheck-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### haplocheck-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### haplocheck-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### haplocheck-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cloudgene.yaml

```bash
$ singularity exec <container> /usr/local/bin/cloudgene.yaml
$ podman run --it --rm --entrypoint /usr/local/bin/cloudgene.yaml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cloudgene.yaml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### haplocheck

```bash
$ singularity exec <container> /usr/local/bin/haplocheck
$ podman run --it --rm --entrypoint /usr/local/bin/haplocheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/haplocheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### haplocheck.jar

```bash
$ singularity exec <container> /usr/local/bin/haplocheck.jar
$ podman run --it --rm --entrypoint /usr/local/bin/haplocheck.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/haplocheck.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mutserve.jar

```bash
$ singularity exec <container> /usr/local/bin/mutserve.jar
$ podman run --it --rm --entrypoint /usr/local/bin/mutserve.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mutserve.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rCRS.fasta

```bash
$ singularity exec <container> /usr/local/bin/rCRS.fasta
$ podman run --it --rm --entrypoint /usr/local/bin/rCRS.fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rCRS.fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
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
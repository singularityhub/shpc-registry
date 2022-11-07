---
layout: container
name:  "quay.io/biocontainers/mobster"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mobster/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mobster/container.yaml"
updated_at: "2022-11-06 23:55:34.611232"
latest: "0.2.4.1--1"
container_url: "https://biocontainers.pro/tools/mobster"
aliases:
 - "MosaikAligner"
 - "MosaikBuild"
 - "MosaikJump"
 - "MosaikText"
 - "mobster"
 - "mobster-to-vcf"
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
 - "0.2.4.1--1"
description: "shpc-registry automated BioContainers addition for mobster"
config: {"url": "https://biocontainers.pro/tools/mobster", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mobster", "latest": {"0.2.4.1--1": "sha256:ca3657866765cadf80910b6d0e6701086fbce8b4a76e2b34af985b0d7076183c"}, "tags": {"0.2.4.1--1": "sha256:ca3657866765cadf80910b6d0e6701086fbce8b4a76e2b34af985b0d7076183c"}, "docker": "quay.io/biocontainers/mobster", "aliases": {"MosaikAligner": "/usr/local/bin/MosaikAligner", "MosaikBuild": "/usr/local/bin/MosaikBuild", "MosaikJump": "/usr/local/bin/MosaikJump", "MosaikText": "/usr/local/bin/MosaikText", "mobster": "/usr/local/bin/mobster", "mobster-to-vcf": "/usr/local/bin/mobster-to-vcf", "extcheck": "/usr/local/bin/extcheck", "java-rmi.cgi": "/usr/local/bin/java-rmi.cgi", "javah": "/usr/local/bin/javah", "jhat": "/usr/local/bin/jhat", "jsadebugd": "/usr/local/bin/jsadebugd", "native2ascii": "/usr/local/bin/native2ascii", "policytool": "/usr/local/bin/policytool", "appletviewer": "/usr/local/bin/appletviewer", "idlj": "/usr/local/bin/idlj", "orbd": "/usr/local/bin/orbd"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mobster.
shpc-registry automated BioContainers addition for mobster
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mobster
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mobster:0.2.4.1--1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mobster/0.2.4.1--1
$ module help quay.io/biocontainers/mobster/0.2.4.1--1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mobster-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mobster-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mobster-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mobster-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mobster-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mobster-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### MosaikAligner

```bash
$ singularity exec <container> /usr/local/bin/MosaikAligner
$ podman run --it --rm --entrypoint /usr/local/bin/MosaikAligner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MosaikAligner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MosaikBuild

```bash
$ singularity exec <container> /usr/local/bin/MosaikBuild
$ podman run --it --rm --entrypoint /usr/local/bin/MosaikBuild   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MosaikBuild   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MosaikJump

```bash
$ singularity exec <container> /usr/local/bin/MosaikJump
$ podman run --it --rm --entrypoint /usr/local/bin/MosaikJump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MosaikJump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MosaikText

```bash
$ singularity exec <container> /usr/local/bin/MosaikText
$ podman run --it --rm --entrypoint /usr/local/bin/MosaikText   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MosaikText   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mobster

```bash
$ singularity exec <container> /usr/local/bin/mobster
$ podman run --it --rm --entrypoint /usr/local/bin/mobster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mobster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mobster-to-vcf

```bash
$ singularity exec <container> /usr/local/bin/mobster-to-vcf
$ podman run --it --rm --entrypoint /usr/local/bin/mobster-to-vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mobster-to-vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
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
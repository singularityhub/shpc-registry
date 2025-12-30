---
layout: container
name:  "tomcat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/tomcat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/tomcat/container.yaml"
updated_at: "2025-12-30 04:32:28.784793"
latest: "11-jdk25"
container_url: "https://hub.docker.com/_/tomcat"

versions:
 - "10.0.5-jdk11-adoptopenjdk-hotspot"
 - "10.0.6-jdk11-adoptopenjdk-hotspot"
 - "10.0.7-jdk11-adoptopenjdk-hotspot"
 - "10.0.8-jdk11-adoptopenjdk-hotspot"
 - "10.1.0"
 - "latest"
 - "10"
 - "10-jdk17"
 - "10-jdk16"
 - "10-jdk15"
 - "10-jdk14"
 - "11.0"
 - "10-jdk21-openjdk"
 - "10-jdk21"
 - "11"
 - "11-jdk21"
 - "11-jdk17"
 - "11-jdk25"
 - "10-jdk25"
description: "Apache Tomcat is an open source implementation of the Java Servlet and JavaServer Pages technologies"
config: {"docker": "tomcat", "url": "https://hub.docker.com/_/tomcat", "maintainer": "@vsoch", "description": "Apache Tomcat is an open source implementation of the Java Servlet and JavaServer Pages technologies", "filter": ["^(?!jdk1[1-7]).*$"], "latest": {"11-jdk25": "sha256:689475f36b76708f19cc939d2d18689de23dd41abdb9e1693c60410cbb7361d6"}, "tags": {"10.0.5-jdk11-adoptopenjdk-hotspot": "sha256:a7418f29d3dd7ad20bcf052b3b6dc2777d118344286c6374bc447fb217a97c08", "10.0.6-jdk11-adoptopenjdk-hotspot": "sha256:c0019c8254bc1017f64e6ffd1612e25b50abca78d98d25f9ff8023e8999f0384", "10.0.7-jdk11-adoptopenjdk-hotspot": "sha256:d75c50123194e5533dd8b397175fab79c9dff69ed5c0bada70be5dff6d8fcc6d", "10.0.8-jdk11-adoptopenjdk-hotspot": "sha256:98ae9e70b3bd2129c2ef83179c38bc902e613f433c6222c88b2c1a2f3bdfd1ec", "10.1.0": "sha256:741cbf2fb47000cf9d231657d1440c5e96dca9bb9175a985501d153cd6ae875d", "latest": "sha256:689475f36b76708f19cc939d2d18689de23dd41abdb9e1693c60410cbb7361d6", "10": "sha256:4b2a232e2b9505c8d96150686b6504f97a61233bd376ba2d60c9c467fd474664", "10-jdk17": "sha256:1c3896808980e90cd874809df16a1e086fa4da79c93bcce3cc6d0effca6e6a1d", "10-jdk16": "sha256:06894e19b914a4e491580d54091ac248d53b0c4c474ff9e55e97e27d9adb45d5", "10-jdk15": "sha256:822bc61a43b972b5f784af5f8f40ce077399c06cfa724fc1cd60ea687f5d9828", "10-jdk14": "sha256:e97bde5b2bba850a96ba59b5500e9448216c989c0061a4e7e5c8d9d64185a36e", "11.0": "sha256:689475f36b76708f19cc939d2d18689de23dd41abdb9e1693c60410cbb7361d6", "10-jdk21-openjdk": "sha256:33e5dab5e662882c87c87813a5a4709c9cc918b7388304b60781c0521ca6e7f2", "10-jdk21": "sha256:ba7b93ce3f2e0c8c83914c390c10be99b553817c157fab6b43ec85fd6374cf6f", "11": "sha256:689475f36b76708f19cc939d2d18689de23dd41abdb9e1693c60410cbb7361d6", "11-jdk21": "sha256:8c905aacac879bcfdbf67ac82acb3244aae13c15848bf633cd49463d46692f24", "11-jdk17": "sha256:f3c91c25276c915557f0d6979c96d4416473b6134187989d2bb587962076d589", "11-jdk25": "sha256:689475f36b76708f19cc939d2d18689de23dd41abdb9e1693c60410cbb7361d6", "10-jdk25": "sha256:4b2a232e2b9505c8d96150686b6504f97a61233bd376ba2d60c9c467fd474664"}}
---

This module is a singularity container wrapper for tomcat.
Apache Tomcat is an open source implementation of the Java Servlet and JavaServer Pages technologies
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install tomcat
```

Or a specific version:

```bash
$ shpc install tomcat:11-jdk25
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load tomcat/11-jdk25
$ module help tomcat/11-jdk25
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tomcat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tomcat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tomcat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tomcat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tomcat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tomcat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### tomcat

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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
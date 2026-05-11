---
layout: container
name:  "tomcat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/tomcat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/tomcat/container.yaml"
updated_at: "2026-05-11 06:00:58.489308"
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
config: {"docker": "tomcat", "url": "https://hub.docker.com/_/tomcat", "maintainer": "@vsoch", "description": "Apache Tomcat is an open source implementation of the Java Servlet and JavaServer Pages technologies", "filter": ["^(?!jdk1[1-7]).*$"], "latest": {"11-jdk25": "sha256:931b145a361d3aa3033e97dd035dace2fe5bc551abfc5aaa0b341a2ac00e8b2f"}, "tags": {"10.0.5-jdk11-adoptopenjdk-hotspot": "sha256:a7418f29d3dd7ad20bcf052b3b6dc2777d118344286c6374bc447fb217a97c08", "10.0.6-jdk11-adoptopenjdk-hotspot": "sha256:c0019c8254bc1017f64e6ffd1612e25b50abca78d98d25f9ff8023e8999f0384", "10.0.7-jdk11-adoptopenjdk-hotspot": "sha256:d75c50123194e5533dd8b397175fab79c9dff69ed5c0bada70be5dff6d8fcc6d", "10.0.8-jdk11-adoptopenjdk-hotspot": "sha256:98ae9e70b3bd2129c2ef83179c38bc902e613f433c6222c88b2c1a2f3bdfd1ec", "10.1.0": "sha256:741cbf2fb47000cf9d231657d1440c5e96dca9bb9175a985501d153cd6ae875d", "latest": "sha256:931b145a361d3aa3033e97dd035dace2fe5bc551abfc5aaa0b341a2ac00e8b2f", "10": "sha256:b5e7bff604922a331d5d634c7958d84afd36257a33030c31b45e6f529247b7fd", "10-jdk17": "sha256:30f3c15abd4642d11ea2aed1a5b1edae0fc500b8a6241e8d1153187a5367f964", "10-jdk16": "sha256:06894e19b914a4e491580d54091ac248d53b0c4c474ff9e55e97e27d9adb45d5", "10-jdk15": "sha256:822bc61a43b972b5f784af5f8f40ce077399c06cfa724fc1cd60ea687f5d9828", "10-jdk14": "sha256:e97bde5b2bba850a96ba59b5500e9448216c989c0061a4e7e5c8d9d64185a36e", "11.0": "sha256:931b145a361d3aa3033e97dd035dace2fe5bc551abfc5aaa0b341a2ac00e8b2f", "10-jdk21-openjdk": "sha256:33e5dab5e662882c87c87813a5a4709c9cc918b7388304b60781c0521ca6e7f2", "10-jdk21": "sha256:8b108012d75caac4bc9554e84c09d3578d58330192c6ffe9603c1f059ab3e7bf", "11": "sha256:931b145a361d3aa3033e97dd035dace2fe5bc551abfc5aaa0b341a2ac00e8b2f", "11-jdk21": "sha256:6a20a22bcb32a619449ba86d7fce2b78c67a8e47c56aff7c70cac95ef7f3bf1e", "11-jdk17": "sha256:f60825ed71b9c78322568af9bca99f550fde3f8747128019ba06356b1b61f8ab", "11-jdk25": "sha256:931b145a361d3aa3033e97dd035dace2fe5bc551abfc5aaa0b341a2ac00e8b2f", "10-jdk25": "sha256:b5e7bff604922a331d5d634c7958d84afd36257a33030c31b45e6f529247b7fd"}}
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
---
layout: container
name:  "tomcat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/tomcat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/tomcat/container.yaml"
updated_at: "2025-12-06 04:05:46.687621"
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
description: "Apache Tomcat is an open source implementation of the Java Servlet and JavaServer Pages technologies"
config: {"docker": "tomcat", "url": "https://hub.docker.com/_/tomcat", "maintainer": "@vsoch", "description": "Apache Tomcat is an open source implementation of the Java Servlet and JavaServer Pages technologies", "filter": ["^(?!jdk1[1-7]).*$"], "latest": {"11-jdk25": "crane digest tomcat:11-jdk25: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit"}, "tags": {"10.0.5-jdk11-adoptopenjdk-hotspot": "sha256:a7418f29d3dd7ad20bcf052b3b6dc2777d118344286c6374bc447fb217a97c08", "10.0.6-jdk11-adoptopenjdk-hotspot": "sha256:c0019c8254bc1017f64e6ffd1612e25b50abca78d98d25f9ff8023e8999f0384", "10.0.7-jdk11-adoptopenjdk-hotspot": "sha256:d75c50123194e5533dd8b397175fab79c9dff69ed5c0bada70be5dff6d8fcc6d", "10.0.8-jdk11-adoptopenjdk-hotspot": "sha256:98ae9e70b3bd2129c2ef83179c38bc902e613f433c6222c88b2c1a2f3bdfd1ec", "10.1.0": "sha256:741cbf2fb47000cf9d231657d1440c5e96dca9bb9175a985501d153cd6ae875d", "latest": "sha256:3d41d69cc052d14ed03211520d15a6391e426cecc041b66715b4e32710bf4f72", "10": "sha256:0e7a4ed4094a76f0fa2083ec5c759685e845540180a5def48b0c494f0bc4b470", "10-jdk17": "sha256:d2cd0027e6b828ad8a5ff7693a20d972f16af0139f7fcecafa0797b31809863e", "10-jdk16": "crane digest tomcat:10-jdk16: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "10-jdk15": "crane digest tomcat:10-jdk15: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "10-jdk14": "crane digest tomcat:10-jdk14: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "11.0": "crane digest tomcat:11.0: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "10-jdk21-openjdk": "crane digest tomcat:10-jdk21-openjdk: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "10-jdk21": "crane digest tomcat:10-jdk21: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "11": "crane digest tomcat:11: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "11-jdk21": "crane digest tomcat:11-jdk21: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "11-jdk17": "crane digest tomcat:11-jdk17: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "11-jdk25": "crane digest tomcat:11-jdk25: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit"}}
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
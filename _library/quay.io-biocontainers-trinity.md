---
layout: container
name:  "quay.io/biocontainers/trinity"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/trinity/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/trinity/container.yaml"
updated_at: "2022-10-29 05:41:28.035440"
latest: "date.2011_11_26--ncurses5.9_8"
container_url: "https://biocontainers.pro/tools/trinity"
aliases:
 - "Trinity-test"
 - "Trinity"
 - "appletviewer"
 - "c2ph"
 - "extcheck"
 - "idlj"
 - "jar"
 - "jarsigner"
 - "java"
 - "java-rmi.cgi"
 - "javac"
versions:
 - "2.11.0--h5ef6573_1"
 - "2.12.0--h5ef6573_0"
 - "2.12.0--ha140323_1"
 - "2.13.2--ha140323_0"
 - "2.13.2--h15cb65e_2"
 - "2.12.0--ha140323_3"
 - "2.13.2--hea94271_3"
 - "date.2011_11_26--ncurses5.9_8"
description: "shpc-registry automated BioContainers addition for trinity"
config: {"docker": "quay.io/biocontainers/trinity", "url": "https://biocontainers.pro/tools/trinity", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for trinity", "filter": ["^(?!.*2011).*$"], "latest": {"date.2011_11_26--ncurses5.9_8": "sha256:eabe346a2adac1bb30aaaa62764f299638daa2a83ef6408722b0f89f8c490e20"}, "tags": {"2.11.0--h5ef6573_1": "sha256:6d35d716aa12ba7b0c715fa8a30359b43ba9151e854dc4407b949e7b57c3a50a", "2.12.0--h5ef6573_0": "sha256:4045560dad56fee946c9bcccd2ba0e373292a5adf8a2f7ba09917cbaeaa74323", "2.12.0--ha140323_1": "sha256:2736617a96c30bce93a149fe5f47b4f4a290a7d21c1503619430db619d9bc3a0", "2.13.2--ha140323_0": "sha256:727ae4211b1a2fdfa33c1bb30fbf8ffc231d610c6497fe7150b031fa9a70b7b1", "2.13.2--h15cb65e_2": "sha256:6c87b7700eab5b4044373fed374c566d4c5b5d9bd6e5f78ad5a07f5ce84ef8c6", "2.12.0--ha140323_3": "sha256:d44cb9353096e558adf34f4b6219c252d6b3523db9555c7dbecd0ed980e68d58", "2.13.2--hea94271_3": "sha256:9107340bc575f8ec80dee7814f325217c3fa51d15f2fc30e9907606fa289f88a", "date.2011_11_26--ncurses5.9_8": "sha256:eabe346a2adac1bb30aaaa62764f299638daa2a83ef6408722b0f89f8c490e20"}, "aliases": {"Trinity-test": "/usr/local/bin/Trinity-test", "Trinity": "/usr/local/bin/Trinity", "appletviewer": "/usr/local/bin/appletviewer", "c2ph": "/usr/local/bin/c2ph", "extcheck": "/usr/local/bin/extcheck", "idlj": "/usr/local/bin/idlj", "jar": "/usr/local/bin/jar", "jarsigner": "/usr/local/bin/jarsigner", "java": "/usr/local/bin/java", "java-rmi.cgi": "/usr/local/bin/java-rmi.cgi", "javac": "/usr/local/bin/javac"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/trinity.
shpc-registry automated BioContainers addition for trinity
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/trinity
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/trinity:2.11.0--h5ef6573_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/trinity/2.11.0--h5ef6573_1
$ module help quay.io/biocontainers/trinity/2.11.0--h5ef6573_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### trinity-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### trinity-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### trinity-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### trinity-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### trinity-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### trinity-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Trinity-test

```bash
$ singularity exec <container> /usr/local/bin/Trinity-test
$ podman run --it --rm --entrypoint /usr/local/bin/Trinity-test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Trinity-test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Trinity

```bash
$ singularity exec <container> /usr/local/bin/Trinity
$ podman run --it --rm --entrypoint /usr/local/bin/Trinity   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Trinity   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### appletviewer

```bash
$ singularity exec <container> /usr/local/bin/appletviewer
$ podman run --it --rm --entrypoint /usr/local/bin/appletviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/appletviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c2ph

```bash
$ singularity exec <container> /usr/local/bin/c2ph
$ podman run --it --rm --entrypoint /usr/local/bin/c2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extcheck

```bash
$ singularity exec <container> /usr/local/bin/extcheck
$ podman run --it --rm --entrypoint /usr/local/bin/extcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idlj

```bash
$ singularity exec <container> /usr/local/bin/idlj
$ podman run --it --rm --entrypoint /usr/local/bin/idlj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idlj   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### java-rmi.cgi

```bash
$ singularity exec <container> /usr/local/bin/java-rmi.cgi
$ podman run --it --rm --entrypoint /usr/local/bin/java-rmi.cgi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/java-rmi.cgi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### javac

```bash
$ singularity exec <container> /usr/local/bin/javac
$ podman run --it --rm --entrypoint /usr/local/bin/javac   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/javac   -v ${PWD} -w ${PWD} <container> -c " $@"
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
---
layout: container
name:  "quay.io/biocontainers/ant"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ant/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ant/container.yaml"
updated_at: "2025-08-04 04:25:00.842275"
latest: "1.10.0--0"
container_url: "https://biocontainers.pro/tools/ant"
aliases:
 - "ant"
 - "ant.bat"
 - "ant.cmd"
 - "antRun"
 - "antRun.bat"
 - "antRun.pl"
 - "antenv.cmd"
 - "complete-ant-cmd.pl"
 - "envset.cmd"
 - "lcp.bat"
 - "runant.pl"
 - "runant.py"
 - "runrc.cmd"
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
 - "1.9.6--1"
 - "1.10.0--0"
description: "shpc-registry automated BioContainers addition for ant"
config: {"url": "https://biocontainers.pro/tools/ant", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ant", "latest": {"1.10.0--0": "sha256:42f829c7c1eadabb8ee6672e507cc7c54e3258ad7dd1124d749e05e529a5a3ca"}, "tags": {"1.9.6--1": "sha256:892a04a32d64ea4a4bfcbf51fc71af02a6143f55a2dc1783c18667bf5421914e", "1.10.0--0": "sha256:42f829c7c1eadabb8ee6672e507cc7c54e3258ad7dd1124d749e05e529a5a3ca"}, "docker": "quay.io/biocontainers/ant", "aliases": {"ant": "/usr/local/bin/ant", "ant.bat": "/usr/local/bin/ant.bat", "ant.cmd": "/usr/local/bin/ant.cmd", "antRun": "/usr/local/bin/antRun", "antRun.bat": "/usr/local/bin/antRun.bat", "antRun.pl": "/usr/local/bin/antRun.pl", "antenv.cmd": "/usr/local/bin/antenv.cmd", "complete-ant-cmd.pl": "/usr/local/bin/complete-ant-cmd.pl", "envset.cmd": "/usr/local/bin/envset.cmd", "lcp.bat": "/usr/local/bin/lcp.bat", "runant.pl": "/usr/local/bin/runant.pl", "runant.py": "/usr/local/bin/runant.py", "runrc.cmd": "/usr/local/bin/runrc.cmd", "extcheck": "/usr/local/bin/extcheck", "java-rmi.cgi": "/usr/local/bin/java-rmi.cgi", "javah": "/usr/local/bin/javah", "jhat": "/usr/local/bin/jhat", "jsadebugd": "/usr/local/bin/jsadebugd", "native2ascii": "/usr/local/bin/native2ascii", "policytool": "/usr/local/bin/policytool", "appletviewer": "/usr/local/bin/appletviewer", "idlj": "/usr/local/bin/idlj", "orbd": "/usr/local/bin/orbd"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ant.
shpc-registry automated BioContainers addition for ant
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ant
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ant:1.10.0--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ant/1.10.0--0
$ module help quay.io/biocontainers/ant/1.10.0--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ant-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ant-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ant-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ant-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ant-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ant-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ant

```bash
$ singularity exec <container> /usr/local/bin/ant
$ podman run --it --rm --entrypoint /usr/local/bin/ant   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ant   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ant.bat

```bash
$ singularity exec <container> /usr/local/bin/ant.bat
$ podman run --it --rm --entrypoint /usr/local/bin/ant.bat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ant.bat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ant.cmd

```bash
$ singularity exec <container> /usr/local/bin/ant.cmd
$ podman run --it --rm --entrypoint /usr/local/bin/ant.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ant.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### antRun

```bash
$ singularity exec <container> /usr/local/bin/antRun
$ podman run --it --rm --entrypoint /usr/local/bin/antRun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/antRun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### antRun.bat

```bash
$ singularity exec <container> /usr/local/bin/antRun.bat
$ podman run --it --rm --entrypoint /usr/local/bin/antRun.bat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/antRun.bat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### antRun.pl

```bash
$ singularity exec <container> /usr/local/bin/antRun.pl
$ podman run --it --rm --entrypoint /usr/local/bin/antRun.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/antRun.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### antenv.cmd

```bash
$ singularity exec <container> /usr/local/bin/antenv.cmd
$ podman run --it --rm --entrypoint /usr/local/bin/antenv.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/antenv.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### complete-ant-cmd.pl

```bash
$ singularity exec <container> /usr/local/bin/complete-ant-cmd.pl
$ podman run --it --rm --entrypoint /usr/local/bin/complete-ant-cmd.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/complete-ant-cmd.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### envset.cmd

```bash
$ singularity exec <container> /usr/local/bin/envset.cmd
$ podman run --it --rm --entrypoint /usr/local/bin/envset.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/envset.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lcp.bat

```bash
$ singularity exec <container> /usr/local/bin/lcp.bat
$ podman run --it --rm --entrypoint /usr/local/bin/lcp.bat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lcp.bat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runant.pl

```bash
$ singularity exec <container> /usr/local/bin/runant.pl
$ podman run --it --rm --entrypoint /usr/local/bin/runant.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runant.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runant.py

```bash
$ singularity exec <container> /usr/local/bin/runant.py
$ podman run --it --rm --entrypoint /usr/local/bin/runant.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runant.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runrc.cmd

```bash
$ singularity exec <container> /usr/local/bin/runrc.cmd
$ podman run --it --rm --entrypoint /usr/local/bin/runrc.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runrc.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
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
---
layout: container
name:  "quay.io/biocontainers/jacusa2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/jacusa2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/jacusa2/container.yaml"
updated_at: "2025-12-29 04:29:56.468581"
latest: "2.1.16--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/jacusa2"
aliases:
 - "JACUSA2"
 - "clhsdb"
 - "hsdb"
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
 - "schemagen"
 - "servertool"
 - "tnameserv"
 - "wsgen"
 - "wsimport"
 - "xjc"
 - "jfr"
 - "jjs"
 - "pack200"
 - "rmic"
 - "rmid"
 - "unpack200"
 - "jdeps"
versions:
 - "2.0.4--hdfd78af_0"
 - "2.1.15--hdfd78af_0"
 - "2.1.16--hdfd78af_0"
description: "singularity registry hpc automated addition for jacusa2"
config: {"url": "https://biocontainers.pro/tools/jacusa2", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for jacusa2", "latest": {"2.1.16--hdfd78af_0": "sha256:28428337703ebb874b3fd704c0479df1be6704d45436a10ea5b7c74381fec433"}, "tags": {"2.0.4--hdfd78af_0": "sha256:b5ef72acf2cd9e1a13c754a2699bb08c7c274c513c2e1338b7077f7367f201a1", "2.1.15--hdfd78af_0": "sha256:0b09fb1a9b462600b6f688a3a02712bb1bd69e380bef77ff57a8d7e67a742e4c", "2.1.16--hdfd78af_0": "sha256:28428337703ebb874b3fd704c0479df1be6704d45436a10ea5b7c74381fec433"}, "docker": "quay.io/biocontainers/jacusa2", "aliases": {"JACUSA2": "/usr/local/bin/JACUSA2", "clhsdb": "/usr/local/bin/clhsdb", "hsdb": "/usr/local/bin/hsdb", "extcheck": "/usr/local/bin/extcheck", "java-rmi.cgi": "/usr/local/bin/java-rmi.cgi", "javah": "/usr/local/bin/javah", "jhat": "/usr/local/bin/jhat", "jsadebugd": "/usr/local/bin/jsadebugd", "native2ascii": "/usr/local/bin/native2ascii", "policytool": "/usr/local/bin/policytool", "appletviewer": "/usr/local/bin/appletviewer", "idlj": "/usr/local/bin/idlj", "orbd": "/usr/local/bin/orbd", "schemagen": "/usr/local/bin/schemagen", "servertool": "/usr/local/bin/servertool", "tnameserv": "/usr/local/bin/tnameserv", "wsgen": "/usr/local/bin/wsgen", "wsimport": "/usr/local/bin/wsimport", "xjc": "/usr/local/bin/xjc", "jfr": "/usr/local/bin/jfr", "jjs": "/usr/local/bin/jjs", "pack200": "/usr/local/bin/pack200", "rmic": "/usr/local/bin/rmic", "rmid": "/usr/local/bin/rmid", "unpack200": "/usr/local/bin/unpack200", "jdeps": "/usr/local/bin/jdeps"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/jacusa2.
singularity registry hpc automated addition for jacusa2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/jacusa2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/jacusa2:2.1.16--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/jacusa2/2.1.16--hdfd78af_0
$ module help quay.io/biocontainers/jacusa2/2.1.16--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### jacusa2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### jacusa2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### jacusa2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### jacusa2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### jacusa2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### jacusa2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### JACUSA2

```bash
$ singularity exec <container> /usr/local/bin/JACUSA2
$ podman run --it --rm --entrypoint /usr/local/bin/JACUSA2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/JACUSA2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clhsdb

```bash
$ singularity exec <container> /usr/local/bin/clhsdb
$ podman run --it --rm --entrypoint /usr/local/bin/clhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hsdb

```bash
$ singularity exec <container> /usr/local/bin/hsdb
$ podman run --it --rm --entrypoint /usr/local/bin/hsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### schemagen

```bash
$ singularity exec <container> /usr/local/bin/schemagen
$ podman run --it --rm --entrypoint /usr/local/bin/schemagen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/schemagen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### servertool

```bash
$ singularity exec <container> /usr/local/bin/servertool
$ podman run --it --rm --entrypoint /usr/local/bin/servertool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/servertool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tnameserv

```bash
$ singularity exec <container> /usr/local/bin/tnameserv
$ podman run --it --rm --entrypoint /usr/local/bin/tnameserv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tnameserv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wsgen

```bash
$ singularity exec <container> /usr/local/bin/wsgen
$ podman run --it --rm --entrypoint /usr/local/bin/wsgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wsgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wsimport

```bash
$ singularity exec <container> /usr/local/bin/wsimport
$ podman run --it --rm --entrypoint /usr/local/bin/wsimport   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wsimport   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xjc

```bash
$ singularity exec <container> /usr/local/bin/xjc
$ podman run --it --rm --entrypoint /usr/local/bin/xjc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xjc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jfr

```bash
$ singularity exec <container> /usr/local/bin/jfr
$ podman run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jjs

```bash
$ singularity exec <container> /usr/local/bin/jjs
$ podman run --it --rm --entrypoint /usr/local/bin/jjs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jjs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pack200

```bash
$ singularity exec <container> /usr/local/bin/pack200
$ podman run --it --rm --entrypoint /usr/local/bin/pack200   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pack200   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rmic

```bash
$ singularity exec <container> /usr/local/bin/rmic
$ podman run --it --rm --entrypoint /usr/local/bin/rmic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rmic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rmid

```bash
$ singularity exec <container> /usr/local/bin/rmid
$ podman run --it --rm --entrypoint /usr/local/bin/rmid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rmid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unpack200

```bash
$ singularity exec <container> /usr/local/bin/unpack200
$ podman run --it --rm --entrypoint /usr/local/bin/unpack200   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unpack200   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jdeps

```bash
$ singularity exec <container> /usr/local/bin/jdeps
$ podman run --it --rm --entrypoint /usr/local/bin/jdeps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jdeps   -v ${PWD} -w ${PWD} <container> -c " $@"
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
---
layout: container
name:  "quay.io/biocontainers/theiacov-gc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/theiacov-gc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/theiacov-gc/container.yaml"
updated_at: "2024-11-01 03:17:20.904192"
latest: "2.3.2--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/theiacov-gc"
aliases:
 - "cromwell"
 - "find"
 - "locate"
 - "theiacov-gc"
 - "theiacov-gc-organize.py"
 - "theiacov-gc-prepare.py"
 - "updatedb"
 - "womtool"
 - "xargs"
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "cups-config"
 - "ippeveprinter"
 - "ipptool"
 - "jfr"
 - "jaotc"
 - "aserver"
 - "jdeprscan"
 - "jhsdb"
 - "jimage"
 - "jlink"
 - "jmod"
 - "jshell"
 - "jjs"
 - "pack200"
 - "rmic"
 - "rmid"
 - "unpack200"
 - "jdeps"
 - "jar"
 - "jarsigner"
versions:
 - "2.3.0--hdfd78af_0"
 - "2.3.1--hdfd78af_0"
 - "2.3.2--hdfd78af_0"
description: "singularity registry hpc automated addition for theiacov-gc"
config: {"url": "https://biocontainers.pro/tools/theiacov-gc", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for theiacov-gc", "latest": {"2.3.2--hdfd78af_0": "sha256:5411172840db6b2b565bc156fabfbc9b3063b37d8cdaa6cedfa00031b0a6a8f9"}, "tags": {"2.3.0--hdfd78af_0": "sha256:df3e316e5703a55f2a14ea14a995bc1c68b2be6d863b4d48705120f33b27e5a9", "2.3.1--hdfd78af_0": "sha256:12eaeed815ba61dcd3cbcf0f893d0bbcc158731437a92ac90fa117bb4ee563a3", "2.3.2--hdfd78af_0": "sha256:5411172840db6b2b565bc156fabfbc9b3063b37d8cdaa6cedfa00031b0a6a8f9"}, "docker": "quay.io/biocontainers/theiacov-gc", "aliases": {"cromwell": "/usr/local/bin/cromwell", "find": "/usr/local/bin/find", "locate": "/usr/local/bin/locate", "theiacov-gc": "/usr/local/bin/theiacov-gc", "theiacov-gc-organize.py": "/usr/local/bin/theiacov-gc-organize.py", "theiacov-gc-prepare.py": "/usr/local/bin/theiacov-gc-prepare.py", "updatedb": "/usr/local/bin/updatedb", "womtool": "/usr/local/bin/womtool", "xargs": "/usr/local/bin/xargs", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "cups-config": "/usr/local/bin/cups-config", "ippeveprinter": "/usr/local/bin/ippeveprinter", "ipptool": "/usr/local/bin/ipptool", "jfr": "/usr/local/bin/jfr", "jaotc": "/usr/local/bin/jaotc", "aserver": "/usr/local/bin/aserver", "jdeprscan": "/usr/local/bin/jdeprscan", "jhsdb": "/usr/local/bin/jhsdb", "jimage": "/usr/local/bin/jimage", "jlink": "/usr/local/bin/jlink", "jmod": "/usr/local/bin/jmod", "jshell": "/usr/local/bin/jshell", "jjs": "/usr/local/bin/jjs", "pack200": "/usr/local/bin/pack200", "rmic": "/usr/local/bin/rmic", "rmid": "/usr/local/bin/rmid", "unpack200": "/usr/local/bin/unpack200", "jdeps": "/usr/local/bin/jdeps", "jar": "/usr/local/bin/jar", "jarsigner": "/usr/local/bin/jarsigner"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/theiacov-gc.
singularity registry hpc automated addition for theiacov-gc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/theiacov-gc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/theiacov-gc:2.3.2--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/theiacov-gc/2.3.2--hdfd78af_0
$ module help quay.io/biocontainers/theiacov-gc/2.3.2--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### theiacov-gc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### theiacov-gc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### theiacov-gc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### theiacov-gc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### theiacov-gc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### theiacov-gc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cromwell

```bash
$ singularity exec <container> /usr/local/bin/cromwell
$ podman run --it --rm --entrypoint /usr/local/bin/cromwell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cromwell   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find

```bash
$ singularity exec <container> /usr/local/bin/find
$ podman run --it --rm --entrypoint /usr/local/bin/find   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### locate

```bash
$ singularity exec <container> /usr/local/bin/locate
$ podman run --it --rm --entrypoint /usr/local/bin/locate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/locate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### theiacov-gc

```bash
$ singularity exec <container> /usr/local/bin/theiacov-gc
$ podman run --it --rm --entrypoint /usr/local/bin/theiacov-gc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/theiacov-gc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### theiacov-gc-organize.py

```bash
$ singularity exec <container> /usr/local/bin/theiacov-gc-organize.py
$ podman run --it --rm --entrypoint /usr/local/bin/theiacov-gc-organize.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/theiacov-gc-organize.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### theiacov-gc-prepare.py

```bash
$ singularity exec <container> /usr/local/bin/theiacov-gc-prepare.py
$ podman run --it --rm --entrypoint /usr/local/bin/theiacov-gc-prepare.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/theiacov-gc-prepare.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### updatedb

```bash
$ singularity exec <container> /usr/local/bin/updatedb
$ podman run --it --rm --entrypoint /usr/local/bin/updatedb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/updatedb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### womtool

```bash
$ singularity exec <container> /usr/local/bin/womtool
$ podman run --it --rm --entrypoint /usr/local/bin/womtool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/womtool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xargs

```bash
$ singularity exec <container> /usr/local/bin/xargs
$ podman run --it --rm --entrypoint /usr/local/bin/xargs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xargs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.11

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.11
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.11

```bash
$ singularity exec <container> /usr/local/bin/idle3.11
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.11

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.11
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11

```bash
$ singularity exec <container> /usr/local/bin/python3.11
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11-config

```bash
$ singularity exec <container> /usr/local/bin/python3.11-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### jfr

```bash
$ singularity exec <container> /usr/local/bin/jfr
$ podman run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jaotc

```bash
$ singularity exec <container> /usr/local/bin/jaotc
$ podman run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jdeprscan

```bash
$ singularity exec <container> /usr/local/bin/jdeprscan
$ podman run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jhsdb

```bash
$ singularity exec <container> /usr/local/bin/jhsdb
$ podman run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jimage

```bash
$ singularity exec <container> /usr/local/bin/jimage
$ podman run --it --rm --entrypoint /usr/local/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jlink

```bash
$ singularity exec <container> /usr/local/bin/jlink
$ podman run --it --rm --entrypoint /usr/local/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jmod

```bash
$ singularity exec <container> /usr/local/bin/jmod
$ podman run --it --rm --entrypoint /usr/local/bin/jmod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jmod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jshell

```bash
$ singularity exec <container> /usr/local/bin/jshell
$ podman run --it --rm --entrypoint /usr/local/bin/jshell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jshell   -v ${PWD} -w ${PWD} <container> -c " $@"
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
---
layout: container
name:  "quay.io/biocontainers/libssw"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/libssw/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/libssw/container.yaml"
updated_at: "2024-03-08 02:43:39.802542"
latest: "1.1--py27h8f2a353_5"
container_url: "https://biocontainers.pro/tools/libssw"
aliases:
 - "example_cpp"
 - "pyssw.py"
 - "ssw.jar"
 - "ssw_lib.py"
 - "ssw_test"
 - "jaotc"
 - "python2-config"
 - "python2.7-config"
 - "jdeprscan"
 - "jhsdb"
 - "jimage"
 - "jlink"
 - "jmod"
 - "jshell"
 - "python2"
versions:
 - "1.1--py27h8f2a353_5"
description: "shpc-registry automated BioContainers addition for libssw"
config: {"url": "https://biocontainers.pro/tools/libssw", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for libssw", "latest": {"1.1--py27h8f2a353_5": "sha256:a4b0a269e5ba2624b99c68ad36456749d95186ec8071c81a31e26559aae696d6"}, "tags": {"1.1--py27h8f2a353_5": "sha256:a4b0a269e5ba2624b99c68ad36456749d95186ec8071c81a31e26559aae696d6"}, "docker": "quay.io/biocontainers/libssw", "aliases": {"example_cpp": "/usr/local/bin/example_cpp", "pyssw.py": "/usr/local/bin/pyssw.py", "ssw.jar": "/usr/local/bin/ssw.jar", "ssw_lib.py": "/usr/local/bin/ssw_lib.py", "ssw_test": "/usr/local/bin/ssw_test", "jaotc": "/usr/local/bin/jaotc", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "jdeprscan": "/usr/local/bin/jdeprscan", "jhsdb": "/usr/local/bin/jhsdb", "jimage": "/usr/local/bin/jimage", "jlink": "/usr/local/bin/jlink", "jmod": "/usr/local/bin/jmod", "jshell": "/usr/local/bin/jshell", "python2": "/usr/local/bin/python2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/libssw.
shpc-registry automated BioContainers addition for libssw
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/libssw
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/libssw:1.1--py27h8f2a353_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/libssw/1.1--py27h8f2a353_5
$ module help quay.io/biocontainers/libssw/1.1--py27h8f2a353_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### libssw-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### libssw-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### libssw-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### libssw-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### libssw-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### libssw-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### example_cpp

```bash
$ singularity exec <container> /usr/local/bin/example_cpp
$ podman run --it --rm --entrypoint /usr/local/bin/example_cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/example_cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyssw.py

```bash
$ singularity exec <container> /usr/local/bin/pyssw.py
$ podman run --it --rm --entrypoint /usr/local/bin/pyssw.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyssw.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ssw.jar

```bash
$ singularity exec <container> /usr/local/bin/ssw.jar
$ podman run --it --rm --entrypoint /usr/local/bin/ssw.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ssw.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ssw_lib.py

```bash
$ singularity exec <container> /usr/local/bin/ssw_lib.py
$ podman run --it --rm --entrypoint /usr/local/bin/ssw_lib.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ssw_lib.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ssw_test

```bash
$ singularity exec <container> /usr/local/bin/ssw_test
$ podman run --it --rm --entrypoint /usr/local/bin/ssw_test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ssw_test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jaotc

```bash
$ singularity exec <container> /usr/local/bin/jaotc
$ podman run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2-config

```bash
$ singularity exec <container> /usr/local/bin/python2-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7-config

```bash
$ singularity exec <container> /usr/local/bin/python2.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### python2

```bash
$ singularity exec <container> /usr/local/bin/python2
$ podman run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
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
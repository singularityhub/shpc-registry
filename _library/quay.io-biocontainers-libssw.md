---
layout: container
name:  "quay.io/biocontainers/libssw"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/libssw/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/libssw/container.yaml"
updated_at: "2022-10-27 00:51:19.948003"
latest: "1.1--py27h8f2a353_5"
container_url: "https://biocontainers.pro/tools/libssw"
aliases:
 - "example_cpp"
 - "pyssw.py"
 - "ssw.jar"
 - "ssw_lib.py"
 - "ssw_test"
versions:
 - "1.1--py27h8f2a353_5"
description: "shpc-registry automated BioContainers addition for libssw"
config: {"url": "https://biocontainers.pro/tools/libssw", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for libssw", "latest": {"1.1--py27h8f2a353_5": "sha256:a4b0a269e5ba2624b99c68ad36456749d95186ec8071c81a31e26559aae696d6"}, "tags": {"1.1--py27h8f2a353_5": "sha256:a4b0a269e5ba2624b99c68ad36456749d95186ec8071c81a31e26559aae696d6"}, "docker": "quay.io/biocontainers/libssw", "aliases": {"example_cpp": "/usr/local/bin/example_cpp", "pyssw.py": "/usr/local/bin/pyssw.py", "ssw.jar": "/usr/local/bin/ssw.jar", "ssw_lib.py": "/usr/local/bin/ssw_lib.py", "ssw_test": "/usr/local/bin/ssw_test"}}
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
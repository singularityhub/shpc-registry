---
layout: container
name:  "quay.io/biocontainers/hmmlearn"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hmmlearn/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hmmlearn/container.yaml"
updated_at: "2024-12-13 03:39:10.780020"
latest: "20151031--py35h24bf2e0_2"
container_url: "https://biocontainers.pro/tools/hmmlearn"
aliases:
 - "conv-template"
 - "from-template"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
versions:
 - "0.1.1--py27h24bf2e0_0"
 - "20151031--py35h24bf2e0_2"
 - "20151031--py27_1"
 - "20151031--py27h24bf2e0_2"
 - "20151031--py35_1"
description: "shpc-registry automated BioContainers addition for hmmlearn"
config: {"url": "https://biocontainers.pro/tools/hmmlearn", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hmmlearn", "latest": {"20151031--py35h24bf2e0_2": "sha256:c57f8868cf42250021df9df6ee94a2cf4963d86b0c60c45691a3827844286930"}, "tags": {"0.1.1--py27h24bf2e0_0": "sha256:7583c6fc15d002b1d4e87f8636636ab1091a5d1a9c5216e1b17b790fef16ef0b", "20151031--py35h24bf2e0_2": "sha256:c57f8868cf42250021df9df6ee94a2cf4963d86b0c60c45691a3827844286930", "20151031--py27_1": "sha256:2b62e1d2fc9ab3d2ea7e1b450ca9debfd88cff0dbaa491ce27d3ae4bed6f84bf", "20151031--py27h24bf2e0_2": "sha256:a79c3ad768b961f7451e1357b079ed5ce0a340bcc8a1dec85675667be07c9a79", "20151031--py35_1": "sha256:95230ac88b8fff51a017f04bda08f373971ef23cc29be09746eb3d8364c2b66d"}, "docker": "quay.io/biocontainers/hmmlearn", "aliases": {"conv-template": "/usr/local/bin/conv-template", "from-template": "/usr/local/bin/from-template", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hmmlearn.
shpc-registry automated BioContainers addition for hmmlearn
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hmmlearn
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hmmlearn:20151031--py35h24bf2e0_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hmmlearn/20151031--py35h24bf2e0_2
$ module help quay.io/biocontainers/hmmlearn/20151031--py35h24bf2e0_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hmmlearn-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hmmlearn-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hmmlearn-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hmmlearn-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hmmlearn-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hmmlearn-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### conv-template

```bash
$ singularity exec <container> /usr/local/bin/conv-template
$ podman run --it --rm --entrypoint /usr/local/bin/conv-template   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conv-template   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### from-template

```bash
$ singularity exec <container> /usr/local/bin/from-template
$ podman run --it --rm --entrypoint /usr/local/bin/from-template   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/from-template   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### python2

```bash
$ singularity exec <container> /usr/local/bin/python2
$ podman run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7

```bash
$ singularity exec <container> /usr/local/bin/python2.7
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle

```bash
$ singularity exec <container> /usr/local/bin/idle
$ podman run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-config

```bash
$ singularity exec <container> /usr/local/bin/python-config
$ podman run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smtpd.py

```bash
$ singularity exec <container> /usr/local/bin/smtpd.py
$ podman run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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
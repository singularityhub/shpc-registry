---
layout: container
name:  "quay.io/biocontainers/python-edlib"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/python-edlib/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/python-edlib/container.yaml"
updated_at: "2024-11-24 03:42:26.655831"
latest: "1.3.9--py310h84f13bb_8"
container_url: "https://biocontainers.pro/tools/python-edlib"
aliases:
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
versions:
 - "1.3.9--py27he8a552f_0"
 - "1.3.9--py38h2494328_4"
 - "1.3.9--py38h2494328_5"
 - "1.3.9--py310h0dbaff4_6"
 - "1.3.9--py311h2a4ad6c_7"
 - "1.3.9--py310h84f13bb_8"
description: "shpc-registry automated BioContainers addition for python-edlib"
config: {"url": "https://biocontainers.pro/tools/python-edlib", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for python-edlib", "latest": {"1.3.9--py310h84f13bb_8": "sha256:47770880a790539eb6f11e22d7a92405969bbd3d7d6cc4b929f3255f03be3749"}, "tags": {"1.3.9--py27he8a552f_0": "sha256:73d9eea9a3a3f41648fc43e4edf15c9f6d69e481c2af43498e84fce1dcdcfbbc", "1.3.9--py38h2494328_4": "sha256:74e1b74979f3fd2e5a08a74b4771534971b0075bef949e3ff50cbf30bda720d3", "1.3.9--py38h2494328_5": "sha256:e3aa76d89f4895355d90ae9f8b87d621c4da17dc3aa1f62105006003cf64f9cd", "1.3.9--py310h0dbaff4_6": "sha256:b5d58ed578f3211ac1dd92233bd62d62f46b5d387e62cb30d3fd75de194782a1", "1.3.9--py311h2a4ad6c_7": "sha256:93423bf593b0d6577540cfa169d464435c916130b11c9306939b98ea5bf4d73c", "1.3.9--py310h84f13bb_8": "sha256:47770880a790539eb6f11e22d7a92405969bbd3d7d6cc4b929f3255f03be3749"}, "docker": "quay.io/biocontainers/python-edlib", "aliases": {"python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/python-edlib.
shpc-registry automated BioContainers addition for python-edlib
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/python-edlib
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/python-edlib:1.3.9--py310h84f13bb_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/python-edlib/1.3.9--py310h84f13bb_8
$ module help quay.io/biocontainers/python-edlib/1.3.9--py310h84f13bb_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### python-edlib-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### python-edlib-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### python-edlib-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### python-edlib-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### python-edlib-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### python-edlib-inspect-deffile:

```bash
$ singularity inspect -d <container>
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
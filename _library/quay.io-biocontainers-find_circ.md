---
layout: container
name:  "quay.io/biocontainers/find_circ"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/find_circ/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/find_circ/container.yaml"
updated_at: "2023-08-25 03:18:09.791128"
latest: "1.2--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/find_circ"
aliases:
 - "cmp_bed.py"
 - "find_circ.py"
 - "maxlength.py"
 - "merge_bed.py"
 - "unmapped2anchors.py"
 - "f2py2"
 - "f2py2.7"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
versions:
 - "1.2--hdfd78af_0"
description: "singularity registry hpc automated addition for find_circ"
config: {"url": "https://biocontainers.pro/tools/find_circ", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for find_circ", "latest": {"1.2--hdfd78af_0": "sha256:0e46cf8c9e35df7bd9a662528382f3e228194d880c40bfd717d3c061ed87d500"}, "tags": {"1.2--hdfd78af_0": "sha256:0e46cf8c9e35df7bd9a662528382f3e228194d880c40bfd717d3c061ed87d500"}, "docker": "quay.io/biocontainers/find_circ", "aliases": {"cmp_bed.py": "/usr/local/bin/cmp_bed.py", "find_circ.py": "/usr/local/bin/find_circ.py", "maxlength.py": "/usr/local/bin/maxlength.py", "merge_bed.py": "/usr/local/bin/merge_bed.py", "unmapped2anchors.py": "/usr/local/bin/unmapped2anchors.py", "f2py2": "/usr/local/bin/f2py2", "f2py2.7": "/usr/local/bin/f2py2.7", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/find_circ.
singularity registry hpc automated addition for find_circ
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/find_circ
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/find_circ:1.2--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/find_circ/1.2--hdfd78af_0
$ module help quay.io/biocontainers/find_circ/1.2--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### find_circ-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### find_circ-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### find_circ-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### find_circ-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### find_circ-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### find_circ-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cmp_bed.py

```bash
$ singularity exec <container> /usr/local/bin/cmp_bed.py
$ podman run --it --rm --entrypoint /usr/local/bin/cmp_bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmp_bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find_circ.py

```bash
$ singularity exec <container> /usr/local/bin/find_circ.py
$ podman run --it --rm --entrypoint /usr/local/bin/find_circ.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find_circ.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maxlength.py

```bash
$ singularity exec <container> /usr/local/bin/maxlength.py
$ podman run --it --rm --entrypoint /usr/local/bin/maxlength.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maxlength.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge_bed.py

```bash
$ singularity exec <container> /usr/local/bin/merge_bed.py
$ podman run --it --rm --entrypoint /usr/local/bin/merge_bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unmapped2anchors.py

```bash
$ singularity exec <container> /usr/local/bin/unmapped2anchors.py
$ podman run --it --rm --entrypoint /usr/local/bin/unmapped2anchors.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unmapped2anchors.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2

```bash
$ singularity exec <container> /usr/local/bin/f2py2
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2.7

```bash
$ singularity exec <container> /usr/local/bin/f2py2.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
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
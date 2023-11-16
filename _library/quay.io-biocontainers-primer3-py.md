---
layout: container
name:  "quay.io/biocontainers/primer3-py"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/primer3-py/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/primer3-py/container.yaml"
updated_at: "2023-11-16 02:48:10.570306"
latest: "2.0.1--py311h031d066_0"
container_url: "https://biocontainers.pro/tools/primer3-py"
aliases:
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
versions:
 - "0.6.1--py27h9801fc8_1"
 - "1.2.0--py311hec16e2b_0"
 - "1.2.1--py311hec16e2b_0"
 - "2.0.0--py311hec16e2b_0"
 - "1.2.2--py311hec16e2b_0"
 - "2.0.1--py311h031d066_0"
description: "shpc-registry automated BioContainers addition for primer3-py"
config: {"url": "https://biocontainers.pro/tools/primer3-py", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for primer3-py", "latest": {"2.0.1--py311h031d066_0": "sha256:ca4233e61403c347ff4d15d670b33461b2215d988df036b8cde11e402f49122a"}, "tags": {"0.6.1--py27h9801fc8_1": "sha256:61a01cd51d6f5e74dff60f08b12aeefb44e74b51a26b2c7146d92fac7fa66593", "1.2.0--py311hec16e2b_0": "sha256:eb6a8c0d9785e85a23ec7427d77ff942f1cd6f5adefec875cd60ea7240ccb210", "1.2.1--py311hec16e2b_0": "sha256:52b73c4300355427a0707859457eb1cec8f32c148796f8b14e9ba16fe49c1e1e", "2.0.0--py311hec16e2b_0": "sha256:5f7ffb160d571bd27e41b3b15638f2ce0f56c92591e679d5626a23992fa37156", "1.2.2--py311hec16e2b_0": "sha256:6043cdd10fe44721b7ee33acb83d87bd7fbb612c783dda15e6d480485f532d97", "2.0.1--py311h031d066_0": "sha256:ca4233e61403c347ff4d15d670b33461b2215d988df036b8cde11e402f49122a"}, "docker": "quay.io/biocontainers/primer3-py", "aliases": {"python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/primer3-py.
shpc-registry automated BioContainers addition for primer3-py
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/primer3-py
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/primer3-py:2.0.1--py311h031d066_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/primer3-py/2.0.1--py311h031d066_0
$ module help quay.io/biocontainers/primer3-py/2.0.1--py311h031d066_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### primer3-py-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### primer3-py-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### primer3-py-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### primer3-py-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### primer3-py-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### primer3-py-inspect-deffile:

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
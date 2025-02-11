---
layout: container
name:  "quay.io/biocontainers/deeptoolsintervals"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/deeptoolsintervals/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/deeptoolsintervals/container.yaml"
updated_at: "2025-02-11 03:31:46.373840"
latest: "0.1.9--py312ha9c1134_11"
container_url: "https://biocontainers.pro/tools/deeptoolsintervals"
aliases:
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
versions:
 - "0.1.9--py27h9801fc8_4"
 - "0.1.9--py39h87d955d_5"
 - "0.1.9--py310h8472f5a_6"
 - "0.1.9--py310h8472f5a_7"
 - "0.1.9--py39h87d955d_7"
 - "0.1.9--py38h4c6a040_8"
 - "0.1.9--py312h21b0f09_9"
 - "0.1.9--py312ha9c1134_10"
 - "0.1.9--py312ha9c1134_11"
description: "shpc-registry automated BioContainers addition for deeptoolsintervals"
config: {"url": "https://biocontainers.pro/tools/deeptoolsintervals", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for deeptoolsintervals", "latest": {"0.1.9--py312ha9c1134_11": "sha256:2190dac55fadd1f8e79371eae1ca7487594c7aece249f50baffcd773c26da9b9"}, "tags": {"0.1.9--py27h9801fc8_4": "sha256:903220a951714054dd1d2386e794cef191ecac6b2cdd0446f30d746e00661642", "0.1.9--py39h87d955d_5": "sha256:0545250d5a69f037a832a3b187470aa59df2681a6b7c239aec8ad411106d41f3", "0.1.9--py310h8472f5a_6": "sha256:97262820c3446fe70596e4ad1f916bd73e31ef9a7b09d739d9d989e6e60e2bb5", "0.1.9--py310h8472f5a_7": "sha256:f80da71c8c20df74fa3f33c11a0803c94662d7d0d2c9e37ce41d51bd866e4d74", "0.1.9--py39h87d955d_7": "sha256:24ef8a946d45e3a5c2ac163f7a5f44cd2038c7941fc18b8e05e924bcd722a79a", "0.1.9--py38h4c6a040_8": "sha256:1b84468e617d594316114d2b5cc13f4fd3d0e755ef583f415444234347745eb5", "0.1.9--py312h21b0f09_9": "sha256:68d5926ba2555c84a29a3c900b7ab74953d6dc682e63310593732920c0e09be0", "0.1.9--py312ha9c1134_10": "sha256:9436d34b2e6d3933ba95e01cf5a6e8ad4e28bc6d43df80b00d23b509717c4a3d", "0.1.9--py312ha9c1134_11": "sha256:2190dac55fadd1f8e79371eae1ca7487594c7aece249f50baffcd773c26da9b9"}, "docker": "quay.io/biocontainers/deeptoolsintervals", "aliases": {"python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/deeptoolsintervals.
shpc-registry automated BioContainers addition for deeptoolsintervals
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/deeptoolsintervals
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/deeptoolsintervals:0.1.9--py312ha9c1134_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/deeptoolsintervals/0.1.9--py312ha9c1134_11
$ module help quay.io/biocontainers/deeptoolsintervals/0.1.9--py312ha9c1134_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### deeptoolsintervals-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### deeptoolsintervals-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### deeptoolsintervals-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### deeptoolsintervals-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### deeptoolsintervals-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### deeptoolsintervals-inspect-deffile:

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
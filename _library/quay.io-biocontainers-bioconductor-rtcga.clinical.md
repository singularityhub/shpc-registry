---
layout: container
name:  "quay.io/biocontainers/bioconductor-rtcga.clinical"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rtcga.clinical/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rtcga.clinical/container.yaml"
updated_at: "2025-02-27 03:33:09.730199"
latest: "20151101.36.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rtcga.clinical"
aliases:
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
versions:
 - "20151101.24.0--r41hdfd78af_1"
 - "20151101.27.0--r42hdfd78af_0"
 - "20151101.30.0--r43hdfd78af_0"
 - "20151101.32.0--r43hdfd78af_0"
 - "20151101.36.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rtcga.clinical"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rtcga.clinical", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rtcga.clinical", "latest": {"20151101.36.0--r44hdfd78af_0": "sha256:ecfc3ca1e26652a3a1de6f680d69987fb5c365d464e85130ee93575401b384bf"}, "tags": {"20151101.24.0--r41hdfd78af_1": "sha256:9c63afdd9a5b588e90b9cf82cca1f4eaed3704b6619dfff4799b0ff8cf9a0def", "20151101.27.0--r42hdfd78af_0": "sha256:0ea98e72882ca471bb8a29a5b1609fa107425fff88c22863794e7d91315c198c", "20151101.30.0--r43hdfd78af_0": "sha256:cb050dc945a64f40ddf987ca3cd823dffb6f6258acf2029d5c943cba7c321fe1", "20151101.32.0--r43hdfd78af_0": "sha256:4e1e1a6826e75bdc7c0f94003eb55056808874aa584a7f8d120d467e1a37445f", "20151101.36.0--r44hdfd78af_0": "sha256:ecfc3ca1e26652a3a1de6f680d69987fb5c365d464e85130ee93575401b384bf"}, "docker": "quay.io/biocontainers/bioconductor-rtcga.clinical", "aliases": {"f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rtcga.clinical.
shpc-registry automated BioContainers addition for bioconductor-rtcga.clinical
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rtcga.clinical
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rtcga.clinical:20151101.36.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rtcga.clinical/20151101.36.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rtcga.clinical/20151101.36.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rtcga.clinical-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rtcga.clinical-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rtcga.clinical-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rtcga.clinical-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rtcga.clinical-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rtcga.clinical-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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
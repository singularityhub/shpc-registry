---
layout: container
name:  "quay.io/biocontainers/jcvi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/jcvi/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/jcvi/container.yaml"
updated_at: "2022-10-29 05:52:07.165639"
latest: "1.1.5--py36h29c9776_0"
container_url: "https://biocontainers.pro/tools/jcvi"
aliases:
 - "coveralls"
 - "cpuinfo"
 - "py.test-benchmark"
 - "pytest-benchmark"
 - "2to3-3.6"
 - "activate-global-python-argcomplete"
 - "acyclic"
 - "assistant"
 - "bcomps"
 - "canbusutil"
 - "ccomps"
 - "certutil"
 - "chardetect"
 - "circo"
versions:
 - "1.1.5--py36h29c9776_0"
description: "shpc-registry automated BioContainers addition for jcvi"
config: {"url": "https://biocontainers.pro/tools/jcvi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for jcvi", "latest": {"1.1.5--py36h29c9776_0": "sha256:f425a65bada8e48b55f298d13782051d9e944439ff9091ce56a33ee9e9f261db"}, "tags": {"1.1.5--py36h29c9776_0": "sha256:f425a65bada8e48b55f298d13782051d9e944439ff9091ce56a33ee9e9f261db"}, "docker": "quay.io/biocontainers/jcvi", "aliases": {"coveralls": "/usr/local/bin/coveralls", "cpuinfo": "/usr/local/bin/cpuinfo", "py.test-benchmark": "/usr/local/bin/py.test-benchmark", "pytest-benchmark": "/usr/local/bin/pytest-benchmark", "2to3-3.6": "/usr/local/bin/2to3-3.6", "activate-global-python-argcomplete": "/usr/local/bin/activate-global-python-argcomplete", "acyclic": "/usr/local/bin/acyclic", "assistant": "/usr/local/bin/assistant", "bcomps": "/usr/local/bin/bcomps", "canbusutil": "/usr/local/bin/canbusutil", "ccomps": "/usr/local/bin/ccomps", "certutil": "/usr/local/bin/certutil", "chardetect": "/usr/local/bin/chardetect", "circo": "/usr/local/bin/circo"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/jcvi.
shpc-registry automated BioContainers addition for jcvi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/jcvi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/jcvi:1.1.5--py36h29c9776_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/jcvi/1.1.5--py36h29c9776_0
$ module help quay.io/biocontainers/jcvi/1.1.5--py36h29c9776_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### jcvi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### jcvi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### jcvi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### jcvi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### jcvi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### jcvi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### coveralls

```bash
$ singularity exec <container> /usr/local/bin/coveralls
$ podman run --it --rm --entrypoint /usr/local/bin/coveralls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coveralls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpuinfo

```bash
$ singularity exec <container> /usr/local/bin/cpuinfo
$ podman run --it --rm --entrypoint /usr/local/bin/cpuinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpuinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### py.test-benchmark

```bash
$ singularity exec <container> /usr/local/bin/py.test-benchmark
$ podman run --it --rm --entrypoint /usr/local/bin/py.test-benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/py.test-benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pytest-benchmark

```bash
$ singularity exec <container> /usr/local/bin/pytest-benchmark
$ podman run --it --rm --entrypoint /usr/local/bin/pytest-benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pytest-benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### activate-global-python-argcomplete

```bash
$ singularity exec <container> /usr/local/bin/activate-global-python-argcomplete
$ podman run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acyclic

```bash
$ singularity exec <container> /usr/local/bin/acyclic
$ podman run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### assistant

```bash
$ singularity exec <container> /usr/local/bin/assistant
$ podman run --it --rm --entrypoint /usr/local/bin/assistant   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/assistant   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bcomps

```bash
$ singularity exec <container> /usr/local/bin/bcomps
$ podman run --it --rm --entrypoint /usr/local/bin/bcomps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcomps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### canbusutil

```bash
$ singularity exec <container> /usr/local/bin/canbusutil
$ podman run --it --rm --entrypoint /usr/local/bin/canbusutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/canbusutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ccomps

```bash
$ singularity exec <container> /usr/local/bin/ccomps
$ podman run --it --rm --entrypoint /usr/local/bin/ccomps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccomps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### certutil

```bash
$ singularity exec <container> /usr/local/bin/certutil
$ podman run --it --rm --entrypoint /usr/local/bin/certutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/certutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### circo

```bash
$ singularity exec <container> /usr/local/bin/circo
$ podman run --it --rm --entrypoint /usr/local/bin/circo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/circo   -v ${PWD} -w ${PWD} <container> -c " $@"
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
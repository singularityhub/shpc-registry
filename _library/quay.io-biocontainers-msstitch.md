---
layout: container
name:  "quay.io/biocontainers/msstitch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/msstitch/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/msstitch/container.yaml"
updated_at: "2024-11-08 03:13:17.048900"
latest: "3.16--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/msstitch"
aliases:
 - "msstitch"
 - "xslt-config"
 - "xsltproc"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
versions:
 - "3.9--pyhdfd78af_0"
 - "3.11--pyhdfd78af_0"
 - "3.10--pyhdfd78af_0"
 - "3.13--pyhdfd78af_0"
 - "3.12--pyhdfd78af_0"
 - "3.14--pyhdfd78af_0"
 - "3.15--pyhdfd78af_0"
 - "3.16--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for msstitch"
config: {"url": "https://biocontainers.pro/tools/msstitch", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for msstitch", "latest": {"3.16--pyhdfd78af_0": "sha256:2811254656851e3868c81af2caa8b7a1b1b8f1d7c07dc07f06bcb969a8a9f955"}, "tags": {"3.9--pyhdfd78af_0": "sha256:22c86ee8f362099c0081c2af88e669429bffcb07ca7b0764c65a4cc749ea0015", "3.11--pyhdfd78af_0": "sha256:e559ceb561205f9e77e1c84b4500d5c206af2ba78548cf4644d453d3005ae3fd", "3.10--pyhdfd78af_0": "sha256:247cb99b9cdfeb7ed6e2a200096574e6108405ad7b6f9dcfa19a24e7fc10fc55", "3.13--pyhdfd78af_0": "sha256:5c49839da79530b941df2fd66b84c8b95bd9dca69f26d76ef2e4dc8427bbfb87", "3.12--pyhdfd78af_0": "sha256:47be4b3f4b66f8a712d9a6ab27e37569720f90dedf3b9293c0fec7c92a5d45ce", "3.14--pyhdfd78af_0": "sha256:e5dda6b879a5c8ca29f2eff32ea46fc78bf201f0c4b77623c0c8316090f95064", "3.15--pyhdfd78af_0": "sha256:257c417314523dc3c9225ee706301bd8f8d4e3c687fa530868bf15c52599c1dc", "3.16--pyhdfd78af_0": "sha256:2811254656851e3868c81af2caa8b7a1b1b8f1d7c07dc07f06bcb969a8a9f955"}, "docker": "quay.io/biocontainers/msstitch", "aliases": {"msstitch": "/usr/local/bin/msstitch", "xslt-config": "/usr/local/bin/xslt-config", "xsltproc": "/usr/local/bin/xsltproc", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/msstitch.
shpc-registry automated BioContainers addition for msstitch
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/msstitch
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/msstitch:3.16--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/msstitch/3.16--pyhdfd78af_0
$ module help quay.io/biocontainers/msstitch/3.16--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### msstitch-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### msstitch-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### msstitch-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### msstitch-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### msstitch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### msstitch-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### msstitch

```bash
$ singularity exec <container> /usr/local/bin/msstitch
$ podman run --it --rm --entrypoint /usr/local/bin/msstitch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/msstitch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xslt-config

```bash
$ singularity exec <container> /usr/local/bin/xslt-config
$ podman run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xsltproc

```bash
$ singularity exec <container> /usr/local/bin/xsltproc
$ podman run --it --rm --entrypoint /usr/local/bin/xsltproc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xsltproc   -v ${PWD} -w ${PWD} <container> -c " $@"
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
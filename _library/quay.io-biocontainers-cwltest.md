---
layout: container
name:  "quay.io/biocontainers/cwltest"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cwltest/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/cwltest/container.yaml"
updated_at: "2022-10-29 05:42:22.799181"
latest: "2.2.20220521103021--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/cwltest"
aliases:
 - "cwltest"
 - "mock-cwl-runner"
 - "2to3-3.10"
 - "black"
 - "blackd"
 - "csv2rdf"
 - "doesitcache"
 - "idle3.10"
 - "normalizer"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
versions:
 - "2.2.20220521103021--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for cwltest"
config: {"url": "https://biocontainers.pro/tools/cwltest", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cwltest", "latest": {"2.2.20220521103021--pyhdfd78af_0": "sha256:3d4b506dfd348f63359e5e772f8e3aa5feb30c60c11b3fa4c5893e1055c01b0a"}, "tags": {"2.2.20220521103021--pyhdfd78af_0": "sha256:3d4b506dfd348f63359e5e772f8e3aa5feb30c60c11b3fa4c5893e1055c01b0a"}, "docker": "quay.io/biocontainers/cwltest", "aliases": {"cwltest": "/usr/local/bin/cwltest", "mock-cwl-runner": "/usr/local/bin/mock-cwl-runner", "2to3-3.10": "/usr/local/bin/2to3-3.10", "black": "/usr/local/bin/black", "blackd": "/usr/local/bin/blackd", "csv2rdf": "/usr/local/bin/csv2rdf", "doesitcache": "/usr/local/bin/doesitcache", "idle3.10": "/usr/local/bin/idle3.10", "normalizer": "/usr/local/bin/normalizer", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cwltest.
shpc-registry automated BioContainers addition for cwltest
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cwltest
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cwltest:2.2.20220521103021--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cwltest/2.2.20220521103021--pyhdfd78af_0
$ module help quay.io/biocontainers/cwltest/2.2.20220521103021--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cwltest-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cwltest-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cwltest-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cwltest-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cwltest-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cwltest-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cwltest

```bash
$ singularity exec <container> /usr/local/bin/cwltest
$ podman run --it --rm --entrypoint /usr/local/bin/cwltest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwltest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mock-cwl-runner

```bash
$ singularity exec <container> /usr/local/bin/mock-cwl-runner
$ podman run --it --rm --entrypoint /usr/local/bin/mock-cwl-runner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mock-cwl-runner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### black

```bash
$ singularity exec <container> /usr/local/bin/black
$ podman run --it --rm --entrypoint /usr/local/bin/black   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/black   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blackd

```bash
$ singularity exec <container> /usr/local/bin/blackd
$ podman run --it --rm --entrypoint /usr/local/bin/blackd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blackd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csv2rdf

```bash
$ singularity exec <container> /usr/local/bin/csv2rdf
$ podman run --it --rm --entrypoint /usr/local/bin/csv2rdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csv2rdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### doesitcache

```bash
$ singularity exec <container> /usr/local/bin/doesitcache
$ podman run --it --rm --entrypoint /usr/local/bin/doesitcache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/doesitcache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
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
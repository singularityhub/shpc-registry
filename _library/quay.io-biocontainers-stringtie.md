---
layout: container
name:  "quay.io/biocontainers/stringtie"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/stringtie/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/stringtie/container.yaml"
updated_at: "2025-12-23 04:22:08.713507"
latest: "3.0.1--h00789bb_0"
container_url: "https://biocontainers.pro/tools/stringtie"
aliases:
 - "prepDE.py"
 - "stringtie"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "2.2.1--hecb563c_2"
 - "2.2.1--h43eeafb_6"
 - "2.2.2--h43eeafb_0"
 - "2.2.3--h43eeafb_0"
 - "2.2.3--h29c0135_1"
 - "3.0.0--h29c0135_0"
 - "3.0.0--h29c0135_1"
 - "3.0.1--h00789bb_0"
description: "shpc-registry automated BioContainers addition for stringtie"
config: {"url": "https://biocontainers.pro/tools/stringtie", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for stringtie", "latest": {"3.0.1--h00789bb_0": "sha256:d64160306b9169005a22857b8b8126ac96f2fde94b4378b6124580fd21344d8b"}, "tags": {"2.2.1--hecb563c_2": "sha256:8f557d827442a99b264caf623e075f4e3bd4421b2ffc8de69bc45156a076dadf", "2.2.1--h43eeafb_6": "sha256:3a57bf3a577e0027d2a35ff9fc5f95ceb376893dd40d467d4b216cc85678e8e6", "2.2.2--h43eeafb_0": "sha256:cc576f430b193ae4f42ac518375b13488957f251460aad3723ff0da38fa99922", "2.2.3--h43eeafb_0": "sha256:3ae64324a4729c6af09eb1246cd315920136758c0d5743845fd1980769087aa3", "2.2.3--h29c0135_1": "sha256:84207eb013dbcff90928d8ddc75902580d3885ce8edaa36b8fab7665a3dc2e3c", "3.0.0--h29c0135_0": "sha256:b538543e1bf7e7a59f4a53dc70c1efbc19c0031c65ec1f0930714b586a1deb2c", "3.0.0--h29c0135_1": "sha256:1e2d08591607f70ee10b830a5fd17eaa3c1c34d25ca28cb224a73658053a1f31", "3.0.1--h00789bb_0": "sha256:d64160306b9169005a22857b8b8126ac96f2fde94b4378b6124580fd21344d8b"}, "docker": "quay.io/biocontainers/stringtie", "aliases": {"prepDE.py": "/usr/local/bin/prepDE.py", "stringtie": "/usr/local/bin/stringtie", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/stringtie.
shpc-registry automated BioContainers addition for stringtie
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/stringtie
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/stringtie:3.0.1--h00789bb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/stringtie/3.0.1--h00789bb_0
$ module help quay.io/biocontainers/stringtie/3.0.1--h00789bb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### stringtie-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### stringtie-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### stringtie-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### stringtie-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### stringtie-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### stringtie-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### prepDE.py

```bash
$ singularity exec <container> /usr/local/bin/prepDE.py
$ podman run --it --rm --entrypoint /usr/local/bin/prepDE.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prepDE.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stringtie

```bash
$ singularity exec <container> /usr/local/bin/stringtie
$ podman run --it --rm --entrypoint /usr/local/bin/stringtie   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stringtie   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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
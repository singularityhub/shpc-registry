---
layout: container
name:  "quay.io/biocontainers/instrain"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/instrain/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/instrain/container.yaml"
updated_at: "2022-10-27 00:37:19.335483"
latest: "1.6.3--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/instrain"
aliases:
 - "ScaffoldLevel_dRep.py"
 - "dRep"
 - "inStrain"
 - "parse_stb.py"
versions:
 - "1.6.3--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for instrain"
config: {"url": "https://biocontainers.pro/tools/instrain", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for instrain", "latest": {"1.6.3--pyhdfd78af_0": "sha256:d5eee857a567b91b778ca593c69ae410fcd804b668dbeaa703f4b0f99232e88a"}, "tags": {"1.6.3--pyhdfd78af_0": "sha256:d5eee857a567b91b778ca593c69ae410fcd804b668dbeaa703f4b0f99232e88a"}, "docker": "quay.io/biocontainers/instrain", "aliases": {"ScaffoldLevel_dRep.py": "/usr/local/bin/ScaffoldLevel_dRep.py", "dRep": "/usr/local/bin/dRep", "inStrain": "/usr/local/bin/inStrain", "parse_stb.py": "/usr/local/bin/parse_stb.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/instrain.
shpc-registry automated BioContainers addition for instrain
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/instrain
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/instrain:1.6.3--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/instrain/1.6.3--pyhdfd78af_0
$ module help quay.io/biocontainers/instrain/1.6.3--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### instrain-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### instrain-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### instrain-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### instrain-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### instrain-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### instrain-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ScaffoldLevel_dRep.py

```bash
$ singularity exec <container> /usr/local/bin/ScaffoldLevel_dRep.py
$ podman run --it --rm --entrypoint /usr/local/bin/ScaffoldLevel_dRep.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ScaffoldLevel_dRep.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dRep

```bash
$ singularity exec <container> /usr/local/bin/dRep
$ podman run --it --rm --entrypoint /usr/local/bin/dRep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dRep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### inStrain

```bash
$ singularity exec <container> /usr/local/bin/inStrain
$ podman run --it --rm --entrypoint /usr/local/bin/inStrain   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/inStrain   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parse_stb.py

```bash
$ singularity exec <container> /usr/local/bin/parse_stb.py
$ podman run --it --rm --entrypoint /usr/local/bin/parse_stb.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parse_stb.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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
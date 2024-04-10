---
layout: container
name:  "quay.io/biocontainers/straglr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/straglr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/straglr/container.yaml"
updated_at: "2024-04-10 02:56:10.838852"
latest: "1.4.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/straglr"
aliases:
 - "pathos_connect"
 - "portpicker"
 - "pox"
 - "ppserver"
 - "straglr.py"
 - "straglr_compare.py"
 - "trf4.10.0-rc.2.linux64.exe"
 - "trf"
 - "get_objgraph"
 - "undill"
 - "edirect.py"
 - "filter-columns"
 - "fuse-segments"
 - "gene2range"
 - "tbl2prod"
 - "uniq-table"
versions:
 - "1.3.0--pyhdfd78af_0"
 - "1.4.0--pyhdfd78af_0"
 - "1.4.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for straglr"
config: {"url": "https://biocontainers.pro/tools/straglr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for straglr", "latest": {"1.4.1--pyhdfd78af_0": "sha256:373914b663a4391e4bc479e891e2c1de0a8b2d41fdfe8fad85a492342a370875"}, "tags": {"1.3.0--pyhdfd78af_0": "sha256:cad130315c7e8c4c33436b660381a3b3725e72f2e3b20afa04d5d194442f6627", "1.4.0--pyhdfd78af_0": "sha256:07f275460d28286002daf3aa54de02a533f5a3406b1874f75c0bcf96813da913", "1.4.1--pyhdfd78af_0": "sha256:373914b663a4391e4bc479e891e2c1de0a8b2d41fdfe8fad85a492342a370875"}, "docker": "quay.io/biocontainers/straglr", "aliases": {"pathos_connect": "/usr/local/bin/pathos_connect", "portpicker": "/usr/local/bin/portpicker", "pox": "/usr/local/bin/pox", "ppserver": "/usr/local/bin/ppserver", "straglr.py": "/usr/local/bin/straglr.py", "straglr_compare.py": "/usr/local/bin/straglr_compare.py", "trf4.10.0-rc.2.linux64.exe": "/usr/local/bin/trf4.10.0-rc.2.linux64.exe", "trf": "/usr/local/bin/trf", "get_objgraph": "/usr/local/bin/get_objgraph", "undill": "/usr/local/bin/undill", "edirect.py": "/usr/local/bin/edirect.py", "filter-columns": "/usr/local/bin/filter-columns", "fuse-segments": "/usr/local/bin/fuse-segments", "gene2range": "/usr/local/bin/gene2range", "tbl2prod": "/usr/local/bin/tbl2prod", "uniq-table": "/usr/local/bin/uniq-table"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/straglr.
shpc-registry automated BioContainers addition for straglr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/straglr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/straglr:1.4.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/straglr/1.4.1--pyhdfd78af_0
$ module help quay.io/biocontainers/straglr/1.4.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### straglr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### straglr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### straglr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### straglr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### straglr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### straglr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pathos_connect

```bash
$ singularity exec <container> /usr/local/bin/pathos_connect
$ podman run --it --rm --entrypoint /usr/local/bin/pathos_connect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pathos_connect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### portpicker

```bash
$ singularity exec <container> /usr/local/bin/portpicker
$ podman run --it --rm --entrypoint /usr/local/bin/portpicker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/portpicker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pox

```bash
$ singularity exec <container> /usr/local/bin/pox
$ podman run --it --rm --entrypoint /usr/local/bin/pox   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pox   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ppserver

```bash
$ singularity exec <container> /usr/local/bin/ppserver
$ podman run --it --rm --entrypoint /usr/local/bin/ppserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ppserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### straglr.py

```bash
$ singularity exec <container> /usr/local/bin/straglr.py
$ podman run --it --rm --entrypoint /usr/local/bin/straglr.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/straglr.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### straglr_compare.py

```bash
$ singularity exec <container> /usr/local/bin/straglr_compare.py
$ podman run --it --rm --entrypoint /usr/local/bin/straglr_compare.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/straglr_compare.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trf4.10.0-rc.2.linux64.exe

```bash
$ singularity exec <container> /usr/local/bin/trf4.10.0-rc.2.linux64.exe
$ podman run --it --rm --entrypoint /usr/local/bin/trf4.10.0-rc.2.linux64.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trf4.10.0-rc.2.linux64.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trf

```bash
$ singularity exec <container> /usr/local/bin/trf
$ podman run --it --rm --entrypoint /usr/local/bin/trf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_objgraph

```bash
$ singularity exec <container> /usr/local/bin/get_objgraph
$ podman run --it --rm --entrypoint /usr/local/bin/get_objgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_objgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### undill

```bash
$ singularity exec <container> /usr/local/bin/undill
$ podman run --it --rm --entrypoint /usr/local/bin/undill   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/undill   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### edirect.py

```bash
$ singularity exec <container> /usr/local/bin/edirect.py
$ podman run --it --rm --entrypoint /usr/local/bin/edirect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edirect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-columns

```bash
$ singularity exec <container> /usr/local/bin/filter-columns
$ podman run --it --rm --entrypoint /usr/local/bin/filter-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fuse-segments

```bash
$ singularity exec <container> /usr/local/bin/fuse-segments
$ podman run --it --rm --entrypoint /usr/local/bin/fuse-segments   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fuse-segments   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gene2range

```bash
$ singularity exec <container> /usr/local/bin/gene2range
$ podman run --it --rm --entrypoint /usr/local/bin/gene2range   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gene2range   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tbl2prod

```bash
$ singularity exec <container> /usr/local/bin/tbl2prod
$ podman run --it --rm --entrypoint /usr/local/bin/tbl2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tbl2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uniq-table

```bash
$ singularity exec <container> /usr/local/bin/uniq-table
$ podman run --it --rm --entrypoint /usr/local/bin/uniq-table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uniq-table   -v ${PWD} -w ${PWD} <container> -c " $@"
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
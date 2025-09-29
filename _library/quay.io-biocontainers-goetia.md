---
layout: container
name:  "quay.io/biocontainers/goetia"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/goetia/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/goetia/container.yaml"
updated_at: "2025-09-29 03:10:59.968390"
latest: "0.14--py36hd181a71_1"
container_url: "https://biocontainers.pro/tools/goetia"
aliases:
 - "bam2fasta"
 - "c-index-test"
 - "clang"
 - "clang++"
 - "clang-5.0"
 - "clang-check"
 - "clang-cl"
 - "clang-cpp"
 - "clang-format"
 - "clang-import-test"
 - "clang-offload-bundler"
 - "clang-rename"
 - "cling-config"
 - "cppyy-generator"
 - "cpuinfo"
 - "draff"
 - "genreflex"
 - "git-clang-format"
 - "goetia"
 - "pathos_connect"
 - "portpicker"
 - "pox"
 - "ppserver"
 - "pyfiglet"
 - "rootcling"
 - "scan-build"
 - "scan-view"
 - "sourmash"
 - "screed"
 - "get_objgraph"
 - "undill"
 - "f2py3.6"
 - "jsonschema"
 - "tqdm"
 - "2to3-3.6"
 - "idle3.6"
 - "pydoc3.6"
 - "python3.6"
versions:
 - "0.14--py36hd181a71_1"
 - "0.14--py37h13b99d1_1"
description: "shpc-registry automated BioContainers addition for goetia"
config: {"url": "https://biocontainers.pro/tools/goetia", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for goetia", "latest": {"0.14--py36hd181a71_1": "sha256:30e6a5ae975f3a1e4ac203ef7835291116de546ab8db00377782ab7158ba8edc"}, "tags": {"0.14--py36hd181a71_1": "sha256:30e6a5ae975f3a1e4ac203ef7835291116de546ab8db00377782ab7158ba8edc", "0.14--py37h13b99d1_1": "sha256:aa5936f416b83dbac7638fb21b84d715f50e186f3b598c8d9d4284377cdffa7a"}, "docker": "quay.io/biocontainers/goetia", "aliases": {"bam2fasta": "/usr/local/bin/bam2fasta", "c-index-test": "/usr/local/bin/c-index-test", "clang": "/usr/local/bin/clang", "clang++": "/usr/local/bin/clang++", "clang-5.0": "/usr/local/bin/clang-5.0", "clang-check": "/usr/local/bin/clang-check", "clang-cl": "/usr/local/bin/clang-cl", "clang-cpp": "/usr/local/bin/clang-cpp", "clang-format": "/usr/local/bin/clang-format", "clang-import-test": "/usr/local/bin/clang-import-test", "clang-offload-bundler": "/usr/local/bin/clang-offload-bundler", "clang-rename": "/usr/local/bin/clang-rename", "cling-config": "/usr/local/bin/cling-config", "cppyy-generator": "/usr/local/bin/cppyy-generator", "cpuinfo": "/usr/local/bin/cpuinfo", "draff": "/usr/local/bin/draff", "genreflex": "/usr/local/bin/genreflex", "git-clang-format": "/usr/local/bin/git-clang-format", "goetia": "/usr/local/bin/goetia", "pathos_connect": "/usr/local/bin/pathos_connect", "portpicker": "/usr/local/bin/portpicker", "pox": "/usr/local/bin/pox", "ppserver": "/usr/local/bin/ppserver", "pyfiglet": "/usr/local/bin/pyfiglet", "rootcling": "/usr/local/bin/rootcling", "scan-build": "/usr/local/bin/scan-build", "scan-view": "/usr/local/bin/scan-view", "sourmash": "/usr/local/bin/sourmash", "screed": "/usr/local/bin/screed", "get_objgraph": "/usr/local/bin/get_objgraph", "undill": "/usr/local/bin/undill", "f2py3.6": "/usr/local/bin/f2py3.6", "jsonschema": "/usr/local/bin/jsonschema", "tqdm": "/usr/local/bin/tqdm", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6", "pydoc3.6": "/usr/local/bin/pydoc3.6", "python3.6": "/usr/local/bin/python3.6"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/goetia.
shpc-registry automated BioContainers addition for goetia
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/goetia
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/goetia:0.14--py36hd181a71_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/goetia/0.14--py36hd181a71_1
$ module help quay.io/biocontainers/goetia/0.14--py36hd181a71_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### goetia-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### goetia-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### goetia-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### goetia-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### goetia-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### goetia-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bam2fasta

```bash
$ singularity exec <container> /usr/local/bin/bam2fasta
$ podman run --it --rm --entrypoint /usr/local/bin/bam2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c-index-test

```bash
$ singularity exec <container> /usr/local/bin/c-index-test
$ podman run --it --rm --entrypoint /usr/local/bin/c-index-test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c-index-test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clang

```bash
$ singularity exec <container> /usr/local/bin/clang
$ podman run --it --rm --entrypoint /usr/local/bin/clang   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clang   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clang++

```bash
$ singularity exec <container> /usr/local/bin/clang++
$ podman run --it --rm --entrypoint /usr/local/bin/clang++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clang++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clang-5.0

```bash
$ singularity exec <container> /usr/local/bin/clang-5.0
$ podman run --it --rm --entrypoint /usr/local/bin/clang-5.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clang-5.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clang-check

```bash
$ singularity exec <container> /usr/local/bin/clang-check
$ podman run --it --rm --entrypoint /usr/local/bin/clang-check   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clang-check   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clang-cl

```bash
$ singularity exec <container> /usr/local/bin/clang-cl
$ podman run --it --rm --entrypoint /usr/local/bin/clang-cl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clang-cl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clang-cpp

```bash
$ singularity exec <container> /usr/local/bin/clang-cpp
$ podman run --it --rm --entrypoint /usr/local/bin/clang-cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clang-cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clang-format

```bash
$ singularity exec <container> /usr/local/bin/clang-format
$ podman run --it --rm --entrypoint /usr/local/bin/clang-format   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clang-format   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clang-import-test

```bash
$ singularity exec <container> /usr/local/bin/clang-import-test
$ podman run --it --rm --entrypoint /usr/local/bin/clang-import-test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clang-import-test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clang-offload-bundler

```bash
$ singularity exec <container> /usr/local/bin/clang-offload-bundler
$ podman run --it --rm --entrypoint /usr/local/bin/clang-offload-bundler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clang-offload-bundler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clang-rename

```bash
$ singularity exec <container> /usr/local/bin/clang-rename
$ podman run --it --rm --entrypoint /usr/local/bin/clang-rename   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clang-rename   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cling-config

```bash
$ singularity exec <container> /usr/local/bin/cling-config
$ podman run --it --rm --entrypoint /usr/local/bin/cling-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cling-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cppyy-generator

```bash
$ singularity exec <container> /usr/local/bin/cppyy-generator
$ podman run --it --rm --entrypoint /usr/local/bin/cppyy-generator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cppyy-generator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpuinfo

```bash
$ singularity exec <container> /usr/local/bin/cpuinfo
$ podman run --it --rm --entrypoint /usr/local/bin/cpuinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpuinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### draff

```bash
$ singularity exec <container> /usr/local/bin/draff
$ podman run --it --rm --entrypoint /usr/local/bin/draff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/draff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genreflex

```bash
$ singularity exec <container> /usr/local/bin/genreflex
$ podman run --it --rm --entrypoint /usr/local/bin/genreflex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genreflex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-clang-format

```bash
$ singularity exec <container> /usr/local/bin/git-clang-format
$ podman run --it --rm --entrypoint /usr/local/bin/git-clang-format   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git-clang-format   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### goetia

```bash
$ singularity exec <container> /usr/local/bin/goetia
$ podman run --it --rm --entrypoint /usr/local/bin/goetia   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/goetia   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### pyfiglet

```bash
$ singularity exec <container> /usr/local/bin/pyfiglet
$ podman run --it --rm --entrypoint /usr/local/bin/pyfiglet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyfiglet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rootcling

```bash
$ singularity exec <container> /usr/local/bin/rootcling
$ podman run --it --rm --entrypoint /usr/local/bin/rootcling   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rootcling   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scan-build

```bash
$ singularity exec <container> /usr/local/bin/scan-build
$ podman run --it --rm --entrypoint /usr/local/bin/scan-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scan-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scan-view

```bash
$ singularity exec <container> /usr/local/bin/scan-view
$ podman run --it --rm --entrypoint /usr/local/bin/scan-view   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scan-view   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sourmash

```bash
$ singularity exec <container> /usr/local/bin/sourmash
$ podman run --it --rm --entrypoint /usr/local/bin/sourmash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sourmash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### screed

```bash
$ singularity exec <container> /usr/local/bin/screed
$ podman run --it --rm --entrypoint /usr/local/bin/screed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/screed   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### f2py3.6

```bash
$ singularity exec <container> /usr/local/bin/f2py3.6
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsonschema

```bash
$ singularity exec <container> /usr/local/bin/jsonschema
$ podman run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tqdm

```bash
$ singularity exec <container> /usr/local/bin/tqdm
$ podman run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.6

```bash
$ singularity exec <container> /usr/local/bin/idle3.6
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.6

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6

```bash
$ singularity exec <container> /usr/local/bin/python3.6
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
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
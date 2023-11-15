---
layout: container
name:  "quay.io/biocontainers/ffgc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ffgc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ffgc/container.yaml"
updated_at: "2023-11-15 02:44:07.764485"
latest: "2.4.2--py311hdfd78af_0"
container_url: "https://biocontainers.pro/tools/ffgc"
aliases:
 - "ffgc_create_project.py"
 - "markdown-it"
 - "clm"
 - "clmformat"
 - "clxdo"
 - "mcl"
 - "mclblastline"
 - "mclcm"
 - "mclpipeline"
 - "mcx"
 - "mcxarray"
 - "mcxassemble"
 - "mcxdeblast"
 - "mcxdump"
 - "mcxi"
 - "mcxload"
 - "mcxmap"
 - "mcxrand"
 - "mcxsubs"
 - "stone"
 - "yte"
 - "plac_runner.py"
 - "docutils"
 - "f2py3.11"
 - "pulptest"
 - "grpc_cpp_plugin"
versions:
 - "2.4.1--py311hdfd78af_0"
 - "2.4.2--py311hdfd78af_0"
description: "singularity registry hpc automated addition for ffgc"
config: {"url": "https://biocontainers.pro/tools/ffgc", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ffgc", "latest": {"2.4.2--py311hdfd78af_0": "sha256:9765171469e3127be8e73b0edf9d9ef2c709fc63c0a3d36f6630077492b86cac"}, "tags": {"2.4.1--py311hdfd78af_0": "sha256:d6a078648a229e559c1e3dafa33abce087409240e8ee1d5c32d141f2968fd385", "2.4.2--py311hdfd78af_0": "sha256:9765171469e3127be8e73b0edf9d9ef2c709fc63c0a3d36f6630077492b86cac"}, "docker": "quay.io/biocontainers/ffgc", "aliases": {"ffgc_create_project.py": "/usr/local/bin/ffgc_create_project.py", "markdown-it": "/usr/local/bin/markdown-it", "clm": "/usr/local/bin/clm", "clmformat": "/usr/local/bin/clmformat", "clxdo": "/usr/local/bin/clxdo", "mcl": "/usr/local/bin/mcl", "mclblastline": "/usr/local/bin/mclblastline", "mclcm": "/usr/local/bin/mclcm", "mclpipeline": "/usr/local/bin/mclpipeline", "mcx": "/usr/local/bin/mcx", "mcxarray": "/usr/local/bin/mcxarray", "mcxassemble": "/usr/local/bin/mcxassemble", "mcxdeblast": "/usr/local/bin/mcxdeblast", "mcxdump": "/usr/local/bin/mcxdump", "mcxi": "/usr/local/bin/mcxi", "mcxload": "/usr/local/bin/mcxload", "mcxmap": "/usr/local/bin/mcxmap", "mcxrand": "/usr/local/bin/mcxrand", "mcxsubs": "/usr/local/bin/mcxsubs", "stone": "/usr/local/bin/stone", "yte": "/usr/local/bin/yte", "plac_runner.py": "/usr/local/bin/plac_runner.py", "docutils": "/usr/local/bin/docutils", "f2py3.11": "/usr/local/bin/f2py3.11", "pulptest": "/usr/local/bin/pulptest", "grpc_cpp_plugin": "/usr/local/bin/grpc_cpp_plugin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ffgc.
singularity registry hpc automated addition for ffgc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ffgc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ffgc:2.4.2--py311hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ffgc/2.4.2--py311hdfd78af_0
$ module help quay.io/biocontainers/ffgc/2.4.2--py311hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ffgc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ffgc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ffgc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ffgc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ffgc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ffgc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ffgc_create_project.py

```bash
$ singularity exec <container> /usr/local/bin/ffgc_create_project.py
$ podman run --it --rm --entrypoint /usr/local/bin/ffgc_create_project.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ffgc_create_project.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### markdown-it

```bash
$ singularity exec <container> /usr/local/bin/markdown-it
$ podman run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clm

```bash
$ singularity exec <container> /usr/local/bin/clm
$ podman run --it --rm --entrypoint /usr/local/bin/clm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clmformat

```bash
$ singularity exec <container> /usr/local/bin/clmformat
$ podman run --it --rm --entrypoint /usr/local/bin/clmformat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clmformat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clxdo

```bash
$ singularity exec <container> /usr/local/bin/clxdo
$ podman run --it --rm --entrypoint /usr/local/bin/clxdo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clxdo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcl

```bash
$ singularity exec <container> /usr/local/bin/mcl
$ podman run --it --rm --entrypoint /usr/local/bin/mcl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mclblastline

```bash
$ singularity exec <container> /usr/local/bin/mclblastline
$ podman run --it --rm --entrypoint /usr/local/bin/mclblastline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mclblastline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mclcm

```bash
$ singularity exec <container> /usr/local/bin/mclcm
$ podman run --it --rm --entrypoint /usr/local/bin/mclcm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mclcm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mclpipeline

```bash
$ singularity exec <container> /usr/local/bin/mclpipeline
$ podman run --it --rm --entrypoint /usr/local/bin/mclpipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mclpipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcx

```bash
$ singularity exec <container> /usr/local/bin/mcx
$ podman run --it --rm --entrypoint /usr/local/bin/mcx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcxarray

```bash
$ singularity exec <container> /usr/local/bin/mcxarray
$ podman run --it --rm --entrypoint /usr/local/bin/mcxarray   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcxarray   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcxassemble

```bash
$ singularity exec <container> /usr/local/bin/mcxassemble
$ podman run --it --rm --entrypoint /usr/local/bin/mcxassemble   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcxassemble   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcxdeblast

```bash
$ singularity exec <container> /usr/local/bin/mcxdeblast
$ podman run --it --rm --entrypoint /usr/local/bin/mcxdeblast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcxdeblast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcxdump

```bash
$ singularity exec <container> /usr/local/bin/mcxdump
$ podman run --it --rm --entrypoint /usr/local/bin/mcxdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcxdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcxi

```bash
$ singularity exec <container> /usr/local/bin/mcxi
$ podman run --it --rm --entrypoint /usr/local/bin/mcxi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcxi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcxload

```bash
$ singularity exec <container> /usr/local/bin/mcxload
$ podman run --it --rm --entrypoint /usr/local/bin/mcxload   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcxload   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcxmap

```bash
$ singularity exec <container> /usr/local/bin/mcxmap
$ podman run --it --rm --entrypoint /usr/local/bin/mcxmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcxmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcxrand

```bash
$ singularity exec <container> /usr/local/bin/mcxrand
$ podman run --it --rm --entrypoint /usr/local/bin/mcxrand   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcxrand   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcxsubs

```bash
$ singularity exec <container> /usr/local/bin/mcxsubs
$ podman run --it --rm --entrypoint /usr/local/bin/mcxsubs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcxsubs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stone

```bash
$ singularity exec <container> /usr/local/bin/stone
$ podman run --it --rm --entrypoint /usr/local/bin/stone   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stone   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yte

```bash
$ singularity exec <container> /usr/local/bin/yte
$ podman run --it --rm --entrypoint /usr/local/bin/yte   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yte   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plac_runner.py

```bash
$ singularity exec <container> /usr/local/bin/plac_runner.py
$ podman run --it --rm --entrypoint /usr/local/bin/plac_runner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plac_runner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### docutils

```bash
$ singularity exec <container> /usr/local/bin/docutils
$ podman run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.11

```bash
$ singularity exec <container> /usr/local/bin/f2py3.11
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pulptest

```bash
$ singularity exec <container> /usr/local/bin/pulptest
$ podman run --it --rm --entrypoint /usr/local/bin/pulptest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pulptest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_cpp_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_cpp_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_cpp_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_cpp_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
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
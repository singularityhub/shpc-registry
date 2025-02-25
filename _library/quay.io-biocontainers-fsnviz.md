---
layout: container
name:  "quay.io/biocontainers/fsnviz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fsnviz/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fsnviz/container.yaml"
updated_at: "2025-02-25 03:26:28.368589"
latest: "0.3.0--pyhdfd78af_6"
container_url: "https://biocontainers.pro/tools/fsnviz"
aliases:
 - "crimson"
 - "fsnviz"
 - "circos"
 - "circos.exe"
 - "compile.bat"
 - "compile.make"
 - "gddiag"
 - "list.modules"
 - "test.modules"
 - "bdf2gdfont.pl"
 - "bdftogd"
 - "gd2copypal"
versions:
 - "0.3.0--pyhdfd78af_5"
 - "0.3.0--pyhdfd78af_6"
description: "shpc-registry automated BioContainers addition for fsnviz"
config: {"url": "https://biocontainers.pro/tools/fsnviz", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fsnviz", "latest": {"0.3.0--pyhdfd78af_6": "sha256:b9d2dae790a3756aef203f2ad092a5de53d55ce790fdaca4dfb36d9aad0deb1a"}, "tags": {"0.3.0--pyhdfd78af_5": "sha256:c51d8d331c80929b4d5d87ca1326687e422e703bdae195cffc83a04c058dece4", "0.3.0--pyhdfd78af_6": "sha256:b9d2dae790a3756aef203f2ad092a5de53d55ce790fdaca4dfb36d9aad0deb1a"}, "docker": "quay.io/biocontainers/fsnviz", "aliases": {"crimson": "/usr/local/bin/crimson", "fsnviz": "/usr/local/bin/fsnviz", "circos": "/usr/local/bin/circos", "circos.exe": "/usr/local/bin/circos.exe", "compile.bat": "/usr/local/bin/compile.bat", "compile.make": "/usr/local/bin/compile.make", "gddiag": "/usr/local/bin/gddiag", "list.modules": "/usr/local/bin/list.modules", "test.modules": "/usr/local/bin/test.modules", "bdf2gdfont.pl": "/usr/local/bin/bdf2gdfont.pl", "bdftogd": "/usr/local/bin/bdftogd", "gd2copypal": "/usr/local/bin/gd2copypal"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fsnviz.
shpc-registry automated BioContainers addition for fsnviz
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fsnviz
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fsnviz:0.3.0--pyhdfd78af_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fsnviz/0.3.0--pyhdfd78af_6
$ module help quay.io/biocontainers/fsnviz/0.3.0--pyhdfd78af_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fsnviz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fsnviz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fsnviz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fsnviz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fsnviz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fsnviz-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### crimson

```bash
$ singularity exec <container> /usr/local/bin/crimson
$ podman run --it --rm --entrypoint /usr/local/bin/crimson   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crimson   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fsnviz

```bash
$ singularity exec <container> /usr/local/bin/fsnviz
$ podman run --it --rm --entrypoint /usr/local/bin/fsnviz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fsnviz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### circos

```bash
$ singularity exec <container> /usr/local/bin/circos
$ podman run --it --rm --entrypoint /usr/local/bin/circos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/circos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### circos.exe

```bash
$ singularity exec <container> /usr/local/bin/circos.exe
$ podman run --it --rm --entrypoint /usr/local/bin/circos.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/circos.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compile.bat

```bash
$ singularity exec <container> /usr/local/bin/compile.bat
$ podman run --it --rm --entrypoint /usr/local/bin/compile.bat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compile.bat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compile.make

```bash
$ singularity exec <container> /usr/local/bin/compile.make
$ podman run --it --rm --entrypoint /usr/local/bin/compile.make   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compile.make   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gddiag

```bash
$ singularity exec <container> /usr/local/bin/gddiag
$ podman run --it --rm --entrypoint /usr/local/bin/gddiag   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gddiag   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### list.modules

```bash
$ singularity exec <container> /usr/local/bin/list.modules
$ podman run --it --rm --entrypoint /usr/local/bin/list.modules   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/list.modules   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test.modules

```bash
$ singularity exec <container> /usr/local/bin/test.modules
$ podman run --it --rm --entrypoint /usr/local/bin/test.modules   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test.modules   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bdf2gdfont.pl

```bash
$ singularity exec <container> /usr/local/bin/bdf2gdfont.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bdf2gdfont.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bdf2gdfont.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bdftogd

```bash
$ singularity exec <container> /usr/local/bin/bdftogd
$ podman run --it --rm --entrypoint /usr/local/bin/bdftogd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bdftogd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gd2copypal

```bash
$ singularity exec <container> /usr/local/bin/gd2copypal
$ podman run --it --rm --entrypoint /usr/local/bin/gd2copypal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gd2copypal   -v ${PWD} -w ${PWD} <container> -c " $@"
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
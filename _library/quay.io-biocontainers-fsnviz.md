---
layout: container
name:  "quay.io/biocontainers/fsnviz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fsnviz/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/fsnviz/container.yaml"
updated_at: "2022-10-29 05:51:24.521018"
latest: "0.3.0--pyhdfd78af_5"
container_url: "https://biocontainers.pro/tools/fsnviz"
aliases:
 - "crimson"
 - "fsnviz"
 - "2to3-3.6"
 - "annotate"
 - "bdf2gdfont.pl"
 - "bdftogd"
 - "circos"
 - "circos.exe"
 - "compile.bat"
 - "compile.make"
 - "cwebp"
 - "dwebp"
versions:
 - "0.3.0--pyhdfd78af_5"
description: "shpc-registry automated BioContainers addition for fsnviz"
config: {"url": "https://biocontainers.pro/tools/fsnviz", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fsnviz", "latest": {"0.3.0--pyhdfd78af_5": "sha256:c51d8d331c80929b4d5d87ca1326687e422e703bdae195cffc83a04c058dece4"}, "tags": {"0.3.0--pyhdfd78af_5": "sha256:c51d8d331c80929b4d5d87ca1326687e422e703bdae195cffc83a04c058dece4"}, "docker": "quay.io/biocontainers/fsnviz", "aliases": {"crimson": "/usr/local/bin/crimson", "fsnviz": "/usr/local/bin/fsnviz", "2to3-3.6": "/usr/local/bin/2to3-3.6", "annotate": "/usr/local/bin/annotate", "bdf2gdfont.pl": "/usr/local/bin/bdf2gdfont.pl", "bdftogd": "/usr/local/bin/bdftogd", "circos": "/usr/local/bin/circos", "circos.exe": "/usr/local/bin/circos.exe", "compile.bat": "/usr/local/bin/compile.bat", "compile.make": "/usr/local/bin/compile.make", "cwebp": "/usr/local/bin/cwebp", "dwebp": "/usr/local/bin/dwebp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fsnviz.
shpc-registry automated BioContainers addition for fsnviz
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fsnviz
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fsnviz:0.3.0--pyhdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fsnviz/0.3.0--pyhdfd78af_5
$ module help quay.io/biocontainers/fsnviz/0.3.0--pyhdfd78af_5
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


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotate

```bash
$ singularity exec <container> /usr/local/bin/annotate
$ podman run --it --rm --entrypoint /usr/local/bin/annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### cwebp

```bash
$ singularity exec <container> /usr/local/bin/cwebp
$ podman run --it --rm --entrypoint /usr/local/bin/cwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dwebp

```bash
$ singularity exec <container> /usr/local/bin/dwebp
$ podman run --it --rm --entrypoint /usr/local/bin/dwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
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
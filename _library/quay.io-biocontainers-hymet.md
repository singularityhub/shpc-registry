---
layout: container
name:  "quay.io/biocontainers/hymet"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hymet/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hymet/container.yaml"
updated_at: "2025-12-22 05:21:22.488990"
latest: "1.2.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/hymet"
aliases:
 - "config.pl"
 - "csvclean"
 - "csvcut"
 - "csvformat"
 - "csvgrep"
 - "csvjoin"
 - "csvjson"
 - "csvlook"
 - "csvpy"
 - "csvsort"
 - "csvsql"
 - "csvstack"
 - "csvstat"
 - "hymet"
 - "hymet-config"
 - "in2csv"
 - "main.pl"
 - "sql2csv"
 - "slugify"
 - "runxlrd.py"
 - "pybabel"
 - "capnp"
 - "capnpc"
 - "capnpc-c++"
 - "capnpc-capnp"
 - "mash"
 - "x86_64-conda-linux-gnu.cfg"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "numpy-config"
 - "sdust"
 - "paftools.js"
 - "k8"
 - "minimap2"
 - "futurize"
 - "pasteurize"
 - "idn2"
 - "tqdm"
 - "wget"
versions:
 - "1.0.0--hdfd78af_0"
 - "1.2.1--hdfd78af_0"
description: "singularity registry hpc automated addition for hymet"
config: {"url": "https://biocontainers.pro/tools/hymet", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for hymet", "latest": {"1.2.1--hdfd78af_0": "sha256:792af8b01b740b75f03a85a0f440a58246e4cc3329f5964819c87bc73967a22e"}, "tags": {"1.0.0--hdfd78af_0": "sha256:b8d234f8c558d326cbe6c4efea2335d052f41c6be60a9b20c450d12e9eae5c91", "1.2.1--hdfd78af_0": "sha256:792af8b01b740b75f03a85a0f440a58246e4cc3329f5964819c87bc73967a22e"}, "docker": "quay.io/biocontainers/hymet", "aliases": {"config.pl": "/usr/local/bin/config.pl", "csvclean": "/usr/local/bin/csvclean", "csvcut": "/usr/local/bin/csvcut", "csvformat": "/usr/local/bin/csvformat", "csvgrep": "/usr/local/bin/csvgrep", "csvjoin": "/usr/local/bin/csvjoin", "csvjson": "/usr/local/bin/csvjson", "csvlook": "/usr/local/bin/csvlook", "csvpy": "/usr/local/bin/csvpy", "csvsort": "/usr/local/bin/csvsort", "csvsql": "/usr/local/bin/csvsql", "csvstack": "/usr/local/bin/csvstack", "csvstat": "/usr/local/bin/csvstat", "hymet": "/usr/local/bin/hymet", "hymet-config": "/usr/local/bin/hymet-config", "in2csv": "/usr/local/bin/in2csv", "main.pl": "/usr/local/bin/main.pl", "sql2csv": "/usr/local/bin/sql2csv", "slugify": "/usr/local/bin/slugify", "runxlrd.py": "/usr/local/bin/runxlrd.py", "pybabel": "/usr/local/bin/pybabel", "capnp": "/usr/local/bin/capnp", "capnpc": "/usr/local/bin/capnpc", "capnpc-c++": "/usr/local/bin/capnpc-c++", "capnpc-capnp": "/usr/local/bin/capnpc-capnp", "mash": "/usr/local/bin/mash", "x86_64-conda-linux-gnu.cfg": "/usr/local/bin/x86_64-conda-linux-gnu.cfg", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "numpy-config": "/usr/local/bin/numpy-config", "sdust": "/usr/local/bin/sdust", "paftools.js": "/usr/local/bin/paftools.js", "k8": "/usr/local/bin/k8", "minimap2": "/usr/local/bin/minimap2", "futurize": "/usr/local/bin/futurize", "pasteurize": "/usr/local/bin/pasteurize", "idn2": "/usr/local/bin/idn2", "tqdm": "/usr/local/bin/tqdm", "wget": "/usr/local/bin/wget"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hymet.
singularity registry hpc automated addition for hymet
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hymet
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hymet:1.2.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hymet/1.2.1--hdfd78af_0
$ module help quay.io/biocontainers/hymet/1.2.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hymet-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hymet-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hymet-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hymet-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hymet-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hymet-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### config.pl

```bash
$ singularity exec <container> /usr/local/bin/config.pl
$ podman run --it --rm --entrypoint /usr/local/bin/config.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/config.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csvclean

```bash
$ singularity exec <container> /usr/local/bin/csvclean
$ podman run --it --rm --entrypoint /usr/local/bin/csvclean   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csvclean   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csvcut

```bash
$ singularity exec <container> /usr/local/bin/csvcut
$ podman run --it --rm --entrypoint /usr/local/bin/csvcut   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csvcut   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csvformat

```bash
$ singularity exec <container> /usr/local/bin/csvformat
$ podman run --it --rm --entrypoint /usr/local/bin/csvformat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csvformat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csvgrep

```bash
$ singularity exec <container> /usr/local/bin/csvgrep
$ podman run --it --rm --entrypoint /usr/local/bin/csvgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csvgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csvjoin

```bash
$ singularity exec <container> /usr/local/bin/csvjoin
$ podman run --it --rm --entrypoint /usr/local/bin/csvjoin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csvjoin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csvjson

```bash
$ singularity exec <container> /usr/local/bin/csvjson
$ podman run --it --rm --entrypoint /usr/local/bin/csvjson   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csvjson   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csvlook

```bash
$ singularity exec <container> /usr/local/bin/csvlook
$ podman run --it --rm --entrypoint /usr/local/bin/csvlook   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csvlook   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csvpy

```bash
$ singularity exec <container> /usr/local/bin/csvpy
$ podman run --it --rm --entrypoint /usr/local/bin/csvpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csvpy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csvsort

```bash
$ singularity exec <container> /usr/local/bin/csvsort
$ podman run --it --rm --entrypoint /usr/local/bin/csvsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csvsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csvsql

```bash
$ singularity exec <container> /usr/local/bin/csvsql
$ podman run --it --rm --entrypoint /usr/local/bin/csvsql   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csvsql   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csvstack

```bash
$ singularity exec <container> /usr/local/bin/csvstack
$ podman run --it --rm --entrypoint /usr/local/bin/csvstack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csvstack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csvstat

```bash
$ singularity exec <container> /usr/local/bin/csvstat
$ podman run --it --rm --entrypoint /usr/local/bin/csvstat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csvstat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hymet

```bash
$ singularity exec <container> /usr/local/bin/hymet
$ podman run --it --rm --entrypoint /usr/local/bin/hymet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hymet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hymet-config

```bash
$ singularity exec <container> /usr/local/bin/hymet-config
$ podman run --it --rm --entrypoint /usr/local/bin/hymet-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hymet-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### in2csv

```bash
$ singularity exec <container> /usr/local/bin/in2csv
$ podman run --it --rm --entrypoint /usr/local/bin/in2csv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/in2csv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### main.pl

```bash
$ singularity exec <container> /usr/local/bin/main.pl
$ podman run --it --rm --entrypoint /usr/local/bin/main.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/main.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sql2csv

```bash
$ singularity exec <container> /usr/local/bin/sql2csv
$ podman run --it --rm --entrypoint /usr/local/bin/sql2csv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sql2csv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### slugify

```bash
$ singularity exec <container> /usr/local/bin/slugify
$ podman run --it --rm --entrypoint /usr/local/bin/slugify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slugify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runxlrd.py

```bash
$ singularity exec <container> /usr/local/bin/runxlrd.py
$ podman run --it --rm --entrypoint /usr/local/bin/runxlrd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runxlrd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pybabel

```bash
$ singularity exec <container> /usr/local/bin/pybabel
$ podman run --it --rm --entrypoint /usr/local/bin/pybabel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybabel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### capnp

```bash
$ singularity exec <container> /usr/local/bin/capnp
$ podman run --it --rm --entrypoint /usr/local/bin/capnp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capnp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### capnpc

```bash
$ singularity exec <container> /usr/local/bin/capnpc
$ podman run --it --rm --entrypoint /usr/local/bin/capnpc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capnpc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### capnpc-c++

```bash
$ singularity exec <container> /usr/local/bin/capnpc-c++
$ podman run --it --rm --entrypoint /usr/local/bin/capnpc-c++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capnpc-c++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### capnpc-capnp

```bash
$ singularity exec <container> /usr/local/bin/capnpc-capnp
$ podman run --it --rm --entrypoint /usr/local/bin/capnpc-capnp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capnpc-capnp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mash

```bash
$ singularity exec <container> /usr/local/bin/mash
$ podman run --it --rm --entrypoint /usr/local/bin/mash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu.cfg

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu.cfg
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.13

```bash
$ singularity exec <container> /usr/local/bin/idle3.13
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.13

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.13
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13

```bash
$ singularity exec <container> /usr/local/bin/python3.13
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13-config

```bash
$ singularity exec <container> /usr/local/bin/python3.13-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdust

```bash
$ singularity exec <container> /usr/local/bin/sdust
$ podman run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paftools.js

```bash
$ singularity exec <container> /usr/local/bin/paftools.js
$ podman run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### k8

```bash
$ singularity exec <container> /usr/local/bin/k8
$ podman run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimap2

```bash
$ singularity exec <container> /usr/local/bin/minimap2
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### futurize

```bash
$ singularity exec <container> /usr/local/bin/futurize
$ podman run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pasteurize

```bash
$ singularity exec <container> /usr/local/bin/pasteurize
$ podman run --it --rm --entrypoint /usr/local/bin/pasteurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pasteurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idn2

```bash
$ singularity exec <container> /usr/local/bin/idn2
$ podman run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tqdm

```bash
$ singularity exec <container> /usr/local/bin/tqdm
$ podman run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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
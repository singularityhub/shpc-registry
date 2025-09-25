---
layout: container
name:  "quay.io/biocontainers/pyloh"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pyloh/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pyloh/container.yaml"
updated_at: "2025-09-25 03:11:05.244173"
latest: "1.4.3--py_2"
container_url: "https://biocontainers.pro/tools/pyloh"
aliases:
 - "PyLOH.py"
 - "qhelpconverter"
 - "guess-ploidy.py"
 - "plot-roh.py"
 - "run-roh.pl"
 - "f2py2"
 - "f2py2.7"
 - "color-chrs.pl"
 - "qwebengine_convert_dict"
 - "plot-vcfstats"
 - "canbusutil"
versions:
 - "1.4.3--py_2"
description: "shpc-registry automated BioContainers addition for pyloh"
config: {"url": "https://biocontainers.pro/tools/pyloh", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pyloh", "latest": {"1.4.3--py_2": "sha256:8be59be43f0b94be8b1dc751135d92e8a1ef611ab6e961a646bafe1c3613e5fa"}, "tags": {"1.4.3--py_2": "sha256:8be59be43f0b94be8b1dc751135d92e8a1ef611ab6e961a646bafe1c3613e5fa"}, "docker": "quay.io/biocontainers/pyloh", "aliases": {"PyLOH.py": "/usr/local/bin/PyLOH.py", "qhelpconverter": "/usr/local/bin/qhelpconverter", "guess-ploidy.py": "/usr/local/bin/guess-ploidy.py", "plot-roh.py": "/usr/local/bin/plot-roh.py", "run-roh.pl": "/usr/local/bin/run-roh.pl", "f2py2": "/usr/local/bin/f2py2", "f2py2.7": "/usr/local/bin/f2py2.7", "color-chrs.pl": "/usr/local/bin/color-chrs.pl", "qwebengine_convert_dict": "/usr/local/bin/qwebengine_convert_dict", "plot-vcfstats": "/usr/local/bin/plot-vcfstats", "canbusutil": "/usr/local/bin/canbusutil"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pyloh.
shpc-registry automated BioContainers addition for pyloh
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pyloh
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pyloh:1.4.3--py_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pyloh/1.4.3--py_2
$ module help quay.io/biocontainers/pyloh/1.4.3--py_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pyloh-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pyloh-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pyloh-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pyloh-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pyloh-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pyloh-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### PyLOH.py

```bash
$ singularity exec <container> /usr/local/bin/PyLOH.py
$ podman run --it --rm --entrypoint /usr/local/bin/PyLOH.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PyLOH.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhelpconverter

```bash
$ singularity exec <container> /usr/local/bin/qhelpconverter
$ podman run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### guess-ploidy.py

```bash
$ singularity exec <container> /usr/local/bin/guess-ploidy.py
$ podman run --it --rm --entrypoint /usr/local/bin/guess-ploidy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guess-ploidy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-roh.py

```bash
$ singularity exec <container> /usr/local/bin/plot-roh.py
$ podman run --it --rm --entrypoint /usr/local/bin/plot-roh.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-roh.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-roh.pl

```bash
$ singularity exec <container> /usr/local/bin/run-roh.pl
$ podman run --it --rm --entrypoint /usr/local/bin/run-roh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-roh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2

```bash
$ singularity exec <container> /usr/local/bin/f2py2
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2.7

```bash
$ singularity exec <container> /usr/local/bin/f2py2.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### color-chrs.pl

```bash
$ singularity exec <container> /usr/local/bin/color-chrs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qwebengine_convert_dict

```bash
$ singularity exec <container> /usr/local/bin/qwebengine_convert_dict
$ podman run --it --rm --entrypoint /usr/local/bin/qwebengine_convert_dict   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qwebengine_convert_dict   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-vcfstats

```bash
$ singularity exec <container> /usr/local/bin/plot-vcfstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-vcfstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-vcfstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### canbusutil

```bash
$ singularity exec <container> /usr/local/bin/canbusutil
$ podman run --it --rm --entrypoint /usr/local/bin/canbusutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/canbusutil   -v ${PWD} -w ${PWD} <container> -c " $@"
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
---
layout: container
name:  "quay.io/biocontainers/genomicconsensus"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/genomicconsensus/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/genomicconsensus/container.yaml"
updated_at: "2022-11-07 01:12:52.476753"
latest: "3.0.2--py27h470a237_2"
container_url: "https://biocontainers.pro/tools/genomicconsensus"
aliases:
 - "ccache-swig"
 - "dataset.py"
 - "gffToBed"
 - "gffToVcf"
 - "pbservice"
 - "plurality"
 - "quiver"
 - "summarizeConsensus"
 - "swig"
 - "variantCaller"
 - "unit2"
 - "avro"
 - "cygdb"
 - "cython"
 - "cythonize"
 - "jsonschema"
 - "guess-ploidy.py"
 - "plot-roh.py"
 - "run-roh.pl"
 - "color-chrs.pl"
versions:
 - "3.0.2--py27h470a237_2"
description: "shpc-registry automated BioContainers addition for genomicconsensus"
config: {"url": "https://biocontainers.pro/tools/genomicconsensus", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for genomicconsensus", "latest": {"3.0.2--py27h470a237_2": "sha256:9528dd0b3f664cb438e4cfb8217171a7e932081047b874d8e473267899e66e16"}, "tags": {"3.0.2--py27h470a237_2": "sha256:9528dd0b3f664cb438e4cfb8217171a7e932081047b874d8e473267899e66e16"}, "docker": "quay.io/biocontainers/genomicconsensus", "aliases": {"ccache-swig": "/usr/local/bin/ccache-swig", "dataset.py": "/usr/local/bin/dataset.py", "gffToBed": "/usr/local/bin/gffToBed", "gffToVcf": "/usr/local/bin/gffToVcf", "pbservice": "/usr/local/bin/pbservice", "plurality": "/usr/local/bin/plurality", "quiver": "/usr/local/bin/quiver", "summarizeConsensus": "/usr/local/bin/summarizeConsensus", "swig": "/usr/local/bin/swig", "variantCaller": "/usr/local/bin/variantCaller", "unit2": "/usr/local/bin/unit2", "avro": "/usr/local/bin/avro", "cygdb": "/usr/local/bin/cygdb", "cython": "/usr/local/bin/cython", "cythonize": "/usr/local/bin/cythonize", "jsonschema": "/usr/local/bin/jsonschema", "guess-ploidy.py": "/usr/local/bin/guess-ploidy.py", "plot-roh.py": "/usr/local/bin/plot-roh.py", "run-roh.pl": "/usr/local/bin/run-roh.pl", "color-chrs.pl": "/usr/local/bin/color-chrs.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/genomicconsensus.
shpc-registry automated BioContainers addition for genomicconsensus
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/genomicconsensus
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/genomicconsensus:3.0.2--py27h470a237_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/genomicconsensus/3.0.2--py27h470a237_2
$ module help quay.io/biocontainers/genomicconsensus/3.0.2--py27h470a237_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### genomicconsensus-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### genomicconsensus-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### genomicconsensus-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### genomicconsensus-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### genomicconsensus-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### genomicconsensus-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ccache-swig

```bash
$ singularity exec <container> /usr/local/bin/ccache-swig
$ podman run --it --rm --entrypoint /usr/local/bin/ccache-swig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccache-swig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dataset.py

```bash
$ singularity exec <container> /usr/local/bin/dataset.py
$ podman run --it --rm --entrypoint /usr/local/bin/dataset.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dataset.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gffToBed

```bash
$ singularity exec <container> /usr/local/bin/gffToBed
$ podman run --it --rm --entrypoint /usr/local/bin/gffToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gffToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gffToVcf

```bash
$ singularity exec <container> /usr/local/bin/gffToVcf
$ podman run --it --rm --entrypoint /usr/local/bin/gffToVcf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gffToVcf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbservice

```bash
$ singularity exec <container> /usr/local/bin/pbservice
$ podman run --it --rm --entrypoint /usr/local/bin/pbservice   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbservice   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plurality

```bash
$ singularity exec <container> /usr/local/bin/plurality
$ podman run --it --rm --entrypoint /usr/local/bin/plurality   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plurality   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quiver

```bash
$ singularity exec <container> /usr/local/bin/quiver
$ podman run --it --rm --entrypoint /usr/local/bin/quiver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quiver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### summarizeConsensus

```bash
$ singularity exec <container> /usr/local/bin/summarizeConsensus
$ podman run --it --rm --entrypoint /usr/local/bin/summarizeConsensus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/summarizeConsensus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### swig

```bash
$ singularity exec <container> /usr/local/bin/swig
$ podman run --it --rm --entrypoint /usr/local/bin/swig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/swig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### variantCaller

```bash
$ singularity exec <container> /usr/local/bin/variantCaller
$ podman run --it --rm --entrypoint /usr/local/bin/variantCaller   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/variantCaller   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unit2

```bash
$ singularity exec <container> /usr/local/bin/unit2
$ podman run --it --rm --entrypoint /usr/local/bin/unit2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unit2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### avro

```bash
$ singularity exec <container> /usr/local/bin/avro
$ podman run --it --rm --entrypoint /usr/local/bin/avro   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/avro   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cygdb

```bash
$ singularity exec <container> /usr/local/bin/cygdb
$ podman run --it --rm --entrypoint /usr/local/bin/cygdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cygdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cython

```bash
$ singularity exec <container> /usr/local/bin/cython
$ podman run --it --rm --entrypoint /usr/local/bin/cython   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cython   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cythonize

```bash
$ singularity exec <container> /usr/local/bin/cythonize
$ podman run --it --rm --entrypoint /usr/local/bin/cythonize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cythonize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsonschema

```bash
$ singularity exec <container> /usr/local/bin/jsonschema
$ podman run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### color-chrs.pl

```bash
$ singularity exec <container> /usr/local/bin/color-chrs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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
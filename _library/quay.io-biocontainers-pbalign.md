---
layout: container
name:  "quay.io/biocontainers/pbalign"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pbalign/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pbalign/container.yaml"
updated_at: "2023-05-05 03:13:47.838854"
latest: "0.3.2--py_1"
container_url: "https://biocontainers.pro/tools/pbalign"
aliases:
 - "bam2sam"
 - "blasr"
 - "createChemistryHeader.py"
 - "extractUnmappedSubreads.py"
 - "loadChemistry.py"
 - "maskAlignedReads.py"
 - "pbalign"
 - "pbbamify"
 - "pbindex"
 - "pbindexdump"
 - "pbmerge"
 - "pbservice"
 - "sawriter"
 - "unit2"
 - "avro"
 - "cygdb"
 - "cython"
 - "cythonize"
 - "f2py2"
 - "f2py2.7"
 - "chardetect"
 - "python2-config"
 - "python2.7-config"
versions:
 - "0.3.2--py_1"
description: "shpc-registry automated BioContainers addition for pbalign"
config: {"url": "https://biocontainers.pro/tools/pbalign", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pbalign", "latest": {"0.3.2--py_1": "sha256:6e8d293a71ce8cb39567f167cd979191f8c456df6b723355fc55ccd8d9016f6e"}, "tags": {"0.3.2--py_1": "sha256:6e8d293a71ce8cb39567f167cd979191f8c456df6b723355fc55ccd8d9016f6e"}, "docker": "quay.io/biocontainers/pbalign", "aliases": {"bam2sam": "/usr/local/bin/bam2sam", "blasr": "/usr/local/bin/blasr", "createChemistryHeader.py": "/usr/local/bin/createChemistryHeader.py", "extractUnmappedSubreads.py": "/usr/local/bin/extractUnmappedSubreads.py", "loadChemistry.py": "/usr/local/bin/loadChemistry.py", "maskAlignedReads.py": "/usr/local/bin/maskAlignedReads.py", "pbalign": "/usr/local/bin/pbalign", "pbbamify": "/usr/local/bin/pbbamify", "pbindex": "/usr/local/bin/pbindex", "pbindexdump": "/usr/local/bin/pbindexdump", "pbmerge": "/usr/local/bin/pbmerge", "pbservice": "/usr/local/bin/pbservice", "sawriter": "/usr/local/bin/sawriter", "unit2": "/usr/local/bin/unit2", "avro": "/usr/local/bin/avro", "cygdb": "/usr/local/bin/cygdb", "cython": "/usr/local/bin/cython", "cythonize": "/usr/local/bin/cythonize", "f2py2": "/usr/local/bin/f2py2", "f2py2.7": "/usr/local/bin/f2py2.7", "chardetect": "/usr/local/bin/chardetect", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pbalign.
shpc-registry automated BioContainers addition for pbalign
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pbalign
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pbalign:0.3.2--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pbalign/0.3.2--py_1
$ module help quay.io/biocontainers/pbalign/0.3.2--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pbalign-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pbalign-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pbalign-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pbalign-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pbalign-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pbalign-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bam2sam

```bash
$ singularity exec <container> /usr/local/bin/bam2sam
$ podman run --it --rm --entrypoint /usr/local/bin/bam2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blasr

```bash
$ singularity exec <container> /usr/local/bin/blasr
$ podman run --it --rm --entrypoint /usr/local/bin/blasr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blasr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### createChemistryHeader.py

```bash
$ singularity exec <container> /usr/local/bin/createChemistryHeader.py
$ podman run --it --rm --entrypoint /usr/local/bin/createChemistryHeader.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/createChemistryHeader.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extractUnmappedSubreads.py

```bash
$ singularity exec <container> /usr/local/bin/extractUnmappedSubreads.py
$ podman run --it --rm --entrypoint /usr/local/bin/extractUnmappedSubreads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extractUnmappedSubreads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### loadChemistry.py

```bash
$ singularity exec <container> /usr/local/bin/loadChemistry.py
$ podman run --it --rm --entrypoint /usr/local/bin/loadChemistry.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/loadChemistry.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maskAlignedReads.py

```bash
$ singularity exec <container> /usr/local/bin/maskAlignedReads.py
$ podman run --it --rm --entrypoint /usr/local/bin/maskAlignedReads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maskAlignedReads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbalign

```bash
$ singularity exec <container> /usr/local/bin/pbalign
$ podman run --it --rm --entrypoint /usr/local/bin/pbalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbbamify

```bash
$ singularity exec <container> /usr/local/bin/pbbamify
$ podman run --it --rm --entrypoint /usr/local/bin/pbbamify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbbamify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbindex

```bash
$ singularity exec <container> /usr/local/bin/pbindex
$ podman run --it --rm --entrypoint /usr/local/bin/pbindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbindexdump

```bash
$ singularity exec <container> /usr/local/bin/pbindexdump
$ podman run --it --rm --entrypoint /usr/local/bin/pbindexdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbindexdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbmerge

```bash
$ singularity exec <container> /usr/local/bin/pbmerge
$ podman run --it --rm --entrypoint /usr/local/bin/pbmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbservice

```bash
$ singularity exec <container> /usr/local/bin/pbservice
$ podman run --it --rm --entrypoint /usr/local/bin/pbservice   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbservice   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sawriter

```bash
$ singularity exec <container> /usr/local/bin/sawriter
$ podman run --it --rm --entrypoint /usr/local/bin/sawriter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sawriter   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2-config

```bash
$ singularity exec <container> /usr/local/bin/python2-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7-config

```bash
$ singularity exec <container> /usr/local/bin/python2.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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
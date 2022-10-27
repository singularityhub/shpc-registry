---
layout: container
name:  "quay.io/biocontainers/pbalign"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pbalign/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/pbalign/container.yaml"
updated_at: "2022-10-27 01:11:58.818157"
latest: "0.3.2--py_1"
container_url: "https://biocontainers.pro/tools/pbalign"
aliases:
 - ".blasr-post-link.sh"
 - ".blasr_libcpp-post-link.sh"
 - ".open"
 - ".pbalign-post-link.sh"
 - ".pbbam-post-link.sh"
 - ".pbcommand-post-link.sh"
 - ".pbcopper-post-link.sh"
 - ".pbcore-post-link.sh"
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
versions:
 - "0.3.2--py_1"
description: "shpc-registry automated BioContainers addition for pbalign"
config: {"url": "https://biocontainers.pro/tools/pbalign", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pbalign", "latest": {"0.3.2--py_1": "sha256:6e8d293a71ce8cb39567f167cd979191f8c456df6b723355fc55ccd8d9016f6e"}, "tags": {"0.3.2--py_1": "sha256:6e8d293a71ce8cb39567f167cd979191f8c456df6b723355fc55ccd8d9016f6e"}, "docker": "quay.io/biocontainers/pbalign", "aliases": {".blasr-post-link.sh": "/usr/local/bin/.blasr-post-link.sh", ".blasr_libcpp-post-link.sh": "/usr/local/bin/.blasr_libcpp-post-link.sh", ".open": "/usr/local/bin/.open", ".pbalign-post-link.sh": "/usr/local/bin/.pbalign-post-link.sh", ".pbbam-post-link.sh": "/usr/local/bin/.pbbam-post-link.sh", ".pbcommand-post-link.sh": "/usr/local/bin/.pbcommand-post-link.sh", ".pbcopper-post-link.sh": "/usr/local/bin/.pbcopper-post-link.sh", ".pbcore-post-link.sh": "/usr/local/bin/.pbcore-post-link.sh", "bam2sam": "/usr/local/bin/bam2sam", "blasr": "/usr/local/bin/blasr", "createChemistryHeader.py": "/usr/local/bin/createChemistryHeader.py", "extractUnmappedSubreads.py": "/usr/local/bin/extractUnmappedSubreads.py", "loadChemistry.py": "/usr/local/bin/loadChemistry.py", "maskAlignedReads.py": "/usr/local/bin/maskAlignedReads.py", "pbalign": "/usr/local/bin/pbalign", "pbbamify": "/usr/local/bin/pbbamify", "pbindex": "/usr/local/bin/pbindex", "pbindexdump": "/usr/local/bin/pbindexdump", "pbmerge": "/usr/local/bin/pbmerge", "pbservice": "/usr/local/bin/pbservice", "sawriter": "/usr/local/bin/sawriter"}}
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


#### .blasr-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.blasr-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.blasr-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.blasr-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .blasr_libcpp-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.blasr_libcpp-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.blasr_libcpp-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.blasr_libcpp-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .open

```bash
$ singularity exec <container> /usr/local/bin/.open
$ podman run --it --rm --entrypoint /usr/local/bin/.open   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.open   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .pbalign-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.pbalign-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.pbalign-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.pbalign-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .pbbam-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.pbbam-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.pbbam-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.pbbam-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .pbcommand-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.pbcommand-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.pbcommand-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.pbcommand-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .pbcopper-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.pbcopper-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.pbcopper-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.pbcopper-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .pbcore-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.pbcore-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.pbcore-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.pbcore-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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
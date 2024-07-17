---
layout: container
name:  "quay.io/biocontainers/dunovo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dunovo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dunovo/container.yaml"
updated_at: "2024-07-17 02:58:44.584486"
latest: "3.0.2--h031d066_3"
container_url: "https://biocontainers.pro/tools/dunovo"
aliases:
 - "align-families.py"
 - "baralign.sh"
 - "bash"
 - "bashbug"
 - "consensus.py"
 - "correct.py"
 - "dunovo.py"
 - "dunovo_parsers.py"
 - "file"
 - "gunzip"
 - "gzexe"
 - "gzip"
 - "loeb-2.0.sh"
 - "make-barcodes.awk"
 - "make-consensi.py"
 - "make-families.sh"
 - "parallel_tools.py"
 - "precheck.py"
 - "safety-not-guaranteed.py"
 - "seqtools.py"
 - "shims.py"
 - "trimmer.py"
 - "uncompress"
 - "zcat"
 - "zcmp"
 - "zdiff"
 - "zegrep"
 - "zfgrep"
 - "zforce"
 - "zgrep"
 - "zless"
 - "zmore"
 - "znew"
 - "bowtie-align-l"
 - "bowtie-align-s"
 - "bowtie-build-l"
 - "bowtie-build-s"
 - "bowtie-inspect-l"
 - "bowtie-inspect-s"
 - "bowtie"
 - "bowtie-build"
 - "bowtie-inspect"
 - "gawk-5.1.0"
versions:
 - "3.0.2--hec16e2b_1"
 - "3.0.2--h031d066_3"
description: "shpc-registry automated BioContainers addition for dunovo"
config: {"url": "https://biocontainers.pro/tools/dunovo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dunovo", "latest": {"3.0.2--h031d066_3": "sha256:4ec1671bcc7dc76d5ce839c2e7293952c901eae3d08ed0b8f6c6d19b8b47e6c3"}, "tags": {"3.0.2--hec16e2b_1": "sha256:70f36252d65e0aa1d8b625e5a2a08ee8637afc4a1cae9c8ee8ed6b14aad2a07d", "3.0.2--h031d066_3": "sha256:4ec1671bcc7dc76d5ce839c2e7293952c901eae3d08ed0b8f6c6d19b8b47e6c3"}, "docker": "quay.io/biocontainers/dunovo", "aliases": {"align-families.py": "/usr/local/bin/align-families.py", "baralign.sh": "/usr/local/bin/baralign.sh", "bash": "/usr/local/bin/bash", "bashbug": "/usr/local/bin/bashbug", "consensus.py": "/usr/local/bin/consensus.py", "correct.py": "/usr/local/bin/correct.py", "dunovo.py": "/usr/local/bin/dunovo.py", "dunovo_parsers.py": "/usr/local/bin/dunovo_parsers.py", "file": "/usr/local/bin/file", "gunzip": "/usr/local/bin/gunzip", "gzexe": "/usr/local/bin/gzexe", "gzip": "/usr/local/bin/gzip", "loeb-2.0.sh": "/usr/local/bin/loeb-2.0.sh", "make-barcodes.awk": "/usr/local/bin/make-barcodes.awk", "make-consensi.py": "/usr/local/bin/make-consensi.py", "make-families.sh": "/usr/local/bin/make-families.sh", "parallel_tools.py": "/usr/local/bin/parallel_tools.py", "precheck.py": "/usr/local/bin/precheck.py", "safety-not-guaranteed.py": "/usr/local/bin/safety-not-guaranteed.py", "seqtools.py": "/usr/local/bin/seqtools.py", "shims.py": "/usr/local/bin/shims.py", "trimmer.py": "/usr/local/bin/trimmer.py", "uncompress": "/usr/local/bin/uncompress", "zcat": "/usr/local/bin/zcat", "zcmp": "/usr/local/bin/zcmp", "zdiff": "/usr/local/bin/zdiff", "zegrep": "/usr/local/bin/zegrep", "zfgrep": "/usr/local/bin/zfgrep", "zforce": "/usr/local/bin/zforce", "zgrep": "/usr/local/bin/zgrep", "zless": "/usr/local/bin/zless", "zmore": "/usr/local/bin/zmore", "znew": "/usr/local/bin/znew", "bowtie-align-l": "/usr/local/bin/bowtie-align-l", "bowtie-align-s": "/usr/local/bin/bowtie-align-s", "bowtie-build-l": "/usr/local/bin/bowtie-build-l", "bowtie-build-s": "/usr/local/bin/bowtie-build-s", "bowtie-inspect-l": "/usr/local/bin/bowtie-inspect-l", "bowtie-inspect-s": "/usr/local/bin/bowtie-inspect-s", "bowtie": "/usr/local/bin/bowtie", "bowtie-build": "/usr/local/bin/bowtie-build", "bowtie-inspect": "/usr/local/bin/bowtie-inspect", "gawk-5.1.0": "/usr/local/bin/gawk-5.1.0"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dunovo.
shpc-registry automated BioContainers addition for dunovo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dunovo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dunovo:3.0.2--h031d066_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dunovo/3.0.2--h031d066_3
$ module help quay.io/biocontainers/dunovo/3.0.2--h031d066_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dunovo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dunovo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dunovo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dunovo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dunovo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dunovo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### align-families.py

```bash
$ singularity exec <container> /usr/local/bin/align-families.py
$ podman run --it --rm --entrypoint /usr/local/bin/align-families.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/align-families.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### baralign.sh

```bash
$ singularity exec <container> /usr/local/bin/baralign.sh
$ podman run --it --rm --entrypoint /usr/local/bin/baralign.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/baralign.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bash

```bash
$ singularity exec <container> /usr/local/bin/bash
$ podman run --it --rm --entrypoint /usr/local/bin/bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bashbug

```bash
$ singularity exec <container> /usr/local/bin/bashbug
$ podman run --it --rm --entrypoint /usr/local/bin/bashbug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bashbug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### consensus.py

```bash
$ singularity exec <container> /usr/local/bin/consensus.py
$ podman run --it --rm --entrypoint /usr/local/bin/consensus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/consensus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### correct.py

```bash
$ singularity exec <container> /usr/local/bin/correct.py
$ podman run --it --rm --entrypoint /usr/local/bin/correct.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/correct.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dunovo.py

```bash
$ singularity exec <container> /usr/local/bin/dunovo.py
$ podman run --it --rm --entrypoint /usr/local/bin/dunovo.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dunovo.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dunovo_parsers.py

```bash
$ singularity exec <container> /usr/local/bin/dunovo_parsers.py
$ podman run --it --rm --entrypoint /usr/local/bin/dunovo_parsers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dunovo_parsers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### file

```bash
$ singularity exec <container> /usr/local/bin/file
$ podman run --it --rm --entrypoint /usr/local/bin/file   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/file   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gunzip

```bash
$ singularity exec <container> /usr/local/bin/gunzip
$ podman run --it --rm --entrypoint /usr/local/bin/gunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gzexe

```bash
$ singularity exec <container> /usr/local/bin/gzexe
$ podman run --it --rm --entrypoint /usr/local/bin/gzexe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gzexe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gzip

```bash
$ singularity exec <container> /usr/local/bin/gzip
$ podman run --it --rm --entrypoint /usr/local/bin/gzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### loeb-2.0.sh

```bash
$ singularity exec <container> /usr/local/bin/loeb-2.0.sh
$ podman run --it --rm --entrypoint /usr/local/bin/loeb-2.0.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/loeb-2.0.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make-barcodes.awk

```bash
$ singularity exec <container> /usr/local/bin/make-barcodes.awk
$ podman run --it --rm --entrypoint /usr/local/bin/make-barcodes.awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make-barcodes.awk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make-consensi.py

```bash
$ singularity exec <container> /usr/local/bin/make-consensi.py
$ podman run --it --rm --entrypoint /usr/local/bin/make-consensi.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make-consensi.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make-families.sh

```bash
$ singularity exec <container> /usr/local/bin/make-families.sh
$ podman run --it --rm --entrypoint /usr/local/bin/make-families.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make-families.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parallel_tools.py

```bash
$ singularity exec <container> /usr/local/bin/parallel_tools.py
$ podman run --it --rm --entrypoint /usr/local/bin/parallel_tools.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parallel_tools.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### precheck.py

```bash
$ singularity exec <container> /usr/local/bin/precheck.py
$ podman run --it --rm --entrypoint /usr/local/bin/precheck.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/precheck.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### safety-not-guaranteed.py

```bash
$ singularity exec <container> /usr/local/bin/safety-not-guaranteed.py
$ podman run --it --rm --entrypoint /usr/local/bin/safety-not-guaranteed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/safety-not-guaranteed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqtools.py

```bash
$ singularity exec <container> /usr/local/bin/seqtools.py
$ podman run --it --rm --entrypoint /usr/local/bin/seqtools.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqtools.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shims.py

```bash
$ singularity exec <container> /usr/local/bin/shims.py
$ podman run --it --rm --entrypoint /usr/local/bin/shims.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shims.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trimmer.py

```bash
$ singularity exec <container> /usr/local/bin/trimmer.py
$ podman run --it --rm --entrypoint /usr/local/bin/trimmer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trimmer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uncompress

```bash
$ singularity exec <container> /usr/local/bin/uncompress
$ podman run --it --rm --entrypoint /usr/local/bin/uncompress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uncompress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zcat

```bash
$ singularity exec <container> /usr/local/bin/zcat
$ podman run --it --rm --entrypoint /usr/local/bin/zcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zcmp

```bash
$ singularity exec <container> /usr/local/bin/zcmp
$ podman run --it --rm --entrypoint /usr/local/bin/zcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zdiff

```bash
$ singularity exec <container> /usr/local/bin/zdiff
$ podman run --it --rm --entrypoint /usr/local/bin/zdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zegrep

```bash
$ singularity exec <container> /usr/local/bin/zegrep
$ podman run --it --rm --entrypoint /usr/local/bin/zegrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zegrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zfgrep

```bash
$ singularity exec <container> /usr/local/bin/zfgrep
$ podman run --it --rm --entrypoint /usr/local/bin/zfgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zfgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zforce

```bash
$ singularity exec <container> /usr/local/bin/zforce
$ podman run --it --rm --entrypoint /usr/local/bin/zforce   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zforce   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zgrep

```bash
$ singularity exec <container> /usr/local/bin/zgrep
$ podman run --it --rm --entrypoint /usr/local/bin/zgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zless

```bash
$ singularity exec <container> /usr/local/bin/zless
$ podman run --it --rm --entrypoint /usr/local/bin/zless   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zless   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zmore

```bash
$ singularity exec <container> /usr/local/bin/zmore
$ podman run --it --rm --entrypoint /usr/local/bin/zmore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zmore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### znew

```bash
$ singularity exec <container> /usr/local/bin/znew
$ podman run --it --rm --entrypoint /usr/local/bin/znew   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/znew   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-align-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie-align-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-align-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie-align-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-build-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie-build-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-build-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie-build-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-inspect-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie-inspect-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-inspect-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie-inspect-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie

```bash
$ singularity exec <container> /usr/local/bin/bowtie
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-build

```bash
$ singularity exec <container> /usr/local/bin/bowtie-build
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-inspect

```bash
$ singularity exec <container> /usr/local/bin/bowtie-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.1.0

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
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
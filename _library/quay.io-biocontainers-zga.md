---
layout: container
name:  "quay.io/biocontainers/zga"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/zga/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/zga/container.yaml"
updated_at: "2024-04-24 02:45:39.492678"
latest: "0.1.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/zga"
aliases:
 - "checkm"
 - "dfast"
 - "dfast_file_downloader.py"
 - "file_downloader.py"
 - "flye"
 - "flye-minimap2"
 - "flye-modules"
 - "flye-samtools"
 - "ghostx"
 - "mga"
 - "miniasm"
 - "minidot"
 - "nxtrim"
 - "sam_add_rg.pl"
 - "unicycler"
 - "unicycler_align"
 - "unicycler_check"
 - "unicycler_polish"
 - "unicycler_scrub"
 - "update_version.sh"
 - "zga"
 - "filter-table"
 - "kmutate.sh"
 - "runhmm.sh"
 - "spdi2prod"
 - "fastp"
 - "pilon"
 - "kmerposition.sh"
 - "reformatpb.sh"
 - "rppr"
 - "summarizecoverage.sh"
versions:
 - "0.0.9.post2--pyhdfd78af_1"
 - "0.1.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for zga"
config: {"url": "https://biocontainers.pro/tools/zga", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for zga", "latest": {"0.1.0--pyhdfd78af_0": "sha256:bdc08cdad66770b01d00b9b14256167b883f142e9030831919085ecfde5a9614"}, "tags": {"0.0.9.post2--pyhdfd78af_1": "sha256:9934c00a59ba9ceb8ede393026a1255450d9a7a2a8ee7fe5891dd613654b00df", "0.1.0--pyhdfd78af_0": "sha256:bdc08cdad66770b01d00b9b14256167b883f142e9030831919085ecfde5a9614"}, "docker": "quay.io/biocontainers/zga", "aliases": {"checkm": "/usr/local/bin/checkm", "dfast": "/usr/local/bin/dfast", "dfast_file_downloader.py": "/usr/local/bin/dfast_file_downloader.py", "file_downloader.py": "/usr/local/bin/file_downloader.py", "flye": "/usr/local/bin/flye", "flye-minimap2": "/usr/local/bin/flye-minimap2", "flye-modules": "/usr/local/bin/flye-modules", "flye-samtools": "/usr/local/bin/flye-samtools", "ghostx": "/usr/local/bin/ghostx", "mga": "/usr/local/bin/mga", "miniasm": "/usr/local/bin/miniasm", "minidot": "/usr/local/bin/minidot", "nxtrim": "/usr/local/bin/nxtrim", "sam_add_rg.pl": "/usr/local/bin/sam_add_rg.pl", "unicycler": "/usr/local/bin/unicycler", "unicycler_align": "/usr/local/bin/unicycler_align", "unicycler_check": "/usr/local/bin/unicycler_check", "unicycler_polish": "/usr/local/bin/unicycler_polish", "unicycler_scrub": "/usr/local/bin/unicycler_scrub", "update_version.sh": "/usr/local/bin/update_version.sh", "zga": "/usr/local/bin/zga", "filter-table": "/usr/local/bin/filter-table", "kmutate.sh": "/usr/local/bin/kmutate.sh", "runhmm.sh": "/usr/local/bin/runhmm.sh", "spdi2prod": "/usr/local/bin/spdi2prod", "fastp": "/usr/local/bin/fastp", "pilon": "/usr/local/bin/pilon", "kmerposition.sh": "/usr/local/bin/kmerposition.sh", "reformatpb.sh": "/usr/local/bin/reformatpb.sh", "rppr": "/usr/local/bin/rppr", "summarizecoverage.sh": "/usr/local/bin/summarizecoverage.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/zga.
shpc-registry automated BioContainers addition for zga
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/zga
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/zga:0.1.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/zga/0.1.0--pyhdfd78af_0
$ module help quay.io/biocontainers/zga/0.1.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### zga-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### zga-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### zga-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### zga-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### zga-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### zga-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### checkm

```bash
$ singularity exec <container> /usr/local/bin/checkm
$ podman run --it --rm --entrypoint /usr/local/bin/checkm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checkm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dfast

```bash
$ singularity exec <container> /usr/local/bin/dfast
$ podman run --it --rm --entrypoint /usr/local/bin/dfast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dfast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dfast_file_downloader.py

```bash
$ singularity exec <container> /usr/local/bin/dfast_file_downloader.py
$ podman run --it --rm --entrypoint /usr/local/bin/dfast_file_downloader.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dfast_file_downloader.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### file_downloader.py

```bash
$ singularity exec <container> /usr/local/bin/file_downloader.py
$ podman run --it --rm --entrypoint /usr/local/bin/file_downloader.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/file_downloader.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flye

```bash
$ singularity exec <container> /usr/local/bin/flye
$ podman run --it --rm --entrypoint /usr/local/bin/flye   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flye   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flye-minimap2

```bash
$ singularity exec <container> /usr/local/bin/flye-minimap2
$ podman run --it --rm --entrypoint /usr/local/bin/flye-minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flye-minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flye-modules

```bash
$ singularity exec <container> /usr/local/bin/flye-modules
$ podman run --it --rm --entrypoint /usr/local/bin/flye-modules   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flye-modules   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flye-samtools

```bash
$ singularity exec <container> /usr/local/bin/flye-samtools
$ podman run --it --rm --entrypoint /usr/local/bin/flye-samtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flye-samtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ghostx

```bash
$ singularity exec <container> /usr/local/bin/ghostx
$ podman run --it --rm --entrypoint /usr/local/bin/ghostx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ghostx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mga

```bash
$ singularity exec <container> /usr/local/bin/mga
$ podman run --it --rm --entrypoint /usr/local/bin/mga   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mga   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### miniasm

```bash
$ singularity exec <container> /usr/local/bin/miniasm
$ podman run --it --rm --entrypoint /usr/local/bin/miniasm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/miniasm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minidot

```bash
$ singularity exec <container> /usr/local/bin/minidot
$ podman run --it --rm --entrypoint /usr/local/bin/minidot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minidot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nxtrim

```bash
$ singularity exec <container> /usr/local/bin/nxtrim
$ podman run --it --rm --entrypoint /usr/local/bin/nxtrim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nxtrim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sam_add_rg.pl

```bash
$ singularity exec <container> /usr/local/bin/sam_add_rg.pl
$ podman run --it --rm --entrypoint /usr/local/bin/sam_add_rg.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sam_add_rg.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unicycler

```bash
$ singularity exec <container> /usr/local/bin/unicycler
$ podman run --it --rm --entrypoint /usr/local/bin/unicycler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unicycler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unicycler_align

```bash
$ singularity exec <container> /usr/local/bin/unicycler_align
$ podman run --it --rm --entrypoint /usr/local/bin/unicycler_align   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unicycler_align   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unicycler_check

```bash
$ singularity exec <container> /usr/local/bin/unicycler_check
$ podman run --it --rm --entrypoint /usr/local/bin/unicycler_check   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unicycler_check   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unicycler_polish

```bash
$ singularity exec <container> /usr/local/bin/unicycler_polish
$ podman run --it --rm --entrypoint /usr/local/bin/unicycler_polish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unicycler_polish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unicycler_scrub

```bash
$ singularity exec <container> /usr/local/bin/unicycler_scrub
$ podman run --it --rm --entrypoint /usr/local/bin/unicycler_scrub   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unicycler_scrub   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### update_version.sh

```bash
$ singularity exec <container> /usr/local/bin/update_version.sh
$ podman run --it --rm --entrypoint /usr/local/bin/update_version.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/update_version.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zga

```bash
$ singularity exec <container> /usr/local/bin/zga
$ podman run --it --rm --entrypoint /usr/local/bin/zga   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zga   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-table

```bash
$ singularity exec <container> /usr/local/bin/filter-table
$ podman run --it --rm --entrypoint /usr/local/bin/filter-table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmutate.sh

```bash
$ singularity exec <container> /usr/local/bin/kmutate.sh
$ podman run --it --rm --entrypoint /usr/local/bin/kmutate.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmutate.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runhmm.sh

```bash
$ singularity exec <container> /usr/local/bin/runhmm.sh
$ podman run --it --rm --entrypoint /usr/local/bin/runhmm.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runhmm.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spdi2prod

```bash
$ singularity exec <container> /usr/local/bin/spdi2prod
$ podman run --it --rm --entrypoint /usr/local/bin/spdi2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spdi2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastp

```bash
$ singularity exec <container> /usr/local/bin/fastp
$ podman run --it --rm --entrypoint /usr/local/bin/fastp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pilon

```bash
$ singularity exec <container> /usr/local/bin/pilon
$ podman run --it --rm --entrypoint /usr/local/bin/pilon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pilon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmerposition.sh

```bash
$ singularity exec <container> /usr/local/bin/kmerposition.sh
$ podman run --it --rm --entrypoint /usr/local/bin/kmerposition.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmerposition.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reformatpb.sh

```bash
$ singularity exec <container> /usr/local/bin/reformatpb.sh
$ podman run --it --rm --entrypoint /usr/local/bin/reformatpb.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reformatpb.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rppr

```bash
$ singularity exec <container> /usr/local/bin/rppr
$ podman run --it --rm --entrypoint /usr/local/bin/rppr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rppr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### summarizecoverage.sh

```bash
$ singularity exec <container> /usr/local/bin/summarizecoverage.sh
$ podman run --it --rm --entrypoint /usr/local/bin/summarizecoverage.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/summarizecoverage.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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
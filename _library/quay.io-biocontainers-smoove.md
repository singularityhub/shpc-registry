---
layout: container
name:  "quay.io/biocontainers/smoove"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/smoove/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/smoove/container.yaml"
updated_at: "2024-05-07 02:55:26.873360"
latest: "0.2.8--h9ee0642_1"
container_url: "https://biocontainers.pro/tools/smoove"
aliases:
 - "cnvanator_to_bedpes.py"
 - "create_coordinates"
 - "duphold"
 - "extractSplitReads_BwaMem"
 - "gsort"
 - "ldc-build-runtime"
 - "ldc-profdata"
 - "ldc-prune-cache"
 - "ldc2"
 - "ldmd2"
 - "lib_stats.R"
 - "lumpy"
 - "lumpy_filter"
 - "lumpyexpress"
 - "mosdepth"
 - "samblaster"
 - "scriptlive"
 - "smoove"
 - "sv_classifier.py"
 - "svtools"
 - "svtyper"
 - "svtyper-sso"
 - "update_info.py"
 - "vcf_allele_freq.py"
 - "vcf_group_multiline.py"
 - "vcf_modify_header.py"
 - "vcf_paste.py"
 - "cal"
 - "chmem"
 - "choom"
 - "chrt"
 - "col"
 - "colcrt"
 - "colrm"
 - "column"
 - "dmesg"
 - "eject"
versions:
 - "0.2.8--h9ee0642_1"
description: "shpc-registry automated BioContainers addition for smoove"
config: {"url": "https://biocontainers.pro/tools/smoove", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for smoove", "latest": {"0.2.8--h9ee0642_1": "sha256:846950fdbc767f476fc563d9488a228933552fc5534011eb1f9c0987722165c8"}, "tags": {"0.2.8--h9ee0642_1": "sha256:846950fdbc767f476fc563d9488a228933552fc5534011eb1f9c0987722165c8"}, "docker": "quay.io/biocontainers/smoove", "aliases": {"cnvanator_to_bedpes.py": "/usr/local/bin/cnvanator_to_bedpes.py", "create_coordinates": "/usr/local/bin/create_coordinates", "duphold": "/usr/local/bin/duphold", "extractSplitReads_BwaMem": "/usr/local/bin/extractSplitReads_BwaMem", "gsort": "/usr/local/bin/gsort", "ldc-build-runtime": "/usr/local/bin/ldc-build-runtime", "ldc-profdata": "/usr/local/bin/ldc-profdata", "ldc-prune-cache": "/usr/local/bin/ldc-prune-cache", "ldc2": "/usr/local/bin/ldc2", "ldmd2": "/usr/local/bin/ldmd2", "lib_stats.R": "/usr/local/bin/lib_stats.R", "lumpy": "/usr/local/bin/lumpy", "lumpy_filter": "/usr/local/bin/lumpy_filter", "lumpyexpress": "/usr/local/bin/lumpyexpress", "mosdepth": "/usr/local/bin/mosdepth", "samblaster": "/usr/local/bin/samblaster", "scriptlive": "/usr/local/bin/scriptlive", "smoove": "/usr/local/bin/smoove", "sv_classifier.py": "/usr/local/bin/sv_classifier.py", "svtools": "/usr/local/bin/svtools", "svtyper": "/usr/local/bin/svtyper", "svtyper-sso": "/usr/local/bin/svtyper-sso", "update_info.py": "/usr/local/bin/update_info.py", "vcf_allele_freq.py": "/usr/local/bin/vcf_allele_freq.py", "vcf_group_multiline.py": "/usr/local/bin/vcf_group_multiline.py", "vcf_modify_header.py": "/usr/local/bin/vcf_modify_header.py", "vcf_paste.py": "/usr/local/bin/vcf_paste.py", "cal": "/usr/local/bin/cal", "chmem": "/usr/local/bin/chmem", "choom": "/usr/local/bin/choom", "chrt": "/usr/local/bin/chrt", "col": "/usr/local/bin/col", "colcrt": "/usr/local/bin/colcrt", "colrm": "/usr/local/bin/colrm", "column": "/usr/local/bin/column", "dmesg": "/usr/local/bin/dmesg", "eject": "/usr/local/bin/eject"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/smoove.
shpc-registry automated BioContainers addition for smoove
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/smoove
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/smoove:0.2.8--h9ee0642_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/smoove/0.2.8--h9ee0642_1
$ module help quay.io/biocontainers/smoove/0.2.8--h9ee0642_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### smoove-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### smoove-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### smoove-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### smoove-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### smoove-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### smoove-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cnvanator_to_bedpes.py

```bash
$ singularity exec <container> /usr/local/bin/cnvanator_to_bedpes.py
$ podman run --it --rm --entrypoint /usr/local/bin/cnvanator_to_bedpes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cnvanator_to_bedpes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create_coordinates

```bash
$ singularity exec <container> /usr/local/bin/create_coordinates
$ podman run --it --rm --entrypoint /usr/local/bin/create_coordinates   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create_coordinates   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### duphold

```bash
$ singularity exec <container> /usr/local/bin/duphold
$ podman run --it --rm --entrypoint /usr/local/bin/duphold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/duphold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extractSplitReads_BwaMem

```bash
$ singularity exec <container> /usr/local/bin/extractSplitReads_BwaMem
$ podman run --it --rm --entrypoint /usr/local/bin/extractSplitReads_BwaMem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extractSplitReads_BwaMem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsort

```bash
$ singularity exec <container> /usr/local/bin/gsort
$ podman run --it --rm --entrypoint /usr/local/bin/gsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldc-build-runtime

```bash
$ singularity exec <container> /usr/local/bin/ldc-build-runtime
$ podman run --it --rm --entrypoint /usr/local/bin/ldc-build-runtime   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldc-build-runtime   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldc-profdata

```bash
$ singularity exec <container> /usr/local/bin/ldc-profdata
$ podman run --it --rm --entrypoint /usr/local/bin/ldc-profdata   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldc-profdata   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldc-prune-cache

```bash
$ singularity exec <container> /usr/local/bin/ldc-prune-cache
$ podman run --it --rm --entrypoint /usr/local/bin/ldc-prune-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldc-prune-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldc2

```bash
$ singularity exec <container> /usr/local/bin/ldc2
$ podman run --it --rm --entrypoint /usr/local/bin/ldc2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldc2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldmd2

```bash
$ singularity exec <container> /usr/local/bin/ldmd2
$ podman run --it --rm --entrypoint /usr/local/bin/ldmd2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldmd2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lib_stats.R

```bash
$ singularity exec <container> /usr/local/bin/lib_stats.R
$ podman run --it --rm --entrypoint /usr/local/bin/lib_stats.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lib_stats.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lumpy

```bash
$ singularity exec <container> /usr/local/bin/lumpy
$ podman run --it --rm --entrypoint /usr/local/bin/lumpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lumpy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lumpy_filter

```bash
$ singularity exec <container> /usr/local/bin/lumpy_filter
$ podman run --it --rm --entrypoint /usr/local/bin/lumpy_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lumpy_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lumpyexpress

```bash
$ singularity exec <container> /usr/local/bin/lumpyexpress
$ podman run --it --rm --entrypoint /usr/local/bin/lumpyexpress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lumpyexpress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mosdepth

```bash
$ singularity exec <container> /usr/local/bin/mosdepth
$ podman run --it --rm --entrypoint /usr/local/bin/mosdepth   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mosdepth   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### samblaster

```bash
$ singularity exec <container> /usr/local/bin/samblaster
$ podman run --it --rm --entrypoint /usr/local/bin/samblaster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/samblaster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scriptlive

```bash
$ singularity exec <container> /usr/local/bin/scriptlive
$ podman run --it --rm --entrypoint /usr/local/bin/scriptlive   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scriptlive   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smoove

```bash
$ singularity exec <container> /usr/local/bin/smoove
$ podman run --it --rm --entrypoint /usr/local/bin/smoove   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smoove   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sv_classifier.py

```bash
$ singularity exec <container> /usr/local/bin/sv_classifier.py
$ podman run --it --rm --entrypoint /usr/local/bin/sv_classifier.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sv_classifier.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svtools

```bash
$ singularity exec <container> /usr/local/bin/svtools
$ podman run --it --rm --entrypoint /usr/local/bin/svtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svtyper

```bash
$ singularity exec <container> /usr/local/bin/svtyper
$ podman run --it --rm --entrypoint /usr/local/bin/svtyper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svtyper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svtyper-sso

```bash
$ singularity exec <container> /usr/local/bin/svtyper-sso
$ podman run --it --rm --entrypoint /usr/local/bin/svtyper-sso   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svtyper-sso   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### update_info.py

```bash
$ singularity exec <container> /usr/local/bin/update_info.py
$ podman run --it --rm --entrypoint /usr/local/bin/update_info.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/update_info.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_allele_freq.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_allele_freq.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_allele_freq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_allele_freq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_group_multiline.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_group_multiline.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_group_multiline.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_group_multiline.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_modify_header.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_modify_header.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_modify_header.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_modify_header.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_paste.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_paste.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_paste.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_paste.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cal

```bash
$ singularity exec <container> /usr/local/bin/cal
$ podman run --it --rm --entrypoint /usr/local/bin/cal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chmem

```bash
$ singularity exec <container> /usr/local/bin/chmem
$ podman run --it --rm --entrypoint /usr/local/bin/chmem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chmem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### choom

```bash
$ singularity exec <container> /usr/local/bin/choom
$ podman run --it --rm --entrypoint /usr/local/bin/choom   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/choom   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chrt

```bash
$ singularity exec <container> /usr/local/bin/chrt
$ podman run --it --rm --entrypoint /usr/local/bin/chrt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chrt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### col

```bash
$ singularity exec <container> /usr/local/bin/col
$ podman run --it --rm --entrypoint /usr/local/bin/col   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/col   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### colcrt

```bash
$ singularity exec <container> /usr/local/bin/colcrt
$ podman run --it --rm --entrypoint /usr/local/bin/colcrt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/colcrt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### colrm

```bash
$ singularity exec <container> /usr/local/bin/colrm
$ podman run --it --rm --entrypoint /usr/local/bin/colrm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/colrm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### column

```bash
$ singularity exec <container> /usr/local/bin/column
$ podman run --it --rm --entrypoint /usr/local/bin/column   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/column   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dmesg

```bash
$ singularity exec <container> /usr/local/bin/dmesg
$ podman run --it --rm --entrypoint /usr/local/bin/dmesg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dmesg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eject

```bash
$ singularity exec <container> /usr/local/bin/eject
$ podman run --it --rm --entrypoint /usr/local/bin/eject   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eject   -v ${PWD} -w ${PWD} <container> -c " $@"
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
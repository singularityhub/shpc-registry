---
layout: container
name:  "quay.io/biocontainers/slamdunk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/slamdunk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/slamdunk/container.yaml"
updated_at: "2023-12-20 02:18:33.652796"
latest: "0.4.3--py_0"
container_url: "https://biocontainers.pro/tools/slamdunk"
aliases:
 - "addr2line"
 - "alleyoop"
 - "ar"
 - "as"
 - "c++filt"
 - "dwp"
 - "elfedit"
 - "gold"
 - "gprof"
 - "ld"
 - "ld.bfd"
 - "ld.gold"
 - "ngm"
 - "ngm-core"
 - "ngm-core-debug"
 - "ngm-debug"
 - "ngm-log"
 - "ngm-utils"
 - "ngm-utils-debug"
 - "nm"
 - "objcopy"
 - "objdump"
 - "oclTool"
 - "ranlib"
 - "readelf"
 - "size"
 - "slamdunk"
 - "splash"
 - "strings"
 - "strip"
 - "varscan"
 - "intersection_matrix.py"
 - "intron_exon_reads.py"
 - "pbt_plotting_example.py"
 - "peak_pie.py"
 - "pybedtools"
 - "venn_gchart.py"
 - "venn_mpl.py"
 - "annotate.py"
 - "pandoc-citeproc"
 - "shiftBed"
versions:
 - "0.4.3--py_0"
description: "shpc-registry automated BioContainers addition for slamdunk"
config: {"url": "https://biocontainers.pro/tools/slamdunk", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for slamdunk", "latest": {"0.4.3--py_0": "sha256:07dd7a65298100e41df542b9efeb6ac825f399c2e45d0b5e579ad55cfdf296c4"}, "tags": {"0.4.3--py_0": "sha256:07dd7a65298100e41df542b9efeb6ac825f399c2e45d0b5e579ad55cfdf296c4"}, "docker": "quay.io/biocontainers/slamdunk", "aliases": {"addr2line": "/usr/local/bin/addr2line", "alleyoop": "/usr/local/bin/alleyoop", "ar": "/usr/local/bin/ar", "as": "/usr/local/bin/as", "c++filt": "/usr/local/bin/c++filt", "dwp": "/usr/local/bin/dwp", "elfedit": "/usr/local/bin/elfedit", "gold": "/usr/local/bin/gold", "gprof": "/usr/local/bin/gprof", "ld": "/usr/local/bin/ld", "ld.bfd": "/usr/local/bin/ld.bfd", "ld.gold": "/usr/local/bin/ld.gold", "ngm": "/usr/local/bin/ngm", "ngm-core": "/usr/local/bin/ngm-core", "ngm-core-debug": "/usr/local/bin/ngm-core-debug", "ngm-debug": "/usr/local/bin/ngm-debug", "ngm-log": "/usr/local/bin/ngm-log", "ngm-utils": "/usr/local/bin/ngm-utils", "ngm-utils-debug": "/usr/local/bin/ngm-utils-debug", "nm": "/usr/local/bin/nm", "objcopy": "/usr/local/bin/objcopy", "objdump": "/usr/local/bin/objdump", "oclTool": "/usr/local/bin/oclTool", "ranlib": "/usr/local/bin/ranlib", "readelf": "/usr/local/bin/readelf", "size": "/usr/local/bin/size", "slamdunk": "/usr/local/bin/slamdunk", "splash": "/usr/local/bin/splash", "strings": "/usr/local/bin/strings", "strip": "/usr/local/bin/strip", "varscan": "/usr/local/bin/varscan", "intersection_matrix.py": "/usr/local/bin/intersection_matrix.py", "intron_exon_reads.py": "/usr/local/bin/intron_exon_reads.py", "pbt_plotting_example.py": "/usr/local/bin/pbt_plotting_example.py", "peak_pie.py": "/usr/local/bin/peak_pie.py", "pybedtools": "/usr/local/bin/pybedtools", "venn_gchart.py": "/usr/local/bin/venn_gchart.py", "venn_mpl.py": "/usr/local/bin/venn_mpl.py", "annotate.py": "/usr/local/bin/annotate.py", "pandoc-citeproc": "/usr/local/bin/pandoc-citeproc", "shiftBed": "/usr/local/bin/shiftBed"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/slamdunk.
shpc-registry automated BioContainers addition for slamdunk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/slamdunk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/slamdunk:0.4.3--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/slamdunk/0.4.3--py_0
$ module help quay.io/biocontainers/slamdunk/0.4.3--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### slamdunk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### slamdunk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### slamdunk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### slamdunk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### slamdunk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### slamdunk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### addr2line

```bash
$ singularity exec <container> /usr/local/bin/addr2line
$ podman run --it --rm --entrypoint /usr/local/bin/addr2line   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/addr2line   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alleyoop

```bash
$ singularity exec <container> /usr/local/bin/alleyoop
$ podman run --it --rm --entrypoint /usr/local/bin/alleyoop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alleyoop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ar

```bash
$ singularity exec <container> /usr/local/bin/ar
$ podman run --it --rm --entrypoint /usr/local/bin/ar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### as

```bash
$ singularity exec <container> /usr/local/bin/as
$ podman run --it --rm --entrypoint /usr/local/bin/as   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/as   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c++filt

```bash
$ singularity exec <container> /usr/local/bin/c++filt
$ podman run --it --rm --entrypoint /usr/local/bin/c++filt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c++filt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dwp

```bash
$ singularity exec <container> /usr/local/bin/dwp
$ podman run --it --rm --entrypoint /usr/local/bin/dwp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dwp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elfedit

```bash
$ singularity exec <container> /usr/local/bin/elfedit
$ podman run --it --rm --entrypoint /usr/local/bin/elfedit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elfedit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gold

```bash
$ singularity exec <container> /usr/local/bin/gold
$ podman run --it --rm --entrypoint /usr/local/bin/gold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gprof

```bash
$ singularity exec <container> /usr/local/bin/gprof
$ podman run --it --rm --entrypoint /usr/local/bin/gprof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gprof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ld

```bash
$ singularity exec <container> /usr/local/bin/ld
$ podman run --it --rm --entrypoint /usr/local/bin/ld   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ld   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ld.bfd

```bash
$ singularity exec <container> /usr/local/bin/ld.bfd
$ podman run --it --rm --entrypoint /usr/local/bin/ld.bfd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ld.bfd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ld.gold

```bash
$ singularity exec <container> /usr/local/bin/ld.gold
$ podman run --it --rm --entrypoint /usr/local/bin/ld.gold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ld.gold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngm

```bash
$ singularity exec <container> /usr/local/bin/ngm
$ podman run --it --rm --entrypoint /usr/local/bin/ngm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngm-core

```bash
$ singularity exec <container> /usr/local/bin/ngm-core
$ podman run --it --rm --entrypoint /usr/local/bin/ngm-core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngm-core   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngm-core-debug

```bash
$ singularity exec <container> /usr/local/bin/ngm-core-debug
$ podman run --it --rm --entrypoint /usr/local/bin/ngm-core-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngm-core-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngm-debug

```bash
$ singularity exec <container> /usr/local/bin/ngm-debug
$ podman run --it --rm --entrypoint /usr/local/bin/ngm-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngm-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngm-log

```bash
$ singularity exec <container> /usr/local/bin/ngm-log
$ podman run --it --rm --entrypoint /usr/local/bin/ngm-log   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngm-log   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngm-utils

```bash
$ singularity exec <container> /usr/local/bin/ngm-utils
$ podman run --it --rm --entrypoint /usr/local/bin/ngm-utils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngm-utils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngm-utils-debug

```bash
$ singularity exec <container> /usr/local/bin/ngm-utils-debug
$ podman run --it --rm --entrypoint /usr/local/bin/ngm-utils-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngm-utils-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nm

```bash
$ singularity exec <container> /usr/local/bin/nm
$ podman run --it --rm --entrypoint /usr/local/bin/nm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### objcopy

```bash
$ singularity exec <container> /usr/local/bin/objcopy
$ podman run --it --rm --entrypoint /usr/local/bin/objcopy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/objcopy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### objdump

```bash
$ singularity exec <container> /usr/local/bin/objdump
$ podman run --it --rm --entrypoint /usr/local/bin/objdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/objdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oclTool

```bash
$ singularity exec <container> /usr/local/bin/oclTool
$ podman run --it --rm --entrypoint /usr/local/bin/oclTool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oclTool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ranlib

```bash
$ singularity exec <container> /usr/local/bin/ranlib
$ podman run --it --rm --entrypoint /usr/local/bin/ranlib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ranlib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### readelf

```bash
$ singularity exec <container> /usr/local/bin/readelf
$ podman run --it --rm --entrypoint /usr/local/bin/readelf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/readelf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### size

```bash
$ singularity exec <container> /usr/local/bin/size
$ podman run --it --rm --entrypoint /usr/local/bin/size   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/size   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### slamdunk

```bash
$ singularity exec <container> /usr/local/bin/slamdunk
$ podman run --it --rm --entrypoint /usr/local/bin/slamdunk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slamdunk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### splash

```bash
$ singularity exec <container> /usr/local/bin/splash
$ podman run --it --rm --entrypoint /usr/local/bin/splash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/splash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### strings

```bash
$ singularity exec <container> /usr/local/bin/strings
$ podman run --it --rm --entrypoint /usr/local/bin/strings   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/strings   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### strip

```bash
$ singularity exec <container> /usr/local/bin/strip
$ podman run --it --rm --entrypoint /usr/local/bin/strip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/strip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### varscan

```bash
$ singularity exec <container> /usr/local/bin/varscan
$ podman run --it --rm --entrypoint /usr/local/bin/varscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/varscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intersection_matrix.py

```bash
$ singularity exec <container> /usr/local/bin/intersection_matrix.py
$ podman run --it --rm --entrypoint /usr/local/bin/intersection_matrix.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intersection_matrix.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intron_exon_reads.py

```bash
$ singularity exec <container> /usr/local/bin/intron_exon_reads.py
$ podman run --it --rm --entrypoint /usr/local/bin/intron_exon_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intron_exon_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbt_plotting_example.py

```bash
$ singularity exec <container> /usr/local/bin/pbt_plotting_example.py
$ podman run --it --rm --entrypoint /usr/local/bin/pbt_plotting_example.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbt_plotting_example.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### peak_pie.py

```bash
$ singularity exec <container> /usr/local/bin/peak_pie.py
$ podman run --it --rm --entrypoint /usr/local/bin/peak_pie.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/peak_pie.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pybedtools

```bash
$ singularity exec <container> /usr/local/bin/pybedtools
$ podman run --it --rm --entrypoint /usr/local/bin/pybedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### venn_gchart.py

```bash
$ singularity exec <container> /usr/local/bin/venn_gchart.py
$ podman run --it --rm --entrypoint /usr/local/bin/venn_gchart.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/venn_gchart.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### venn_mpl.py

```bash
$ singularity exec <container> /usr/local/bin/venn_mpl.py
$ podman run --it --rm --entrypoint /usr/local/bin/venn_mpl.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/venn_mpl.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotate.py

```bash
$ singularity exec <container> /usr/local/bin/annotate.py
$ podman run --it --rm --entrypoint /usr/local/bin/annotate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc-citeproc

```bash
$ singularity exec <container> /usr/local/bin/pandoc-citeproc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-citeproc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-citeproc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiftBed

```bash
$ singularity exec <container> /usr/local/bin/shiftBed
$ podman run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
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
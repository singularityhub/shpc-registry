---
layout: container
name:  "quay.io/biocontainers/misopy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/misopy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/misopy/container.yaml"
updated_at: "2023-11-28 02:39:06.622774"
latest: "0.5.4--py27h9801fc8_5"
container_url: "https://biocontainers.pro/tools/misopy"
aliases:
 - "compare_miso"
 - "exon_utils"
 - "filter_events"
 - "index_gff"
 - "miso"
 - "miso_pack"
 - "miso_zip"
 - "module_availability"
 - "pe_utils"
 - "plot.py"
 - "run_events_analysis.py"
 - "run_miso.py"
 - "sam_to_bam"
 - "sashimi_plot"
 - "summarize_miso"
 - "test_miso"
 - "varfilter.py"
 - "qhelpconverter"
 - "f2py2"
 - "f2py2.7"
 - "qwebengine_convert_dict"
 - "canbusutil"
 - "qgltf"
 - "qmlcachegen"
 - "qscxmlc"
 - "qtattributionsscanner"
 - "repc"
versions:
 - "0.5.4--py27h9801fc8_5"
description: "shpc-registry automated BioContainers addition for misopy"
config: {"url": "https://biocontainers.pro/tools/misopy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for misopy", "latest": {"0.5.4--py27h9801fc8_5": "sha256:b9fef964b1087d05d539e104e7f9b6adc219e7cfc4a804360ea8f39e1ff88867"}, "tags": {"0.5.4--py27h9801fc8_5": "sha256:b9fef964b1087d05d539e104e7f9b6adc219e7cfc4a804360ea8f39e1ff88867"}, "docker": "quay.io/biocontainers/misopy", "aliases": {"compare_miso": "/usr/local/bin/compare_miso", "exon_utils": "/usr/local/bin/exon_utils", "filter_events": "/usr/local/bin/filter_events", "index_gff": "/usr/local/bin/index_gff", "miso": "/usr/local/bin/miso", "miso_pack": "/usr/local/bin/miso_pack", "miso_zip": "/usr/local/bin/miso_zip", "module_availability": "/usr/local/bin/module_availability", "pe_utils": "/usr/local/bin/pe_utils", "plot.py": "/usr/local/bin/plot.py", "run_events_analysis.py": "/usr/local/bin/run_events_analysis.py", "run_miso.py": "/usr/local/bin/run_miso.py", "sam_to_bam": "/usr/local/bin/sam_to_bam", "sashimi_plot": "/usr/local/bin/sashimi_plot", "summarize_miso": "/usr/local/bin/summarize_miso", "test_miso": "/usr/local/bin/test_miso", "varfilter.py": "/usr/local/bin/varfilter.py", "qhelpconverter": "/usr/local/bin/qhelpconverter", "f2py2": "/usr/local/bin/f2py2", "f2py2.7": "/usr/local/bin/f2py2.7", "qwebengine_convert_dict": "/usr/local/bin/qwebengine_convert_dict", "canbusutil": "/usr/local/bin/canbusutil", "qgltf": "/usr/local/bin/qgltf", "qmlcachegen": "/usr/local/bin/qmlcachegen", "qscxmlc": "/usr/local/bin/qscxmlc", "qtattributionsscanner": "/usr/local/bin/qtattributionsscanner", "repc": "/usr/local/bin/repc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/misopy.
shpc-registry automated BioContainers addition for misopy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/misopy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/misopy:0.5.4--py27h9801fc8_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/misopy/0.5.4--py27h9801fc8_5
$ module help quay.io/biocontainers/misopy/0.5.4--py27h9801fc8_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### misopy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### misopy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### misopy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### misopy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### misopy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### misopy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### compare_miso

```bash
$ singularity exec <container> /usr/local/bin/compare_miso
$ podman run --it --rm --entrypoint /usr/local/bin/compare_miso   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compare_miso   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exon_utils

```bash
$ singularity exec <container> /usr/local/bin/exon_utils
$ podman run --it --rm --entrypoint /usr/local/bin/exon_utils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exon_utils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_events

```bash
$ singularity exec <container> /usr/local/bin/filter_events
$ podman run --it --rm --entrypoint /usr/local/bin/filter_events   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_events   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index_gff

```bash
$ singularity exec <container> /usr/local/bin/index_gff
$ podman run --it --rm --entrypoint /usr/local/bin/index_gff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index_gff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### miso

```bash
$ singularity exec <container> /usr/local/bin/miso
$ podman run --it --rm --entrypoint /usr/local/bin/miso   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/miso   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### miso_pack

```bash
$ singularity exec <container> /usr/local/bin/miso_pack
$ podman run --it --rm --entrypoint /usr/local/bin/miso_pack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/miso_pack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### miso_zip

```bash
$ singularity exec <container> /usr/local/bin/miso_zip
$ podman run --it --rm --entrypoint /usr/local/bin/miso_zip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/miso_zip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### module_availability

```bash
$ singularity exec <container> /usr/local/bin/module_availability
$ podman run --it --rm --entrypoint /usr/local/bin/module_availability   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/module_availability   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pe_utils

```bash
$ singularity exec <container> /usr/local/bin/pe_utils
$ podman run --it --rm --entrypoint /usr/local/bin/pe_utils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pe_utils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot.py

```bash
$ singularity exec <container> /usr/local/bin/plot.py
$ podman run --it --rm --entrypoint /usr/local/bin/plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_events_analysis.py

```bash
$ singularity exec <container> /usr/local/bin/run_events_analysis.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_events_analysis.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_events_analysis.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_miso.py

```bash
$ singularity exec <container> /usr/local/bin/run_miso.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_miso.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_miso.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sam_to_bam

```bash
$ singularity exec <container> /usr/local/bin/sam_to_bam
$ podman run --it --rm --entrypoint /usr/local/bin/sam_to_bam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sam_to_bam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sashimi_plot

```bash
$ singularity exec <container> /usr/local/bin/sashimi_plot
$ podman run --it --rm --entrypoint /usr/local/bin/sashimi_plot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sashimi_plot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### summarize_miso

```bash
$ singularity exec <container> /usr/local/bin/summarize_miso
$ podman run --it --rm --entrypoint /usr/local/bin/summarize_miso   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/summarize_miso   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test_miso

```bash
$ singularity exec <container> /usr/local/bin/test_miso
$ podman run --it --rm --entrypoint /usr/local/bin/test_miso   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test_miso   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### varfilter.py

```bash
$ singularity exec <container> /usr/local/bin/varfilter.py
$ podman run --it --rm --entrypoint /usr/local/bin/varfilter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/varfilter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhelpconverter

```bash
$ singularity exec <container> /usr/local/bin/qhelpconverter
$ podman run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### qwebengine_convert_dict

```bash
$ singularity exec <container> /usr/local/bin/qwebengine_convert_dict
$ podman run --it --rm --entrypoint /usr/local/bin/qwebengine_convert_dict   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qwebengine_convert_dict   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### canbusutil

```bash
$ singularity exec <container> /usr/local/bin/canbusutil
$ podman run --it --rm --entrypoint /usr/local/bin/canbusutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/canbusutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qgltf

```bash
$ singularity exec <container> /usr/local/bin/qgltf
$ podman run --it --rm --entrypoint /usr/local/bin/qgltf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qgltf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qmlcachegen

```bash
$ singularity exec <container> /usr/local/bin/qmlcachegen
$ podman run --it --rm --entrypoint /usr/local/bin/qmlcachegen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qmlcachegen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qscxmlc

```bash
$ singularity exec <container> /usr/local/bin/qscxmlc
$ podman run --it --rm --entrypoint /usr/local/bin/qscxmlc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qscxmlc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qtattributionsscanner

```bash
$ singularity exec <container> /usr/local/bin/qtattributionsscanner
$ podman run --it --rm --entrypoint /usr/local/bin/qtattributionsscanner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qtattributionsscanner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### repc

```bash
$ singularity exec <container> /usr/local/bin/repc
$ podman run --it --rm --entrypoint /usr/local/bin/repc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/repc   -v ${PWD} -w ${PWD} <container> -c " $@"
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
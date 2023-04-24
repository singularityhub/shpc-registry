---
layout: container
name:  "quay.io/biocontainers/chorus2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/chorus2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/chorus2/container.yaml"
updated_at: "2023-04-24 02:42:00.076610"
latest: "2.01--py39h09cc20e_1"
container_url: "https://biocontainers.pro/tools/chorus2"
aliases:
 - "Chorus2"
 - "ChorusDraftPrebuild"
 - "ChorusGUI"
 - "ChorusHomo"
 - "ChorusNGSfilter"
 - "ChorusNGSselect"
 - "ChorusNoRef"
 - "ChorusPBGUI"
 - "pyfasta"
 - "gff2gff.py"
 - "jellyfish"
 - "qhelpconverter"
 - "bwa"
 - "guess-ploidy.py"
 - "plot-roh.py"
 - "run-roh.pl"
 - "color-chrs.pl"
 - "qwebengine_convert_dict"
 - "plot-vcfstats"
versions:
 - "2.01--py39h09cc20e_1"
description: "shpc-registry automated BioContainers addition for chorus2"
config: {"url": "https://biocontainers.pro/tools/chorus2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for chorus2", "latest": {"2.01--py39h09cc20e_1": "sha256:83e1cb499bc45319d56cf3c220c2627b1e69b888fb245ca3d9808b85fcfbceae"}, "tags": {"2.01--py39h09cc20e_1": "sha256:83e1cb499bc45319d56cf3c220c2627b1e69b888fb245ca3d9808b85fcfbceae"}, "docker": "quay.io/biocontainers/chorus2", "aliases": {"Chorus2": "/usr/local/bin/Chorus2", "ChorusDraftPrebuild": "/usr/local/bin/ChorusDraftPrebuild", "ChorusGUI": "/usr/local/bin/ChorusGUI", "ChorusHomo": "/usr/local/bin/ChorusHomo", "ChorusNGSfilter": "/usr/local/bin/ChorusNGSfilter", "ChorusNGSselect": "/usr/local/bin/ChorusNGSselect", "ChorusNoRef": "/usr/local/bin/ChorusNoRef", "ChorusPBGUI": "/usr/local/bin/ChorusPBGUI", "pyfasta": "/usr/local/bin/pyfasta", "gff2gff.py": "/usr/local/bin/gff2gff.py", "jellyfish": "/usr/local/bin/jellyfish", "qhelpconverter": "/usr/local/bin/qhelpconverter", "bwa": "/usr/local/bin/bwa", "guess-ploidy.py": "/usr/local/bin/guess-ploidy.py", "plot-roh.py": "/usr/local/bin/plot-roh.py", "run-roh.pl": "/usr/local/bin/run-roh.pl", "color-chrs.pl": "/usr/local/bin/color-chrs.pl", "qwebengine_convert_dict": "/usr/local/bin/qwebengine_convert_dict", "plot-vcfstats": "/usr/local/bin/plot-vcfstats"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/chorus2.
shpc-registry automated BioContainers addition for chorus2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/chorus2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/chorus2:2.01--py39h09cc20e_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/chorus2/2.01--py39h09cc20e_1
$ module help quay.io/biocontainers/chorus2/2.01--py39h09cc20e_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### chorus2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### chorus2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### chorus2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### chorus2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### chorus2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### chorus2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Chorus2

```bash
$ singularity exec <container> /usr/local/bin/Chorus2
$ podman run --it --rm --entrypoint /usr/local/bin/Chorus2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Chorus2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ChorusDraftPrebuild

```bash
$ singularity exec <container> /usr/local/bin/ChorusDraftPrebuild
$ podman run --it --rm --entrypoint /usr/local/bin/ChorusDraftPrebuild   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ChorusDraftPrebuild   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ChorusGUI

```bash
$ singularity exec <container> /usr/local/bin/ChorusGUI
$ podman run --it --rm --entrypoint /usr/local/bin/ChorusGUI   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ChorusGUI   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ChorusHomo

```bash
$ singularity exec <container> /usr/local/bin/ChorusHomo
$ podman run --it --rm --entrypoint /usr/local/bin/ChorusHomo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ChorusHomo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ChorusNGSfilter

```bash
$ singularity exec <container> /usr/local/bin/ChorusNGSfilter
$ podman run --it --rm --entrypoint /usr/local/bin/ChorusNGSfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ChorusNGSfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ChorusNGSselect

```bash
$ singularity exec <container> /usr/local/bin/ChorusNGSselect
$ podman run --it --rm --entrypoint /usr/local/bin/ChorusNGSselect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ChorusNGSselect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ChorusNoRef

```bash
$ singularity exec <container> /usr/local/bin/ChorusNoRef
$ podman run --it --rm --entrypoint /usr/local/bin/ChorusNoRef   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ChorusNoRef   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ChorusPBGUI

```bash
$ singularity exec <container> /usr/local/bin/ChorusPBGUI
$ podman run --it --rm --entrypoint /usr/local/bin/ChorusPBGUI   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ChorusPBGUI   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyfasta

```bash
$ singularity exec <container> /usr/local/bin/pyfasta
$ podman run --it --rm --entrypoint /usr/local/bin/pyfasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyfasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2gff.py

```bash
$ singularity exec <container> /usr/local/bin/gff2gff.py
$ podman run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jellyfish

```bash
$ singularity exec <container> /usr/local/bin/jellyfish
$ podman run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhelpconverter

```bash
$ singularity exec <container> /usr/local/bin/qhelpconverter
$ podman run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa

```bash
$ singularity exec <container> /usr/local/bin/bwa
$ podman run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
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